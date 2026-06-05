"""Create representative OD path case figures 13 and 14."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import validate_od_paths as od  # noqa: E402


ROOT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs")
OUT_DIR = ROOT / "final_figures_stable_tail_gnn"
FIG_DIR = OUT_DIR / "figures"
TABLE_DIR = OUT_DIR / "tables"
RISK_DIR = ROOT / "risk_matrices" / "gcn_teg_concat_splitB_seed0_epochs50_floor_0p01"
PAIR_FILE = ROOT / "od_paths" / "od_formal_floor001_p50_k50_cached_floor_0p01_a0p9_l1_p75" / "od_pairs.csv"
YEAR = "data_2021"
K_PATHS = 50
ALPHA = 0.90
LAMBDA_RE = 1.0


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


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


def path_string(path: list[int]) -> str:
    return " ".join(str(node) for node in path)


def edge_set(path: list[int]) -> set[tuple[int, int]]:
    return {tuple(sorted((left, right))) for left, right in zip(path[:-1], path[1:])}


def path_overlap(left: list[int], right: list[int]) -> float:
    left_edges = edge_set(left)
    right_edges = edge_set(right)
    union = left_edges | right_edges
    if not union:
        return 1.0
    return len(left_edges & right_edges) / len(union)


def high_edge_count(graph: nx.Graph, path: list[int], threshold: float) -> int:
    risks = od.path_edge_risks(graph, path)
    return int(np.sum(risks >= threshold))


def evaluate_pairs() -> tuple[nx.Graph, float, float, list[dict[str, object]]]:
    graph, scores_norm, _ = od.load_graph(RISK_DIR, YEAR)
    graph = od.largest_component_subgraph(graph)

    risks = np.asarray([data["risk"] for _, _, data in graph.edges(data=True)], dtype=float)
    p75 = float(np.percentile(risks, 75))
    p90 = float(np.percentile(risks, 90))

    rows: list[dict[str, object]] = []
    for pair in read_csv(PAIR_FILE):
        src = int(pair["src"])
        dst = int(pair["dst"])
        candidates = od.shortest_simple_candidates(graph, src, dst, K_PATHS)
        threshold_value = p75
        hop_path = [int(node) for node in nx.shortest_path(graph, src, dst, weight="hop")]
        cvar_path = od.choose_cvar_path(graph, candidates, threshold_value, ALPHA)
        cvar_re_path = od.choose_cvar_re_path(graph, candidates, threshold_value, LAMBDA_RE, ALPHA)

        hop_metrics = od.path_metrics(graph, hop_path, threshold_value)
        cvar_metrics = od.path_metrics(graph, cvar_path, threshold_value)
        cvar_re_metrics = od.path_metrics(graph, cvar_re_path, threshold_value)

        cvar90_reduction = (hop_metrics.cvar90 - cvar_metrics.cvar90) / (hop_metrics.cvar90 + od.EPS)
        hop_increase = (cvar_metrics.hop - hop_metrics.hop) / (hop_metrics.hop + od.EPS)
        re_reduction = (cvar_metrics.re - cvar_re_metrics.re) / (cvar_metrics.re + od.EPS)
        rows.append(
            {
                "group": pair["group"],
                "src": src,
                "dst": dst,
                "hop_path": hop_path,
                "cvar_path": cvar_path,
                "cvar_re_path": cvar_re_path,
                "hop_path_str": path_string(hop_path),
                "cvar_path_str": path_string(cvar_path),
                "cvar_re_path_str": path_string(cvar_re_path),
                "hop_hop": hop_metrics.hop,
                "cvar_hop": cvar_metrics.hop,
                "cvar_re_hop": cvar_re_metrics.hop,
                "hop_cvar90": hop_metrics.cvar90,
                "cvar_cvar90": cvar_metrics.cvar90,
                "cvar_re_cvar90": cvar_re_metrics.cvar90,
                "hop_max_risk": hop_metrics.max_risk,
                "cvar_max_risk": cvar_metrics.max_risk,
                "cvar_re_max_risk": cvar_re_metrics.max_risk,
                "hop_re": hop_metrics.re,
                "cvar_re": cvar_metrics.re,
                "cvar_concentration_re": cvar_re_metrics.re,
                "cvar90_reduction": cvar90_reduction,
                "hop_increase": hop_increase,
                "re_reduction_from_concentration": re_reduction,
                "hop_cvar_overlap": path_overlap(hop_path, cvar_path),
                "cvar_concentration_overlap": path_overlap(cvar_path, cvar_re_path),
                "hop_p90_edge_count": high_edge_count(graph, hop_path, p90),
                "cvar_p90_edge_count": high_edge_count(graph, cvar_path, p90),
                "cvar_re_p90_edge_count": high_edge_count(graph, cvar_re_path, p90),
            }
        )

    return graph, p75, p90, rows


def select_case(rows: list[dict[str, object]]) -> dict[str, object]:
    candidates = [
        row
        for row in rows
        if row["hop_path"] != row["cvar_path"]
        and row["cvar_path"] != row["cvar_re_path"]
        and float(row["cvar90_reduction"]) > 0
        and float(row["hop_increase"]) >= 0
        and int(row["hop_p90_edge_count"]) >= 1
    ]
    if not candidates:
        candidates = [
            row
            for row in rows
            if row["hop_path"] != row["cvar_path"]
            and float(row["cvar90_reduction"]) > 0
            and int(row["hop_p90_edge_count"]) >= 1
        ]
    if not candidates:
        candidates = [row for row in rows if row["hop_path"] != row["cvar_path"]]

    mean_reduction = float(np.mean([float(row["cvar90_reduction"]) for row in rows]))
    mean_hop_inc = float(np.mean([float(row["hop_increase"]) for row in rows]))
    std_reduction = float(np.std([float(row["cvar90_reduction"]) for row in rows]) + 1e-12)
    std_hop_inc = float(np.std([float(row["hop_increase"]) for row in rows]) + 1e-12)

    def score(row: dict[str, object]) -> float:
        concentration_penalty = 0.0 if row["cvar_path"] != row["cvar_re_path"] else 2.0
        high_edge_penalty = abs(int(row["hop_p90_edge_count"]) - 2) * 0.25
        return (
            abs(float(row["cvar90_reduction"]) - mean_reduction) / std_reduction
            + abs(float(row["hop_increase"]) - mean_hop_inc) / std_hop_inc
            + concentration_penalty
            + high_edge_penalty
        )

    selected = min(candidates, key=score)
    selected["selection_score"] = score(selected)
    selected["mean_cvar90_reduction_all_od"] = mean_reduction
    selected["mean_hop_increase_all_od"] = mean_hop_inc
    return selected


def case_rows(case: dict[str, object]) -> list[dict[str, object]]:
    method_map = [
        ("Hop-shortest", "hop"),
        ("CVaR-risk", "cvar"),
        ("CVaR+Concentration", "cvar_re"),
    ]
    rows: list[dict[str, object]] = []
    for method, prefix in method_map:
        rows.append(
            {
                "method": method,
                "group": case["group"],
                "src": case["src"],
                "dst": case["dst"],
                "path": case[f"{prefix}_path_str"],
                "hop": case[f"{prefix}_hop"],
                "cvar90": case[f"{prefix}_cvar90"],
                "max_risk": case[f"{prefix}_max_risk"],
                "re": case["cvar_concentration_re"] if prefix == "cvar_re" else case[f"{prefix}_re"],
                "p90_edge_count": case[f"{prefix}_p90_edge_count"],
            }
        )
    return rows


def subgraph_for_paths(graph: nx.Graph, paths: list[list[int]], p90: float) -> nx.Graph:
    path_nodes = set().union(*(set(path) for path in paths))
    nodes = set(path_nodes)
    for node in sorted(path_nodes):
        neighbors = sorted(
            graph.neighbors(node),
            key=lambda nbr: graph[node][nbr]["risk"],
            reverse=True,
        )
        nodes.update(neighbors[:5])

    if len(nodes) > 130:
        ranked = sorted(
            nodes - path_nodes,
            key=lambda node: max((graph[node][nbr]["risk"] for nbr in graph.neighbors(node)), default=0.0),
            reverse=True,
        )
        nodes = set(path_nodes) | set(ranked[: 130 - len(path_nodes)])

    sub = graph.subgraph(nodes).copy()
    for left, right in edge_set(paths[0]) | edge_set(paths[1]) | (edge_set(paths[2]) if len(paths) > 2 else set()):
        if graph.has_edge(left, right):
            sub.add_edge(left, right, **graph[left][right])
    return sub


def draw_base(ax: plt.Axes, graph: nx.Graph, pos: dict[int, np.ndarray], p75: float, p90: float) -> None:
    low_edges = []
    mid_edges = []
    high_edges = []
    for left, right, data in graph.edges(data=True):
        risk = float(data["risk"])
        if risk >= p90:
            high_edges.append((left, right))
        elif risk >= p75:
            mid_edges.append((left, right))
        else:
            low_edges.append((left, right))

    nx.draw_networkx_edges(graph, pos, edgelist=low_edges, ax=ax, edge_color="#d0d0d0", width=0.7, alpha=0.45)
    nx.draw_networkx_edges(graph, pos, edgelist=mid_edges, ax=ax, edge_color="#f6b44b", width=1.0, alpha=0.50)
    nx.draw_networkx_edges(graph, pos, edgelist=high_edges, ax=ax, edge_color="#d62728", width=1.6, alpha=0.70)
    nx.draw_networkx_nodes(graph, pos, ax=ax, node_size=20, node_color="#eeeeee", edgecolors="white", linewidths=0.3)


def draw_path_edges(
    ax: plt.Axes,
    graph: nx.Graph,
    edges: list[tuple[int, int]],
    pos: dict[int, np.ndarray],
    color: str,
    label: str,
    width: float,
    style: str = "solid",
) -> None:
    if not edges:
        return
    nx.draw_networkx_edges(
        graph,
        pos,
        ax=ax,
        edgelist=edges,
        edge_color=color,
        width=width,
        alpha=0.95,
        label=label,
        style=style,
    )


def draw_path(ax: plt.Axes, path: list[int], pos: dict[int, np.ndarray], color: str, label: str, width: float) -> None:
    edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(
        nx.Graph(edges),
        pos,
        ax=ax,
        edgelist=edges,
        edge_color=color,
        width=width,
        alpha=0.95,
        label=label,
    )
    nx.draw_networkx_nodes(nx.Graph(edges), pos, ax=ax, nodelist=path, node_size=34, node_color=color, alpha=0.85)


def draw_path_comparison(
    ax: plt.Axes,
    graph: nx.Graph,
    left_path: list[int],
    right_path: list[int],
    pos: dict[int, np.ndarray],
    left_color: str,
    right_color: str,
    left_label: str,
    right_label: str,
) -> None:
    left_edges = list(zip(left_path[:-1], left_path[1:]))
    right_edges = list(zip(right_path[:-1], right_path[1:]))
    left_set = edge_set(left_path)
    right_set = edge_set(right_path)
    shared = [edge for edge in left_edges if tuple(sorted(edge)) in (left_set & right_set)]
    left_unique = [edge for edge in left_edges if tuple(sorted(edge)) not in right_set]
    right_unique = [edge for edge in right_edges if tuple(sorted(edge)) not in left_set]

    draw_path_edges(ax, graph, shared, pos, "#555555", "Shared segment", 3.0)
    draw_path_edges(ax, graph, left_unique, pos, left_color, left_label, 4.2, "dashed")
    draw_path_edges(ax, graph, right_unique, pos, right_color, right_label, 4.2)
    nx.draw_networkx_nodes(graph, pos, ax=ax, nodelist=left_path, node_size=30, node_color=left_color, alpha=0.55)
    nx.draw_networkx_nodes(graph, pos, ax=ax, nodelist=right_path, node_size=38, node_color=right_color, alpha=0.75)


def annotate_od(ax: plt.Axes, pos: dict[int, np.ndarray], src: int, dst: int) -> None:
    ax.scatter([pos[src][0]], [pos[src][1]], s=150, c="#111111", marker="s", zorder=5)
    ax.scatter([pos[dst][0]], [pos[dst][1]], s=170, c="#111111", marker="X", zorder=5)
    ax.text(pos[src][0], pos[src][1], " S", fontsize=11, fontweight="bold", va="bottom")
    ax.text(pos[dst][0], pos[dst][1], " T", fontsize=11, fontweight="bold", va="bottom")


def metric_box(fig: plt.Figure, text: str) -> None:
    fig.text(
        0.5,
        0.02,
        text,
        ha="center",
        va="bottom",
        fontsize=9,
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "edgecolor": "#cccccc", "alpha": 0.92},
    )


def savefig(fig: plt.Figure, name: str) -> None:
    fig.savefig(FIG_DIR / f"{name}.png", dpi=300, bbox_inches="tight")
    fig.savefig(FIG_DIR / f"{name}.svg", bbox_inches="tight")
    plt.close(fig)


def create_figures(graph: nx.Graph, p75: float, p90: float, case: dict[str, object]) -> None:
    hop_path = case["hop_path"]
    cvar_path = case["cvar_path"]
    cvar_re_path = case["cvar_re_path"]
    assert isinstance(hop_path, list) and isinstance(cvar_path, list) and isinstance(cvar_re_path, list)

    sub = subgraph_for_paths(graph, [hop_path, cvar_path, cvar_re_path], p90)
    pos = nx.spring_layout(sub, seed=42, weight=None, iterations=200)
    src = int(case["src"])
    dst = int(case["dst"])

    fig13, ax13 = plt.subplots(figsize=(9.2, 7.2))
    draw_base(ax13, sub, pos, p75, p90)
    draw_path_comparison(
        ax13,
        sub,
        hop_path,
        cvar_path,
        pos,
        "#1f77b4",
        "#2ca02c",
        "Hop-shortest unique",
        "CVaR-risk unique",
    )
    annotate_od(ax13, pos, src, dst)
    ax13.set_title("Figure 13: Hop-shortest vs CVaR-risk on a Representative OD")
    ax13.legend(loc="upper right", frameon=True)
    ax13.axis("off")
    metric_box(
        fig13,
        (
            f"Selected OD {src}->{dst}. CVaR90 reduction={float(case['cvar90_reduction']):.1%}; "
            f"Hop increase={float(case['hop_increase']):.1%}; "
            f"MaxRisk {float(case['hop_max_risk']):.4f}->{float(case['cvar_max_risk']):.4f}. "
            "Layout is algorithmic and not geographic."
        ),
    )
    savefig(fig13, "fig13_od_hop_vs_cvar_path")

    fig14, ax14 = plt.subplots(figsize=(9.2, 7.2))
    draw_base(ax14, sub, pos, p75, p90)
    draw_path_comparison(
        ax14,
        sub,
        cvar_path,
        cvar_re_path,
        pos,
        "#1f77b4",
        "#9467bd",
        "CVaR-risk unique",
        "CVaR+Concentration unique",
    )
    annotate_od(ax14, pos, src, dst)
    ax14.set_title("Figure 14: CVaR-risk vs CVaR+Concentration")
    ax14.legend(loc="upper right", frameon=True)
    ax14.axis("off")
    metric_box(
        fig14,
        (
            f"Same OD {src}->{dst}. RE {float(case['cvar_re']):.5f}->"
            f"{float(case['cvar_concentration_re']):.5f}; "
            f"Concentration path overlap={float(case['cvar_concentration_overlap']):.1%}; "
            "red background edges are above global P90 risk."
        ),
    )
    savefig(fig14, "fig14_od_cvar_vs_concentration_path")


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update(
        {
            "font.size": 10,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
        }
    )

    graph, p75, p90, rows = evaluate_pairs()
    case = select_case(rows)
    create_figures(graph, p75, p90, case)

    write_csv(
        TABLE_DIR / "fig13_14_candidate_od_scores.csv",
        [
            {
                key: value
                for key, value in row.items()
                if not isinstance(value, list)
            }
            for row in rows
        ],
    )
    write_csv(TABLE_DIR / "fig13_14_selected_od_metrics.csv", case_rows(case))
    (TABLE_DIR / "fig13_14_selected_od_meta.json").write_text(
        json.dumps(
            {
                "risk_source": "Stable-Tail GNN",
                "risk_dir": str(RISK_DIR),
                "pair_file": str(PAIR_FILE),
                "year": YEAR,
                "k_paths": K_PATHS,
                "cvar_alpha": ALPHA,
                "lambda_re": LAMBDA_RE,
                "re_threshold": "p75",
                "p75_edge_risk": p75,
                "p90_edge_risk": p90,
                "selected_group": case["group"],
                "selected_src": case["src"],
                "selected_dst": case["dst"],
                "selection_rule": (
                    "Path differs from Hop-shortest, CVaR90 reduction and hop increase are close "
                    "to 150-OD averages, Hop-shortest contains high-risk edges, and CVaR+Concentration changes path when possible."
                ),
                "layout_note": (
                    "Node positions are generated by NetworkX spring_layout for regional association display only; "
                    "they are not true geographic coordinates."
                ),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote figures 13-14 to {FIG_DIR}")
    print(f"Selected OD: {case['src']} -> {case['dst']} ({case['group']})")


if __name__ == "__main__":
    main()
