"""Audit hazardous materials trajectory graph data.

The script reads the zip dataset without extracting it, computes basic graph,
label, feature, and edge-attribute diagnostics, and writes JSON/CSV/Markdown
reports.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import math
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

import numpy as np


DEFAULT_ZIP = Path(r"D:\城市危险化学品运输车辆轨迹数据.zip")
DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\audit")
YEARS = ("data_2020", "data_2021")
EPS = 1e-12


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", type=Path, default=DEFAULT_ZIP, help="Input zip file.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Directory for audit reports.",
    )
    return parser.parse_args()


def read_npy_from_zip(zf: zipfile.ZipFile, year: str, filename: str) -> np.ndarray:
    matches = [name for name in zf.namelist() if name.endswith(f"{year}/{filename}")]
    if not matches:
        raise FileNotFoundError(f"Could not find {year}/{filename} in zip.")

    with zf.open(matches[0]) as handle:
        return np.load(io.BytesIO(handle.read()), allow_pickle=False)


def quantiles(values: np.ndarray) -> dict[str, float]:
    flat = np.asarray(values, dtype=float).reshape(-1)
    return {
        "min": float(np.min(flat)),
        "max": float(np.max(flat)),
        "mean": float(np.mean(flat)),
        "std": float(np.std(flat)),
        "p50": float(np.percentile(flat, 50)),
        "p90": float(np.percentile(flat, 90)),
        "p95": float(np.percentile(flat, 95)),
        "p99": float(np.percentile(flat, 99)),
    }


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node: int) -> int:
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, left: int, right: int) -> None:
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return
        if self.rank[root_left] < self.rank[root_right]:
            root_left, root_right = root_right, root_left
        self.parent[root_right] = root_left
        if self.rank[root_left] == self.rank[root_right]:
            self.rank[root_left] += 1

    def component_sizes(self) -> list[int]:
        counts: Counter[int] = Counter(self.find(node) for node in range(len(self.parent)))
        return sorted(counts.values(), reverse=True)


def weak_component_sizes(num_nodes: int, edges: np.ndarray) -> list[int]:
    uf = UnionFind(num_nodes)
    for src, dst in edges:
        uf.union(int(src), int(dst))
    return uf.component_sizes()


def strongly_connected_component_sizes(num_nodes: int, edges: np.ndarray) -> list[int]:
    adj: list[list[int]] = [[] for _ in range(num_nodes)]
    rev: list[list[int]] = [[] for _ in range(num_nodes)]
    for src_raw, dst_raw in edges:
        src = int(src_raw)
        dst = int(dst_raw)
        adj[src].append(dst)
        rev[dst].append(src)

    visited = [False] * num_nodes
    order: list[int] = []

    for start in range(num_nodes):
        if visited[start]:
            continue
        stack: list[tuple[int, int]] = [(start, 0)]
        visited[start] = True
        while stack:
            node, next_idx = stack[-1]
            if next_idx < len(adj[node]):
                nxt = adj[node][next_idx]
                stack[-1] = (node, next_idx + 1)
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, 0))
            else:
                order.append(node)
                stack.pop()

    visited = [False] * num_nodes
    sizes: list[int] = []
    for start in reversed(order):
        if visited[start]:
            continue
        size = 0
        stack = [start]
        visited[start] = True
        while stack:
            node = stack.pop()
            size += 1
            for nxt in rev[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)
        sizes.append(size)

    return sorted(sizes, reverse=True)


def undirected_edge_summary(edges: np.ndarray, edge_attr: np.ndarray) -> dict[str, float | int]:
    merged: dict[tuple[int, int], float] = {}
    directed_pairs = set()
    reciprocal_count = 0

    weights = edge_attr.reshape(-1).astype(float)
    for (src_raw, dst_raw), weight in zip(edges, weights):
        src = int(src_raw)
        dst = int(dst_raw)
        directed_pairs.add((src, dst))
        key = (min(src, dst), max(src, dst))
        merged[key] = max(merged.get(key, -math.inf), float(weight))

    for src, dst in directed_pairs:
        if src != dst and (dst, src) in directed_pairs:
            reciprocal_count += 1

    merged_weights = np.array(list(merged.values()), dtype=float)
    stats = quantiles(merged_weights) if merged_weights.size else {}
    return {
        "directed_edge_count": int(len(directed_pairs)),
        "undirected_edge_count_max_merge": int(len(merged)),
        "reciprocal_directed_edge_count": int(reciprocal_count),
        "self_loop_count": int(sum(1 for src, dst in directed_pairs if src == dst)),
        **{f"undirected_weight_{key}": value for key, value in stats.items()},
    }


def label_summary(labels: np.ndarray) -> dict[str, int | dict[str, int]]:
    labels_int = labels.astype(int)
    counts = Counter(int(value) for value in labels_int)
    high = sum(counts.get(label, 0) for label in (6, 7, 8))
    labeled = sum(count for label, count in counts.items() if label != 0)
    return {
        "unlabeled_count": int(counts.get(0, 0)),
        "labeled_count": int(labeled),
        "high_risk_count_6_8": int(high),
        "label_counts": {str(label): int(counts.get(label, 0)) for label in range(9)},
    }


def feature_summary(features: np.ndarray) -> dict[str, float | int]:
    per_feature_mean = np.mean(features, axis=0)
    per_feature_std = np.std(features, axis=0)
    return {
        "feature_global_min": float(np.min(features)),
        "feature_global_max": float(np.max(features)),
        "feature_global_mean": float(np.mean(features)),
        "feature_global_std": float(np.std(features)),
        "feature_mean_abs_mean": float(np.mean(np.abs(per_feature_mean))),
        "feature_mean_std": float(np.mean(per_feature_std)),
        "near_zero_std_feature_count": int(np.sum(per_feature_std < 1e-8)),
    }


def audit_year(zf: zipfile.ZipFile, year: str) -> dict[str, object]:
    x = read_npy_from_zip(zf, year, "data.x.npy")
    y = read_npy_from_zip(zf, year, "data.y.npy")
    edges = read_npy_from_zip(zf, year, "data.edge_index.npy")
    edge_attr = read_npy_from_zip(zf, year, "data.edge_attribute.npy")

    weak_sizes = weak_component_sizes(x.shape[0], edges)
    scc_sizes = strongly_connected_component_sizes(x.shape[0], edges)

    return {
        "year": year,
        "node_count": int(x.shape[0]),
        "feature_dim": int(x.shape[1]),
        "edge_count": int(edges.shape[0]),
        "edge_attr_dim": int(edge_attr.shape[1] if edge_attr.ndim > 1 else 1),
        "label_summary": label_summary(y),
        "edge_attribute_summary": quantiles(edge_attr),
        "feature_summary": feature_summary(x),
        "graph_summary": {
            "largest_weak_component": int(weak_sizes[0]) if weak_sizes else 0,
            "weak_component_count": int(len(weak_sizes)),
            "largest_strong_component": int(scc_sizes[0]) if scc_sizes else 0,
            "strong_component_count": int(len(scc_sizes)),
            "top5_weak_components": [int(value) for value in weak_sizes[:5]],
            "top5_strong_components": [int(value) for value in scc_sizes[:5]],
        },
        "undirected_summary": undirected_edge_summary(edges, edge_attr),
    }


def flatten_for_csv(record: dict[str, object]) -> dict[str, object]:
    label = record["label_summary"]
    edge = record["edge_attribute_summary"]
    graph = record["graph_summary"]
    feature = record["feature_summary"]
    undirected = record["undirected_summary"]
    assert isinstance(label, dict)
    assert isinstance(edge, dict)
    assert isinstance(graph, dict)
    assert isinstance(feature, dict)
    assert isinstance(undirected, dict)

    row: dict[str, object] = {
        "year": record["year"],
        "node_count": record["node_count"],
        "edge_count": record["edge_count"],
        "feature_dim": record["feature_dim"],
        "labeled_count": label["labeled_count"],
        "unlabeled_count": label["unlabeled_count"],
        "high_risk_count_6_8": label["high_risk_count_6_8"],
        "largest_weak_component": graph["largest_weak_component"],
        "weak_component_count": graph["weak_component_count"],
        "largest_strong_component": graph["largest_strong_component"],
        "strong_component_count": graph["strong_component_count"],
    }
    row.update({f"edge_attr_{key}": value for key, value in edge.items()})
    row.update(feature)
    row.update(undirected)

    counts = label["label_counts"]
    assert isinstance(counts, dict)
    for label_id in range(9):
        row[f"label_{label_id}"] = counts[str(label_id)]
    return row


def write_csv(path: Path, rows: Iterable[dict[str, object]]) -> None:
    rows = list(rows)
    if not rows:
        return
    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def markdown_report(records: list[dict[str, object]]) -> str:
    lines = [
        "# Hazardous Materials Trajectory Graph Data Audit",
        "",
        "## Summary",
        "",
        "| Year | Nodes | Edges | Labeled | Unlabeled | High risk 6-8 | Edge attr mean | Edge attr P95 | Largest WCC | Largest SCC |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for record in records:
        label = record["label_summary"]
        edge = record["edge_attribute_summary"]
        graph = record["graph_summary"]
        assert isinstance(label, dict)
        assert isinstance(edge, dict)
        assert isinstance(graph, dict)
        lines.append(
            "| {year} | {nodes} | {edges} | {labeled} | {unlabeled} | {high} | "
            "{mean:.6f} | {p95:.6f} | {wcc} | {scc} |".format(
                year=record["year"],
                nodes=record["node_count"],
                edges=record["edge_count"],
                labeled=label["labeled_count"],
                unlabeled=label["unlabeled_count"],
                high=label["high_risk_count_6_8"],
                mean=edge["mean"],
                p95=edge["p95"],
                wcc=graph["largest_weak_component"],
                scc=graph["largest_strong_component"],
            )
        )

    lines.extend(["", "## Label Distribution", ""])
    for record in records:
        label = record["label_summary"]
        assert isinstance(label, dict)
        counts = label["label_counts"]
        assert isinstance(counts, dict)
        lines.append(f"### {record['year']}")
        lines.append("")
        lines.append("| Label | Count |")
        lines.append("|---:|---:|")
        for label_id in range(9):
            lines.append(f"| {label_id} | {counts[str(label_id)]} |")
        lines.append("")

    lines.extend(
        [
            "## Notes",
            "",
            "- Label 0 is treated as unlabeled, not low risk.",
            "- High risk is defined as labels 6, 7, and 8.",
            "- The main path-validation graph should be undirected using max edge-attribute merge.",
            "- Strongly connected components are reported only to diagnose directed reachability.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(args.zip) as zf:
        records = [audit_year(zf, year) for year in YEARS]

    json_path = args.output_dir / "audit_summary.json"
    csv_path = args.output_dir / "audit_summary.csv"
    md_path = args.output_dir / "audit_report.md"

    json_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(csv_path, [flatten_for_csv(record) for record in records])
    md_path.write_text(markdown_report(records), encoding="utf-8")

    print(f"Wrote {json_path}")
    print(f"Wrote {csv_path}")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()

