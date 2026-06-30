"""Export node risks, edge risks, and 5x8 risk matrices from a checkpoint.

By default this script only loads a checkpoint produced by
``train_risk_model.py``. This guarantees that node evaluation and downstream
risk matrices use the identical trained state. Legacy train-and-export
behaviour is available only through the explicit ``--train-before-export``
diagnostic flag.

The loaded model predicts node risk probabilities for both yearly graphs and
converts them into continuous edge risks:

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
        "--checkpoint",
        type=Path,
        default=None,
        help="Checkpoint created by train_risk_model.py (required by default).",
    )
    parser.add_argument(
        "--train-before-export",
        action="store_true",
        help="Explicit legacy mode: train a new model before exporting.",
    )
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
            "ua_gnn",
            "ua_teg_gnn",
            "stable_tail_ua_gnn",
            "stable_tail_ec_gnn",
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
    parser.add_argument("--lambda-nll", type=float, default=0.0)
    parser.add_argument("--lambda-var", type=float, default=0.0)
    parser.add_argument("--ec-delta-max", type=float, default=0.05)
    parser.add_argument("--lambda-edge", type=float, default=0.0)
    parser.add_argument("--lambda-edge-high", type=float, default=0.0)
    parser.add_argument("--lambda-distill", type=float, default=0.0)
    parser.add_argument("--lambda-delta", type=float, default=0.0)
    parser.add_argument("--ec-teacher-epochs", type=int, default=50)
    parser.add_argument("--gamma-unc", type=float, default=0.5)
    parser.add_argument("--logvar-min", type=float, default=-5.0)
    parser.add_argument("--logvar-max", type=float, default=2.0)
    parser.add_argument(
        "--uncertainty-tau",
        type=float,
        default=0.0,
        help="Use S_norm + tau * sigma_norm for uncertainty-aware robust risk.",
    )
    parser.add_argument("--stage1-epochs", type=int, default=0)
    parser.add_argument("--split-b-val-fraction", type=float, default=0.2)
    parser.add_argument(
        "--checkpoint-selection", choices=["best", "last"], default="best"
    )
    parser.add_argument("--checkpoint-score-pr-weight", type=float, default=0.8)
    parser.add_argument("--checkpoint-min-recall", type=float, default=0.0)
    parser.add_argument("--checkpoint-max-high-fn", type=float, default=1.0)
    parser.add_argument("--checkpoint-dir", type=Path, default=None)
    parser.add_argument("--gate-normalized", action="store_true")
    parser.add_argument("--feature-standardization", action="store_true")
    parser.add_argument(
        "--edge-normalization",
        choices=["per_year", "shared_2020", "shared_train"],
        default="per_year",
    )
    parser.add_argument("--experiment-tag", default="")
    return parser.parse_args()


def fit_model(args: argparse.Namespace) -> tuple[dict[str, object], train_risk_model.RiskModel, list[train_risk_model.GraphData]]:
    result = train_risk_model.train(args)
    checkpoint = Path(str(result["checkpoint_path"]))
    _payload, model, graphs = train_risk_model.load_checkpoint_model(
        checkpoint, args.zip
    )
    return result, model, graphs


def load_model_for_export(
    args: argparse.Namespace,
) -> tuple[
    dict[str, object],
    train_risk_model.RiskModel,
    list[train_risk_model.GraphData],
]:
    if args.checkpoint is None:
        if not args.train_before_export:
            raise SystemExit(
                "--checkpoint is required. Use --train-before-export only for explicit legacy diagnostics."
            )
        return fit_model(args)

    payload, model, graphs = train_risk_model.load_checkpoint_model(
        args.checkpoint, args.zip
    )
    model_cfg = payload["model_config"]
    train_cfg = payload["training_config"]
    args.model = str(model_cfg["model"])
    args.hidden_dim = int(model_cfg["hidden_dim"])
    args.dropout = float(model_cfg["dropout"])
    args.gamma_unc = float(model_cfg["gamma_unc"])
    args.logvar_min = float(model_cfg["logvar_min"])
    args.logvar_max = float(model_cfg["logvar_max"])
    args.ec_delta_max = float(model_cfg["ec_delta_max"])
    args.split = str(train_cfg["split"])
    args.seed = int(train_cfg["seed"])
    args.epochs = int(train_cfg["epochs"])

    split_map = payload["split_map"]
    metrics: dict[str, dict[str, float]] = {}
    with torch.no_grad():
        for graph in graphs:
            logits, log_var = model.forward_outputs(graph)
            for split_name in ("train", "val", "test"):
                idx = split_map[graph.year][split_name]
                values = train_risk_model.evaluate(logits, graph.y, idx, log_var)
                if values:
                    metrics[f"{graph.year}_{split_name}"] = values
    result = {
        "model": args.model,
        "split": args.split,
        "seed": args.seed,
        "epochs": args.epochs,
        "best_epoch": int(train_cfg["best_epoch"]),
        "checkpoint_path": str(args.checkpoint.resolve()),
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
        if model.model == "stable_tail_ec_gnn":
            logits, base_norm_t, calibrated_norm_t, delta_t, _probs_t = model.forward_ec_outputs(graph)
            log_var = None
            calibrated_norm = calibrated_norm_t.cpu().numpy()
            delta = delta_t.cpu().numpy()
        else:
            logits, log_var = model.forward_outputs(graph)
            calibrated_norm = None
            delta = None
        probs = F.softmax(logits, dim=1).cpu().numpy()
    levels = np.arange(1, train_risk_model.NUM_CLASSES + 1, dtype=np.float32)
    scores = probs @ levels
    scores_norm = (scores - 1.0) / 7.0
    p_high = probs[:, 5:].sum(axis=1)
    pred_label = np.argmax(probs, axis=1) + 1
    pred = {
        "probs": probs,
        "scores": scores,
        "scores_norm": np.clip(scores_norm, 0.0, 1.0),
        "p_high": p_high,
        "pred_label": pred_label.astype(np.int64),
    }
    if calibrated_norm is not None:
        pred["scores_ec_norm"] = calibrated_norm
        pred["delta_ec"] = delta
    if log_var is not None:
        sigma = np.sqrt(np.exp(log_var.cpu().numpy()))
        sigma_min = float(np.min(sigma))
        sigma_max = float(np.max(sigma))
        pred["sigma"] = sigma
        pred["sigma_norm"] = np.clip(
            (sigma - sigma_min) / (sigma_max - sigma_min + EPS), 0.0, 1.0
        )
    return pred


def write_node_csv(path: Path, labels: np.ndarray, pred: dict[str, np.ndarray]) -> None:
    probs = pred["probs"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        fields = ["node_id", "label", "pred_label", "S_i", "S_i_norm", "P_high"]
        if "scores_ec_norm" in pred:
            fields += ["S_i_ec_norm", "delta_ec"]
        if "sigma" in pred:
            fields += ["sigma", "sigma_norm"]
        fields += [
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
            if "scores_ec_norm" in pred:
                row["S_i_ec_norm"] = float(pred["scores_ec_norm"][node_id])
                row["delta_ec"] = float(pred["delta_ec"][node_id])
            if "sigma" in pred:
                row["sigma"] = float(pred["sigma"][node_id])
                row["sigma_norm"] = float(pred["sigma_norm"][node_id])
            for cls_idx in range(train_risk_model.NUM_CLASSES):
                row[f"p_{cls_idx + 1}"] = float(probs[node_id, cls_idx])
            writer.writerow(row)


def build_edge_risk(
    graph: train_risk_model.GraphData,
    pred: dict[str, np.ndarray],
    risk_mode: str,
    exposure_delta: float,
    uncertainty_tau: float,
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
    base_norm = pred.get("scores_ec_norm", pred["scores_norm"])
    cls_norm = pred["scores_norm"]
    if uncertainty_tau > 0 and "sigma_norm" in pred:
        robust_norm = np.clip(base_norm + uncertainty_tau * pred["sigma_norm"], 0.0, 1.0)
    else:
        robust_norm = base_norm
    severity_norm = np.maximum(robust_norm[src], robust_norm[dst])
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
        "severity_norm_mean": np.maximum(cls_norm[src], cls_norm[dst]),
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
        f"- Source: `{payload['model_source']}`; checkpoint: `{payload.get('checkpoint_path')}`; selected epoch: `{payload.get('best_epoch')}`."
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
    result, model, graphs = load_model_for_export(args)

    if args.risk_mode == "exposure_floor":
        risk_suffix = f"floor_{args.exposure_delta:g}".replace(".", "p")
    else:
        risk_suffix = args.risk_mode
    if args.uncertainty_tau > 0:
        risk_suffix = f"{risk_suffix}_tau_{args.uncertainty_tau:g}".replace(".", "p")
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
        edge = build_edge_risk(
            graph,
            pred,
            args.risk_mode,
            args.exposure_delta,
            args.uncertainty_tau,
        )
        mat = matrix_5x8(edge)

        node_payload = {
            "probs": pred["probs"],
            "scores": pred["scores"],
            "scores_norm": pred["scores_norm"],
            "p_high": pred["p_high"],
            "pred_label": pred["pred_label"],
            "labels": labels,
        }
        if "sigma" in pred:
            node_payload["sigma"] = pred["sigma"]
            node_payload["sigma_norm"] = pred["sigma_norm"]
        np.savez(
            out_dir / f"{graph.year}_node_risk.npz",
            **node_payload,
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
        "uncertainty_tau": args.uncertainty_tau,
        "experiment_tag": args.experiment_tag,
        "checkpoint_path": result.get("checkpoint_path"),
        "best_epoch": result.get("best_epoch", args.epochs),
        "model_source": "trained_during_export" if args.train_before_export else "checkpoint",
        "alpha_ord": args.alpha_ord,
        "alpha_hr": args.alpha_hr,
        "alpha_topk": args.alpha_topk,
        "lambda_nll": args.lambda_nll,
        "lambda_var": args.lambda_var,
        "ec_delta_max": args.ec_delta_max,
        "lambda_edge": args.lambda_edge,
        "lambda_edge_high": args.lambda_edge_high,
        "lambda_distill": args.lambda_distill,
        "lambda_delta": args.lambda_delta,
        "ec_teacher_epochs": args.ec_teacher_epochs,
        "gamma_unc": args.gamma_unc,
        "logvar_min": args.logvar_min,
        "logvar_max": args.logvar_max,
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
