"""Export tail-enhanced risk matrices from existing model predictions.

The enhanced node score is:

    S_tail = clip(S_norm + eta * P_high, 0, 1)

The edge risk keeps the final floor exposure:

    R_ij = w_floor * max(S_tail_i, S_tail_j)
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np


DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\risk_matrices")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-risk-dir", type=Path, required=True)
    parser.add_argument("--eta", type=float, required=True)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--name", required=True)
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


def export_year(base_dir: Path, out_dir: Path, year: str, eta: float) -> dict[str, object]:
    node = np.load(base_dir / f"{year}_node_risk.npz")
    edge_ref = np.load(base_dir / f"{year}_edge_risk.npz")

    probs = node["probs"]
    labels = node["labels"].astype(np.int64)
    scores = node["scores"]
    p_high = node["p_high"]
    scores_norm = np.clip(node["scores_norm"] + eta * p_high, 0.0, 1.0)
    pred_label = node["pred_label"]

    src = edge_ref["src"]
    dst = edge_ref["dst"]
    w_raw = edge_ref["w_raw"]
    w_norm = edge_ref["w_norm"]
    severity = 1.0 + 7.0 * np.maximum(scores_norm[src], scores_norm[dst])
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
    rows = []
    for idx in range(edge["edge_id"].shape[0]):
        rows.append({field: edge[field][idx].item() for field in fields})
    write_csv(out_dir / f"{year}_edge_risk.csv", rows)
    write_matrix(out_dir / f"{year}_matrix_5x8.csv", p_level, c_level)

    return {
        "year": year,
        "eta": eta,
        "edge_count": int(risk.shape[0]),
        "risk_mean": float(risk.mean()),
        "risk_p95": float(np.percentile(risk, 95)),
        "risk_p99": float(np.percentile(risk, 99)),
        "risk_max": float(risk.max()),
    }


def main() -> None:
    args = parse_args()
    out_dir = args.output_dir / args.name
    out_dir.mkdir(parents=True, exist_ok=True)
    summaries = [
        export_year(args.base_risk_dir, out_dir, "data_2020", args.eta),
        export_year(args.base_risk_dir, out_dir, "data_2021", args.eta),
    ]
    payload = {
        "name": args.name,
        "base_risk_dir": str(args.base_risk_dir),
        "eta": args.eta,
        "definition": "S_tail = clip(S_norm + eta * P_high, 0, 1)",
        "summaries": summaries,
    }
    (out_dir / "export_summary.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    lines = ["# Tail-Enhanced Risk Matrix Export", ""]
    for summary in summaries:
        lines.append(
            "- {year}: eta={eta}, mean={risk_mean:.6f}, P95={risk_p95:.6f}, P99={risk_p99:.6f}, max={risk_max:.6f}.".format(
                **summary
            )
        )
    (out_dir / "export_report.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote tail-enhanced risk matrix to {out_dir}")


if __name__ == "__main__":
    main()
