"""Export an ensemble risk matrix by averaging node probabilities."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np


DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\risk_matrices")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("risk_dirs", nargs="+", type=Path)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--name", required=True)
    parser.add_argument(
        "--weights",
        default="",
        help="Optional comma-separated weights matching risk_dirs; defaults to equal weights.",
    )
    return parser.parse_args()


def quantile_levels(values: np.ndarray, num_levels: int) -> np.ndarray:
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty_like(order)
    ranks[order] = np.arange(values.shape[0])
    levels = np.floor(ranks * num_levels / max(1, values.shape[0])).astype(np.int64) + 1
    return np.clip(levels, 1, num_levels)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_matrix(path: Path, p_level: np.ndarray, c_level: np.ndarray) -> None:
    mat = np.zeros((5, 8), dtype=np.int64)
    for p_val, c_val in zip(p_level, c_level):
        mat[int(p_val) - 1, int(c_val) - 1] += 1
    rows = []
    for p_idx in range(5):
        row: dict[str, object] = {"P_level": p_idx + 1}
        for c_idx in range(8):
            row[f"C_{c_idx + 1}"] = int(mat[p_idx, c_idx])
        rows.append(row)
    write_csv(path, rows)


def parse_weights(value: str, count: int) -> np.ndarray:
    if not value:
        return np.full(count, 1.0 / count, dtype=float)
    weights = np.asarray([float(item.strip()) for item in value.split(",") if item.strip()], dtype=float)
    if weights.shape[0] != count:
        raise ValueError(f"Expected {count} weights, got {weights.shape[0]}")
    total = float(weights.sum())
    if total <= 0:
        raise ValueError("Weights must sum to a positive value")
    return weights / total


def export_year(
    risk_dirs: list[Path], weights: np.ndarray, out_dir: Path, year: str
) -> dict[str, object]:
    nodes = [np.load(path / f"{year}_node_risk.npz") for path in risk_dirs]
    edge_ref = np.load(risk_dirs[0] / f"{year}_edge_risk.npz")

    probs = np.zeros_like(nodes[0]["probs"], dtype=float)
    for weight, node in zip(weights, nodes):
        probs += weight * node["probs"]
    labels = nodes[0]["labels"].astype(np.int64)
    levels = np.arange(1, probs.shape[1] + 1, dtype=np.float32)
    scores = probs @ levels
    scores_norm = np.clip((scores - 1.0) / 7.0, 0.0, 1.0)
    p_high = probs[:, 5:].sum(axis=1)
    pred_label = np.argmax(probs, axis=1) + 1

    src = edge_ref["src"]
    dst = edge_ref["dst"]
    w_raw = edge_ref["w_raw"]
    w_norm = edge_ref["w_norm"]
    severity = np.maximum(scores[src], scores[dst])
    severity_norm = np.maximum(scores_norm[src], scores_norm[dst])
    risk = w_norm * severity_norm
    p_level = quantile_levels(w_norm, 5)
    c_level = np.clip(np.ceil(severity), 1, 8).astype(np.int64)
    risk_level = p_level * c_level

    edge = {
        "edge_id": edge_ref["edge_id"],
        "src": src,
        "dst": dst,
        "w_raw": w_raw,
        "w_norm": w_norm,
        "severity": severity,
        "severity_norm": severity_norm,
        "R_ij": risk,
        "P_level": p_level,
        "C_level": c_level,
        "RiskLevel": risk_level,
    }
    np.savez(
        out_dir / f"{year}_node_risk.npz",
        probs=probs,
        scores=scores,
        scores_norm=scores_norm,
        p_high=p_high,
        pred_label=pred_label,
        labels=labels,
    )
    np.savez(out_dir / f"{year}_edge_risk.npz", **edge)

    node_rows = []
    for node_id in range(labels.shape[0]):
        row: dict[str, object] = {
            "node_id": node_id,
            "label": int(labels[node_id]),
            "pred_label": int(pred_label[node_id]),
            "S_i": float(scores[node_id]),
            "S_i_norm": float(scores_norm[node_id]),
            "P_high": float(p_high[node_id]),
        }
        for cls_idx in range(probs.shape[1]):
            row[f"p_{cls_idx + 1}"] = float(probs[node_id, cls_idx])
        node_rows.append(row)
    write_csv(out_dir / f"{year}_node_risk.csv", node_rows)

    fields = [
        "edge_id",
        "src",
        "dst",
        "w_raw",
        "w_norm",
        "severity",
        "severity_norm",
        "R_ij",
        "P_level",
        "C_level",
        "RiskLevel",
    ]
    edge_rows = []
    for idx in range(edge["edge_id"].shape[0]):
        edge_rows.append({field: edge[field][idx].item() for field in fields})
    write_csv(out_dir / f"{year}_edge_risk.csv", edge_rows)
    write_matrix(out_dir / f"{year}_matrix_5x8.csv", p_level, c_level)

    return {
        "year": year,
        "edge_count": int(risk.shape[0]),
        "risk_mean": float(risk.mean()),
        "risk_p95": float(np.percentile(risk, 95)),
        "risk_p99": float(np.percentile(risk, 99)),
        "risk_max": float(risk.max()),
    }


def main() -> None:
    args = parse_args()
    weights = parse_weights(args.weights, len(args.risk_dirs))
    out_dir = args.output_dir / args.name
    out_dir.mkdir(parents=True, exist_ok=True)
    summaries = [
        export_year(args.risk_dirs, weights, out_dir, "data_2020"),
        export_year(args.risk_dirs, weights, out_dir, "data_2021"),
    ]
    payload = {
        "name": args.name,
        "risk_dirs": [str(path) for path in args.risk_dirs],
        "weights": weights.tolist(),
        "ensemble": "mean node probabilities",
        "summaries": summaries,
    }
    (out_dir / "export_summary.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    lines = ["# Ensemble Risk Matrix Export", ""]
    for summary in summaries:
        lines.append(
            "- {year}: edges={edge_count}, mean={risk_mean:.6f}, P95={risk_p95:.6f}, P99={risk_p99:.6f}, max={risk_max:.6f}.".format(
                **summary
            )
        )
    (out_dir / "export_report.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote ensemble risk matrix to {out_dir}")


if __name__ == "__main__":
    main()
