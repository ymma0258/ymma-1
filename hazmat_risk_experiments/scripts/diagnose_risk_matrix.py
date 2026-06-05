"""Diagnose exported edge-risk matrices."""

from __future__ import annotations

import argparse
import csv
import json
import random
from pathlib import Path

import networkx as nx
import numpy as np


DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\risk_matrices")
EPS = 1e-12


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("risk_dirs", nargs="+", type=Path)
    parser.add_argument("--year", default="data_2021", choices=["data_2020", "data_2021"])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--sample-pairs", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--batch-name", default="risk_matrix_diagnostics")
    return parser.parse_args()


def load_graph(risk_dir: Path, year: str) -> tuple[nx.Graph, np.ndarray, np.ndarray]:
    edge = np.load(risk_dir / f"{year}_edge_risk.npz")
    node = np.load(risk_dir / f"{year}_node_risk.npz")
    graph = nx.Graph()
    for src, dst, risk, raw_w in zip(edge["src"], edge["dst"], edge["R_ij"], edge["w_raw"]):
        graph.add_edge(int(src), int(dst), risk=float(risk), w_raw=float(raw_w))
    return graph, node["scores_norm"], node["labels"]


def reachable_ratio(graph: nx.Graph, sample_pairs: int, seed: int) -> float:
    rng = random.Random(seed)
    nodes = list(graph.nodes)
    if len(nodes) < 2:
        return 0.0
    reachable = 0
    for _ in range(sample_pairs):
        src, dst = rng.sample(nodes, 2)
        if nx.has_path(graph, src, dst):
            reachable += 1
    return reachable / sample_pairs


def diagnose(risk_dir: Path, year: str, sample_pairs: int, seed: int) -> dict[str, object]:
    graph, scores_norm, _ = load_graph(risk_dir, year)
    risks = np.asarray([data["risk"] for _, _, data in graph.edges(data=True)], dtype=float)
    attrs = np.asarray([data["w_raw"] for _, _, data in graph.edges(data=True)], dtype=float)
    largest = max(nx.connected_components(graph), key=len) if graph.number_of_nodes() else set()
    largest_graph = graph.subgraph(largest)
    graph_nodes = np.asarray(list(graph.nodes), dtype=int)
    scores = scores_norm[graph_nodes] if graph_nodes.size else np.asarray([], dtype=float)

    return {
        "risk_dir": str(risk_dir),
        "risk_version": risk_dir.name,
        "year": year,
        "node_count": graph.number_of_nodes(),
        "edge_count": graph.number_of_edges(),
        "zero_risk_edge_count": int(np.sum(risks <= EPS)),
        "zero_risk_edge_ratio": float(np.mean(risks <= EPS)) if risks.size else 0.0,
        "risk_min": float(np.min(risks)) if risks.size else 0.0,
        "risk_p25": float(np.percentile(risks, 25)) if risks.size else 0.0,
        "risk_p50": float(np.percentile(risks, 50)) if risks.size else 0.0,
        "risk_p75": float(np.percentile(risks, 75)) if risks.size else 0.0,
        "risk_p90": float(np.percentile(risks, 90)) if risks.size else 0.0,
        "risk_p95": float(np.percentile(risks, 95)) if risks.size else 0.0,
        "risk_p99": float(np.percentile(risks, 99)) if risks.size else 0.0,
        "risk_max": float(np.max(risks)) if risks.size else 0.0,
        "edge_attribute_zero_ratio": float(np.mean(attrs <= EPS)) if attrs.size else 0.0,
        "S_i_norm_zero_or_near_zero_ratio": float(np.mean(scores <= 1e-6)) if scores.size else 0.0,
        "component_count": nx.number_connected_components(graph) if graph.number_of_nodes() else 0,
        "largest_component_nodes": largest_graph.number_of_nodes(),
        "largest_component_edges": largest_graph.number_of_edges(),
        "od_reachable_ratio": reachable_ratio(graph, sample_pairs, seed),
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_report(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# Risk Matrix Diagnostics",
        "",
        "| Version | Edges | Zero ratio | P25 | P50 | P75 | P90 | P95 | P99 | Max | LCC nodes | LCC edges | OD reachable |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {ver} | {edges} | {zero:.3%} | {p25:.6f} | {p50:.6f} | {p75:.6f} | {p90:.6f} | {p95:.6f} | {p99:.6f} | {mx:.6f} | {nodes} | {lcc_edges} | {reach:.3%} |".format(
                ver=row["risk_version"],
                edges=row["edge_count"],
                zero=row["zero_risk_edge_ratio"],
                p25=row["risk_p25"],
                p50=row["risk_p50"],
                p75=row["risk_p75"],
                p90=row["risk_p90"],
                p95=row["risk_p95"],
                p99=row["risk_p99"],
                mx=row["risk_max"],
                nodes=row["largest_component_nodes"],
                lcc_edges=row["largest_component_edges"],
                reach=row["od_reachable_ratio"],
            )
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    out_dir = args.output_dir / args.batch_name
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = [diagnose(path, args.year, args.sample_pairs, args.seed) for path in args.risk_dirs]
    write_csv(out_dir / "risk_matrix_diagnostics.csv", rows)
    (out_dir / "risk_matrix_diagnostics.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_report(out_dir / "risk_matrix_diagnostics.md", rows)
    print(f"Wrote risk matrix diagnostics to {out_dir}")


if __name__ == "__main__":
    main()

