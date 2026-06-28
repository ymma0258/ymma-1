"""Create post-hoc Risk-Calibrated Stable-Tail risk matrices.

Stable-Tail RC-GNN is not a retrained model. It keeps Stable-Tail GNN node
probabilities and node-risk metrics unchanged, then applies a constrained
calibration to the normalized node risk used for edge-risk matrices:

    s_rc = clip(s_stable + delta * P_high * (1 - s_stable), 0, 1)

The continuous edge risk is then:

    R_ij = w_floor * max(s_rc_i, s_rc_j)

This script writes a complete risk-matrix directory compatible with the OD and
PyVRP downstream scripts while leaving the source Stable-Tail outputs intact.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from pathlib import Path

import numpy as np


DEFAULT_INPUT_ROOT = Path(
    r"D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\risk_matrices"
)
DEFAULT_OUTPUT_ROOT = Path(
    r"D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\stable_tail_rc_posthoc"
    r"\risk_matrices"
)
EPS = 1e-12


def parse_float_list(value: str) -> list[float]:
    return [float(item.strip()) for item in value.split(",") if item.strip()]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-root", type=Path, default=DEFAULT_INPUT_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--source-prefix", default="gcn_teg_concat")
    parser.add_argument("--seeds", default="0,1,2,3,4,5,6,7,8,9")
    parser.add_argument("--deltas", default="0.03,0.05,0.08")
    parser.add_argument("--years", default="data_2020,data_2021")
    parser.add_argument("--tag", default="10seed")
    return parser.parse_args()


def quantile_levels(values: np.ndarray, num_levels: int) -> np.ndarray:
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty_like(order)
    ranks[order] = np.arange(values.shape[0])
    levels = np.floor(ranks * num_levels / max(1, values.shape[0])).astype(np.int64) + 1
    return np.clip(levels, 1, num_levels)


def matrix_5x8(edge: dict[str, np.ndarray]) -> np.ndarray:
    mat = np.zeros((5, 8), dtype=np.int64)
    for p_level, c_level in zip(edge["P_level"], edge["C_level"]):
        mat[int(p_level) - 1, int(c_level) - 1] += 1
    return mat


def write_matrix_csv(path: Path, mat: np.ndarray) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["P_level"] + [f"C_{idx}" for idx in range(1, 9)])
        for p_idx in range(5):
            writer.writerow([p_idx + 1] + mat[p_idx].tolist())


def write_edge_csv(path: Path, edge: dict[str, np.ndarray]) -> None:
    fields = [
        "edge_id",
        "src",
        "dst",
        "w_raw",
        "w_norm",
        "severity",
        "severity_norm_mean",
        "severity_norm",
        "R_ij",
        "P_level",
        "C_level",
        "RiskLevel",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for idx in range(edge["edge_id"].shape[0]):
            writer.writerow({field: edge[field][idx].item() for field in fields})


def write_node_csv(path: Path, labels: np.ndarray, payload: dict[str, np.ndarray]) -> None:
    probs = payload["probs"]
    fields = [
        "node_id",
        "label",
        "pred_label",
        "S_i",
        "S_i_norm",
        "S_i_rc_norm",
        "delta_rc",
        "P_high",
    ] + [f"p_{idx}" for idx in range(1, 9)]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for node_id in range(labels.shape[0]):
            row = {
                "node_id": node_id,
                "label": int(labels[node_id]),
                "pred_label": int(payload["pred_label"][node_id]),
                "S_i": float(payload["scores"][node_id]),
                "S_i_norm": float(payload["scores_norm"][node_id]),
                "S_i_rc_norm": float(payload["scores_rc_norm"][node_id]),
                "delta_rc": float(payload["delta_rc"][node_id]),
                "P_high": float(payload["p_high"][node_id]),
            }
            for cls_idx in range(8):
                row[f"p_{cls_idx + 1}"] = float(probs[node_id, cls_idx])
            writer.writerow(row)


def write_rows_csv(path: Path, rows: list[dict[str, float | int]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def top_edges(edge: dict[str, np.ndarray], top_n: int = 20) -> list[dict[str, float | int]]:
    order = np.argsort(edge["R_ij"])[::-1][:top_n]
    rows: list[dict[str, float | int]] = []
    for rank, idx in enumerate(order, start=1):
        rows.append(
            {
                "rank": rank,
                "edge_id": int(edge["edge_id"][idx]),
                "src": int(edge["src"][idx]),
                "dst": int(edge["dst"][idx]),
                "R_ij": float(edge["R_ij"][idx]),
                "w_norm": float(edge["w_norm"][idx]),
                "severity": float(edge["severity"][idx]),
                "P_level": int(edge["P_level"][idx]),
                "C_level": int(edge["C_level"][idx]),
                "RiskLevel": int(edge["RiskLevel"][idx]),
            }
        )
    return rows


def top_nodes(labels: np.ndarray, payload: dict[str, np.ndarray], top_n: int = 20) -> list[dict[str, float | int]]:
    order = np.argsort(payload["scores_rc_norm"])[::-1][:top_n]
    rows: list[dict[str, float | int]] = []
    for rank, idx in enumerate(order, start=1):
        rows.append(
            {
                "rank": rank,
                "node_id": int(idx),
                "label": int(labels[idx]),
                "pred_label": int(payload["pred_label"][idx]),
                "S_i": float(payload["scores"][idx]),
                "S_i_norm": float(payload["scores_norm"][idx]),
                "S_i_rc_norm": float(payload["scores_rc_norm"][idx]),
                "P_high": float(payload["p_high"][idx]),
            }
        )
    return rows


def risk_summary(edge: dict[str, np.ndarray], mat: np.ndarray) -> dict[str, object]:
    risks = edge["R_ij"]
    return {
        "edge_count": int(risks.shape[0]),
        "risk_min": float(np.min(risks)),
        "risk_max": float(np.max(risks)),
        "risk_mean": float(np.mean(risks)),
        "risk_p25": float(np.percentile(risks, 25)),
        "risk_p50": float(np.percentile(risks, 50)),
        "risk_p75": float(np.percentile(risks, 75)),
        "risk_p90": float(np.percentile(risks, 90)),
        "risk_p95": float(np.percentile(risks, 95)),
        "risk_p99": float(np.percentile(risks, 99)),
        "zero_risk_edge_count": int(np.sum(risks <= EPS)),
        "zero_risk_edge_ratio": float(np.mean(risks <= EPS)),
        "edge_attribute_zero_ratio": float(np.mean(edge["w_raw"] <= EPS)),
        "matrix_5x8": mat.tolist(),
    }


def calibrate_node_payload(source_npz: Path, delta: float) -> tuple[dict[str, np.ndarray], np.ndarray]:
    with np.load(source_npz) as data:
        payload = {key: data[key] for key in data.files}
    labels = payload["labels"].astype(np.int64)
    base = np.clip(payload["scores_norm"].astype(float), 0.0, 1.0)
    p_high = np.clip(payload["p_high"].astype(float), 0.0, 1.0)
    delta_rc = delta * p_high * (1.0 - base)
    payload["scores_rc_norm"] = np.clip(base + delta_rc, 0.0, 1.0)
    payload["delta_rc"] = delta_rc
    return payload, labels


def calibrate_edge_payload(
    source_npz: Path, node_payload: dict[str, np.ndarray]
) -> dict[str, np.ndarray]:
    with np.load(source_npz) as data:
        edge = {key: data[key].copy() for key in data.files}
    src = edge["src"].astype(np.int64)
    dst = edge["dst"].astype(np.int64)
    base_norm = node_payload["scores_norm"]
    rc_norm = node_payload["scores_rc_norm"]
    scores = node_payload["scores"]
    edge["severity"] = np.maximum(scores[src], scores[dst])
    edge["severity_norm_mean"] = np.maximum(base_norm[src], base_norm[dst])
    edge["severity_norm"] = np.maximum(rc_norm[src], rc_norm[dst])
    edge["R_ij"] = edge["w_norm"] * edge["severity_norm"]
    edge["P_level"] = quantile_levels(edge["w_norm"], 5)
    edge["C_level"] = np.clip(np.ceil(edge["severity"]), 1, 8).astype(np.int64)
    edge["RiskLevel"] = edge["P_level"] * edge["C_level"]
    return edge


def copy_static_files(src_dir: Path, dst_dir: Path) -> None:
    for name in ["export_report.md"]:
        src = src_dir / name
        if src.exists():
            shutil.copy2(src, dst_dir / name)


def main() -> None:
    args = parse_args()
    seeds = [int(seed) for seed in args.seeds.split(",") if seed.strip()]
    deltas = parse_float_list(args.deltas)
    years = [year.strip() for year in args.years.split(",") if year.strip()]
    args.output_root.mkdir(parents=True, exist_ok=True)

    summary_rows: list[dict[str, object]] = []
    for delta in deltas:
        delta_tag = f"delta{delta:g}".replace(".", "p")
        for seed in seeds:
            src_dir = (
                args.input_root
                / f"{args.source_prefix}_splitB_seed{seed}_epochs50_10seed_floor_0p01"
            )
            if not src_dir.exists():
                raise FileNotFoundError(src_dir)
            dst_dir = (
                args.output_root
                / f"stable_tail_rc_gnn_splitB_seed{seed}_{args.tag}_floor_0p01_{delta_tag}"
            )
            dst_dir.mkdir(parents=True, exist_ok=True)
            copy_static_files(src_dir, dst_dir)

            risk_summaries: dict[str, object] = {}
            for year in years:
                node_payload, labels = calibrate_node_payload(
                    src_dir / f"{year}_node_risk.npz", delta
                )
                edge = calibrate_edge_payload(
                    src_dir / f"{year}_edge_risk.npz", node_payload
                )
                mat = matrix_5x8(edge)

                np.savez(dst_dir / f"{year}_node_risk.npz", **node_payload)
                np.savez(dst_dir / f"{year}_edge_risk.npz", **edge)
                write_node_csv(dst_dir / f"{year}_node_risk.csv", labels, node_payload)
                write_edge_csv(dst_dir / f"{year}_edge_risk.csv", edge)
                write_matrix_csv(dst_dir / f"{year}_matrix_5x8.csv", mat)
                write_rows_csv(dst_dir / f"{year}_top20_nodes.csv", top_nodes(labels, node_payload))
                write_rows_csv(dst_dir / f"{year}_top20_edges.csv", top_edges(edge))
                risk_summaries[year] = risk_summary(edge, mat)

            payload = {
                "model": "stable_tail_rc_gnn",
                "source_model": args.source_prefix,
                "seed": seed,
                "delta": delta,
                "risk_mode": "exposure_floor",
                "exposure_delta": 0.01,
                "posthoc_formula": "clip(S_i_norm + delta * P_high * (1 - S_i_norm), 0, 1)",
                "risk_summaries": risk_summaries,
            }
            (dst_dir / "export_summary.json").write_text(
                json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            for year, summary in risk_summaries.items():
                row = {
                    "delta": delta,
                    "seed": seed,
                    "year": year,
                    "risk_dir": str(dst_dir),
                }
                row.update({key: value for key, value in summary.items() if key != "matrix_5x8"})
                summary_rows.append(row)

    if summary_rows:
        fields = list(summary_rows[0].keys())
        with (args.output_root / "rc_risk_matrix_summary.csv").open(
            "w", newline="", encoding="utf-8"
        ) as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(summary_rows)
    print(f"Wrote RC risk matrices to {args.output_root}")


if __name__ == "__main__":
    main()
