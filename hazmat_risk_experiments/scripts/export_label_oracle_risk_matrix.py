"""Export a label-risk oracle matrix from an existing floor risk export.

Labeled nodes use the true ordinal label as S_i. Unlabeled nodes keep the
base model prediction. This is an analysis-only upper reference, not a
deployable method.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np


DEFAULT_BASE = Path(
    r"D:\PyVRP-main\hazmat_risk_experiments\outputs\risk_matrices"
    r"\teg_gnn_splitB_seed0_epochs20_floor_0p01"
)
DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\risk_matrices")
EPS = 1e-12


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-risk-dir", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--name", default="label_oracle_floor_0p01")
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


def matrix_5x8(edge: dict[str, np.ndarray]) -> np.ndarray:
    mat = np.zeros((5, 8), dtype=np.int64)
    for p_level, c_level in zip(edge["P_level"], edge["C_level"]):
        mat[int(p_level) - 1, int(c_level) - 1] += 1
    return mat


def write_matrix(path: Path, mat: np.ndarray) -> None:
    rows = []
    for p_idx in range(5):
        row: dict[str, object] = {"P_level": p_idx + 1}
        for c_idx in range(8):
            row[f"C_{c_idx + 1}"] = int(mat[p_idx, c_idx])
        rows.append(row)
    write_csv(path, rows)


def export_year(base_dir: Path, out_dir: Path, year: str) -> dict[str, object]:
    node = np.load(base_dir / f"{year}_node_risk.npz")
    edge_base = np.load(base_dir / f"{year}_edge_risk.npz")

    labels = node["labels"].astype(np.int64)
    probs = node["probs"].copy()
    scores = node["scores"].copy()
    labeled = labels > 0
    scores[labeled] = labels[labeled].astype(np.float32)
    scores_norm = np.clip((scores - 1.0) / 7.0, 0.0, 1.0)

    for idx in np.where(labeled)[0]:
        probs[idx, :] = 0.0
        probs[idx, labels[idx] - 1] = 1.0
    p_high = probs[:, 5:].sum(axis=1)
    pred_label = np.argmax(probs, axis=1) + 1

    src = edge_base["src"]
    dst = edge_base["dst"]
    w_raw = edge_base["w_raw"]
    w_norm = edge_base["w_norm"]
    severity = np.maximum(scores[src], scores[dst])
    severity_norm = np.maximum(scores_norm[src], scores_norm[dst])
    risk = w_norm * severity_norm
    p_level = quantile_levels(w_norm, 5)
    c_level = np.clip(np.ceil(severity), 1, 8).astype(np.int64)
    risk_level = p_level * c_level
    edge = {
        "edge_id": edge_base["edge_id"],
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

    edge_rows = []
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
    for idx in range(edge["edge_id"].shape[0]):
        edge_rows.append({field: edge[field][idx].item() for field in fields})
    write_csv(out_dir / f"{year}_edge_risk.csv", edge_rows)
    write_matrix(out_dir / f"{year}_matrix_5x8.csv", matrix_5x8(edge))

    risks = risk
    return {
        "year": year,
        "node_count": int(labels.shape[0]),
        "labeled_nodes": int(labeled.sum()),
        "edge_count": int(risks.shape[0]),
        "risk_mean": float(risks.mean()),
        "risk_p90": float(np.percentile(risks, 90)),
        "risk_p95": float(np.percentile(risks, 95)),
        "risk_p99": float(np.percentile(risks, 99)),
        "risk_max": float(risks.max()),
        "zero_risk_edge_ratio": float(np.mean(risks <= EPS)),
    }


def main() -> None:
    args = parse_args()
    out_dir = args.output_dir / args.name
    out_dir.mkdir(parents=True, exist_ok=True)
    summaries = [
        export_year(args.base_risk_dir, out_dir, "data_2020"),
        export_year(args.base_risk_dir, out_dir, "data_2021"),
    ]
    payload = {
        "name": args.name,
        "base_risk_dir": str(args.base_risk_dir),
        "definition": "labeled nodes use true y; unlabeled nodes use base predictions",
        "risk_mode": "floor_0.01",
        "summaries": summaries,
    }
    (out_dir / "export_summary.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    lines = ["# Label-Risk Oracle Export", ""]
    for summary in summaries:
        lines.append(
            "- {year}: labeled={labeled_nodes}, edges={edge_count}, mean={risk_mean:.6f}, P95={risk_p95:.6f}, max={risk_max:.6f}, zero={zero_risk_edge_ratio:.3%}.".format(
                **summary
            )
        )
    (out_dir / "export_report.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote label-risk oracle to {out_dir}")


if __name__ == "__main__":
    main()
