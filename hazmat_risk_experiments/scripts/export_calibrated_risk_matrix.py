"""Export calibrated edge-risk matrices from an existing node-risk export."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from pathlib import Path

import numpy as np


DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\risk_matrices")
EPS = 1e-12


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-risk-dir", type=Path, required=True)
    parser.add_argument("--year", default="data_2021", choices=["data_2020", "data_2021"])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--batch-name", required=True)
    parser.add_argument("--theta1", type=float, default=1.0)
    parser.add_argument("--theta2", type=float, required=True)
    parser.add_argument("--theta3", type=float, required=True)
    return parser.parse_args()


def quantile_levels(values: np.ndarray, num_levels: int) -> np.ndarray:
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty_like(order)
    ranks[order] = np.arange(values.shape[0])
    levels = np.floor(ranks * num_levels / max(1, values.shape[0])).astype(np.int64) + 1
    return np.clip(levels, 1, num_levels)


def normalize(values: np.ndarray) -> np.ndarray:
    return (values - values.min()) / (values.max() - values.min() + EPS)


def build_calibrated_edge(
    edge_data: np.lib.npyio.NpzFile,
    node_data: np.lib.npyio.NpzFile,
    theta1: float,
    theta2: float,
    theta3: float,
) -> dict[str, np.ndarray]:
    src = edge_data["src"].astype(np.int64)
    dst = edge_data["dst"].astype(np.int64)
    scores_norm = np.asarray(node_data["scores_norm"], dtype=float)
    scores = np.asarray(node_data["scores"], dtype=float)
    p_high = np.asarray(node_data["p_high"], dtype=float)
    w_norm = np.asarray(edge_data["w_norm"], dtype=float)

    max_score = np.maximum(scores_norm[src], scores_norm[dst])
    max_phigh = np.maximum(p_high[src], p_high[dst])
    avg_score = (scores_norm[src] + scores_norm[dst]) / 2.0
    combined = theta1 * max_score + theta2 * max_phigh + theta3 * avg_score
    calibrated = normalize(combined)
    risk = w_norm * calibrated
    severity_cont = np.maximum(scores[src], scores[dst])
    p_level = quantile_levels(w_norm, 5)
    c_level = np.clip(np.ceil(severity_cont), 1, 8).astype(np.int64)

    return {
        "edge_id": edge_data["edge_id"],
        "src": src,
        "dst": dst,
        "w_raw": edge_data["w_raw"],
        "w_norm": w_norm,
        "severity": severity_cont,
        "severity_norm": calibrated,
        "severity_base_max": max_score,
        "severity_high_tail": max_phigh,
        "severity_avg": avg_score,
        "R_ij": risk,
        "P_level": p_level,
        "C_level": c_level,
        "RiskLevel": p_level * c_level,
    }


def matrix_5x8(edge: dict[str, np.ndarray]) -> np.ndarray:
    mat = np.zeros((5, 8), dtype=np.int64)
    for p_level, c_level in zip(edge["P_level"], edge["C_level"]):
        mat[int(p_level) - 1, int(c_level) - 1] += 1
    return mat


def write_edge_csv(path: Path, edge: dict[str, np.ndarray]) -> None:
    fields = [
        "edge_id",
        "src",
        "dst",
        "w_raw",
        "w_norm",
        "severity",
        "severity_norm",
        "severity_base_max",
        "severity_high_tail",
        "severity_avg",
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


def write_matrix_csv(path: Path, mat: np.ndarray) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["P_level"] + [f"C_{idx}" for idx in range(1, 9)])
        for p_idx in range(5):
            writer.writerow([p_idx + 1] + mat[p_idx].tolist())


def main() -> None:
    args = parse_args()
    out_dir = args.output_dir / args.batch_name
    out_dir.mkdir(parents=True, exist_ok=True)

    node_src = args.source_risk_dir / f"{args.year}_node_risk.npz"
    edge_src = args.source_risk_dir / f"{args.year}_edge_risk.npz"
    node_data = np.load(node_src)
    edge_data = np.load(edge_src)
    edge = build_calibrated_edge(
        edge_data,
        node_data,
        args.theta1,
        args.theta2,
        args.theta3,
    )

    shutil.copy2(node_src, out_dir / f"{args.year}_node_risk.npz")
    np.savez_compressed(out_dir / f"{args.year}_edge_risk.npz", **edge)
    write_edge_csv(out_dir / f"{args.year}_edge_risk.csv", edge)
    write_matrix_csv(out_dir / f"{args.year}_risk_matrix_5x8.csv", matrix_5x8(edge))
    (out_dir / "calibration_meta.json").write_text(
        json.dumps(
            {
                "source_risk_dir": str(args.source_risk_dir),
                "year": args.year,
                "formula": "R=w_floor*Normalize(theta1*max(S)+theta2*max(P_high)+theta3*avg(S))",
                "theta1": args.theta1,
                "theta2": args.theta2,
                "theta3": args.theta3,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote calibrated risk matrix to {out_dir}")


if __name__ == "__main__":
    main()
