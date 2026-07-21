"""Post-process a Stable-Tail GNN risk export without retraining the model."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

import numpy as np


METHODS = (
    "edge_tail_correction",
    "tail_only_correction",
    "node_calibration",
    "risk_matrix_ensemble",
)
CALIBRATION_SCHEMA_VERSION = 4


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-risk-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--method", choices=METHODS, required=True)
    parser.add_argument("--alpha", type=float, default=0.1)
    parser.add_argument("--rho", type=float, default=0.2)
    parser.add_argument("--tail-quantile", type=float, default=0.90)
    parser.add_argument("--tail-sharpness", type=float, default=20.0)
    parser.add_argument("--hard-tail", action="store_true")
    parser.add_argument("--p-high-mode", choices=("raw", "gate"), default="raw")
    parser.add_argument("--p-high-gate-threshold", type=float, default=0.5)
    parser.add_argument("--year", choices=["data_2020", "data_2021", "all"], default="data_2021")
    parser.add_argument("--clip", action=argparse.BooleanOptionalAction, default=True)
    return parser.parse_args()


def quantile_levels(values: np.ndarray, levels: int) -> np.ndarray:
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty_like(order)
    ranks[order] = np.arange(values.size)
    return np.clip(np.floor(ranks * levels / max(1, values.size)).astype(int) + 1, 1, levels)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def load_payload(path: Path) -> dict[str, np.ndarray]:
    if not path.exists():
        raise FileNotFoundError(f"Required Stable-Tail export file is missing: {path}")
    with np.load(path, allow_pickle=False) as data:
        return {key: np.asarray(data[key]).copy() for key in data.files}


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def node_terms(node: dict[str, np.ndarray]) -> tuple[np.ndarray, np.ndarray, list[str]]:
    fallbacks: list[str] = []
    if "scores_norm" in node:
        score = np.asarray(node["scores_norm"], dtype=float)
    elif "scores" in node:
        score = np.clip((np.asarray(node["scores"], dtype=float) - 1.0) / 7.0, 0.0, 1.0)
        fallbacks.append("scores_norm_from_scores")
    else:
        raise KeyError("Node export has neither scores_norm nor scores")
    if "p_high" in node:
        p_high = np.asarray(node["p_high"], dtype=float)
    elif "probs" in node and node["probs"].shape[1] >= 8:
        p_high = np.asarray(node["probs"][:, 5:8].sum(axis=1), dtype=float)
        fallbacks.append("p_high_from_probs_6_8")
    else:
        p_high = np.clip(score, 0.0, 1.0)
        fallbacks.append("p_high_from_scores_norm")
    return np.clip(score, 0.0, 1.0), np.clip(p_high, 0.0, 1.0), fallbacks


def exposure_terms(edge: dict[str, np.ndarray]) -> tuple[np.ndarray, np.ndarray, list[str]]:
    fallbacks: list[str] = []
    if "w_raw" in edge:
        w_raw = np.asarray(edge["w_raw"], dtype=float)
    elif "w_norm" in edge:
        w_raw = np.clip((np.asarray(edge["w_norm"], dtype=float) - 0.01) / 0.99, 0.0, 1.0)
        fallbacks.append("w_raw_inferred_from_w_floor_delta_0p01")
    else:
        w_raw = np.ones_like(np.asarray(edge["R_ij"], dtype=float))
        fallbacks.append("w_raw_fallback_ones")
    if "w_norm" in edge:
        w_floor = np.asarray(edge["w_norm"], dtype=float)
    else:
        w_floor = 0.01 + 0.99 * w_raw
        fallbacks.append("w_floor_rebuilt_delta_0p01")
    return np.clip(w_raw, 0.0, 1.0), np.clip(w_floor, 0.0, 1.0), fallbacks


def node_exposure(node_count: int, src: np.ndarray, dst: np.ndarray, w_raw: np.ndarray) -> np.ndarray:
    totals = np.zeros(node_count, dtype=float)
    counts = np.zeros(node_count, dtype=float)
    np.add.at(totals, src, w_raw)
    np.add.at(totals, dst, w_raw)
    np.add.at(counts, src, 1.0)
    np.add.at(counts, dst, 1.0)
    return np.divide(totals, counts, out=np.zeros_like(totals), where=counts > 0)


def calibrate(
    method: str,
    base_risk: np.ndarray,
    score: np.ndarray,
    p_high: np.ndarray,
    src: np.ndarray,
    dst: np.ndarray,
    w_raw: np.ndarray,
    w_floor: np.ndarray,
    alpha: float,
    rho: float,
    tail_quantile: float,
    tail_sharpness: float,
    hard_tail: bool,
    p_high_mode: str,
    p_high_gate_threshold: float,
) -> tuple[np.ndarray, np.ndarray, dict[str, object]]:
    if p_high_mode == "raw":
        p_high_used = p_high.copy()
        p_high_note = "P_high is used without thresholding."
    elif p_high_mode == "gate":
        p_high_used = np.where(p_high >= p_high_gate_threshold, p_high, 0.0)
        p_high_note = "P_high values below threshold are set to zero."
    else:
        raise ValueError(f"Unsupported p-high mode: {p_high_mode}")
    edge_high = np.maximum(p_high_used[src], p_high_used[dst])
    teg_tail = w_raw * edge_high
    active_score = score.copy()
    details: dict[str, object] = {
        "p_high_mode": p_high_mode,
        "p_high_gate_threshold": p_high_gate_threshold,
        "p_high_note": p_high_note,
        "p_high_raw_min": float(p_high.min()),
        "p_high_raw_max": float(p_high.max()),
        "p_high_raw_mean": float(p_high.mean()),
        "p_high_used_min": float(p_high_used.min()),
        "p_high_used_max": float(p_high_used.max()),
        "p_high_used_mean": float(p_high_used.mean()),
        "active_high_risk_nodes": int(np.count_nonzero(p_high_used)),
    }
    if method == "edge_tail_correction":
        risk = base_risk * (1.0 + alpha * teg_tail)
        details["formula"] = "R_final = R_base * (1 + alpha * w_raw * max(P_high_used_i,P_high_used_j))"
    elif method == "tail_only_correction":
        threshold = float(np.quantile(base_risk, tail_quantile))
        if hard_tail:
            tail_gate = (base_risk >= threshold).astype(float)
        else:
            z = np.clip(tail_sharpness * (base_risk - threshold), -60.0, 60.0)
            tail_gate = 1.0 / (1.0 + np.exp(-z))
        risk = base_risk + alpha * tail_gate * teg_tail
        details.update(
            formula="R_final = R_base + alpha * tail_gate * w_raw * max(P_high_used_i,P_high_used_j)",
            q_tail=threshold,
            tail_gate="hard" if hard_tail else "sigmoid",
        )
    elif method == "node_calibration":
        exposure = node_exposure(score.size, src, dst, w_raw)
        active_score = np.clip(score + alpha * exposure * p_high_used, 0.0, 1.0)
        risk = w_floor * np.maximum(active_score[src], active_score[dst])
        details.update(
            formula="S_final=clip(S_base+alpha*E_mean*P_high_used,0,1); R_final=w_floor*max(S_final_i,S_final_j)",
            node_exposure="mean_incident_w_raw",
        )
    else:
        base_scale = float(np.quantile(base_risk, 0.95))
        positive_teg_tail = teg_tail[teg_tail > 0]
        teg_scale = (
            float(np.quantile(positive_teg_tail, 0.95))
            if positive_teg_tail.size
            else 0.0
        )
        scale = base_scale / teg_scale if teg_scale > 0 else 0.0
        if teg_scale > 0:
            teg_norm = teg_tail * scale
            risk = (1.0 - rho) * base_risk + rho * teg_norm
            ensemble_fallback = None
        else:
            risk = base_risk.copy()
            ensemble_fallback = "no_active_tail_edges_keep_base"
        details.update(
            formula="R_final=(1-rho)*R_base+rho*R_teg_tail_norm; R_teg_tail=w_raw*max(P_high_used_i,P_high_used_j)",
            normalization="P95(R_base)/P95(positive R_teg_tail)",
            normalization_scale=scale,
            positive_teg_tail_edges=int(positive_teg_tail.size),
            ensemble_fallback=ensemble_fallback,
        )
    return risk, active_score, details


def write_year_files(
    out_dir: Path,
    year: str,
    node: dict[str, np.ndarray],
    edge: dict[str, np.ndarray],
    active_score: np.ndarray,
    risk: np.ndarray,
    method: str,
) -> None:
    src = edge["src"].astype(int)
    dst = edge["dst"].astype(int)
    w_floor = np.asarray(edge["w_norm"], dtype=float)
    severity_norm = np.divide(risk, w_floor, out=np.zeros_like(risk), where=w_floor > 0)
    node_severity_norm = np.maximum(active_score[src], active_score[dst])
    severity = 1.0 + 7.0 * np.clip(node_severity_norm, 0.0, 1.0)
    p_level = quantile_levels(w_floor, 5)
    c_level = np.clip(np.ceil(severity), 1, 8).astype(np.int64)
    edge.update(
        severity=severity.astype(np.float32),
        severity_norm_mean=node_severity_norm.astype(np.float32),
        severity_norm=severity_norm.astype(np.float32),
        R_ij=risk.astype(np.float32),
        P_level=p_level.astype(np.int64),
        C_level=c_level,
        RiskLevel=(p_level * c_level).astype(np.int64),
    )
    if method == "node_calibration":
        node["scores_base_norm"] = np.asarray(node["scores_norm"]).copy()
        node["scores_calibrated"] = active_score.astype(np.float32)
        node["scores_norm"] = active_score.astype(np.float32)
        node["scores"] = (1.0 + 7.0 * active_score).astype(np.float32)
    np.savez_compressed(out_dir / f"{year}_node_risk.npz", **node)
    np.savez_compressed(out_dir / f"{year}_edge_risk.npz", **edge)

    probs = node.get("probs")
    rows: list[dict[str, object]] = []
    for idx in range(active_score.size):
        row: dict[str, object] = {
            "node_id": idx,
            "label": int(node.get("labels", np.zeros(active_score.size))[idx]),
            "pred_label": int(node.get("pred_label", np.zeros(active_score.size))[idx]),
            "S_i": float(node.get("scores", active_score)[idx]),
            "S_i_norm": float(active_score[idx]),
            "P_high": float(node.get("p_high", active_score)[idx]),
        }
        if probs is not None:
            for cls in range(probs.shape[1]):
                row[f"p_{cls + 1}"] = float(probs[idx, cls])
        rows.append(row)
    write_csv(out_dir / f"{year}_node_risk.csv", rows)

    fields = [key for key in ("edge_id", "src", "dst", "w_raw", "w_norm", "severity", "severity_norm_mean", "severity_norm", "R_ij", "P_level", "C_level", "RiskLevel") if key in edge]
    edge_rows = [
        {field: np.asarray(edge[field])[idx].item() for field in fields}
        for idx in range(risk.size)
    ]
    write_csv(out_dir / f"{year}_edge_risk.csv", edge_rows)
    matrix = np.zeros((5, 8), dtype=int)
    for p_val, c_val in zip(p_level, c_level):
        matrix[p_val - 1, c_val - 1] += 1
    write_csv(
        out_dir / f"{year}_matrix_5x8.csv",
        [{"P_level": idx + 1, **{f"C_{j + 1}": int(matrix[idx, j]) for j in range(8)}} for idx in range(5)],
    )
    top = np.argsort(risk)[::-1][:20]
    write_csv(out_dir / f"{year}_top20_edges.csv", [edge_rows[int(idx)] for idx in top])
    node_top = np.argsort(active_score)[::-1][:20]
    write_csv(out_dir / f"{year}_top20_nodes.csv", [rows[int(idx)] for idx in node_top])


def main() -> None:
    args = parse_args()
    if args.alpha < 0 or not 0 <= args.rho <= 1:
        raise ValueError("alpha must be non-negative and rho must be in [0,1]")
    if not 0 < args.tail_quantile < 1 or args.tail_sharpness <= 0:
        raise ValueError("tail-quantile must be in (0,1) and tail-sharpness positive")
    if not 0 <= args.p_high_gate_threshold <= 1:
        raise ValueError("p-high-gate-threshold must be in [0,1]")
    if not args.base_risk_dir.exists():
        raise FileNotFoundError(f"Base Stable-Tail risk directory missing: {args.base_risk_dir}")
    out_dir = args.output_dir / args.name
    if out_dir.exists():
        shutil.rmtree(out_dir)
    shutil.copytree(args.base_risk_dir, out_dir)
    years = ["data_2020", "data_2021"] if args.year == "all" else [args.year]
    summaries: list[dict[str, object]] = []
    p_high_raw_all: list[np.ndarray] = []
    p_high_used_all: list[np.ndarray] = []
    fallbacks: list[str] = []
    source_fingerprints: dict[str, str] = {}
    for year in years:
        node_path = args.base_risk_dir / f"{year}_node_risk.npz"
        edge_path = args.base_risk_dir / f"{year}_edge_risk.npz"
        node = load_payload(node_path)
        edge = load_payload(edge_path)
        source_fingerprints[node_path.name] = file_sha256(node_path)
        source_fingerprints[edge_path.name] = file_sha256(edge_path)
        score, p_high, node_fallbacks = node_terms(node)
        node["p_high"] = p_high.astype(np.float32)
        w_raw, w_floor, edge_fallbacks = exposure_terms(edge)
        edge["w_raw"] = w_raw.astype(np.float32)
        edge["w_norm"] = w_floor.astype(np.float32)
        fallbacks.extend(f"{year}:{item}" for item in [*node_fallbacks, *edge_fallbacks])
        src, dst = edge["src"].astype(int), edge["dst"].astype(int)
        base_risk = np.asarray(edge["R_ij"], dtype=float)
        risk, active_score, details = calibrate(
            args.method, base_risk, score, p_high, src, dst, w_raw, w_floor,
            args.alpha, args.rho, args.tail_quantile, args.tail_sharpness, args.hard_tail,
            args.p_high_mode, args.p_high_gate_threshold,
        )
        p_high_raw_all.append(p_high)
        if args.p_high_mode == "raw":
            p_high_used_all.append(p_high)
        else:
            p_high_used_all.append(
                np.where(p_high >= args.p_high_gate_threshold, p_high, 0.0)
            )
        clip_upper = float(base_risk.max())
        if args.clip:
            risk = np.clip(risk, 0.0, clip_upper)
        write_year_files(out_dir, year, node, edge, active_score, risk, args.method)
        summaries.append(
            {
                "year": year,
                "edge_count": int(risk.size),
                "base_mean": float(base_risk.mean()),
                "risk_mean": float(risk.mean()),
                "risk_p90": float(np.quantile(risk, 0.90)),
                "risk_p95": float(np.quantile(risk, 0.95)),
                "risk_max": float(risk.max()),
                "clip_upper": clip_upper if args.clip else None,
                **details,
            }
        )
    p_high_raw = np.concatenate(p_high_raw_all)
    p_high_used = np.concatenate(p_high_used_all)
    meta = {
        "schema_version": CALIBRATION_SCHEMA_VERSION,
        "name": args.name,
        "method": args.method,
        "alpha": args.alpha,
        "rho": args.rho,
        "tail_quantile": args.tail_quantile,
        "tail_sharpness": args.tail_sharpness,
        "hard_tail": args.hard_tail,
        "p_high_mode": args.p_high_mode,
        "p_high_gate_threshold": args.p_high_gate_threshold,
        "p_high_note": (
            "P_high is used without thresholding."
            if args.p_high_mode == "raw"
            else "P_high values below threshold are set to zero."
        ),
        "p_high_raw_min": float(p_high_raw.min()),
        "p_high_raw_max": float(p_high_raw.max()),
        "p_high_raw_mean": float(p_high_raw.mean()),
        "p_high_used_min": float(p_high_used.min()),
        "p_high_used_max": float(p_high_used.max()),
        "p_high_used_mean": float(p_high_used.mean()),
        "year": args.year,
        "clip": args.clip,
        "base_risk_dir": str(args.base_risk_dir.resolve()),
        "formula": summaries[0]["formula"] if summaries else None,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_fingerprints": source_fingerprints,
        "fallbacks": sorted(set(fallbacks)),
        "summaries": summaries,
    }
    for filename in ("meta.json", "calibration_meta.json", "export_summary.json"):
        (out_dir / filename).write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / "export_report.md").write_text(
        f"# Stable-Tail post-processing calibration\n\nMethod: `{args.method}`; alpha={args.alpha}; rho={args.rho}; P_high mode=`{args.p_high_mode}`.\n",
        encoding="utf-8",
    )
    print(f"Wrote Stable-Tail calibration to {out_dir}")


if __name__ == "__main__":
    main()
