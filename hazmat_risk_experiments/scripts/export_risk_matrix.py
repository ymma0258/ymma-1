"""Export node risks, edge risks, and 5x8 risk matrices.

This script trains one configured risk model, predicts node risk probabilities
for both yearly graphs, and converts them into continuous edge risks:

    R_ij = w_ij * max(S_i_norm, S_j_norm)

It also creates a 5x8 trajectory-exposure/severity matrix for explanation.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import torch
from torch.nn import functional as F


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import train_risk_model  # noqa: E402


DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\risk_matrices")
EPS = 1e-12


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", type=Path, default=train_risk_model.DEFAULT_ZIP)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--model",
        default="teg_gnn",
        choices=[
            "mlp",
            "gcn",
            "weighted_gcn",
            "edge_gat",
            "teg_gnn",
            "gcn_teg_concat",
            "gcn_teg_residual_fixed",
            "gcn_teg_residual_learnable",
        ],
    )
    parser.add_argument("--split", default="B", choices=["A", "B", "C"])
    parser.add_argument(
        "--risk-mode",
        choices=["raw", "exposure_floor", "positive_only"],
        default="raw",
    )
    parser.add_argument("--exposure-delta", type=float, default=0.01)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--hidden-dim", type=int, default=64)
    parser.add_argument("--dropout", type=float, default=0.2)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--topk-frac", type=float, default=0.2)
    parser.add_argument("--alpha-ord", type=float, default=0.5)
    parser.add_argument("--alpha-hr", type=float, default=1.0)
    parser.add_argument("--alpha-topk", type=float, default=0.3)
    parser.add_argument("--stage1-epochs", type=int, default=0)
    parser.add_argument("--experiment-tag", default="")
    return parser.parse_args()


def fit_model(args: argparse.Namespace) -> tuple[dict[str, object], train_risk_model.RiskModel, list[train_risk_model.GraphData]]:
    train_risk_model.set_seed(args.seed)
    import zipfile

    with zipfile.ZipFile(args.zip) as zf:
        graph20 = train_risk_model.load_graph(zf, "data_2020")
        graph21 = train_risk_model.load_graph(zf, "data_2021")

    graphs = [graph20, graph21]
    split_map = train_risk_model.build_splits(graph20, graph21, args.split, args.seed)
    model = train_risk_model.RiskModel(args.model, graph20.x.shape[1], args.hidden_dim, args.dropout)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    weights = train_risk_model.class_weights(graphs, split_map)

    train_labels: list[int] = []
    for graph in graphs:
        idx = split_map[graph.year]["train"]
        if idx.size:
            train_labels.extend(graph.y.numpy()[idx].tolist())

    high_pos = sum(1 for label in train_labels if label >= 6)
    high_neg = sum(1 for label in train_labels if 0 < label < 6)
    pos_weight = min(high_neg / max(high_pos, 1), 5.0)

    history: list[dict[str, float]] = []
    for epoch in range(args.epochs):
        model.train()
        optimizer.zero_grad()
        total_loss = torch.tensor(0.0)
        full_loss = epoch >= args.stage1_epochs
        for graph in graphs:
            logits = model(graph)
            total_loss = total_loss + train_risk_model.compute_loss(
                logits,
                graph.y,
                split_map[graph.year]["train"],
                weights,
                args,
                full_loss,
                pos_weight,
            )
        total_loss.backward()
        optimizer.step()
        history.append({"epoch": epoch + 1, "loss": float(total_loss.detach())})

    model.eval()
    metrics: dict[str, dict[str, float]] = {}
    with torch.no_grad():
        for graph in graphs:
            logits = model(graph)
            for split_name in ("train", "val", "test"):
                idx = split_map[graph.year][split_name]
                result = train_risk_model.evaluate(logits, graph.y, idx)
                if result:
                    metrics[f"{graph.year}_{split_name}"] = result

    result: dict[str, object] = {
        "model": args.model,
        "split": args.split,
        "seed": args.seed,
        "epochs": args.epochs,
        "pos_weight": pos_weight,
        "history": history,
        "metrics": metrics,
        "split_sizes": {
            year: {name: int(idx.size) for name, idx in splits.items()}
            for year, splits in split_map.items()
        },
    }
    return result, model, graphs


def quantile_levels(values: np.ndarray, num_levels: int) -> np.ndarray:
    """Return near-equal-frequency levels.

    Edge exposure has many repeated values in this dataset. Threshold-based
    quantile cuts can collapse all rows into the last bin when several
    thresholds are identical, so the display matrix uses rank-based bins.
    Continuous downstream risk still uses the original normalized values.
    """

    order = np.argsort(values, kind="mergesort")
    ranks = np.empty_like(order)
    ranks[order] = np.arange(values.shape[0])
    levels = np.floor(ranks * num_levels / max(1, values.shape[0])).astype(np.int64) + 1
    return np.clip(levels, 1, num_levels)


def unique_undirected_edges(graph: train_risk_model.GraphData) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    edge_index = graph.edge_index.numpy().T
    weights = graph.edge_weight.numpy()
    keep = edge_index[:, 0] < edge_index[:, 1]
    undirected = edge_index[keep]
    undirected_weights = weights[keep]
    edge_ids = np.arange(undirected.shape[0], dtype=np.int64)
    return edge_ids, undirected, undirected_weights


def node_predictions(model: train_risk_model.RiskModel, graph: train_risk_model.GraphData) -> dict[str, np.ndarray]:
    with torch.no_grad():
        logits = model(graph)
        probs = F.softmax(logits, dim=1).cpu().numpy()
    levels = np.arange(1, train_risk_model.NUM_CLASSES + 1, dtype=np.float32)
    scores = probs @ levels
    scores_norm = (scores - 1.0) / 7.0
    p_high = probs[:, 5:].sum(axis=1)
    pred_label = np.argmax(probs, axis=1) + 1
    return {
        "probs": probs,
        "scores": scores,
        "scores_norm": np.clip(scores_norm, 0.0, 1.0),
        "p_high": p_high,
        "pred_label": pred_label.astype(np.int64),
    }


def write_node_csv(path: Path, labels: np.ndarray, pred: dict[str, np.ndarray]) -> None:
    probs = pred["probs"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        fields = ["node_id", "label", "pred_label", "S_i", "S_i_norm", "P_high"] + [
            f"p_{idx}" for idx in range(1, train_risk_model.NUM_CLASSES + 1)
        ]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for node_id in range(labels.shape[0]):
            row = {
                "node_id": node_id,
                "label": int(labels[node_id]),
                "pred_label": int(pred["pred_label"][node_id]),
                "S_i": float(pred["scores"][node_id]),
                "S_i_norm": float(pred["scores_norm"][node_id]),
                "P_high": float(pred["p_high"][node_id]),
            }
            for cls_idx in range(train_risk_model.NUM_CLASSES):
                row[f"p_{cls_idx + 1}"] = float(probs[node_id, cls_idx])
            writer.writerow(row)


def build_edge_risk(
    graph: train_risk_model.GraphData,
    pred: dict[str, np.ndarray],
    risk_mode: str,
    exposure_delta: float,
) -> dict[str, np.ndarray]:
    edge_ids, edges, weights = unique_undirected_edges(graph)
    raw_weights = weights.copy()

    if risk_mode == "positive_only":
        keep = raw_weights > EPS
        edge_ids = edge_ids[keep]
        edges = edges[keep]
        weights = weights[keep]
        raw_weights = raw_weights[keep]
    elif risk_mode == "exposure_floor":
        weights = exposure_delta + (1.0 - exposure_delta) * weights
    elif risk_mode != "raw":
        raise ValueError(f"Unknown risk mode: {risk_mode}")

    src = edges[:, 0]
    dst = edges[:, 1]
    severity_cont = np.maximum(pred["scores"][src], pred["scores"][dst])
    severity_norm = np.maximum(pred["scores_norm"][src], pred["scores_norm"][dst])
    risk = weights * severity_norm
    p_level = quantile_levels(weights, 5)
    c_level = np.clip(np.ceil(severity_cont), 1, 8).astype(np.int64)
    risk_level = p_level * c_level
    return {
        "edge_id": edge_ids,
        "src": src,
        "dst": dst,
        "w_raw": raw_weights,
        "w_norm": weights,
        "severity": severity_cont,
        "severity_norm": severity_norm,
        "R_ij": risk,
        "P_level": p_level,
        "C_level": c_level,
        "RiskLevel": risk_level,
    }


def write_edge_csv(path: Path, edge: dict[str, np.ndarray]) -> None:
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
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for idx in range(edge["edge_id"].shape[0]):
            writer.writerow({field: edge[field][idx].item() for field in fields})


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


def top_nodes(labels: np.ndarray, pred: dict[str, np.ndarray], top_n: int = 20) -> list[dict[str, float | int]]:
    order = np.argsort(pred["scores_norm"])[::-1][:top_n]
    rows: list[dict[str, float | int]] = []
    for rank, idx in enumerate(order, start=1):
        rows.append(
            {
                "rank": rank,
                "node_id": int(idx),
                "label": int(labels[idx]),
                "pred_label": int(pred["pred_label"][idx]),
                "S_i": float(pred["scores"][idx]),
                "S_i_norm": float(pred["scores_norm"][idx]),
                "P_high": float(pred["p_high"][idx]),
            }
        )
    return rows


def write_rows_csv(path: Path, rows: list[dict[str, float | int]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


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


def write_report(path: Path, payload: dict[str, object]) -> None:
    lines = ["# Risk Matrix Export Report", ""]
    lines.append("## Model")
    lines.append("")
    lines.append(
        f"- Model: `{payload['model']}`; split: `{payload['split']}`; seed: `{payload['seed']}`; epochs: `{payload['epochs']}`."
    )
    lines.append(
        f"- Risk mode: `{payload['risk_mode']}`; exposure delta: `{payload['exposure_delta']}`."
    )
    lines.append("")
    lines.append("## Metrics")
    lines.append("")
    metrics = payload["metrics"]
    assert isinstance(metrics, dict)
    for split_name, values in metrics.items():
        assert isinstance(values, dict)
        lines.append(
            f"- `{split_name}`: Macro-F1={values.get('macro_f1', float('nan')):.4f}, "
            f"MAE={values.get('mae', float('nan')):.4f}, QWK={values.get('qwk', float('nan')):.4f}, "
            f"Recall@6-8={values.get('recall_6_8', float('nan')):.4f}."
        )
    lines.append("")
    lines.append("## Edge Risk Summary")
    lines.append("")
    summaries = payload["risk_summaries"]
    assert isinstance(summaries, dict)
    for year, summary in summaries.items():
        assert isinstance(summary, dict)
        lines.append(
            f"- `{year}`: edges={summary['edge_count']}, mean={summary['risk_mean']:.6f}, "
            f"P75={summary['risk_p75']:.6f}, P90={summary['risk_p90']:.6f}, "
            f"P95={summary['risk_p95']:.6f}, P99={summary['risk_p99']:.6f}, "
            f"max={summary['risk_max']:.6f}, zero_ratio={summary['zero_risk_edge_ratio']:.6f}."
        )
    lines.append("")
    lines.append("The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    result, model, graphs = fit_model(args)

    if args.risk_mode == "exposure_floor":
        risk_suffix = f"floor_{args.exposure_delta:g}".replace(".", "p")
    else:
        risk_suffix = args.risk_mode
    tag_suffix = f"_{args.experiment_tag}" if args.experiment_tag else ""
    model_dir_name = (
        f"{args.model}_split{args.split}_seed{args.seed}_epochs{args.epochs}{tag_suffix}_{risk_suffix}"
    )
    out_dir = args.output_dir / model_dir_name
    out_dir.mkdir(parents=True, exist_ok=True)

    risk_summaries: dict[str, object] = {}
    for graph in graphs:
        labels = graph.y.numpy().astype(np.int64)
        pred = node_predictions(model, graph)
        edge = build_edge_risk(graph, pred, args.risk_mode, args.exposure_delta)
        mat = matrix_5x8(edge)

        np.savez(
            out_dir / f"{graph.year}_node_risk.npz",
            probs=pred["probs"],
            scores=pred["scores"],
            scores_norm=pred["scores_norm"],
            p_high=pred["p_high"],
            pred_label=pred["pred_label"],
            labels=labels,
        )
        np.savez(out_dir / f"{graph.year}_edge_risk.npz", **edge)
        write_node_csv(out_dir / f"{graph.year}_node_risk.csv", labels, pred)
        write_edge_csv(out_dir / f"{graph.year}_edge_risk.csv", edge)
        write_matrix_csv(out_dir / f"{graph.year}_matrix_5x8.csv", mat)
        write_rows_csv(out_dir / f"{graph.year}_top20_nodes.csv", top_nodes(labels, pred))
        write_rows_csv(out_dir / f"{graph.year}_top20_edges.csv", top_edges(edge))
        risk_summaries[graph.year] = risk_summary(edge, mat)

    payload = {
        "model": args.model,
        "split": args.split,
        "seed": args.seed,
        "epochs": args.epochs,
        "risk_mode": args.risk_mode,
        "exposure_delta": args.exposure_delta,
        "experiment_tag": args.experiment_tag,
        "alpha_ord": args.alpha_ord,
        "alpha_hr": args.alpha_hr,
        "alpha_topk": args.alpha_topk,
        "metrics": result["metrics"],
        "split_sizes": result["split_sizes"],
        "risk_summaries": risk_summaries,
    }
    (out_dir / "export_summary.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_report(out_dir / "export_report.md", payload)
    print(f"Wrote risk matrix export to {out_dir}")


if __name__ == "__main__":
    main()
