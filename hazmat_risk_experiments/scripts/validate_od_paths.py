"""Validate OD paths using exported continuous edge risks.

The script implements stage 5 of the experiment plan. It samples OD pairs from
the largest connected component and compares four path choices:

- Hop-shortest
- Mean-risk shortest
- CVaR-risk path among k hop-short candidate paths
- CVaR + Concentration path among the same candidates
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import networkx as nx
import numpy as np
from scipy.stats import wilcoxon


DEFAULT_RISK_DIR = Path(
    r"D:\PyVRP-main\hazmat_risk_experiments\outputs\risk_matrices\teg_gnn_splitB_seed0_epochs20"
)
DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\od_paths")
EPS = 1e-12


def paired_wilcoxon_p(base_values: np.ndarray, method_values: np.ndarray) -> float:
    diff = np.asarray(base_values, dtype=float) - np.asarray(method_values, dtype=float)
    if diff.size == 0 or np.all(np.abs(diff) <= EPS):
        return 1.0
    try:
        return float(wilcoxon(base_values, method_values, zero_method="wilcox").pvalue)
    except ValueError:
        return 1.0


@dataclass
class PathMetrics:
    hop: int
    mean_risk: float
    max_risk: float
    cvar80: float
    cvar90: float
    cvar95: float
    re: float
    hhi: float
    gini: float
    total_risk: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--risk-dir", type=Path, default=DEFAULT_RISK_DIR)
    parser.add_argument("--year", default="data_2021", choices=["data_2020", "data_2021"])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--pairs-per-group", type=int, default=10)
    parser.add_argument("--k-paths", type=int, default=20)
    parser.add_argument("--lambda-re", type=float, default=1.0)
    parser.add_argument("--cvar-alpha", type=float, default=0.90)
    parser.add_argument("--re-threshold", choices=["mean", "p75", "p90"], default="mean")
    parser.add_argument("--risk-floor", type=float, default=1e-4)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--batch-name", default="od_smoke")
    return parser.parse_args()


def gini(values: np.ndarray) -> float:
    values = np.asarray(values, dtype=float)
    if values.size == 0:
        return 0.0
    total = float(values.sum())
    if total <= EPS:
        return 0.0
    sorted_values = np.sort(values)
    n = values.size
    index = np.arange(1, n + 1)
    return float((2 * np.sum(index * sorted_values) / (n * total)) - ((n + 1) / n))


def cvar(values: np.ndarray, alpha: float) -> float:
    values = np.asarray(values, dtype=float)
    if values.size == 0:
        return 0.0
    threshold = float(np.quantile(values, alpha, method="higher"))
    tail = values[values >= threshold]
    return float(tail.mean()) if tail.size else threshold


def hhi(values: np.ndarray) -> float:
    values = np.asarray(values, dtype=float)
    total = float(values.sum())
    if total <= EPS:
        return 0.0
    shares = values / (total + EPS)
    return float(np.sum(shares * shares))


def edge_risk(graph: nx.Graph, left: int, right: int, risk_attr: str = "risk") -> float:
    return float(graph[left][right][risk_attr])


def path_edge_risks(graph: nx.Graph, path: list[int], risk_attr: str = "risk") -> np.ndarray:
    risks = []
    for left, right in zip(path[:-1], path[1:]):
        risks.append(edge_risk(graph, left, right, risk_attr))
    return np.asarray(risks, dtype=float)


def path_metrics(
    graph: nx.Graph,
    path: list[int],
    re_threshold_value: float,
    risk_attr: str = "risk",
) -> PathMetrics:
    risks = path_edge_risks(graph, path, risk_attr)
    if risks.size == 0:
        return PathMetrics(0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    return PathMetrics(
        hop=int(risks.size),
        mean_risk=float(risks.mean()),
        max_risk=float(risks.max()),
        cvar80=cvar(risks, 0.80),
        cvar90=cvar(risks, 0.90),
        cvar95=cvar(risks, 0.95),
        re=float(np.maximum(risks - re_threshold_value, 0.0).mean()),
        hhi=hhi(risks),
        gini=gini(risks),
        total_risk=float(risks.sum()),
    )


def load_graph(risk_dir: Path, year: str) -> tuple[nx.Graph, np.ndarray, np.ndarray]:
    edge_data = np.load(risk_dir / f"{year}_edge_risk.npz")
    node_data = np.load(risk_dir / f"{year}_node_risk.npz")

    graph = nx.Graph()
    for src, dst, risk, exposure in zip(
        edge_data["src"],
        edge_data["dst"],
        edge_data["R_ij"],
        edge_data["w_norm"],
    ):
        graph.add_edge(int(src), int(dst), risk=float(risk), exposure=float(exposure), hop=1.0)

    scores_norm = node_data["scores_norm"]
    labels = node_data["labels"]
    return graph, scores_norm, labels


def add_floor_risk(graph: nx.Graph, floor: float) -> None:
    for _, _, data in graph.edges(data=True):
        data["risk_floor"] = floor + (1.0 - floor) * float(data["risk"])


def risk_distribution_summary(graph: nx.Graph, scores_norm: np.ndarray) -> dict[str, float | int]:
    risks = np.asarray([data["risk"] for _, _, data in graph.edges(data=True)], dtype=float)
    exposures = np.asarray(
        [data["exposure"] for _, _, data in graph.edges(data=True)], dtype=float
    )
    graph_nodes = np.asarray(list(graph.nodes), dtype=int)
    node_scores = scores_norm[graph_nodes]
    return {
        "edge_count": int(risks.size),
        "zero_risk_edge_count": int(np.sum(risks <= EPS)),
        "zero_risk_edge_ratio": float(np.mean(risks <= EPS)),
        "risk_min": float(np.min(risks)),
        "risk_p25": float(np.percentile(risks, 25)),
        "risk_p50": float(np.percentile(risks, 50)),
        "risk_p75": float(np.percentile(risks, 75)),
        "risk_p90": float(np.percentile(risks, 90)),
        "risk_p95": float(np.percentile(risks, 95)),
        "risk_p99": float(np.percentile(risks, 99)),
        "risk_max": float(np.max(risks)),
        "edge_attribute_zero_ratio": float(np.mean(exposures <= EPS)),
        "S_i_norm_zero_or_near_zero_ratio": float(np.mean(node_scores <= 1e-6)),
    }


def largest_component_subgraph(graph: nx.Graph) -> nx.Graph:
    largest_nodes = max(nx.connected_components(graph), key=len)
    return graph.subgraph(largest_nodes).copy()


def sample_pairs(
    graph: nx.Graph,
    scores_norm: np.ndarray,
    pairs_per_group: int,
    seed: int,
) -> list[dict[str, int | str]]:
    rng = random.Random(seed)
    nodes = list(graph.nodes)
    component_set = set(nodes)

    threshold = float(np.quantile(scores_norm[nodes], 0.80))
    high_nodes = [node for node in nodes if scores_norm[node] >= threshold]
    normal_nodes = [node for node in nodes if scores_norm[node] < threshold]

    groups = [
        ("high_high", high_nodes, high_nodes),
        ("high_normal", high_nodes, normal_nodes),
        ("normal_high", normal_nodes, high_nodes),
    ]

    pairs: list[dict[str, int | str]] = []
    used: set[tuple[str, int, int]] = set()
    for group_name, starts, ends in groups:
        attempts = 0
        while len([pair for pair in pairs if pair["group"] == group_name]) < pairs_per_group:
            attempts += 1
            if attempts > pairs_per_group * 1000:
                raise RuntimeError(f"Could not sample enough OD pairs for {group_name}")
            src = rng.choice(starts)
            dst = rng.choice(ends)
            if src == dst:
                continue
            if src not in component_set or dst not in component_set:
                continue
            key = (group_name, src, dst)
            if key in used:
                continue
            used.add(key)
            pairs.append({"group": group_name, "src": int(src), "dst": int(dst)})

    return pairs


def shortest_simple_candidates(
    graph: nx.Graph, src: int, dst: int, k_paths: int
) -> list[list[int]]:
    candidates: list[list[int]] = []
    for path in nx.shortest_simple_paths(graph, src, dst, weight="hop"):
        candidates.append([int(node) for node in path])
        if len(candidates) >= k_paths:
            break
    return candidates


def choose_cvar_path(
    graph: nx.Graph,
    candidates: list[list[int]],
    re_threshold_value: float,
    cvar_alpha: float,
) -> list[int]:
    return min(
        candidates,
        key=lambda path: (
            cvar(path_edge_risks(graph, path), cvar_alpha),
            path_metrics(graph, path, re_threshold_value).max_risk,
            len(path),
        ),
    )


def choose_cvar_re_path(
    graph: nx.Graph,
    candidates: list[list[int]],
    re_threshold_value: float,
    lambda_re: float,
    cvar_alpha: float,
) -> list[int]:
    def objective(path: list[int]) -> tuple[float, float, int]:
        risks = path_edge_risks(graph, path)
        metrics = path_metrics(graph, path, re_threshold_value)
        return (cvar(risks, cvar_alpha) + lambda_re * metrics.re, metrics.max_risk, metrics.hop)

    return min(candidates, key=objective)


def method_paths(
    graph: nx.Graph,
    src: int,
    dst: int,
    k_paths: int,
    re_threshold_value: float,
    lambda_re: float,
    cvar_alpha: float,
) -> dict[str, list[int]]:
    hop_path = nx.shortest_path(graph, src, dst, weight="hop")
    mean_risk_raw_path = nx.shortest_path(graph, src, dst, weight="risk")
    mean_risk_floor_path = nx.shortest_path(graph, src, dst, weight="risk_floor")
    candidates = shortest_simple_candidates(graph, src, dst, k_paths)
    return {
        "Hop-shortest": [int(node) for node in hop_path],
        "Mean-risk-raw": [int(node) for node in mean_risk_raw_path],
        "Mean-risk-floor": [int(node) for node in mean_risk_floor_path],
        "CVaR-risk": choose_cvar_path(
            graph, candidates, re_threshold_value, cvar_alpha
        ),
        "CVaR+Concentration": choose_cvar_re_path(
            graph, candidates, re_threshold_value, lambda_re, cvar_alpha
        ),
    }


def metric_row(
    pair: dict[str, int | str],
    method: str,
    path: list[int],
    metrics: PathMetrics,
    baseline: PathMetrics,
) -> dict[str, object]:
    return {
        "group": pair["group"],
        "src": pair["src"],
        "dst": pair["dst"],
        "method": method,
        "path": " ".join(map(str, path)),
        "hop": metrics.hop,
        "mean_risk": metrics.mean_risk,
        "max_risk": metrics.max_risk,
        "cvar80": metrics.cvar80,
        "cvar90": metrics.cvar90,
        "cvar95": metrics.cvar95,
        "re": metrics.re,
        "hhi": metrics.hhi,
        "gini": metrics.gini,
        "total_risk": metrics.total_risk,
        "hop_increase_pct": (metrics.hop - baseline.hop) / (baseline.hop + EPS),
        "risk_reduction_pct": (baseline.total_risk - metrics.total_risk)
        / (baseline.total_risk + EPS),
        "cvar90_reduction_pct": (baseline.cvar90 - metrics.cvar90)
        / (baseline.cvar90 + EPS),
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    metrics = [
        "hop",
        "mean_risk",
        "max_risk",
        "cvar80",
        "cvar90",
        "re",
        "hhi",
        "gini",
        "total_risk",
        "hop_increase_pct",
        "risk_reduction_pct",
        "cvar90_reduction_pct",
    ]
    grouped: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        grouped.setdefault(str(row["method"]), []).append(row)

    baseline_by_pair = {
        (row["group"], row["src"], row["dst"]): row
        for row in rows
        if row["method"] == "Hop-shortest"
    }
    cvar_by_pair = {
        (row["group"], row["src"], row["dst"]): row
        for row in rows
        if row["method"] == "CVaR-risk"
    }

    summary: list[dict[str, object]] = []
    for method, group_rows in sorted(grouped.items()):
        out: dict[str, object] = {"method": method, "runs": len(group_rows)}
        for metric in metrics:
            values = np.asarray([float(row[metric]) for row in group_rows], dtype=float)
            out[f"{metric}_mean"] = float(values.mean())
            out[f"{metric}_std"] = float(values.std(ddof=1)) if values.size > 1 else 0.0

        for metric in ("total_risk", "max_risk", "cvar80", "cvar90", "re", "gini"):
            method_values = np.asarray([float(row[metric]) for row in group_rows], dtype=float)
            base_values = np.asarray(
                [
                    float(baseline_by_pair[(row["group"], row["src"], row["dst"])][metric])
                    for row in group_rows
                ],
                dtype=float,
            )
            per_od = (base_values - method_values) / (base_values + EPS)
            out[f"{metric}_mean_baseline"] = float(base_values.mean())
            out[f"{metric}_mean_method"] = float(method_values.mean())
            out[f"{metric}_aggregate_reduction"] = float(
                (base_values.mean() - method_values.mean()) / (base_values.mean() + EPS)
            )
            out[f"{metric}_mean_per_od_reduction"] = float(per_od.mean())
            out[f"{metric}_median_per_od_reduction"] = float(np.median(per_od))
            out[f"{metric}_wilcoxon_p"] = paired_wilcoxon_p(base_values, method_values)
        overlaps = np.asarray(
            [
                str(row["path"])
                == str(cvar_by_pair[(row["group"], row["src"], row["dst"])]["path"])
                for row in group_rows
            ],
            dtype=float,
        )
        out["path_overlap_with_cvar"] = float(overlaps.mean())
        out["selected_path_changed_rate"] = float(1.0 - overlaps.mean())
        summary.append(out)
    return summary


def write_report(path: Path, summary_rows: list[dict[str, object]], meta: dict[str, object]) -> None:
    lines = [
        "# OD Path Validation Report",
        "",
        f"- Year: `{meta['year']}`",
        f"- OD pairs: `{meta['num_pairs']}`",
        f"- k candidate paths: `{meta['k_paths']}`",
        f"- lambda RE: `{meta['lambda_re']}`",
        f"- CVaR alpha: `{meta['cvar_alpha']}`",
        f"- RE threshold: `{meta['re_threshold']}` = `{meta['re_threshold_value']}`",
        f"- risk floor: `{meta['risk_floor']}`",
        "",
        "| Method | Hop | MaxRisk | CVaR80 | CVaR90 | RE | Gini | Hop inc. | Total risk agg. red. | Total risk mean per-OD red. | CVaR90 agg. red. | CVaR90 mean per-OD red. | Path overlap w/ CVaR | Changed rate |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary_rows:
        lines.append(
            "| {method} | {hop:.3f} | {maxrisk:.6f} | {cvar80:.6f} | {cvar90:.6f} | {re:.6f} | {gini:.6f} | {hopinc:.3%} | {riskagg:.3%} | {riskmean:.3%} | {cvaragg:.3%} | {cvarmean:.3%} | {overlap:.3%} | {changed:.3%} |".format(
                method=row["method"],
                hop=row["hop_mean"],
                maxrisk=row["max_risk_mean"],
                cvar80=row["cvar80_mean"],
                cvar90=row["cvar90_mean"],
                re=row["re_mean"],
                gini=row["gini_mean"],
                hopinc=row["hop_increase_pct_mean"],
                riskagg=row["total_risk_aggregate_reduction"],
                riskmean=row["total_risk_mean_per_od_reduction"],
                cvaragg=row["cvar90_aggregate_reduction"],
                cvarmean=row["cvar90_mean_per_od_reduction"],
                overlap=row["path_overlap_with_cvar"],
                changed=row["selected_path_changed_rate"],
            )
        )
    lines.extend(
        [
            "",
            "Aggregate reduction is computed from method and baseline means. Mean per-OD reduction first computes a paired reduction for each OD and then averages those reductions.",
            "This is an OD path-validation run on the regional association graph, not a real-road navigation experiment.",
            "Continuous edge risk `R_ij` is used for all downstream metrics.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_dir = args.output_dir / args.batch_name
    out_dir.mkdir(parents=True, exist_ok=True)

    graph, scores_norm, labels = load_graph(args.risk_dir, args.year)
    graph = largest_component_subgraph(graph)
    add_floor_risk(graph, args.risk_floor)
    pairs = sample_pairs(graph, scores_norm, args.pairs_per_group, args.seed)
    graph_risks = np.asarray([data["risk"] for _, _, data in graph.edges(data=True)], dtype=float)
    if args.re_threshold == "mean":
        re_threshold_value = float(np.mean(graph_risks))
    elif args.re_threshold == "p75":
        re_threshold_value = float(np.percentile(graph_risks, 75))
    elif args.re_threshold == "p90":
        re_threshold_value = float(np.percentile(graph_risks, 90))
    else:
        raise ValueError(f"Unknown RE threshold: {args.re_threshold}")
    risk_diag = risk_distribution_summary(graph, scores_norm)

    detail_rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    for idx, pair in enumerate(pairs, start=1):
        src = int(pair["src"])
        dst = int(pair["dst"])
        try:
            paths = method_paths(
                graph,
                src,
                dst,
                args.k_paths,
                re_threshold_value,
                args.lambda_re,
                args.cvar_alpha,
            )
            baseline_metrics = path_metrics(
                graph, paths["Hop-shortest"], re_threshold_value
            )
            for method, path in paths.items():
                metrics = path_metrics(graph, path, re_threshold_value)
                detail_rows.append(metric_row(pair, method, path, metrics, baseline_metrics))
        except Exception as exc:  # noqa: BLE001 - batch validation records OD failures.
            failures.append({"pair_index": idx, **pair, "error": repr(exc)})

    summary_rows = summarize(detail_rows)
    meta = {
        "year": args.year,
        "risk_dir": str(args.risk_dir),
        "num_pairs": len(pairs),
        "num_successful_pairs": len({(row["group"], row["src"], row["dst"]) for row in detail_rows}),
        "num_failures": len(failures),
        "pairs_per_group": args.pairs_per_group,
        "k_paths": args.k_paths,
        "lambda_re": args.lambda_re,
        "cvar_alpha": args.cvar_alpha,
        "re_threshold": args.re_threshold,
        "re_threshold_value": re_threshold_value,
        "risk_floor": args.risk_floor,
        "seed": args.seed,
        "largest_component_nodes": graph.number_of_nodes(),
        "largest_component_edges": graph.number_of_edges(),
        "risk_diagnostics": risk_diag,
    }

    write_csv(out_dir / "od_pairs.csv", pairs)
    write_csv(out_dir / "od_path_detail.csv", detail_rows)
    write_csv(out_dir / "od_path_summary.csv", summary_rows)
    (out_dir / "od_path_failures.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out_dir / "od_path_meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out_dir / "risk_diagnostics.json").write_text(
        json.dumps(risk_diag, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_report(out_dir / "od_path_report.md", summary_rows, meta)
    print(f"Wrote OD path validation to {out_dir}")


if __name__ == "__main__":
    main()
