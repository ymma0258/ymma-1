"""Train baseline and TEG-TailGNN risk models.

This script implements the stage-2 experiment scaffold:

- Load 2020/2021 graph data directly from the zip dataset.
- Merge directed edges into an undirected graph using max edge exposure.
- Build split A/B/C masks without treating label 0 as low risk.
- Train MLP, GCN, Weighted-GCN, or TEG-GNN with CE/ordinal/high-risk/top-k losses.
- Report classification and high-risk metrics.

The default arguments run a short smoke test. Increase ``--epochs`` for real
experiments.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import math
import random
import zipfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import (
    average_precision_score,
    cohen_kappa_score,
    f1_score,
    mean_absolute_error,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from torch import nn
from torch.nn import functional as F


DEFAULT_ZIP = Path(r"D:\城市危险化学品运输车辆轨迹数据.zip")
DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\models")
EPS = 1e-12
NUM_CLASSES = 8
RISK_LEVELS = torch.arange(1, NUM_CLASSES + 1, dtype=torch.float32)


@dataclass
class GraphData:
    year: str
    x: torch.Tensor
    y: torch.Tensor
    edge_index: torch.Tensor
    edge_weight: torch.Tensor
    labeled_idx: np.ndarray


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", type=Path, default=DEFAULT_ZIP)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--model",
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
        default="teg_gnn",
    )
    parser.add_argument("--split", choices=["A", "B", "C"], default="A")
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--hidden-dim", type=int, default=64)
    parser.add_argument("--dropout", type=float, default=0.2)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--topk-frac", type=float, default=0.2)
    parser.add_argument("--alpha-ord", type=float, default=0.5)
    parser.add_argument("--alpha-hr", type=float, default=1.0)
    parser.add_argument("--alpha-topk", type=float, default=0.3)
    parser.add_argument("--experiment-tag", default="", help="Optional suffix for output files.")
    parser.add_argument(
        "--stage1-epochs",
        type=int,
        default=0,
        help="Epochs using CE + 0.5 ordinal loss before full loss.",
    )
    return parser.parse_args()


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def read_npy(zf: zipfile.ZipFile, year: str, filename: str) -> np.ndarray:
    matches = [name for name in zf.namelist() if name.endswith(f"{year}/{filename}")]
    if not matches:
        raise FileNotFoundError(f"Could not find {year}/{filename}")
    with zf.open(matches[0]) as handle:
        return np.load(io.BytesIO(handle.read()), allow_pickle=False)


def merge_undirected_max(
    edge_index: np.ndarray, edge_weight: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    merged: dict[tuple[int, int], float] = {}
    weights = edge_weight.reshape(-1).astype(float)
    for (src_raw, dst_raw), weight in zip(edge_index, weights):
        src = int(src_raw)
        dst = int(dst_raw)
        if src == dst:
            continue
        key = (min(src, dst), max(src, dst))
        merged[key] = max(merged.get(key, -math.inf), float(weight))

    undirected_edges: list[tuple[int, int]] = []
    undirected_weights: list[float] = []
    for (src, dst), weight in merged.items():
        undirected_edges.append((src, dst))
        undirected_edges.append((dst, src))
        undirected_weights.append(weight)
        undirected_weights.append(weight)

    return np.asarray(undirected_edges, dtype=np.int64), np.asarray(
        undirected_weights, dtype=np.float32
    )


def normalize_edge_weight(weights: np.ndarray) -> np.ndarray:
    capped = np.minimum(weights.astype(np.float32), np.percentile(weights, 99))
    min_val = float(np.min(capped))
    max_val = float(np.max(capped))
    return (capped - min_val) / (max_val - min_val + EPS)


def load_graph(zf: zipfile.ZipFile, year: str) -> GraphData:
    x = read_npy(zf, year, "data.x.npy").astype(np.float32)
    y = read_npy(zf, year, "data.y.npy").astype(np.int64)
    edge_index = read_npy(zf, year, "data.edge_index.npy")
    edge_attr = read_npy(zf, year, "data.edge_attribute.npy")

    undirected_edges, undirected_weights = merge_undirected_max(edge_index, edge_attr)
    undirected_weights = normalize_edge_weight(undirected_weights)
    labeled_idx = np.flatnonzero(y > 0)

    return GraphData(
        year=year,
        x=torch.from_numpy(x),
        y=torch.from_numpy(y),
        edge_index=torch.from_numpy(undirected_edges.T).long(),
        edge_weight=torch.from_numpy(undirected_weights).float(),
        labeled_idx=labeled_idx,
    )


def stratified_split(
    indices: np.ndarray, labels: np.ndarray, test_size: float, seed: int
) -> tuple[np.ndarray, np.ndarray]:
    return train_test_split(
        indices,
        test_size=test_size,
        random_state=seed,
        stratify=labels[indices],
    )


def build_splits(
    graph20: GraphData, graph21: GraphData, split: str, seed: int
) -> dict[str, dict[str, np.ndarray]]:
    y20 = graph20.y.numpy()
    y21 = graph21.y.numpy()

    if split == "A":
        train20, val20 = stratified_split(graph20.labeled_idx, y20, 0.2, seed)
        return {
            "data_2020": {"train": train20, "val": val20, "test": np.array([], dtype=int)},
            "data_2021": {
                "train": np.array([], dtype=int),
                "val": np.array([], dtype=int),
                "test": graph21.labeled_idx,
            },
        }

    if split == "B":
        train21, test21 = stratified_split(graph21.labeled_idx, y21, 0.5, seed)
        return {
            "data_2020": {
                "train": graph20.labeled_idx,
                "val": np.array([], dtype=int),
                "test": np.array([], dtype=int),
            },
            "data_2021": {
                "train": train21,
                "val": np.array([], dtype=int),
                "test": test21,
            },
        }

    train21, test21 = stratified_split(graph21.labeled_idx, y21, 0.5, seed)
    return {
        "data_2020": {
            "train": np.array([], dtype=int),
            "val": np.array([], dtype=int),
            "test": np.array([], dtype=int),
        },
        "data_2021": {
            "train": train21,
            "val": np.array([], dtype=int),
            "test": test21,
        },
    }


def normalize_messages(
    num_nodes: int, edge_index: torch.Tensor, edge_weight: torch.Tensor | None
) -> torch.Tensor:
    src, dst = edge_index
    if edge_weight is None:
        weight = torch.ones(src.shape[0], dtype=torch.float32, device=edge_index.device)
    else:
        weight = edge_weight.to(edge_index.device)
    degree = torch.zeros(num_nodes, dtype=torch.float32, device=edge_index.device)
    degree.index_add_(0, dst, weight)
    return weight / (degree[dst] + EPS)


class GraphConv(nn.Module):
    def __init__(self, dim: int, weighted: bool) -> None:
        super().__init__()
        self.linear = nn.Linear(dim, dim)
        self.weighted = weighted

    def forward(
        self, x: torch.Tensor, edge_index: torch.Tensor, edge_weight: torch.Tensor
    ) -> torch.Tensor:
        src, dst = edge_index
        weights = edge_weight if self.weighted else None
        norm = normalize_messages(x.shape[0], edge_index, weights)
        msg = self.linear(x[src]) * norm.unsqueeze(1)
        out = torch.zeros_like(msg.new_zeros((x.shape[0], msg.shape[1])))
        out.index_add_(0, dst, msg)
        return out


class EdgeGatedConv(nn.Module):
    def __init__(self, dim: int) -> None:
        super().__init__()
        self.msg = nn.Linear(dim, dim)
        self.edge_gate = nn.Linear(1, dim)
        self.node_gate = nn.Linear(2 * dim, dim)

    def forward(
        self, x: torch.Tensor, edge_index: torch.Tensor, edge_weight: torch.Tensor
    ) -> torch.Tensor:
        src, dst = edge_index
        edge_term = self.edge_gate(edge_weight.unsqueeze(1))
        node_term = self.node_gate(torch.cat([x[src], x[dst]], dim=1))
        gate = torch.sigmoid(edge_term + node_term)
        norm = normalize_messages(x.shape[0], edge_index, edge_weight)
        msg = gate * self.msg(x[src]) * norm.unsqueeze(1)
        out = torch.zeros_like(msg.new_zeros((x.shape[0], msg.shape[1])))
        out.index_add_(0, dst, msg)
        return out


class EdgeGATConv(nn.Module):
    def __init__(self, dim: int) -> None:
        super().__init__()
        self.linear = nn.Linear(dim, dim)
        self.attn = nn.Linear(2 * dim + 1, 1)
        self.leaky_relu = nn.LeakyReLU(0.2)

    def forward(
        self, x: torch.Tensor, edge_index: torch.Tensor, edge_weight: torch.Tensor
    ) -> torch.Tensor:
        src, dst = edge_index
        h = self.linear(x)
        attn_input = torch.cat([h[src], h[dst], edge_weight.unsqueeze(1)], dim=1)
        scores = self.leaky_relu(self.attn(attn_input)).squeeze(1)

        max_per_dst = torch.full(
            (x.shape[0],), -torch.inf, dtype=scores.dtype, device=scores.device
        )
        max_per_dst.scatter_reduce_(0, dst, scores, reduce="amax", include_self=True)
        exp_scores = torch.exp(scores - max_per_dst[dst])
        denom = torch.zeros(x.shape[0], dtype=scores.dtype, device=scores.device)
        denom.index_add_(0, dst, exp_scores)
        alpha = exp_scores / (denom[dst] + EPS)

        msg = h[src] * alpha.unsqueeze(1)
        out = torch.zeros_like(h)
        out.index_add_(0, dst, msg)
        return out


class RiskModel(nn.Module):
    def __init__(self, model: str, in_dim: int, hidden_dim: int, dropout: float) -> None:
        super().__init__()
        self.model = model
        self.encoder = nn.Linear(in_dim, hidden_dim)
        self.dropout = nn.Dropout(dropout)
        self.mu: nn.Parameter | None = None

        if model == "mlp":
            self.layers = nn.ModuleList()
        elif model == "gcn":
            self.layers = nn.ModuleList(
                [GraphConv(hidden_dim, weighted=False), GraphConv(hidden_dim, weighted=False)]
            )
        elif model == "weighted_gcn":
            self.layers = nn.ModuleList(
                [GraphConv(hidden_dim, weighted=True), GraphConv(hidden_dim, weighted=True)]
            )
        elif model == "edge_gat":
            self.layers = nn.ModuleList([EdgeGATConv(hidden_dim), EdgeGATConv(hidden_dim)])
        elif model == "teg_gnn":
            self.layers = nn.ModuleList([EdgeGatedConv(hidden_dim), EdgeGatedConv(hidden_dim)])
        elif model in {
            "gcn_teg_concat",
            "gcn_teg_residual_fixed",
            "gcn_teg_residual_learnable",
        }:
            self.gcn_layers = nn.ModuleList(
                [GraphConv(hidden_dim, weighted=False), GraphConv(hidden_dim, weighted=False)]
            )
            self.teg_layers = nn.ModuleList(
                [EdgeGatedConv(hidden_dim), EdgeGatedConv(hidden_dim)]
            )
            self.layers = nn.ModuleList()
            if model == "gcn_teg_concat":
                self.fusion = nn.Sequential(
                    nn.Linear(2 * hidden_dim, hidden_dim),
                    nn.ReLU(),
                    nn.Dropout(dropout),
                )
            elif model == "gcn_teg_residual_learnable":
                self.mu = nn.Parameter(torch.tensor(0.1, dtype=torch.float32))
        else:
            raise ValueError(f"Unknown model: {model}")

        self.classifier = nn.Linear(hidden_dim, NUM_CLASSES)

    def _run_layers(
        self,
        h: torch.Tensor,
        layers: nn.ModuleList,
        graph: GraphData,
    ) -> torch.Tensor:
        for layer in layers:
            residual = h
            h = F.relu(layer(h, graph.edge_index, graph.edge_weight))
            h = self.dropout(h + residual)
        return h

    def forward(self, graph: GraphData) -> torch.Tensor:
        h = F.relu(self.encoder(graph.x))
        if self.model == "mlp":
            h = self.dropout(h)
            return self.classifier(h)

        if self.model in {
            "gcn_teg_concat",
            "gcn_teg_residual_fixed",
            "gcn_teg_residual_learnable",
        }:
            h_gcn = self._run_layers(h, self.gcn_layers, graph)
            h_teg = self._run_layers(h, self.teg_layers, graph)
            if self.model == "gcn_teg_concat":
                h = self.fusion(torch.cat([h_gcn, h_teg], dim=1))
            else:
                mu = self.mu if self.mu is not None else h.new_tensor(0.1)
                h = h_gcn + mu * h_teg
            return self.classifier(h)

        for layer in self.layers:
            residual = h
            h = F.relu(layer(h, graph.edge_index, graph.edge_weight))
            h = self.dropout(h + residual)
        return self.classifier(h)


def class_weights(graphs: list[GraphData], split_map: dict[str, dict[str, np.ndarray]]) -> torch.Tensor:
    counts = np.zeros(NUM_CLASSES, dtype=np.float32)
    by_year = {graph.year: graph for graph in graphs}
    for year, splits in split_map.items():
        idx = splits["train"]
        if idx.size == 0:
            continue
        labels = by_year[year].y.numpy()[idx]
        for label in labels:
            counts[int(label) - 1] += 1
    weights = 1.0 / np.log1p(np.maximum(counts, 1.0))
    weights = weights / weights.mean()
    return torch.from_numpy(weights.astype(np.float32))


def risk_scores(probs: torch.Tensor) -> torch.Tensor:
    levels = RISK_LEVELS.to(probs.device)
    return torch.sum(probs * levels, dim=1)


def topk_loss(losses: torch.Tensor, frac: float) -> torch.Tensor:
    if losses.numel() == 0:
        return losses.new_tensor(0.0)
    k = max(1, int(math.ceil(losses.numel() * frac)))
    return torch.topk(losses, k=k, largest=True).values.mean()


def compute_loss(
    logits: torch.Tensor,
    labels: torch.Tensor,
    idx: np.ndarray,
    weights: torch.Tensor,
    args: argparse.Namespace,
    full_loss: bool,
    pos_weight: float,
) -> torch.Tensor:
    if idx.size == 0:
        return logits.new_tensor(0.0)

    idx_t = torch.from_numpy(idx).long()
    y = labels[idx_t] - 1
    selected = logits[idx_t]

    ce_each = F.cross_entropy(selected, y, weight=weights, reduction="none")
    ce = ce_each.mean()
    probs = F.softmax(selected, dim=1)
    s_i = risk_scores(probs)
    ord_loss = torch.mean(torch.abs(s_i - (y.float() + 1.0)))

    if not full_loss:
        return ce + 0.5 * ord_loss

    z = (y >= 5).float()
    p_high = torch.clamp(probs[:, 5:].sum(dim=1), EPS, 1.0 - EPS)
    hr = F.binary_cross_entropy(
        p_high,
        z,
        weight=torch.where(z > 0, torch.full_like(z, pos_weight), torch.ones_like(z)),
    )
    tail = topk_loss(ce_each, args.topk_frac)
    return ce + args.alpha_ord * ord_loss + args.alpha_hr * hr + args.alpha_topk * tail


def evaluate(logits: torch.Tensor, labels: torch.Tensor, idx: np.ndarray) -> dict[str, float]:
    if idx.size == 0:
        return {}
    idx_t = torch.from_numpy(idx).long()
    y_true = labels[idx_t].numpy().astype(int)
    probs = F.softmax(logits[idx_t], dim=1).detach().numpy()
    y_pred = np.argmax(probs, axis=1) + 1
    s_pred = np.sum(probs * np.arange(1, NUM_CLASSES + 1), axis=1)

    high_true = y_true >= 6
    high_pred = y_pred >= 6
    high_scores = probs[:, 5:].sum(axis=1)

    if np.unique(high_true).size > 1:
        pr_auc = float(average_precision_score(high_true.astype(int), high_scores))
    else:
        pr_auc = float("nan")

    y_bin = label_binarize(y_true, classes=np.arange(1, NUM_CLASSES + 1))
    pred_bin = label_binarize(y_pred, classes=np.arange(1, NUM_CLASSES + 1))
    del y_bin, pred_bin  # Kept explicit: multiclass PR-AUC is not a main smoke metric.

    high_count = max(1, int(high_true.sum()))
    high_fn_rate = float(np.logical_and(high_true, ~high_pred).sum() / high_count)

    return {
        "macro_f1": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "weighted_f1": float(f1_score(y_true, y_pred, average="weighted", zero_division=0)),
        "mae": float(mean_absolute_error(y_true, s_pred)),
        "qwk": float(cohen_kappa_score(y_true, y_pred, weights="quadratic")),
        "recall_6_8": float(recall_score(high_true, high_pred, zero_division=0)),
        "precision_6_8": float(precision_score(high_true, high_pred, zero_division=0)),
        "pr_auc_high": pr_auc,
        "high_fn_rate": high_fn_rate,
    }


def train(args: argparse.Namespace) -> dict[str, object]:
    set_seed(args.seed)
    with zipfile.ZipFile(args.zip) as zf:
        graph20 = load_graph(zf, "data_2020")
        graph21 = load_graph(zf, "data_2021")

    graphs = [graph20, graph21]
    by_year = {graph.year: graph for graph in graphs}
    split_map = build_splits(graph20, graph21, args.split, args.seed)

    model = RiskModel(args.model, graph20.x.shape[1], args.hidden_dim, args.dropout)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    weights = class_weights(graphs, split_map)

    train_labels = []
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
            total_loss = total_loss + compute_loss(
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
                result = evaluate(logits, graph.y, idx)
                if result:
                    metrics[f"{graph.year}_{split_name}"] = result

    return {
        "model": args.model,
        "split": args.split,
        "seed": args.seed,
        "epochs": args.epochs,
        "experiment_tag": getattr(args, "experiment_tag", ""),
        "alpha_ord": args.alpha_ord,
        "alpha_hr": args.alpha_hr,
        "alpha_topk": args.alpha_topk,
        "topk_frac": args.topk_frac,
        "stage1_epochs": args.stage1_epochs,
        "pos_weight": pos_weight,
        "history": history,
        "metrics": metrics,
        "split_sizes": {
            year: {name: int(idx.size) for name, idx in splits.items()}
            for year, splits in split_map.items()
        },
    }


def write_outputs(args: argparse.Namespace, result: dict[str, object]) -> None:
    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{args.model}_split{args.split}_seed{args.seed}_epochs{args.epochs}"
    tag = getattr(args, "experiment_tag", "")
    if tag:
        stem = f"{stem}_{tag}"
    json_path = args.output_dir / f"{stem}.json"
    csv_path = args.output_dir / f"{stem}_metrics.csv"
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    rows: list[dict[str, object]] = []
    metrics = result["metrics"]
    assert isinstance(metrics, dict)
    for split_name, values in metrics.items():
        row = {"split": split_name}
        assert isinstance(values, dict)
        row.update(values)
        rows.append(row)

    if rows:
        with csv_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    print(f"Wrote {json_path}")
    if rows:
        print(f"Wrote {csv_path}")


def main() -> None:
    args = parse_args()
    result = train(args)
    write_outputs(args, result)
    print(json.dumps(result["metrics"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
