"""Train baseline and TEG-TailGNN risk models.

This script implements the stage-2 experiment scaffold:

- Load 2020/2021 graph data directly from the zip dataset.
- Merge directed edges into an undirected graph using max edge exposure.
- Build split A/B/C masks without treating label 0 as low risk.
- Train MLP, GCN, GAT, GraphSAGE, Weighted-GCN, or TEG-GNN with
  CE/ordinal/high-risk/top-k losses.
- Report classification and high-risk metrics.
- Optionally train uncertainty-aware GNN variants that estimate an ordinal
  risk mean and a per-node predictive variance.
- Train a Stable-Tail UA-GNN variant where uncertainty gates the TEG branch
  instead of directly amplifying tail risk.
- Train a Stable-Tail EC-GNN variant that keeps the Stable-Tail node
  classifier and adds a small edge-risk calibration head for downstream
  risk-matrix construction.

The default arguments run a short smoke test. Increase ``--epochs`` for real
experiments.
"""

from __future__ import annotations

import argparse
import copy
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

# Keep the historical experiment keys loadable: published checkpoints contain
# these strings in ``model_config``.  The paper-facing aliases below provide
# unambiguous entries for the new comparison and ablation experiments.
MODEL_CHOICES = [
    "mlp",
    "gcn",
    "gcn_only",
    "weighted_gcn",
    "gat",
    "edge_gat",
    "graphsage",
    "graphsage_teg_concat",
    "graphsage_teg_gate",
    "sgformer_adapted",
    "sgformer_teg_concat",
    "sgformer_teg_gate",
    "gradformer_adapted",
    "teg_gnn",
    "teg_only",
    "gcn_teg_concat",
    "stable_tail_gnn",
    "gcn_teg_residual_fixed",
    "gcn_teg_residual_learnable",
    "ua_gnn",
    "ua_teg_gnn",
    "stable_tail_ua_gnn",
    "stable_tail_ec_gnn",
]

PAPER_MODEL_NAMES = {
    "gcn": "GCN",
    "gcn_only": "GCN-only branch",
    "gat": "GAT",
    "graphsage": "GraphSAGE",
    "graphsage_teg_concat": "GraphSAGE-TEG-Concat",
    "graphsage_teg_gate": "GraphSAGE-TEG-Gate",
    "sgformer_adapted": "SGFormer-adapted",
    "sgformer_teg_concat": "SGFormer-TEG-Concat",
    "sgformer_teg_gate": "SGFormer-TEG-Gate",
    "gradformer_adapted": "Gradformer-adapted",
    "teg_gnn": "TEG-only",
    "teg_only": "TEG-only",
    "gcn_teg_concat": "Stable-Tail GNN",
    "stable_tail_gnn": "Stable-Tail GNN",
}


@dataclass
class GraphData:
    year: str
    x: torch.Tensor
    y: torch.Tensor
    edge_index: torch.Tensor
    edge_weight: torch.Tensor
    labeled_idx: np.ndarray


@dataclass
class PreprocessingState:
    """Training-fitted transforms reused verbatim during checkpoint export."""

    edge_mode: str
    edge_min: float | None = None
    edge_p99: float | None = None
    feature_mean: torch.Tensor | None = None
    feature_std: torch.Tensor | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", type=Path, default=DEFAULT_ZIP)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--model",
        choices=MODEL_CHOICES,
        default="teg_gnn",
    )
    parser.add_argument("--split", choices=["A", "B", "C"], default="A")
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--hidden-dim", type=int, default=64)
    parser.add_argument("--dropout", type=float, default=0.2)
    parser.add_argument("--gradformer-max-hops", type=int, default=3)
    parser.add_argument("--gradformer-lambda-init", type=float, default=1.0)
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
    parser.add_argument(
        "--ec-teacher-epochs",
        type=int,
        default=50,
        help="Epochs for the frozen Stable-Tail teacher used by stable_tail_ec_gnn.",
    )
    parser.add_argument(
        "--gamma-unc",
        type=float,
        default=0.5,
        help="Strength of uncertainty suppression in stable_tail_ua_gnn.",
    )
    parser.add_argument("--logvar-min", type=float, default=-5.0)
    parser.add_argument("--logvar-max", type=float, default=2.0)
    parser.add_argument("--experiment-tag", default="", help="Optional suffix for output files.")
    parser.add_argument(
        "--stage1-epochs",
        type=int,
        default=0,
        help="Epochs using CE + 0.5 ordinal loss before full loss.",
    )
    parser.add_argument(
        "--split-b-val-fraction",
        type=float,
        default=0.2,
        help="Fraction of Split B's 2021 adaptation pool reserved for validation.",
    )
    parser.add_argument(
        "--checkpoint-selection",
        choices=["best", "last"],
        default="best",
        help="Select the best validation epoch or preserve legacy last-epoch behaviour.",
    )
    parser.add_argument("--checkpoint-score-pr-weight", type=float, default=0.8)
    parser.add_argument("--checkpoint-min-recall", type=float, default=0.0)
    parser.add_argument("--checkpoint-max-high-fn", type=float, default=1.0)
    parser.add_argument(
        "--checkpoint-dir",
        type=Path,
        default=None,
        help="Checkpoint directory; defaults to OUTPUT_DIR/checkpoints.",
    )
    parser.add_argument(
        "--gate-normalized",
        action="store_true",
        help="Include the scalar TEG gate in neighbour normalization (ST-v2).",
    )
    parser.add_argument(
        "--feature-standardization",
        action="store_true",
        help="Fit feature mean/std on training nodes and apply it to both years.",
    )
    parser.add_argument(
        "--edge-normalization",
        choices=["per_year", "shared_2020", "shared_train"],
        default="per_year",
        help="Exposure scaling policy. per_year preserves the legacy model.",
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


def fit_edge_weight_scaler(weights: np.ndarray) -> tuple[float, float]:
    values = weights.astype(np.float32)
    p99 = float(np.percentile(values, 99))
    return float(np.min(np.minimum(values, p99))), p99


def transform_edge_weight(weights: np.ndarray, min_val: float, p99: float) -> np.ndarray:
    capped = np.minimum(weights.astype(np.float32), p99)
    return np.clip((capped - min_val) / (p99 - min_val + EPS), 0.0, 1.0)


def normalize_edge_weight(weights: np.ndarray) -> np.ndarray:
    min_val, p99 = fit_edge_weight_scaler(weights)
    return transform_edge_weight(weights, min_val, p99)


def load_graph(
    zf: zipfile.ZipFile, year: str, *, normalize_edges: bool = True
) -> GraphData:
    x = read_npy(zf, year, "data.x.npy").astype(np.float32)
    y = read_npy(zf, year, "data.y.npy").astype(np.int64)
    edge_index = read_npy(zf, year, "data.edge_index.npy")
    edge_attr = read_npy(zf, year, "data.edge_attribute.npy")

    undirected_edges, undirected_weights = merge_undirected_max(edge_index, edge_attr)
    if normalize_edges:
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
    graph20: GraphData,
    graph21: GraphData,
    split: str,
    seed: int,
    split_b_val_fraction: float = 0.2,
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
        adapt21, test21 = stratified_split(graph21.labeled_idx, y21, 0.5, seed)
        if not 0.0 <= split_b_val_fraction < 1.0:
            raise ValueError("split_b_val_fraction must be in [0, 1)")
        if split_b_val_fraction == 0.0:
            # Explicit compatibility mode for reproducing the historical
            # last-epoch Split B baseline. Formal new runs should use 0.2.
            train21 = adapt21
            val21 = np.array([], dtype=int)
        else:
            train21, val21 = stratified_split(
                adapt21, y21, split_b_val_fraction, seed
            )
        return {
            "data_2020": {
                "train": graph20.labeled_idx,
                "val": np.array([], dtype=int),
                "test": np.array([], dtype=int),
            },
            "data_2021": {
                "train": train21,
                "val": val21,
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


def _training_edge_weights(
    graph: GraphData, train_idx: np.ndarray
) -> np.ndarray:
    """Select edges touching at least one training node for scaler fitting."""

    if train_idx.size == 0:
        return np.array([], dtype=np.float32)
    train_mask = np.zeros(graph.x.shape[0], dtype=bool)
    train_mask[train_idx] = True
    edges = graph.edge_index.numpy()
    keep = train_mask[edges[0]] | train_mask[edges[1]]
    return graph.edge_weight.numpy()[keep]


def fit_and_apply_preprocessing(
    graphs: list[GraphData],
    split_map: dict[str, dict[str, np.ndarray]],
    edge_mode: str,
    standardize_features: bool,
) -> PreprocessingState:
    """Fit preprocessing using training information and transform both graphs."""

    state = PreprocessingState(edge_mode=edge_mode)
    if edge_mode == "per_year":
        for graph in graphs:
            graph.edge_weight = torch.from_numpy(
                normalize_edge_weight(graph.edge_weight.numpy())
            ).float()
    else:
        if edge_mode == "shared_2020":
            fit_weights = graphs[0].edge_weight.numpy()
        elif edge_mode == "shared_train":
            selected = [
                _training_edge_weights(graph, split_map[graph.year]["train"])
                for graph in graphs
            ]
            selected = [values for values in selected if values.size]
            if not selected:
                raise ValueError("No training-connected edges available for scaling")
            fit_weights = np.concatenate(selected)
        else:
            raise ValueError(f"Unknown edge normalization mode: {edge_mode}")
        state.edge_min, state.edge_p99 = fit_edge_weight_scaler(fit_weights)
        for graph in graphs:
            graph.edge_weight = torch.from_numpy(
                transform_edge_weight(
                    graph.edge_weight.numpy(), state.edge_min, state.edge_p99
                )
            ).float()

    if standardize_features:
        train_features = [
            graph.x[torch.from_numpy(split_map[graph.year]["train"]).long()]
            for graph in graphs
            if split_map[graph.year]["train"].size
        ]
        fitted = torch.cat(train_features, dim=0)
        state.feature_mean = fitted.mean(dim=0)
        state.feature_std = fitted.std(dim=0, unbiased=False).clamp_min(1e-6)
        for graph in graphs:
            graph.x = (graph.x - state.feature_mean) / state.feature_std
    return state


def apply_preprocessing_state(
    graphs: list[GraphData], state: PreprocessingState
) -> None:
    """Apply a checkpoint's fitted transforms without refitting on export data."""

    if state.edge_mode == "per_year":
        for graph in graphs:
            graph.edge_weight = torch.from_numpy(
                normalize_edge_weight(graph.edge_weight.numpy())
            ).float()
    else:
        if state.edge_min is None or state.edge_p99 is None:
            raise ValueError("Shared edge scaler is missing from checkpoint")
        for graph in graphs:
            graph.edge_weight = torch.from_numpy(
                transform_edge_weight(
                    graph.edge_weight.numpy(), state.edge_min, state.edge_p99
                )
            ).float()
    if state.feature_mean is not None and state.feature_std is not None:
        for graph in graphs:
            graph.x = (graph.x - state.feature_mean) / state.feature_std


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
    def __init__(self, dim: int, gate_normalized: bool = False) -> None:
        super().__init__()
        self.gate_normalized = gate_normalized
        self.msg = nn.Linear(dim, dim)
        self.edge_gate = nn.Linear(1, dim)
        self.node_gate = nn.Linear(2 * dim, dim)

    def forward(
        self,
        x: torch.Tensor,
        edge_index: torch.Tensor,
        edge_weight: torch.Tensor,
        node_reliability: torch.Tensor | None = None,
    ) -> torch.Tensor:
        src, dst = edge_index
        edge_term = self.edge_gate(edge_weight.unsqueeze(1))
        node_term = self.node_gate(torch.cat([x[src], x[dst]], dim=1))
        gate = torch.sigmoid(edge_term + node_term)
        if node_reliability is not None:
            edge_reliability = torch.sqrt(
                torch.clamp(node_reliability[src] * node_reliability[dst], min=EPS)
            )
            gate = gate * edge_reliability.unsqueeze(1)
        if self.gate_normalized:
            # A scalar gate participates in neighbour normalization, matching
            # the exposure-gated attention interpretation used by ST-v2.
            gate_scalar = gate.mean(dim=1)
            norm = normalize_messages(
                x.shape[0], edge_index, edge_weight * gate_scalar
            )
            msg = self.msg(x[src]) * norm.unsqueeze(1)
        else:
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


class GATConv(nn.Module):
    """Single-head graph attention without trajectory-exposure features."""

    def __init__(self, dim: int) -> None:
        super().__init__()
        self.linear = nn.Linear(dim, dim, bias=False)
        self.attn_src = nn.Parameter(torch.empty(dim))
        self.attn_dst = nn.Parameter(torch.empty(dim))
        self.bias = nn.Parameter(torch.zeros(dim))
        nn.init.xavier_uniform_(self.linear.weight)
        nn.init.xavier_uniform_(self.attn_src.unsqueeze(0))
        nn.init.xavier_uniform_(self.attn_dst.unsqueeze(0))

    def forward(
        self, x: torch.Tensor, edge_index: torch.Tensor, edge_weight: torch.Tensor
    ) -> torch.Tensor:
        del edge_weight  # Standard GAT is an X + edge_index baseline.
        src, dst = edge_index
        h = self.linear(x)
        scores = F.leaky_relu(
            (h[src] * self.attn_src).sum(dim=1)
            + (h[dst] * self.attn_dst).sum(dim=1),
            negative_slope=0.2,
        )
        max_per_dst = torch.full(
            (x.shape[0],), -torch.inf, dtype=scores.dtype, device=scores.device
        )
        max_per_dst.scatter_reduce_(0, dst, scores, reduce="amax", include_self=True)
        exp_scores = torch.exp(scores - max_per_dst[dst])
        denom = torch.zeros(x.shape[0], dtype=scores.dtype, device=scores.device)
        denom.index_add_(0, dst, exp_scores)
        alpha = exp_scores / (denom[dst] + EPS)
        out = torch.zeros_like(h)
        out.index_add_(0, dst, h[src] * alpha.unsqueeze(1))
        return out + self.bias


class GraphSAGEConv(nn.Module):
    """Full-neighbour mean GraphSAGE layer for the transductive graph."""

    def __init__(self, dim: int) -> None:
        super().__init__()
        self.linear = nn.Linear(2 * dim, dim)

    def forward(
        self, x: torch.Tensor, edge_index: torch.Tensor, edge_weight: torch.Tensor
    ) -> torch.Tensor:
        del edge_weight  # GraphSAGE baseline uses topology, not exposure.
        src, dst = edge_index
        neighbours = torch.zeros_like(x)
        neighbours.index_add_(0, dst, x[src])
        degree = torch.zeros(x.shape[0], dtype=x.dtype, device=x.device)
        degree.index_add_(0, dst, torch.ones_like(dst, dtype=x.dtype))
        neighbours = neighbours / degree.clamp_min(1.0).unsqueeze(1)
        return self.linear(torch.cat([x, neighbours], dim=1))


class SGFormerAttention(nn.Module):
    """Approximation-free linear global attention from SGFormer."""

    def __init__(self, dim: int) -> None:
        super().__init__()
        self.q = nn.Linear(dim, dim, bias=False)
        self.k = nn.Linear(dim, dim, bias=False)
        self.v = nn.Linear(dim, dim, bias=False)

    def forward(
        self, x: torch.Tensor, edge_index: torch.Tensor, edge_weight: torch.Tensor
    ) -> torch.Tensor:
        del edge_index, edge_weight
        q = F.normalize(self.q(x), p=2, dim=-1, eps=1e-6)
        k = F.normalize(self.k(x), p=2, dim=-1, eps=1e-6)
        v = self.v(x)
        node_count = x.shape[0]
        kv = k.transpose(0, 1) @ v
        numerator = q @ kv + node_count * v
        denominator = q @ k.sum(dim=0) + node_count
        return numerator / denominator.clamp_min(1e-6).unsqueeze(1)


def k_hop_pairs(
    edge_index: torch.Tensor, num_nodes: int, max_hops: int
) -> tuple[torch.Tensor, torch.Tensor]:
    """Build directed shortest-path pairs up to ``max_hops`` on CPU."""

    neighbours: list[set[int]] = [set() for _ in range(num_nodes)]
    for src, dst in edge_index.detach().cpu().t().tolist():
        neighbours[int(src)].add(int(dst))
    sources: list[int] = []
    destinations: list[int] = []
    distances: list[int] = []
    for destination in range(num_nodes):
        visited = {destination}
        frontier = {destination}
        sources.append(destination)
        destinations.append(destination)
        distances.append(0)
        for distance in range(1, max_hops + 1):
            next_frontier: set[int] = set()
            for node in frontier:
                next_frontier.update(neighbours[node])
            next_frontier.difference_update(visited)
            if not next_frontier:
                break
            for source in sorted(next_frontier):
                sources.append(source)
                destinations.append(destination)
                distances.append(distance)
            visited.update(next_frontier)
            frontier = next_frontier
    pairs = torch.tensor([sources, destinations], dtype=torch.long)
    return pairs, torch.tensor(distances, dtype=torch.float32)


class GradformerConv(nn.Module):
    """Sparse node-classification adaptation of Gradformer's decay attention."""

    def __init__(
        self, dim: int, max_hops: int = 3, lambda_init: float = 1.0, heads: int = 4
    ) -> None:
        super().__init__()
        if dim % heads:
            raise ValueError("Gradformer hidden dimension must be divisible by heads")
        self.dim = dim
        self.heads = heads
        self.head_dim = dim // heads
        self.max_hops = max_hops
        self.q = nn.Linear(dim, dim, bias=False)
        self.k = nn.Linear(dim, dim, bias=False)
        self.v = nn.Linear(dim, dim, bias=False)
        self.out = nn.Linear(dim, dim)
        inverse_softplus = math.log(math.expm1(max(lambda_init, 1e-4)))
        self.raw_lambda = nn.Parameter(torch.full((heads,), inverse_softplus))
        self._pair_cache: dict[tuple[int, int], tuple[torch.Tensor, torch.Tensor]] = {}

    def _pairs(
        self, edge_index: torch.Tensor, num_nodes: int
    ) -> tuple[torch.Tensor, torch.Tensor]:
        key = (int(edge_index.data_ptr()), num_nodes)
        if key not in self._pair_cache:
            self._pair_cache[key] = k_hop_pairs(
                edge_index, num_nodes, self.max_hops
            )
        pairs, distance = self._pair_cache[key]
        return pairs.to(edge_index.device), distance.to(edge_index.device)

    def forward(
        self, x: torch.Tensor, edge_index: torch.Tensor, edge_weight: torch.Tensor
    ) -> torch.Tensor:
        del edge_weight
        pairs, distance = self._pairs(edge_index, x.shape[0])
        src, dst = pairs
        q = self.q(x).view(-1, self.heads, self.head_dim)
        k = self.k(x).view(-1, self.heads, self.head_dim)
        v = self.v(x).view(-1, self.heads, self.head_dim)
        scores = (q[dst] * k[src]).sum(dim=-1) / math.sqrt(self.head_dim)
        decay = F.softplus(self.raw_lambda).unsqueeze(0) * distance.unsqueeze(1)
        scores = scores - decay

        max_per_dst = torch.full(
            (x.shape[0], self.heads),
            -torch.inf,
            dtype=scores.dtype,
            device=scores.device,
        )
        index = dst.unsqueeze(1).expand(-1, self.heads)
        max_per_dst.scatter_reduce_(0, index, scores, reduce="amax", include_self=True)
        exp_scores = torch.exp(scores - max_per_dst[dst])
        denominator = torch.zeros_like(max_per_dst)
        denominator.index_add_(0, dst, exp_scores)
        alpha = exp_scores / (denominator[dst] + EPS)
        messages = v[src] * alpha.unsqueeze(-1)
        aggregated = torch.zeros(
            (x.shape[0], self.heads, self.head_dim),
            dtype=x.dtype,
            device=x.device,
        )
        aggregated.index_add_(0, dst, messages)
        return self.out(aggregated.reshape(x.shape[0], self.dim))


class RiskModel(nn.Module):
    def __init__(
        self,
        model: str,
        in_dim: int,
        hidden_dim: int,
        dropout: float,
        gamma_unc: float = 0.5,
        logvar_min: float = -5.0,
        logvar_max: float = 2.0,
        ec_delta_max: float = 0.05,
        gate_normalized: bool = False,
        gradformer_max_hops: int = 3,
        gradformer_lambda_init: float = 1.0,
    ) -> None:
        super().__init__()
        self.model = model
        self.encoder = nn.Linear(in_dim, hidden_dim)
        self.dropout = nn.Dropout(dropout)
        self.mu: nn.Parameter | None = None
        self.has_uncertainty = model in {
            "ua_gnn",
            "ua_teg_gnn",
            "stable_tail_ua_gnn",
        }
        self.gamma_unc = gamma_unc
        self.logvar_min = logvar_min
        self.logvar_max = logvar_max
        self.ec_delta_max = ec_delta_max

        if model == "mlp":
            self.layers = nn.ModuleList()
        elif model in {"gcn", "gcn_only"}:
            self.layers = nn.ModuleList(
                [GraphConv(hidden_dim, weighted=False), GraphConv(hidden_dim, weighted=False)]
            )
        elif model == "weighted_gcn":
            self.layers = nn.ModuleList(
                [GraphConv(hidden_dim, weighted=True), GraphConv(hidden_dim, weighted=True)]
            )
        elif model == "edge_gat":
            self.layers = nn.ModuleList([EdgeGATConv(hidden_dim), EdgeGATConv(hidden_dim)])
        elif model == "gat":
            self.layers = nn.ModuleList([GATConv(hidden_dim), GATConv(hidden_dim)])
        elif model == "graphsage":
            self.layers = nn.ModuleList(
                [GraphSAGEConv(hidden_dim), GraphSAGEConv(hidden_dim)]
            )
        elif model in {"graphsage_teg_concat", "graphsage_teg_gate"}:
            self.sage_layers = nn.ModuleList(
                [GraphSAGEConv(hidden_dim), GraphSAGEConv(hidden_dim)]
            )
            self.teg_layers = nn.ModuleList(
                [
                    EdgeGatedConv(hidden_dim, gate_normalized),
                    EdgeGatedConv(hidden_dim, gate_normalized),
                ]
            )
            if model == "graphsage_teg_concat":
                self.fusion = nn.Sequential(
                    nn.Linear(2 * hidden_dim, hidden_dim),
                    nn.ReLU(),
                    nn.Dropout(dropout),
                )
            else:
                self.gate = nn.Sequential(
                    nn.Linear(2 * hidden_dim, hidden_dim),
                    nn.ReLU(),
                    nn.Dropout(dropout),
                    nn.Linear(hidden_dim, 1),
                    nn.Sigmoid(),
                )
            self.layers = nn.ModuleList()
        elif model == "sgformer_adapted":
            self.global_attention = SGFormerAttention(hidden_dim)
            self.local_layers = nn.ModuleList(
                [GraphConv(hidden_dim, weighted=False)]
            )
            self.sg_fusion = nn.Linear(2 * hidden_dim, hidden_dim)
            self.layers = nn.ModuleList()
        elif model in {"sgformer_teg_concat", "sgformer_teg_gate"}:
            self.global_attention = SGFormerAttention(hidden_dim)
            self.local_layers = nn.ModuleList(
                [GraphConv(hidden_dim, weighted=False)]
            )
            self.sg_fusion = nn.Linear(2 * hidden_dim, hidden_dim)
            self.teg_layers = nn.ModuleList(
                [
                    EdgeGatedConv(hidden_dim, gate_normalized),
                    EdgeGatedConv(hidden_dim, gate_normalized),
                ]
            )
            if model == "sgformer_teg_concat":
                self.fusion = nn.Sequential(
                    nn.Linear(2 * hidden_dim, hidden_dim),
                    nn.ReLU(),
                    nn.Dropout(dropout),
                )
            else:
                self.gate = nn.Sequential(
                    nn.Linear(2 * hidden_dim, hidden_dim),
                    nn.ReLU(),
                    nn.Dropout(dropout),
                    nn.Linear(hidden_dim, 1),
                    nn.Sigmoid(),
                )
            self.layers = nn.ModuleList()
        elif model == "gradformer_adapted":
            self.layers = nn.ModuleList(
                [
                    GradformerConv(
                        hidden_dim,
                        max_hops=gradformer_max_hops,
                        lambda_init=gradformer_lambda_init,
                    )
                ]
            )
        elif model in {"teg_gnn", "teg_only"}:
            self.layers = nn.ModuleList(
                [
                    EdgeGatedConv(hidden_dim, gate_normalized),
                    EdgeGatedConv(hidden_dim, gate_normalized),
                ]
            )
        elif model in {
            "gcn_teg_concat",
            "stable_tail_gnn",
            "gcn_teg_residual_fixed",
            "gcn_teg_residual_learnable",
            "ua_teg_gnn",
            "stable_tail_ua_gnn",
            "stable_tail_ec_gnn",
        }:
            self.gcn_layers = nn.ModuleList(
                [GraphConv(hidden_dim, weighted=False), GraphConv(hidden_dim, weighted=False)]
            )
            self.teg_layers = nn.ModuleList(
                [
                    EdgeGatedConv(hidden_dim, gate_normalized),
                    EdgeGatedConv(hidden_dim, gate_normalized),
                ]
            )
            self.layers = nn.ModuleList()
            if model in {
                "gcn_teg_concat",
                "stable_tail_gnn",
                "ua_teg_gnn",
                "stable_tail_ua_gnn",
                "stable_tail_ec_gnn",
            }:
                self.fusion = nn.Sequential(
                    nn.Linear(2 * hidden_dim, hidden_dim),
                    nn.ReLU(),
                    nn.Dropout(dropout),
                )
            elif model == "gcn_teg_residual_learnable":
                self.mu = nn.Parameter(torch.tensor(0.1, dtype=torch.float32))
        elif model == "ua_gnn":
            self.layers = nn.ModuleList(
                [GraphConv(hidden_dim, weighted=False), GraphConv(hidden_dim, weighted=False)]
            )
        else:
            raise ValueError(f"Unknown model: {model}")

        self.classifier = nn.Linear(hidden_dim, NUM_CLASSES)
        if self.has_uncertainty:
            self.uncertainty_head = nn.Linear(hidden_dim, 1)
        if model == "stable_tail_ua_gnn":
            self.base_classifier = nn.Linear(hidden_dim, NUM_CLASSES)
        if model == "stable_tail_ec_gnn":
            self.calibration_head = nn.Sequential(
                nn.Linear(hidden_dim, hidden_dim),
                nn.ReLU(),
                nn.Dropout(dropout),
                nn.Linear(hidden_dim, 1),
            )

    def _run_layers(
        self,
        h: torch.Tensor,
        layers: nn.ModuleList,
        graph: GraphData,
        node_reliability: torch.Tensor | None = None,
    ) -> torch.Tensor:
        for layer in layers:
            residual = h
            if isinstance(layer, EdgeGatedConv):
                h = F.relu(
                    layer(h, graph.edge_index, graph.edge_weight, node_reliability)
                )
            else:
                h = F.relu(layer(h, graph.edge_index, graph.edge_weight))
            h = self.dropout(h + residual)
        return h

    def _run_plain_layers(
        self,
        h: torch.Tensor,
        layers: nn.ModuleList,
        graph: GraphData,
    ) -> torch.Tensor:
        """Run the explicitly non-residual branches used by concat models."""
        for layer in layers:
            if isinstance(layer, EdgeGatedConv):
                h = layer(h, graph.edge_index, graph.edge_weight)
            else:
                h = layer(h, graph.edge_index, graph.edge_weight)
            h = self.dropout(F.relu(h))
        return h

    def _encode_sgformer(self, h: torch.Tensor, graph: GraphData) -> torch.Tensor:
        global_h = F.relu(
            self.global_attention(h, graph.edge_index, graph.edge_weight)
        )
        local_h = self._run_layers(h, self.local_layers, graph)
        return self.dropout(
            F.relu(self.sg_fusion(torch.cat([global_h, local_h], dim=1))) + h
        )

    def _gate_fusion(
        self, left: torch.Tensor, right: torch.Tensor
    ) -> torch.Tensor:
        gate = self.gate(torch.cat([left, right], dim=1))
        return self.dropout(gate * left + (1.0 - gate) * right)

    def encode(self, graph: GraphData) -> torch.Tensor:
        h = F.relu(self.encoder(graph.x))
        if self.model == "mlp":
            return self.dropout(h)

        if self.model == "sgformer_adapted":
            return self._encode_sgformer(h, graph)

        if self.model == "graphsage_teg_concat":
            h_sage = self._run_plain_layers(h, self.sage_layers, graph)
            h_teg = self._run_plain_layers(h, self.teg_layers, graph)
            return self.fusion(torch.cat([h_sage, h_teg], dim=1))

        if self.model == "graphsage_teg_gate":
            h_sage = self._run_plain_layers(h, self.sage_layers, graph)
            h_teg = self._run_plain_layers(h, self.teg_layers, graph)
            return self._gate_fusion(h_sage, h_teg)

        if self.model == "sgformer_teg_concat":
            h_sgformer = self._encode_sgformer(h, graph)
            h_teg = self._run_plain_layers(h, self.teg_layers, graph)
            return self.fusion(torch.cat([h_sgformer, h_teg], dim=1))

        if self.model == "sgformer_teg_gate":
            h_sgformer = self._encode_sgformer(h, graph)
            h_teg = self._run_plain_layers(h, self.teg_layers, graph)
            return self._gate_fusion(h_sgformer, h_teg)

        if self.model in {
            "gcn_teg_concat",
            "stable_tail_gnn",
            "gcn_teg_residual_fixed",
            "gcn_teg_residual_learnable",
            "ua_teg_gnn",
            "stable_tail_ua_gnn",
            "stable_tail_ec_gnn",
        }:
            h_gcn = self._run_layers(h, self.gcn_layers, graph)
            h_teg = self._run_layers(h, self.teg_layers, graph)
            if self.model in {
                "gcn_teg_concat",
                "stable_tail_gnn",
                "ua_teg_gnn",
                "stable_tail_ec_gnn",
            }:
                h = self.fusion(torch.cat([h_gcn, h_teg], dim=1))
            else:
                mu = self.mu if self.mu is not None else h.new_tensor(0.1)
                h = h_gcn + mu * h_teg
            return h

        for layer in self.layers:
            residual = h
            h = F.relu(layer(h, graph.edge_index, graph.edge_weight))
            h = self.dropout(h + residual)
        return h

    def forward(self, graph: GraphData) -> torch.Tensor:
        if self.model == "stable_tail_ua_gnn":
            return self.forward_outputs(graph)[0]
        return self.classifier(self.encode(graph))

    def forward_outputs(self, graph: GraphData) -> tuple[torch.Tensor, torch.Tensor | None]:
        if self.model == "stable_tail_ua_gnn":
            h0 = F.relu(self.encoder(graph.x))
            h_gcn = self._run_layers(h0, self.gcn_layers, graph)

            # Estimate uncertainty from the stable GCN branch. The TEG branch is
            # deliberately excluded here to avoid feeding tail-amplified features
            # back into the uncertainty estimate.
            log_var = self.uncertainty_head(h_gcn).squeeze(1).clamp(
                self.logvar_min, self.logvar_max
            )
            sigma = torch.sqrt(torch.exp(log_var))
            reliability = torch.exp(-self.gamma_unc * sigma).clamp(EPS, 1.0)

            h_teg = self._run_layers(h0, self.teg_layers, graph, reliability)
            h = self.fusion(torch.cat([h_gcn, h_teg], dim=1))
            return self.classifier(h), log_var

        h = self.encode(graph)
        logits = self.classifier(h)
        if not self.has_uncertainty:
            return logits, None
        log_var = self.uncertainty_head(h).squeeze(1).clamp(
            self.logvar_min, self.logvar_max
        )
        return logits, log_var

    def forward_ec_outputs(
        self, graph: GraphData
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        """Return node logits and calibrated normalized risk for EC-GNN.

        The classifier probabilities remain the node-risk prediction used for
        node metrics. The calibrated score is only used by the edge-risk matrix
        and edge-level training losses.
        """

        if self.model != "stable_tail_ec_gnn":
            raise ValueError("forward_ec_outputs is only valid for stable_tail_ec_gnn")
        h = self.encode(graph)
        logits = self.classifier(h)
        probs = F.softmax(logits, dim=1)
        base_norm = torch.clamp((risk_scores(probs) - 1.0) / 7.0, 0.0, 1.0)
        delta = self.ec_delta_max * torch.tanh(self.calibration_head(h).squeeze(1))
        calibrated = torch.clamp(base_norm + delta, 0.0, 1.0)
        return logits, base_norm, calibrated, delta, probs


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
    log_var: torch.Tensor | None,
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
        base_loss = ce + 0.5 * ord_loss
        if log_var is None or args.lambda_nll <= 0:
            return base_loss
        selected_log_var = log_var[idx_t]
        nll = 0.5 * torch.exp(-selected_log_var) * (s_i - (y.float() + 1.0)).pow(2)
        nll = (nll + 0.5 * selected_log_var).mean()
        var_reg = torch.exp(selected_log_var).mean()
        return base_loss + args.lambda_nll * nll + args.lambda_var * var_reg

    z = (y >= 5).float()
    p_high = torch.clamp(probs[:, 5:].sum(dim=1), EPS, 1.0 - EPS)
    hr = F.binary_cross_entropy(
        p_high,
        z,
        weight=torch.where(z > 0, torch.full_like(z, pos_weight), torch.ones_like(z)),
    )
    tail = topk_loss(ce_each, args.topk_frac)
    loss = ce + args.alpha_ord * ord_loss + args.alpha_hr * hr + args.alpha_topk * tail
    if log_var is not None and args.lambda_nll > 0:
        selected_log_var = log_var[idx_t]
        nll = 0.5 * torch.exp(-selected_log_var) * (s_i - (y.float() + 1.0)).pow(2)
        nll = (nll + 0.5 * selected_log_var).mean()
        var_reg = torch.exp(selected_log_var).mean()
        loss = loss + args.lambda_nll * nll + args.lambda_var * var_reg
    return loss


def compute_edge_calibration_loss(
    graph: GraphData,
    train_idx: np.ndarray,
    calibrated_norm: torch.Tensor,
    probs: torch.Tensor,
    pos_weight: float,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Compute edge-level severity and high-risk losses for train-labeled edges.

    Only edges with at least one training-labeled endpoint participate. Edges
    with both endpoints labeled receive weight 1.0; one-labeled-endpoint edges
    receive weight 0.5. This avoids leaking validation/test labels into the
    edge calibration objective.
    """

    if train_idx.size == 0:
        zero = calibrated_norm.new_tensor(0.0)
        return zero, zero

    device = calibrated_norm.device
    train_mask = torch.zeros(graph.y.shape[0], dtype=torch.bool, device=device)
    train_mask[torch.from_numpy(train_idx).long().to(device)] = True
    src, dst = graph.edge_index.to(device)

    # Use one direction per undirected edge because load_graph stores both
    # directions. This keeps the edge loss from double-counting the same pair.
    one_way = src < dst
    src = src[one_way]
    dst = dst[one_way]
    src_labeled = train_mask[src]
    dst_labeled = train_mask[dst]
    keep = src_labeled | dst_labeled
    if not torch.any(keep):
        zero = calibrated_norm.new_tensor(0.0)
        return zero, zero

    src = src[keep]
    dst = dst[keep]
    src_labeled = src_labeled[keep]
    dst_labeled = dst_labeled[keep]
    both_labeled = src_labeled & dst_labeled
    edge_weight = torch.where(
        both_labeled,
        torch.ones_like(calibrated_norm[src]),
        torch.full_like(calibrated_norm[src], 0.5),
    )

    y = graph.y.to(device)
    y_src = torch.clamp((y[src].float() - 1.0) / 7.0, 0.0, 1.0)
    y_dst = torch.clamp((y[dst].float() - 1.0) / 7.0, 0.0, 1.0)
    target = torch.where(
        both_labeled,
        torch.maximum(y_src, y_dst),
        torch.where(src_labeled, y_src, y_dst),
    )
    pred = torch.maximum(calibrated_norm[src], calibrated_norm[dst])
    edge_loss_each = F.smooth_l1_loss(pred, target, reduction="none")
    edge_loss = torch.sum(edge_loss_each * edge_weight) / (edge_weight.sum() + EPS)

    high_src = (y[src] >= 6) & src_labeled
    high_dst = (y[dst] >= 6) & dst_labeled
    z = (high_src | high_dst).float()
    p_high = torch.clamp(probs[:, 5:].sum(dim=1), EPS, 1.0 - EPS)
    pred_high = torch.maximum(p_high[src], p_high[dst])
    high_weight = torch.where(
        z > 0,
        torch.full_like(z, pos_weight),
        torch.ones_like(z),
    )
    edge_high_each = F.binary_cross_entropy(pred_high, z, reduction="none")
    edge_high = torch.sum(edge_high_each * high_weight * edge_weight) / (
        torch.sum(high_weight * edge_weight) + EPS
    )
    return edge_loss, edge_high


def compute_distill_loss(
    logits: torch.Tensor,
    teacher_logits: torch.Tensor,
    idx: np.ndarray,
) -> torch.Tensor:
    if idx.size == 0:
        return logits.new_tensor(0.0)
    idx_t = torch.from_numpy(idx).long()
    selected = logits[idx_t]
    teacher_selected = teacher_logits[idx_t].detach()
    log_probs = F.log_softmax(selected, dim=1)
    teacher_probs = F.softmax(teacher_selected, dim=1)
    kl = F.kl_div(log_probs, teacher_probs, reduction="batchmean")
    s_student = risk_scores(F.softmax(selected, dim=1))
    s_teacher = risk_scores(teacher_probs)
    score_loss = F.mse_loss(s_student, s_teacher)
    return kl + score_loss


def train_stable_tail_teacher(
    args: argparse.Namespace,
    graphs: list[GraphData],
    split_map: dict[str, dict[str, np.ndarray]],
    weights: torch.Tensor,
    pos_weight: float,
) -> RiskModel:
    """Train a frozen Stable-Tail teacher for EC-GNN distillation.

    The project historically treats ``gcn_teg_concat`` as Stable-Tail GNN, so
    that same backbone is used as the teacher without reading or overwriting
    any existing result files.
    """

    teacher = RiskModel(
        "gcn_teg_concat",
        graphs[0].x.shape[1],
        args.hidden_dim,
        args.dropout,
        gate_normalized=getattr(args, "gate_normalized", False),
    )
    optimizer = torch.optim.AdamW(
        teacher.parameters(), lr=args.lr, weight_decay=args.weight_decay
    )
    teacher_epochs = max(0, int(getattr(args, "ec_teacher_epochs", args.epochs)))
    for epoch in range(teacher_epochs):
        teacher.train()
        optimizer.zero_grad()
        total_loss = torch.tensor(0.0)
        full_loss = epoch >= args.stage1_epochs
        for graph in graphs:
            logits, log_var = teacher.forward_outputs(graph)
            total_loss = total_loss + compute_loss(
                logits,
                log_var,
                graph.y,
                split_map[graph.year]["train"],
                weights,
                args,
                full_loss,
                pos_weight,
            )
        total_loss.backward()
        optimizer.step()
    teacher.eval()
    for param in teacher.parameters():
        param.requires_grad_(False)
    return teacher


def expected_calibration_error(
    confidences: np.ndarray, correct: np.ndarray, num_bins: int = 10
) -> float:
    ece = 0.0
    for lower in np.linspace(0.0, 1.0, num_bins, endpoint=False):
        upper = lower + 1.0 / num_bins
        if upper >= 1.0:
            mask = (confidences >= lower) & (confidences <= upper)
        else:
            mask = (confidences >= lower) & (confidences < upper)
        if not np.any(mask):
            continue
        ece += float(mask.mean() * abs(correct[mask].mean() - confidences[mask].mean()))
    return ece


def ranking_metrics(y_true: np.ndarray, scores: np.ndarray) -> dict[str, float]:
    """Compute high-risk retrieval metrics used by downstream ranking tasks."""

    if y_true.size == 0:
        return {}
    order = np.argsort(-scores, kind="stable")
    high = y_true >= 6
    high_count = max(1, int(high.sum()))

    def top_count(fraction: float) -> int:
        return min(y_true.size, max(1, int(math.ceil(y_true.size * fraction))))

    top10 = order[: top_count(0.10)]
    top20 = order[: top_count(0.20)]
    cutoff = top_count(0.20)
    relevance = np.power(2.0, y_true.astype(float) - 1.0) - 1.0
    discounts = 1.0 / np.log2(np.arange(2, cutoff + 2, dtype=float))
    dcg = float(np.sum(relevance[order[:cutoff]] * discounts))
    ideal = np.argsort(-relevance, kind="stable")[:cutoff]
    ideal_dcg = float(np.sum(relevance[ideal] * discounts))

    return {
        "high_risk_recall_at_top10pct": float(high[top10].sum() / high_count),
        "high_risk_recall_at_top20pct": float(high[top20].sum() / high_count),
        "ndcg_at_top20pct": dcg / ideal_dcg if ideal_dcg > 0 else 0.0,
        "high_risk_hits_at_10": float(high[order[: min(10, y_true.size)]].sum()),
        "high_risk_hits_at_20": float(high[order[: min(20, y_true.size)]].sum()),
    }


def evaluate(
    logits: torch.Tensor,
    labels: torch.Tensor,
    idx: np.ndarray,
    log_var: torch.Tensor | None = None,
) -> dict[str, float]:
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
    one_hot = np.eye(NUM_CLASSES, dtype=np.float32)[y_true - 1]
    brier = float(np.mean(np.sum((probs - one_hot) ** 2, axis=1)))
    confidence = probs.max(axis=1)
    correct = y_pred == y_true
    ece = expected_calibration_error(confidence, correct.astype(float))

    result = {
        "macro_f1": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "weighted_f1": float(f1_score(y_true, y_pred, average="weighted", zero_division=0)),
        "mae": float(mean_absolute_error(y_true, s_pred)),
        "qwk": float(cohen_kappa_score(y_true, y_pred, weights="quadratic")),
        "recall_6_8": float(recall_score(high_true, high_pred, zero_division=0)),
        "precision_6_8": float(precision_score(high_true, high_pred, zero_division=0)),
        "pr_auc_high": pr_auc,
        "high_fn_rate": high_fn_rate,
        "brier": brier,
        "ece": ece,
    }
    result.update(ranking_metrics(y_true, s_pred))
    if log_var is not None:
        lv = log_var[idx_t].detach().numpy()
        sigma = np.sqrt(np.exp(lv))
        nll = 0.5 * np.exp(-lv) * (s_pred - y_true.astype(float)) ** 2 + 0.5 * lv
        result["ordinal_nll"] = float(np.mean(nll))
        result["uncertainty_mean"] = float(np.mean(sigma))
        result["correct_uncertainty"] = float(np.mean(sigma[correct])) if np.any(correct) else float("nan")
        result["error_uncertainty"] = float(np.mean(sigma[~correct])) if np.any(~correct) else float("nan")
        if np.unique(correct).size > 1 and np.std(sigma) > 0:
            result["error_uncertainty_corr"] = float(np.corrcoef((~correct).astype(float), sigma)[0, 1])
        else:
            result["error_uncertainty_corr"] = float("nan")
        high_fn = np.logical_and(high_true, ~high_pred)
        result["high_fn_uncertainty"] = float(np.mean(sigma[high_fn])) if np.any(high_fn) else float("nan")
    return result


def evaluate_across_graphs(
    model: RiskModel,
    graphs: list[GraphData],
    split_map: dict[str, dict[str, np.ndarray]],
    split_name: str,
) -> dict[str, float]:
    """Evaluate one logical split jointly across yearly graphs."""

    logits_parts: list[torch.Tensor] = []
    labels_parts: list[torch.Tensor] = []
    log_var_parts: list[torch.Tensor] = []
    has_log_var = False
    model.eval()
    with torch.no_grad():
        for graph in graphs:
            idx = split_map[graph.year][split_name]
            if idx.size == 0:
                continue
            idx_t = torch.from_numpy(idx).long()
            logits, log_var = model.forward_outputs(graph)
            logits_parts.append(logits[idx_t])
            labels_parts.append(graph.y[idx_t])
            if log_var is not None:
                log_var_parts.append(log_var[idx_t])
                has_log_var = True
    if not logits_parts:
        return {}
    logits_all = torch.cat(logits_parts, dim=0)
    labels_all = torch.cat(labels_parts, dim=0)
    log_var_all = torch.cat(log_var_parts, dim=0) if has_log_var else None
    idx_all = np.arange(labels_all.shape[0], dtype=np.int64)
    return evaluate(logits_all, labels_all, idx_all, log_var_all)


def checkpoint_score(metrics: dict[str, float], args: argparse.Namespace) -> float:
    """Score validation epochs for ordinal accuracy and high-risk ranking."""

    return -metrics["mae"] + getattr(args, "checkpoint_score_pr_weight", 0.8) * metrics[
        "pr_auc_high"
    ]


def checkpoint_constraints_hold(
    metrics: dict[str, float], args: argparse.Namespace
) -> bool:
    return (
        metrics["recall_6_8"] >= getattr(args, "checkpoint_min_recall", 0.0)
        and metrics["high_fn_rate"] <= getattr(args, "checkpoint_max_high_fn", 1.0)
    )


def checkpoint_stem(args: argparse.Namespace) -> str:
    stem = f"{args.model}_split{args.split}_seed{args.seed}_epochs{args.epochs}"
    tag = getattr(args, "experiment_tag", "")
    return f"{stem}_{tag}" if tag else stem


def preprocessing_to_payload(state: PreprocessingState) -> dict[str, object]:
    return {
        "edge_mode": state.edge_mode,
        "edge_min": state.edge_min,
        "edge_p99": state.edge_p99,
        "feature_mean": state.feature_mean,
        "feature_std": state.feature_std,
    }


def preprocessing_from_payload(payload: dict[str, object]) -> PreprocessingState:
    return PreprocessingState(
        edge_mode=str(payload["edge_mode"]),
        edge_min=payload.get("edge_min"),
        edge_p99=payload.get("edge_p99"),
        feature_mean=payload.get("feature_mean"),
        feature_std=payload.get("feature_std"),
    )


def save_checkpoint(
    args: argparse.Namespace,
    model: RiskModel,
    preprocessing: PreprocessingState,
    split_map: dict[str, dict[str, np.ndarray]],
    best_epoch: int,
    validation_metrics: dict[str, float],
) -> Path:
    checkpoint_dir = getattr(args, "checkpoint_dir", None) or (
        args.output_dir / "checkpoints"
    )
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    path = checkpoint_dir / f"{checkpoint_stem(args)}.pt"
    torch.save(
        {
            "format_version": 1,
            "model_state_dict": model.state_dict(),
            "model_config": {
                "model": args.model,
                "in_dim": int(model.encoder.in_features),
                "hidden_dim": args.hidden_dim,
                "dropout": args.dropout,
                "gamma_unc": getattr(args, "gamma_unc", 0.5),
                "logvar_min": getattr(args, "logvar_min", -5.0),
                "logvar_max": getattr(args, "logvar_max", 2.0),
                "ec_delta_max": getattr(args, "ec_delta_max", 0.05),
                "gate_normalized": getattr(args, "gate_normalized", False),
                "gradformer_max_hops": getattr(args, "gradformer_max_hops", 3),
                "gradformer_lambda_init": getattr(
                    args, "gradformer_lambda_init", 1.0
                ),
            },
            "training_config": {
                "split": args.split,
                "seed": args.seed,
                "epochs": args.epochs,
                "best_epoch": best_epoch,
                "split_b_val_fraction": getattr(args, "split_b_val_fraction", 0.2),
                "checkpoint_selection": getattr(args, "checkpoint_selection", "best"),
            },
            "preprocessing": preprocessing_to_payload(preprocessing),
            "split_map": split_map,
            "validation_metrics": validation_metrics,
        },
        path,
    )
    return path


def load_checkpoint_model(
    checkpoint_path: Path, zip_path: Path
) -> tuple[dict[str, object], RiskModel, list[GraphData]]:
    """Load exactly one trained model and its fitted preprocessing state."""

    payload = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    config = payload["model_config"]
    model = RiskModel(**config)
    model.load_state_dict(payload["model_state_dict"])
    model.eval()
    with zipfile.ZipFile(zip_path) as zf:
        graph20 = load_graph(zf, "data_2020", normalize_edges=False)
        graph21 = load_graph(zf, "data_2021", normalize_edges=False)
    graphs = [graph20, graph21]
    apply_preprocessing_state(
        graphs, preprocessing_from_payload(payload["preprocessing"])
    )
    return payload, model, graphs


def train(args: argparse.Namespace) -> dict[str, object]:
    set_seed(args.seed)
    with zipfile.ZipFile(args.zip) as zf:
        graph20 = load_graph(zf, "data_2020", normalize_edges=False)
        graph21 = load_graph(zf, "data_2021", normalize_edges=False)

    graphs = [graph20, graph21]
    split_map = build_splits(
        graph20,
        graph21,
        args.split,
        args.seed,
        getattr(args, "split_b_val_fraction", 0.2),
    )
    preprocessing = fit_and_apply_preprocessing(
        graphs,
        split_map,
        getattr(args, "edge_normalization", "per_year"),
        getattr(args, "feature_standardization", False),
    )

    model = RiskModel(
        args.model,
        graph20.x.shape[1],
        args.hidden_dim,
        args.dropout,
        getattr(args, "gamma_unc", 0.5),
        getattr(args, "logvar_min", -5.0),
        getattr(args, "logvar_max", 2.0),
        getattr(args, "ec_delta_max", 0.05),
        getattr(args, "gate_normalized", False),
        getattr(args, "gradformer_max_hops", 3),
        getattr(args, "gradformer_lambda_init", 1.0),
    )
    weights = class_weights(graphs, split_map)

    train_labels = []
    for graph in graphs:
        idx = split_map[graph.year]["train"]
        if idx.size:
            train_labels.extend(graph.y.numpy()[idx].tolist())
    high_pos = sum(1 for label in train_labels if label >= 6)
    high_neg = sum(1 for label in train_labels if 0 < label < 6)
    pos_weight = min(high_neg / max(high_pos, 1), 5.0)

    teacher: RiskModel | None = None
    if args.model == "stable_tail_ec_gnn" and args.lambda_distill > 0:
        teacher = train_stable_tail_teacher(args, graphs, split_map, weights, pos_weight)

    if args.model == "stable_tail_ec_gnn":
        cal_params = list(model.calibration_head.parameters())
        cal_ids = {id(param) for param in cal_params}
        backbone_params = [
            param for param in model.parameters() if id(param) not in cal_ids
        ]
        optimizer = torch.optim.AdamW(
            [
                {"params": backbone_params, "lr": args.lr},
                {"params": cal_params, "lr": args.lr},
            ],
            weight_decay=args.weight_decay,
        )
    else:
        optimizer = torch.optim.AdamW(
            model.parameters(), lr=args.lr, weight_decay=args.weight_decay
        )

    history: list[dict[str, float]] = []
    best_state: dict[str, torch.Tensor] | None = None
    best_epoch = args.epochs
    best_score = -math.inf
    best_validation: dict[str, float] = {}
    best_satisfied_constraints = False
    for epoch in range(args.epochs):
        model.train()
        optimizer.zero_grad()
        total_loss = torch.tensor(0.0)
        full_loss = epoch >= args.stage1_epochs
        if args.model == "stable_tail_ec_gnn":
            # Keep the stable GCN/TEG representation from drifting too much
            # once edge calibration starts; the small calibration head keeps
            # the original learning rate.
            optimizer.param_groups[0]["lr"] = args.lr * (0.4 if full_loss else 1.0)
            optimizer.param_groups[1]["lr"] = args.lr
        for graph in graphs:
            if args.model == "stable_tail_ec_gnn":
                logits, _base_norm, calibrated_norm, delta, probs = model.forward_ec_outputs(graph)
                node_loss = compute_loss(
                    logits,
                    None,
                    graph.y,
                    split_map[graph.year]["train"],
                    weights,
                    args,
                    full_loss,
                    pos_weight,
                )
                loss = node_loss
                if teacher is not None:
                    with torch.no_grad():
                        teacher_logits, _teacher_log_var = teacher.forward_outputs(graph)
                    loss = loss + args.lambda_distill * compute_distill_loss(
                        logits,
                        teacher_logits,
                        split_map[graph.year]["train"],
                    )
                if full_loss:
                    edge_loss, edge_high = compute_edge_calibration_loss(
                        graph,
                        split_map[graph.year]["train"],
                        calibrated_norm,
                        probs,
                        pos_weight,
                    )
                    loss = (
                        loss
                        + args.lambda_edge * edge_loss
                        + args.lambda_edge_high * edge_high
                        + args.lambda_delta * delta.pow(2).mean()
                    )
                total_loss = total_loss + loss
            else:
                logits, log_var = model.forward_outputs(graph)
                total_loss = total_loss + compute_loss(
                    logits,
                    log_var,
                    graph.y,
                    split_map[graph.year]["train"],
                    weights,
                    args,
                    full_loss,
                    pos_weight,
                )
        total_loss.backward()
        optimizer.step()
        row = {"epoch": epoch + 1, "loss": float(total_loss.detach())}
        validation = evaluate_across_graphs(model, graphs, split_map, "val")
        if validation:
            score = checkpoint_score(validation, args)
            constraints_ok = checkpoint_constraints_hold(validation, args)
            row.update(
                {
                    "val_score": score,
                    "val_mae": validation["mae"],
                    "val_pr_auc_high": validation["pr_auc_high"],
                    "val_recall_6_8": validation["recall_6_8"],
                    "val_high_fn_rate": validation["high_fn_rate"],
                }
            )
            should_select = score > best_score and (
                constraints_ok or not best_satisfied_constraints
            )
            if constraints_ok and not best_satisfied_constraints:
                should_select = True
            if should_select:
                best_state = copy.deepcopy(model.state_dict())
                best_epoch = epoch + 1
                best_score = score
                best_validation = validation
                best_satisfied_constraints = constraints_ok
        history.append(row)

    if (
        getattr(args, "checkpoint_selection", "best") == "best"
        and best_state is not None
    ):
        model.load_state_dict(best_state)
    else:
        best_epoch = args.epochs
        best_validation = evaluate_across_graphs(model, graphs, split_map, "val")
        best_score = (
            checkpoint_score(best_validation, args) if best_validation else -math.inf
        )
        best_satisfied_constraints = (
            checkpoint_constraints_hold(best_validation, args)
            if best_validation
            else False
        )

    model.eval()
    metrics: dict[str, dict[str, float]] = {}
    with torch.no_grad():
        for graph in graphs:
            logits, log_var = model.forward_outputs(graph)
            for split_name in ("train", "val", "test"):
                idx = split_map[graph.year][split_name]
                result = evaluate(logits, graph.y, idx, log_var)
                if result:
                    metrics[f"{graph.year}_{split_name}"] = result

    checkpoint_path = save_checkpoint(
        args, model, preprocessing, split_map, best_epoch, best_validation
    )
    return {
        "model": args.model,
        "paper_model_name": PAPER_MODEL_NAMES.get(args.model, args.model),
        "split": args.split,
        "seed": args.seed,
        "epochs": args.epochs,
        "experiment_tag": getattr(args, "experiment_tag", ""),
        "alpha_ord": args.alpha_ord,
        "alpha_hr": args.alpha_hr,
        "alpha_topk": args.alpha_topk,
        "lambda_nll": args.lambda_nll,
        "lambda_var": args.lambda_var,
        "ec_delta_max": getattr(args, "ec_delta_max", 0.05),
        "lambda_edge": getattr(args, "lambda_edge", 0.0),
        "lambda_edge_high": getattr(args, "lambda_edge_high", 0.0),
        "lambda_distill": getattr(args, "lambda_distill", 0.0),
        "lambda_delta": getattr(args, "lambda_delta", 0.0),
        "ec_teacher_epochs": getattr(args, "ec_teacher_epochs", 0),
        "gamma_unc": getattr(args, "gamma_unc", 0.5),
        "logvar_min": getattr(args, "logvar_min", -5.0),
        "logvar_max": getattr(args, "logvar_max", 2.0),
        "topk_frac": args.topk_frac,
        "stage1_epochs": args.stage1_epochs,
        "best_epoch": best_epoch,
        "checkpoint_path": str(checkpoint_path),
        "checkpoint_selection": getattr(args, "checkpoint_selection", "best"),
        "checkpoint_score": best_score if math.isfinite(best_score) else None,
        "checkpoint_constraints_satisfied": best_satisfied_constraints,
        "best_validation_metrics": best_validation,
        "split_b_val_fraction": getattr(args, "split_b_val_fraction", 0.2),
        "gate_normalized": getattr(args, "gate_normalized", False),
        "feature_standardization": getattr(args, "feature_standardization", False),
        "edge_normalization": getattr(args, "edge_normalization", "per_year"),
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
