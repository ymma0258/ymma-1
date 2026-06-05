"""Create representative VRP route and edge-burden figures."""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import validate_pyvrp_cvrp as vrp  # noqa: E402


ROOT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs")
OUT_DIR = ROOT / "final_figures_stable_tail_gnn"
FIG_DIR = OUT_DIR / "figures"
TABLE_DIR = OUT_DIR / "tables"
RISK_DIR = ROOT / "risk_matrices" / "gcn_teg_concat_splitB_seed0_epochs50_floor_0p01"
BETA_RUN_ROOT = ROOT / "pyvrp_cvrp" / "stable_tail_pyvrp50_beta_curve_fixedAB"
CONC_RUN_ROOT = ROOT / "pyvrp_cvrp" / "concat_concentration_pyvrp50_beta1_lambda0_1_fixedAB"
YEAR = "data_2021"


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


def run_dir(root: Path, customer_set: str) -> Path:
    return root.parent / f"{root.name}_{customer_set}_Stable-Tail-GNN"


def concentration_run_dir(customer_set: str) -> Path:
    return CONC_RUN_ROOT.parent / f"{CONC_RUN_ROOT.name}_{customer_set}_GCN+TEG-concat"


def load_meta(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def row_float(row: dict[str, str], key: str) -> float:
    return float(row[key])


def row_int(row: dict[str, str], key: str) -> int:
    return int(float(row[key]))


def edge_key(left: int, right: int) -> tuple[int, int]:
    return tuple(sorted((int(left), int(right))))


def route_edges(inst: vrp.CVRPInstance, routes: list[list[int]]) -> list[list[tuple[int, int]]]:
    expanded: list[list[tuple[int, int]]] = []
    for seq in routes:
        edges: list[tuple[int, int]] = []
        for left, right in zip(seq[:-1], seq[1:]):
            path = inst.hop_paths[(int(left), int(right))]
            edges.extend(edge_key(src, dst) for src, dst in zip(path[:-1], path[1:]))
        expanded.append(edges)
    return expanded


def route_nodes(inst: vrp.CVRPInstance, routes: list[list[int]]) -> set[int]:
    nodes: set[int] = set()
    for seq in routes:
        for left, right in zip(seq[:-1], seq[1:]):
            path = inst.hop_paths[(int(left), int(right))]
            nodes.update(int(node) for node in path)
    return nodes


def burden_counter(route_edge_lists: list[list[tuple[int, int]]]) -> Counter[tuple[int, int]]:
    counter: Counter[tuple[int, int]] = Counter()
    for edges in route_edge_lists:
        counter.update(edges)
    return counter


def edge_risk(graph: nx.Graph, edge: tuple[int, int]) -> float:
    return float(graph[edge[0]][edge[1]]["risk"])


def total_burden(graph: nx.Graph, counter: Counter[tuple[int, int]]) -> dict[tuple[int, int], float]:
    return {edge: count * edge_risk(graph, edge) for edge, count in counter.items()}


def load_instance(customer_set: str) -> tuple[nx.Graph, vrp.CVRPInstance, dict[str, object]]:
    meta = load_meta(run_dir(BETA_RUN_ROOT, customer_set) / "pyvrp_cvrp_meta.json")
    graph, scores_norm, _ = vrp.load_graph(RISK_DIR, YEAR)
    graph = vrp.largest_component(graph)
    inst = vrp.build_instance(
        graph,
        scores_norm,
        num_customers=int(meta["num_customers"]),
        num_vehicles=int(meta["num_vehicles"]),
        capacity=int(meta["capacity"]),
        customer_set=customer_set,
        sample_seed=0,
        fixed_depot=int(meta["depot"]),
        fixed_customers=[int(node) for node in meta["customers"]],
        concentration_threshold="p75",
    )
    return graph, inst, meta


def detail_rows(customer_set: str) -> list[dict[str, str]]:
    return read_csv(run_dir(BETA_RUN_ROOT, customer_set) / "pyvrp_cvrp_detail.csv")


def concentration_rows(customer_set: str) -> list[dict[str, str]]:
    return read_csv(concentration_run_dir(customer_set) / "pyvrp_cvrp_detail.csv")


def pair_rows_by_seed(rows: list[dict[str, str]], beta_left: float, beta_right: float) -> list[dict[str, object]]:
    grouped: dict[int, dict[float, dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row_int(row, "seed"), {})[row_float(row, "beta")] = row

    pairs = []
    for seed, by_beta in grouped.items():
        if beta_left not in by_beta or beta_right not in by_beta:
            continue
        left = by_beta[beta_left]
        right = by_beta[beta_right]
        pairs.append(
            {
                "seed": seed,
                "left": left,
                "right": right,
                "cost_increase": (row_float(right, "pyvrp_cost") - row_float(left, "pyvrp_cost"))
                / (row_float(left, "pyvrp_cost") + vrp.EPS),
                "risk_reduction": (row_float(left, "global_risk") - row_float(right, "global_risk"))
                / (row_float(left, "global_risk") + vrp.EPS),
                "edge_gini_reduction": (
                    row_float(left, "edge_burden_gini_used") - row_float(right, "edge_burden_gini_used")
                )
                / (row_float(left, "edge_burden_gini_used") + vrp.EPS),
            }
        )
    return pairs


def pair_concentration_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[int, dict[float, dict[str, str]]] = {}
    for row in rows:
        if abs(row_float(row, "beta") - 1.0) > 1e-9:
            continue
        grouped.setdefault(row_int(row, "seed"), {})[row_float(row, "lambda_concentration")] = row

    pairs = []
    for seed, by_lambda in grouped.items():
        if 0.0 not in by_lambda or 1.0 not in by_lambda:
            continue
        left = by_lambda[0.0]
        right = by_lambda[1.0]
        pairs.append(
            {
                "seed": seed,
                "left": left,
                "right": right,
                "risk_reduction": (row_float(left, "global_risk") - row_float(right, "global_risk"))
                / (row_float(left, "global_risk") + vrp.EPS),
                "edge_gini_reduction": (
                    row_float(left, "edge_burden_gini_used") - row_float(right, "edge_burden_gini_used")
                )
                / (row_float(left, "edge_burden_gini_used") + vrp.EPS),
                "top10_reduction": (row_float(left, "top10_burden_share") - row_float(right, "top10_burden_share"))
                / (row_float(left, "top10_burden_share") + vrp.EPS),
            }
        )
    return pairs


def route_overlap(inst: vrp.CVRPInstance, left: dict[str, str], right: dict[str, str]) -> float:
    left_edges = set().union(*route_edges(inst, json.loads(left["routes"])))
    right_edges = set().union(*route_edges(inst, json.loads(right["routes"])))
    union = left_edges | right_edges
    return len(left_edges & right_edges) / len(union) if union else 1.0


def select_beta_case() -> dict[str, object]:
    candidates: list[dict[str, object]] = []
    for customer_set in ["A", "B"]:
        graph, inst, _ = load_instance(customer_set)
        del graph
        pairs = pair_rows_by_seed(detail_rows(customer_set), 0.0, 1.0)
        mean_cost = float(np.mean([pair["cost_increase"] for pair in pairs]))
        mean_risk = float(np.mean([pair["risk_reduction"] for pair in pairs]))
        mean_gini = float(np.mean([pair["edge_gini_reduction"] for pair in pairs]))
        for pair in pairs:
            overlap = route_overlap(inst, pair["left"], pair["right"])
            pair.update(
                {
                    "customer_set": customer_set,
                    "route_overlap": overlap,
                    "mean_cost_increase": mean_cost,
                    "mean_risk_reduction": mean_risk,
                    "mean_edge_gini_reduction": mean_gini,
                }
            )
            candidates.append(pair)

    def score(pair: dict[str, object]) -> float:
        overlap_penalty = 0.0 if float(pair["route_overlap"]) < 0.95 else 1.0
        gini_bonus = -0.5 if float(pair["edge_gini_reduction"]) > 0 else 0.0
        return (
            abs(float(pair["cost_increase"]) - float(pair["mean_cost_increase"]))
            + abs(float(pair["risk_reduction"]) - float(pair["mean_risk_reduction"]))
            + abs(float(pair["edge_gini_reduction"]) - float(pair["mean_edge_gini_reduction"]))
            + overlap_penalty
            + gini_bonus
        )

    case = min(candidates, key=score)
    case["selection_score"] = score(case)
    return case


def select_concentration_case(preferred_set: str | None = None) -> dict[str, object]:
    candidates: list[dict[str, object]] = []
    for customer_set in ["A", "B"]:
        graph, inst, _ = load_instance(customer_set)
        del graph
        pairs = pair_concentration_rows(concentration_rows(customer_set))
        mean_risk = float(np.mean([pair["risk_reduction"] for pair in pairs]))
        mean_gini = float(np.mean([pair["edge_gini_reduction"] for pair in pairs]))
        mean_top10 = float(np.mean([pair["top10_reduction"] for pair in pairs]))
        for pair in pairs:
            overlap = route_overlap(inst, pair["left"], pair["right"])
            pair.update(
                {
                    "customer_set": customer_set,
                    "route_overlap": overlap,
                    "mean_risk_reduction": mean_risk,
                    "mean_edge_gini_reduction": mean_gini,
                    "mean_top10_reduction": mean_top10,
                }
            )
            candidates.append(pair)

    def score(pair: dict[str, object]) -> float:
        set_penalty = 0.0 if preferred_set is None or pair["customer_set"] == preferred_set else 0.25
        overlap_penalty = 0.0 if float(pair["route_overlap"]) < 0.95 else 0.5
        return (
            abs(float(pair["risk_reduction"]) - float(pair["mean_risk_reduction"]))
            + abs(float(pair["edge_gini_reduction"]) - float(pair["mean_edge_gini_reduction"]))
            + abs(float(pair["top10_reduction"]) - float(pair["mean_top10_reduction"]))
            + set_penalty
            + overlap_penalty
        )

    case = min(candidates, key=score)
    case["selection_score"] = score(case)
    return case


def subgraph_for_routes(graph: nx.Graph, edge_lists: list[list[tuple[int, int]]], depot: int, customers: list[int]) -> nx.Graph:
    used_edges = set().union(*(set(edges) for edges in edge_lists))
    used_nodes = {node for edge in used_edges for node in edge}
    used_nodes.add(depot)
    used_nodes.update(customers)
    nodes = set(used_nodes)
    for node in sorted(used_nodes):
        if node not in graph:
            continue
        neighbors = sorted(graph.neighbors(node), key=lambda nbr: graph[node][nbr]["risk"], reverse=True)
        nodes.update(neighbors[:3])
    if len(nodes) > 260:
        path_nodes = set(used_nodes)
        ranked = sorted(
            nodes - path_nodes,
            key=lambda node: max((graph[node][nbr]["risk"] for nbr in graph.neighbors(node)), default=0.0),
            reverse=True,
        )
        nodes = path_nodes | set(ranked[: 260 - len(path_nodes)])
    sub = graph.subgraph(nodes).copy()
    for left, right in used_edges:
        if graph.has_edge(left, right):
            sub.add_edge(left, right, **graph[left][right])
    return sub


def subgraph_for_difference(
    graph: nx.Graph,
    left_edges: list[list[tuple[int, int]]],
    right_edges: list[list[tuple[int, int]]],
    depot: int,
    customers: list[int],
) -> nx.Graph:
    left_set = set().union(*(set(edges) for edges in left_edges))
    right_set = set().union(*(set(edges) for edges in right_edges))
    changed_edges = left_set ^ right_set
    shared_edges = left_set & right_set
    focus_edges = changed_edges | {
        edge for edge in shared_edges if edge_risk(graph, edge) >= risk_quantile(graph, 0.90)
    }
    focus_nodes = {node for edge in focus_edges for node in edge}
    focus_nodes.add(depot)
    focus_nodes.update(node for node in customers if node in focus_nodes)
    nodes = set(focus_nodes)
    for node in sorted(focus_nodes):
        if node not in graph:
            continue
        neighbors = sorted(graph.neighbors(node), key=lambda nbr: graph[node][nbr]["risk"], reverse=True)
        nodes.update(neighbors[:2])
    return graph.subgraph(nodes).copy()


def subgraph_for_burden(
    graph: nx.Graph,
    left_edges: list[list[tuple[int, int]]],
    right_edges: list[list[tuple[int, int]]],
    depot: int,
    customers: list[int],
    top_n: int = 20,
) -> nx.Graph:
    left_burden = total_burden(graph, burden_counter(left_edges))
    right_burden = total_burden(graph, burden_counter(right_edges))
    top_edges = set(top_burden_edges(left_burden, top_n)) | set(top_burden_edges(right_burden, top_n))
    nodes = {node for edge in top_edges for node in edge}
    nodes.add(depot)
    nodes.update(node for node in customers if node in nodes)
    for node in sorted(list(nodes)):
        if node not in graph:
            continue
        neighbors = sorted(graph.neighbors(node), key=lambda nbr: graph[node][nbr]["risk"], reverse=True)
        nodes.update(neighbors[:2])
    return graph.subgraph(nodes).copy()


def risk_quantile(graph: nx.Graph, quantile: float) -> float:
    risks = np.asarray([float(data["risk"]) for _, _, data in graph.edges(data=True)], dtype=float)
    return float(np.quantile(risks, quantile))


def visible_edges(graph: nx.Graph, edges: list[tuple[int, int]] | set[tuple[int, int]]) -> list[tuple[int, int]]:
    return [edge for edge in edges if graph.has_edge(edge[0], edge[1])]


def draw_background_high_risk(ax: plt.Axes, graph: nx.Graph, pos: dict[int, np.ndarray], p90: float) -> None:
    high = []
    for left, right, data in graph.edges(data=True):
        risk = float(data["risk"])
        if risk >= p90:
            high.append((left, right))
    nx.draw_networkx_edges(graph, pos, edgelist=list(graph.edges), ax=ax, edge_color="#dddddd", width=0.35, alpha=0.16)
    nx.draw_networkx_edges(graph, pos, edgelist=high, ax=ax, edge_color="#f05a5a", width=1.35, alpha=0.45)


def draw_customers(ax: plt.Axes, graph: nx.Graph, pos: dict[int, np.ndarray], depot: int, customers: list[int]) -> None:
    visible_customers = [node for node in customers if node in graph and node in pos]
    nx.draw_networkx_nodes(graph, pos, nodelist=list(graph.nodes), ax=ax, node_size=8, node_color="#eeeeee", alpha=0.80)
    nx.draw_networkx_nodes(graph, pos, nodelist=visible_customers, ax=ax, node_size=34, node_color="#ffffff", edgecolors="#555555", linewidths=0.6)
    nx.draw_networkx_nodes(graph, pos, nodelist=[depot], ax=ax, node_size=120, node_color="#111111", node_shape="s")
    ax.text(pos[depot][0], pos[depot][1], " Depot", fontsize=9, fontweight="bold", va="bottom")


def draw_route_difference_panel(
    ax: plt.Axes,
    graph: nx.Graph,
    pos: dict[int, np.ndarray],
    depot: int,
    customers: list[int],
    left_edge_lists: list[list[tuple[int, int]]],
    right_edge_lists: list[list[tuple[int, int]]],
    p90: float,
) -> None:
    left_set = set().union(*(set(edges) for edges in left_edge_lists))
    right_set = set().union(*(set(edges) for edges in right_edge_lists))
    shared = visible_edges(graph, sorted(left_set & right_set))
    left_only = visible_edges(graph, sorted(left_set - right_set))
    right_only = visible_edges(graph, sorted(right_set - left_set))

    draw_background_high_risk(ax, graph, pos, p90)
    nx.draw_networkx_edges(graph, pos, edgelist=shared, ax=ax, edge_color="#777777", width=1.8, alpha=0.60, label="Shared")
    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist=left_only,
        ax=ax,
        edge_color="#d62728",
        width=2.9,
        alpha=0.92,
        label="Cost-only unique",
    )
    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist=right_only,
        ax=ax,
        edge_color="#2ca02c",
        width=2.9,
        alpha=0.92,
        label="Risk-aware unique",
    )
    draw_customers(ax, graph, pos, depot, customers)
    ax.set_title("Changed regional edges between beta=0 and beta=1")
    ax.legend(loc="upper right", frameon=True)
    ax.axis("off")


def top_burden_edges(burden: dict[tuple[int, int], float], top_n: int) -> list[tuple[int, int]]:
    return [edge for edge, _ in sorted(burden.items(), key=lambda item: item[1], reverse=True)[:top_n]]


def draw_top_burden_panel(
    ax: plt.Axes,
    graph: nx.Graph,
    pos: dict[int, np.ndarray],
    depot: int,
    customers: list[int],
    route_edge_lists: list[list[tuple[int, int]]],
    title: str,
) -> None:
    counter = burden_counter(route_edge_lists)
    counter = Counter(
        {edge: count for edge, count in counter.items() if graph.has_edge(edge[0], edge[1])}
    )
    burden = total_burden(graph, counter)
    top_edges = top_burden_edges(burden, 20)
    values = np.asarray([burden[edge] for edge in top_edges], dtype=float)
    min_val = float(values.min()) if values.size else 0.0
    max_val = float(values.max()) if values.size else 1.0

    nx.draw_networkx_edges(graph, pos, edgelist=list(graph.edges), ax=ax, edge_color="#dddddd", width=0.45, alpha=0.18)
    for edge in top_edges:
        value = burden[edge]
        scale = (value - min_val) / (max_val - min_val + vrp.EPS)
        color = plt.get_cmap("YlOrRd")(0.35 + 0.60 * scale)
        width = 2.4 + 6.0 * scale
        nx.draw_networkx_edges(graph, pos, edgelist=[edge], ax=ax, edge_color=[color], width=width, alpha=0.92)
    draw_customers(ax, graph, pos, depot, customers)
    ax.set_title(title)
    ax.axis("off")


def savefig(fig: plt.Figure, name: str) -> None:
    fig.savefig(FIG_DIR / f"{name}.png", dpi=300, bbox_inches="tight")
    fig.savefig(FIG_DIR / f"{name}.svg", bbox_inches="tight")
    plt.close(fig)


def case_routes(case: dict[str, object], graph: nx.Graph, inst: vrp.CVRPInstance, left_label: str, right_label: str):
    left_routes = json.loads(case["left"]["routes"])
    right_routes = json.loads(case["right"]["routes"])
    left_edges = route_edges(inst, left_routes)
    right_edges = route_edges(inst, right_routes)
    all_edges = left_edges + right_edges
    sub = subgraph_for_routes(graph, all_edges, inst.depot, inst.customers)
    pos = nx.spring_layout(sub, seed=13, weight=None, iterations=220)
    risks = np.asarray([data["risk"] for _, _, data in graph.edges(data=True)], dtype=float)
    p75 = float(np.quantile(risks, 0.75))
    p90 = float(np.quantile(risks, 0.90))
    return left_edges, right_edges, sub, pos, p75, p90, left_label, right_label


def create_route_comparison(case: dict[str, object]) -> None:
    graph, inst, _ = load_instance(str(case["customer_set"]))
    left_edges, right_edges, _, _, _, p90, _, _ = case_routes(
        case, graph, inst, "Cost-only", "Risk-aware"
    )
    sub = subgraph_for_difference(graph, left_edges, right_edges, inst.depot, inst.customers)
    pos = nx.spring_layout(sub, seed=15, weight=None, iterations=220)
    fig, ax = plt.subplots(figsize=(10.5, 7.6))
    draw_route_difference_panel(
        ax,
        sub,
        pos,
        inst.depot,
        inst.customers,
        left_edges,
        right_edges,
        p90,
    )
    fig.suptitle("Figure 15: How risk-aware CVRP reroutes around high-risk edges", fontweight="bold")
    fig.text(
        0.5,
        0.02,
        (
            f"Set {case['customer_set']}, seed={case['seed']}. "
            f"Cost increase={float(case['cost_increase']):.1%}; "
            f"Global risk reduction={float(case['risk_reduction']):.1%}; "
            f"Edge burden Gini reduction={float(case['edge_gini_reduction']):.1%}. "
            "Node positions use an algorithmic layout and are not geographic."
        ),
        ha="center",
        fontsize=9,
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "edgecolor": "#cccccc", "alpha": 0.92},
    )
    savefig(fig, "fig15_vrp_cost_only_vs_risk_aware")


def create_burden_comparison(case: dict[str, object]) -> None:
    graph, inst, _ = load_instance(str(case["customer_set"]))
    left_edges, right_edges, _, _, _, _, _, _ = case_routes(
        case, graph, inst, "Risk-aware", "Concentration-aware"
    )
    sub = subgraph_for_routes(graph, left_edges + right_edges, inst.depot, inst.customers)
    pos = nx.spring_layout(sub, seed=16, weight=None, k=0.10, iterations=500, scale=1.0)
    fig, axes = plt.subplots(1, 2, figsize=(15, 7.2))
    draw_top_burden_panel(
        axes[0],
        sub,
        pos,
        inst.depot,
        inst.customers,
        left_edges,
        "(a) Risk-aware VRP, beta=1, lambda=0",
    )
    draw_top_burden_panel(
        axes[1],
        sub,
        pos,
        inst.depot,
        inst.customers,
        right_edges,
        "(b) Concentration-aware VRP, beta=1, lambda=1",
    )
    fig.suptitle("Figure 16: Top edge-burden redistribution under concentration-aware VRP", fontweight="bold")
    fig.text(
        0.5,
        0.02,
        (
            f"Set {case['customer_set']}, seed={case['seed']}. "
            f"Global risk reduction={float(case['risk_reduction']):.1%}; "
            f"Edge burden Gini reduction={float(case['edge_gini_reduction']):.1%}; "
            f"Top10 burden share reduction={float(case['top10_reduction']):.1%}. "
            "Edge width/color encode burden = usage x risk."
        ),
        ha="center",
        fontsize=9,
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "edgecolor": "#cccccc", "alpha": 0.92},
    )
    savefig(fig, "fig16_vrp_edge_burden_redistribution")


def abstract_customer_positions(inst: vrp.CVRPInstance, graph: nx.Graph) -> dict[int, np.ndarray]:
    nodes = [inst.depot] + inst.customers
    complete = nx.Graph()
    complete.add_nodes_from(range(len(nodes)))
    for i, src in enumerate(nodes):
        for j, dst in enumerate(nodes):
            if i < j:
                path = inst.hop_paths[(i, j)]
                complete.add_edge(i, j, weight=max(1, len(path) - 1))

    layout = nx.kamada_kawai_layout(complete, weight="weight", scale=1.0)
    return {idx: np.asarray(layout[idx], dtype=float) for idx in complete.nodes}


def draw_abstract_routes(
    ax: plt.Axes,
    inst: vrp.CVRPInstance,
    routes: list[list[int]],
    pos: dict[int, np.ndarray],
    title: str,
    customer_risks: np.ndarray,
    show_labels: bool = True,
) -> None:
    vehicle_colors = ["#1f77b4", "#2ca02c", "#ff7f0e", "#9467bd", "#d62728"]
    customer_indices = list(range(1, len(inst.customers) + 1))
    risk_values = customer_risks[np.asarray(inst.customers, dtype=int)]
    low_thr, high_thr = np.quantile(risk_values, [0.50, 0.80])
    node_colors = []
    for value in risk_values:
        if value >= high_thr:
            node_colors.append("#d73027")
        elif value >= low_thr:
            node_colors.append("#fdae61")
        else:
            node_colors.append("#fee08b")

    for route_idx, seq in enumerate(routes):
        color = vehicle_colors[route_idx % len(vehicle_colors)]
        coords = []
        for seq_pos, node in enumerate(seq):
            point = pos[int(node)].copy()
            if int(node) == 0 and len(seq) > 2:
                neighbor = pos[int(seq[1] if seq_pos == 0 else seq[-2])]
                direction = neighbor - point
                norm = np.linalg.norm(direction)
                if norm > 1e-12:
                    direction = direction / norm
                    tangent = np.asarray([-direction[1], direction[0]])
                    point = point + tangent * (route_idx - 2) * 0.018
            coords.append(point)
        coords = np.asarray(coords, dtype=float)
        ax.plot(
            coords[:, 0],
            coords[:, 1],
            color=color,
            lw=2.2,
            alpha=0.82,
            solid_capstyle="round",
            solid_joinstyle="round",
            zorder=2,
            label=f"Vehicle {route_idx + 1}",
        )
        segment_indices = np.linspace(0, len(seq) - 2, num=min(3, len(seq) - 1), dtype=int)
        for seg_idx in sorted(set(int(idx) for idx in segment_indices)):
            left_pos = coords[seg_idx]
            right_pos = coords[seg_idx + 1]
            start = left_pos + 0.55 * (right_pos - left_pos)
            end = left_pos + 0.70 * (right_pos - left_pos)
            ax.annotate(
                "",
                xy=(end[0], end[1]),
                xytext=(start[0], start[1]),
                arrowprops={
                    "arrowstyle": "-|>",
                    "color": color,
                    "lw": 1.4,
                    "alpha": 0.95,
                    "mutation_scale": 10,
                },
                zorder=3,
            )

    ax.scatter(
        [pos[idx][0] for idx in customer_indices],
        [pos[idx][1] for idx in customer_indices],
        s=54,
        c=node_colors,
        edgecolors="#7f4f00",
        linewidths=0.7,
        zorder=4,
    )
    ax.scatter([pos[0][0]], [pos[0][1]], s=190, c="#111111", marker="s", zorder=5)
    ax.text(pos[0][0], pos[0][1], " Depot", fontsize=10, fontweight="bold", va="bottom", zorder=6)

    if show_labels:
        for idx in customer_indices:
            if idx in {1, 10, 20, 30, 40, 50}:
                ax.text(pos[idx][0], pos[idx][1], str(idx), fontsize=7, ha="center", va="center", zorder=7)

    ax.set_title(title)
    ax.axis("off")
    ax.legend(loc="upper right", frameon=True, fontsize=8)


def create_abstract_vrp_comparison(case: dict[str, object]) -> None:
    graph, inst, _ = load_instance(str(case["customer_set"]))
    _, scores_norm, _ = vrp.load_graph(RISK_DIR, YEAR)
    pos = abstract_customer_positions(inst, graph)
    cost_routes = json.loads(case["left"]["routes"])
    risk_routes = json.loads(case["right"]["routes"])

    fig, axes = plt.subplots(1, 2, figsize=(15, 7.2))
    draw_abstract_routes(axes[0], inst, cost_routes, pos, "(a) Cost-only CVRP, beta=0", scores_norm)
    draw_abstract_routes(axes[1], inst, risk_routes, pos, "(b) Risk-aware CVRP, beta=1", scores_norm)
    fig.suptitle("Figure 17: Cost-only and risk-aware CVRP route solutions", fontweight="bold")
    fig.text(
        0.5,
        0.02,
        (
            f"Set {case['customer_set']}, seed={case['seed']}. "
            f"Cost increase={float(case['cost_increase']):.1%}; "
            f"Global risk reduction={float(case['risk_reduction']):.1%}; "
            f"Edge burden Gini reduction={float(case['edge_gini_reduction']):.1%}. "
            "This abstract customer-level layout shows closed CVRP tours and does not show intermediate regional nodes."
        ),
        ha="center",
        fontsize=9,
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "edgecolor": "#cccccc", "alpha": 0.92},
    )
    savefig(fig, "fig17_abstract_cvrp_route_solutions")


def write_case_tables(beta_case: dict[str, object], conc_case: dict[str, object]) -> None:
    def compact(row: dict[str, str], label: str) -> dict[str, object]:
        return {
            "label": label,
            "beta": row["beta"],
            "lambda_concentration": row["lambda_concentration"],
            "seed": row["seed"],
            "pyvrp_cost": row["pyvrp_cost"],
            "global_risk": row["global_risk"],
            "global_cvar90": row["global_cvar90"],
            "max_vehicle_risk": row["max_vehicle_risk"],
            "edge_burden_gini_used": row["edge_burden_gini_used"],
            "top10_burden_share": row["top10_burden_share"],
            "routes": row["routes"],
        }

    write_csv(
        TABLE_DIR / "fig15_vrp_cost_risk_selected_case.csv",
        [
            compact(beta_case["left"], "cost_only_beta0"),
            compact(beta_case["right"], "risk_aware_beta1"),
            {
                "label": "selection_metrics",
                "customer_set": beta_case["customer_set"],
                "seed": beta_case["seed"],
                "cost_increase": beta_case["cost_increase"],
                "risk_reduction": beta_case["risk_reduction"],
                "edge_gini_reduction": beta_case["edge_gini_reduction"],
                "route_overlap": beta_case["route_overlap"],
                "selection_score": beta_case["selection_score"],
            },
        ],
    )
    write_csv(
        TABLE_DIR / "fig17_abstract_cvrp_selected_case.csv",
        [
            compact(beta_case["left"], "cost_only_beta0"),
            compact(beta_case["right"], "risk_aware_beta1"),
            {
                "label": "figure17_metrics",
                "figure": "fig17_abstract_cvrp_route_solutions",
                "customer_set": beta_case["customer_set"],
                "seed": beta_case["seed"],
                "comparison": "customer-level closed tours for beta=0 vs beta=1",
                "cost_increase": beta_case["cost_increase"],
                "risk_reduction": beta_case["risk_reduction"],
                "edge_gini_reduction": beta_case["edge_gini_reduction"],
                "route_overlap": beta_case["route_overlap"],
                "note": "Abstract CVRP tour figure; intermediate regional nodes are omitted.",
            },
        ],
    )
    write_csv(
        TABLE_DIR / "fig16_vrp_burden_selected_case.csv",
        [
            compact(conc_case["left"], "risk_aware_lambda0"),
            compact(conc_case["right"], "concentration_aware_lambda1"),
            {
                "label": "selection_metrics",
                "customer_set": conc_case["customer_set"],
                "seed": conc_case["seed"],
                "risk_reduction": conc_case["risk_reduction"],
                "edge_gini_reduction": conc_case["edge_gini_reduction"],
                "top10_reduction": conc_case["top10_reduction"],
                "route_overlap": conc_case["route_overlap"],
                "selection_score": conc_case["selection_score"],
            },
        ],
    )
    (TABLE_DIR / "fig15_16_vrp_figure_meta.json").write_text(
        json.dumps(
            {
                "risk_source": "Stable-Tail GNN",
                "risk_dir": str(RISK_DIR),
                "route_figure": {
                    "figure": "fig15_vrp_cost_only_vs_risk_aware",
                    "comparison": "beta=0 vs beta=1",
                    "customer_set": beta_case["customer_set"],
                    "seed": beta_case["seed"],
                    "selection_rule": (
                        "Choose a seed/customer set whose beta=1 risk reduction, cost increase, "
                        "and edge-burden Gini change are close to their five-seed averages, with visible route differences."
                    ),
                },
                "burden_figure": {
                    "figure": "fig16_vrp_edge_burden_redistribution",
                    "comparison": "lambda=0 vs lambda=1 at beta=1",
                    "customer_set": conc_case["customer_set"],
                    "seed": conc_case["seed"],
                    "selection_rule": (
                        "Choose a seed/customer set whose lambda=1 edge-burden Gini, Top10 share, "
                        "and global-risk changes are close to their five-seed averages, with visible route differences."
                    ),
                },
                "abstract_route_figure": {
                    "figure": "fig17_abstract_cvrp_route_solutions",
                    "comparison": "customer-level closed tours for beta=0 vs beta=1",
                    "customer_set": beta_case["customer_set"],
                    "seed": beta_case["seed"],
                    "note": (
                        "This figure shows only depot-customer-customer-depot closed CVRP tours. "
                        "Intermediate regional graph nodes and edges are intentionally omitted."
                    ),
                },
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
    beta_case = select_beta_case()
    conc_case = select_concentration_case(preferred_set=str(beta_case["customer_set"]))
    create_route_comparison(beta_case)
    create_burden_comparison(conc_case)
    create_abstract_vrp_comparison(beta_case)
    write_case_tables(beta_case, conc_case)
    print(f"Wrote VRP figures 15-17 to {FIG_DIR}")
    print(
        "Selected route case: set={set_name}, seed={seed}; burden case: set={bset}, seed={bseed}".format(
            set_name=beta_case["customer_set"],
            seed=beta_case["seed"],
            bset=conc_case["customer_set"],
            bseed=conc_case["seed"],
        )
    )


if __name__ == "__main__":
    main()
