"""Validate risk-aware CVRP instances with PyVRP.

This implements stage 6 of the experiment plan. It constructs a synthetic CVRP
from regional risk graph nodes, solves it with PyVRP, expands the resulting
customer routes back to regional graph paths, and computes posterior risk and
fairness metrics.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import time
from dataclasses import dataclass
from pathlib import Path

import networkx as nx
import numpy as np
from pyvrp import Model
from pyvrp.stop import MaxRuntime


DEFAULT_RISK_DIR = Path(
    r"D:\PyVRP-main\hazmat_risk_experiments\outputs\risk_matrices\teg_gnn_splitB_seed0_epochs20"
)
DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\pyvrp_cvrp")
EPS = 1e-12


@dataclass
class CVRPInstance:
    depot: int
    customers: list[int]
    demands: list[int]
    capacity: int
    num_vehicles: int
    d_norm: np.ndarray
    q_norm: np.ndarray
    q_tail_norm: np.ndarray
    f_norm: np.ndarray
    hop_paths: dict[tuple[int, int], list[int]]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--risk-dir", type=Path, default=DEFAULT_RISK_DIR)
    parser.add_argument("--year", default="data_2021", choices=["data_2020", "data_2021"])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--num-customers", type=int, default=20)
    parser.add_argument("--num-vehicles", type=int, default=4)
    parser.add_argument("--capacity", type=int, default=5)
    parser.add_argument("--customer-set", choices=["A", "B"], default="A")
    parser.add_argument("--betas", default="0,0.5")
    parser.add_argument("--lambda-concentration", default="0")
    parser.add_argument(
        "--tail-risk-eta",
        type=float,
        default=0.0,
        help=(
            "Blend path risk sum and path CVaR90 in the CVRP objective: "
            "Q_tail=(1-eta)Q_sum+eta*Q_CVaR90. Default 0 keeps the original Q_sum."
        ),
    )
    parser.add_argument("--concentration-threshold", choices=["mean", "p75", "p90"], default="p75")
    parser.add_argument("--seeds", default="0")
    parser.add_argument("--max-runtime", type=float, default=10.0)
    parser.add_argument("--scale", type=int, default=10000)
    parser.add_argument("--sample-seed", type=int, default=0)
    parser.add_argument(
        "--fixed-instance-meta",
        type=Path,
        default=None,
        help="Optional PyVRP meta JSON whose depot/customers are reused.",
    )
    parser.add_argument("--batch-name", default="pyvrp_cvrp_smoke")
    return parser.parse_args()


def parse_float_csv(value: str) -> list[float]:
    return [float(item.strip()) for item in value.split(",") if item.strip()]


def parse_int_csv(value: str) -> list[int]:
    return [int(item.strip()) for item in value.split(",") if item.strip()]


def gini(values: np.ndarray) -> float:
    values = np.asarray(values, dtype=float)
    if values.size == 0 or values.sum() <= EPS:
        return 0.0
    sorted_values = np.sort(values)
    n = values.size
    idx = np.arange(1, n + 1)
    return float((2 * np.sum(idx * sorted_values) / (n * values.sum())) - ((n + 1) / n))


def cvar(values: np.ndarray, alpha: float = 0.90) -> float:
    values = np.asarray(values, dtype=float)
    if values.size == 0:
        return 0.0
    threshold = float(np.quantile(values, alpha, method="higher"))
    tail = values[values >= threshold]
    return float(tail.mean()) if tail.size else threshold


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
    return graph, node_data["scores_norm"], node_data["labels"]


def largest_component(graph: nx.Graph) -> nx.Graph:
    nodes = max(nx.connected_components(graph), key=len)
    return graph.subgraph(nodes).copy()


def node_exposure(graph: nx.Graph) -> dict[int, float]:
    return {
        int(node): float(sum(data["exposure"] for _, _, data in graph.edges(node, data=True)))
        for node in graph.nodes
    }


def choose_depot(graph: nx.Graph) -> int:
    exposures = node_exposure(graph)
    return max(exposures, key=exposures.get)


def choose_customers(
    graph: nx.Graph,
    scores_norm: np.ndarray,
    num_customers: int,
    depot: int,
    customer_set: str,
    seed: int,
) -> list[int]:
    rng = random.Random(seed)
    nodes = [int(node) for node in graph.nodes if int(node) != depot]
    exposures = node_exposure(graph)

    top_risk_threshold = float(np.quantile(scores_norm[nodes], 0.80))
    exposure_vals = np.asarray([exposures[node] for node in nodes], dtype=float)
    top_exp_threshold = float(np.quantile(exposure_vals, 0.80))

    high_risk = [node for node in nodes if scores_norm[node] >= top_risk_threshold]
    high_exposure = [node for node in nodes if exposures[node] >= top_exp_threshold]
    ordinary = [
        node
        for node in nodes
        if scores_norm[node] < top_risk_threshold and exposures[node] < top_exp_threshold
    ]

    if customer_set == "A":
        counts = [round(num_customers * 0.5), round(num_customers * 0.3)]
    else:
        counts = [round(num_customers * 0.3), round(num_customers * 0.3)]
    counts.append(num_customers - sum(counts))

    selected: list[int] = []
    for pool, count in zip([high_risk, high_exposure, ordinary], counts):
        candidates = [node for node in pool if node not in selected]
        if len(candidates) < count:
            count = len(candidates)
        selected.extend(rng.sample(candidates, count))

    while len(selected) < num_customers:
        candidates = [node for node in nodes if node not in selected]
        selected.append(rng.choice(candidates))

    return selected[:num_customers]


def path_risk(graph: nx.Graph, path: list[int]) -> float:
    return float(sum(graph[left][right]["risk"] for left, right in zip(path[:-1], path[1:])))


def path_cvar90(graph: nx.Graph, path: list[int]) -> float:
    risks = [float(graph[left][right]["risk"]) for left, right in zip(path[:-1], path[1:])]
    return cvar(np.asarray(risks, dtype=float), 0.90)


def path_concentration(graph: nx.Graph, path: list[int], threshold: float) -> float:
    return float(
        sum(
            max(float(graph[left][right]["risk"]) - threshold, 0.0)
            for left, right in zip(path[:-1], path[1:])
        )
    )


def concentration_threshold_value(graph: nx.Graph, threshold: str) -> float:
    risks = np.asarray([float(data["risk"]) for _, _, data in graph.edges(data=True)], dtype=float)
    if risks.size == 0:
        return 0.0
    if threshold == "mean":
        return float(risks.mean())
    if threshold == "p90":
        return float(np.quantile(risks, 0.90))
    return float(np.quantile(risks, 0.75))


def normalize_matrix(matrix: np.ndarray) -> np.ndarray:
    mask = ~np.eye(matrix.shape[0], dtype=bool)
    values = matrix[mask]
    return (matrix - values.min()) / (values.max() - values.min() + EPS)


def build_instance(
    graph: nx.Graph,
    scores_norm: np.ndarray,
    num_customers: int,
    num_vehicles: int,
    capacity: int,
    customer_set: str,
    sample_seed: int,
    fixed_depot: int | None = None,
    fixed_customers: list[int] | None = None,
    concentration_threshold: str = "p75",
    tail_risk_eta: float = 0.0,
) -> CVRPInstance:
    if fixed_depot is not None and fixed_customers is not None:
        depot = fixed_depot
        customers = fixed_customers[:num_customers]
        missing = [node for node in [depot] + customers if node not in graph]
        if missing:
            raise ValueError(f"Fixed instance nodes missing from graph: {missing[:10]}")
        if len(customers) != num_customers:
            raise ValueError(
                f"Fixed customer count {len(customers)} does not match {num_customers}"
            )
    else:
        depot = choose_depot(graph)
        customers = choose_customers(
            graph, scores_norm, num_customers, depot, customer_set, sample_seed
        )
    nodes = [depot] + customers
    n = len(nodes)
    d = np.zeros((n, n), dtype=float)
    q = np.zeros((n, n), dtype=float)
    q_cvar = np.zeros((n, n), dtype=float)
    f = np.zeros((n, n), dtype=float)
    paths: dict[tuple[int, int], list[int]] = {}
    threshold_value = concentration_threshold_value(graph, concentration_threshold)

    for i, src in enumerate(nodes):
        lengths, path_map = nx.single_source_dijkstra(
            graph, src, weight="hop", target=None
        )
        del lengths
        for j, dst in enumerate(nodes):
            if i == j:
                paths[(i, j)] = [src]
                continue
            path = [int(node) for node in path_map[dst]]
            paths[(i, j)] = path
            d[i, j] = len(path) - 1
            q[i, j] = path_risk(graph, path)
            q_cvar[i, j] = path_cvar90(graph, path)
            f[i, j] = path_concentration(graph, path, threshold_value)

    d_norm = normalize_matrix(d)
    q_norm = normalize_matrix(q)
    q_tail = (1.0 - tail_risk_eta) * q + tail_risk_eta * q_cvar
    q_tail_norm = normalize_matrix(q_tail)
    f_norm = normalize_matrix(f)
    d_norm = (d_norm + d_norm.T) / 2
    q_norm = (q_norm + q_norm.T) / 2
    q_tail_norm = (q_tail_norm + q_tail_norm.T) / 2
    f_norm = (f_norm + f_norm.T) / 2
    np.fill_diagonal(d_norm, 0.0)
    np.fill_diagonal(q_norm, 0.0)
    np.fill_diagonal(q_tail_norm, 0.0)
    np.fill_diagonal(f_norm, 0.0)

    return CVRPInstance(
        depot=depot,
        customers=customers,
        demands=[1] * num_customers,
        capacity=capacity,
        num_vehicles=num_vehicles,
        d_norm=d_norm,
        q_norm=q_norm,
        q_tail_norm=q_tail_norm,
        f_norm=f_norm,
        hop_paths=paths,
    )


def solve_pyvrp(cost: np.ndarray, inst: CVRPInstance, seed: int, runtime: float, scale: int):
    model = Model()
    locations = []
    for idx in range(cost.shape[0]):
        locations.append(model.add_location(x=idx, y=0))

    depot = model.add_depot(locations[0], name=f"depot_{inst.depot}")
    model.add_vehicle_type(
        num_available=inst.num_vehicles,
        capacity=inst.capacity,
        start_depot=depot,
        end_depot=depot,
    )
    for client_idx, demand in enumerate(inst.demands, start=1):
        model.add_client(
            locations[client_idx],
            delivery=demand,
            name=f"node_{inst.customers[client_idx - 1]}",
        )

    int_cost = np.rint(cost * scale).astype(int)
    np.fill_diagonal(int_cost, 0)
    for i, frm in enumerate(locations):
        for j, to in enumerate(locations):
            model.add_edge(frm, to, distance=int(int_cost[i, j]))

    return model.solve(stop=MaxRuntime(runtime), seed=seed, display=False)


def route_client_sequence(route) -> list[int]:
    seq = [0]
    for activity in route:
        if activity.is_client():
            # PyVRP client activity indices are zero-based among clients.
            seq.append(int(activity.idx) + 1)
    seq.append(0)
    return seq


def expand_route_edges(inst: CVRPInstance, seq: list[int]) -> list[tuple[int, int, float]]:
    expanded: list[tuple[int, int, float]] = []
    for left, right in zip(seq[:-1], seq[1:]):
        path = inst.hop_paths[(left, right)]
        for src, dst in zip(path[:-1], path[1:]):
            # Risk will be filled by caller from graph.
            expanded.append((int(src), int(dst), 0.0))
    return expanded


def route_risks(graph: nx.Graph, inst: CVRPInstance, seq: list[int]) -> np.ndarray:
    risks = []
    for left, right in zip(seq[:-1], seq[1:]):
        path = inst.hop_paths[(left, right)]
        for src, dst in zip(path[:-1], path[1:]):
            risks.append(float(graph[src][dst]["risk"]))
    return np.asarray(risks, dtype=float)


def edge_burden(graph: nx.Graph, inst: CVRPInstance, sequences: list[list[int]]) -> np.ndarray:
    burdens: dict[tuple[int, int], float] = {}
    for seq in sequences:
        for left, right in zip(seq[:-1], seq[1:]):
            path = inst.hop_paths[(left, right)]
            for src, dst in zip(path[:-1], path[1:]):
                key = (min(src, dst), max(src, dst))
                burdens[key] = burdens.get(key, 0.0) + float(graph[src][dst]["risk"])
    return np.asarray(list(burdens.values()), dtype=float)


def posterior_metrics(
    graph: nx.Graph,
    inst: CVRPInstance,
    result,
    beta: float,
    lambda_concentration: float,
    seed: int,
) -> dict[str, object]:
    sequences = [route_client_sequence(route) for route in result.best.routes()]
    route_risk_values = []
    route_cvars = []
    all_risks = []
    for seq in sequences:
        risks = route_risks(graph, inst, seq)
        route_risk_values.append(float(risks.sum()))
        route_cvars.append(cvar(risks, 0.90))
        all_risks.extend(risks.tolist())

    route_risks_arr = np.asarray(route_risk_values, dtype=float)
    all_risks_arr = np.asarray(all_risks, dtype=float)
    burdens = edge_burden(graph, inst, sequences)
    top_count = max(1, int(math.ceil(burdens.size * 0.10))) if burdens.size else 0
    top_share = (
        float(np.sort(burdens)[-top_count:].sum() / (burdens.sum() + EPS))
        if top_count
        else 0.0
    )

    return {
        "beta": beta,
        "lambda_concentration": lambda_concentration,
        "seed": seed,
        "is_feasible": bool(result.is_feasible()),
        "pyvrp_cost": int(result.cost()),
        "num_routes": int(result.best.num_routes()),
        "routes": json.dumps(sequences),
        "global_risk": float(all_risks_arr.sum()) if all_risks_arr.size else 0.0,
        "global_cvar90": cvar(all_risks_arr, 0.90),
        "max_vehicle_risk": float(route_risks_arr.max()) if route_risks_arr.size else 0.0,
        "max_vehicle_cvar90": float(max(route_cvars)) if route_cvars else 0.0,
        "vehicle_risk_gini": gini(route_risks_arr),
        "risk_variance": float(route_risks_arr.var()) if route_risks_arr.size else 0.0,
        "edge_burden_gini_used": gini(burdens),
        "top10_burden_share": top_share,
        "max_edge_burden": float(burdens.max()) if burdens.size else 0.0,
    }


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    metrics = [
        "pyvrp_cost",
        "global_risk",
        "global_cvar90",
        "max_vehicle_risk",
        "max_vehicle_cvar90",
        "vehicle_risk_gini",
        "risk_variance",
        "edge_burden_gini_used",
        "top10_burden_share",
        "max_edge_burden",
    ]
    grouped: dict[tuple[float, float], list[dict[str, object]]] = {}
    for row in rows:
        key = (float(row["beta"]), float(row.get("lambda_concentration", 0.0)))
        grouped.setdefault(key, []).append(row)

    base_group = grouped.get((0.0, 0.0), [])
    base_risk = np.mean([float(row["global_risk"]) for row in base_group]) if base_group else 0.0
    base_cost = np.mean([float(row["pyvrp_cost"]) for row in base_group]) if base_group else 0.0
    summary = []
    for (beta, lambda_concentration), group_rows in sorted(grouped.items()):
        out: dict[str, object] = {
            "beta": beta,
            "lambda_concentration": lambda_concentration,
            "runs": len(group_rows),
        }
        for metric in metrics:
            vals = np.asarray([float(row[metric]) for row in group_rows], dtype=float)
            out[f"{metric}_mean"] = float(vals.mean())
            out[f"{metric}_std"] = float(vals.std(ddof=1)) if vals.size > 1 else 0.0
        out["cost_increase_pct"] = (
            (float(out["pyvrp_cost_mean"]) - base_cost) / (base_cost + EPS)
            if base_cost > EPS
            else 0.0
        )
        out["risk_reduction_pct"] = (
            (base_risk - float(out["global_risk_mean"])) / (base_risk + EPS)
            if base_risk > EPS
            else 0.0
        )
        summary.append(out)
    return summary


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


def write_report(path: Path, summary: list[dict[str, object]], meta: dict[str, object]) -> None:
    lines = [
        "# PyVRP-CVRP Downstream Validation Report",
        "",
        f"- Year: `{meta['year']}`",
        f"- Customers: `{meta['num_customers']}`",
        f"- Vehicles: `{meta['num_vehicles']}`",
        f"- Capacity: `{meta['capacity']}`",
        f"- Customer set: `{meta['customer_set']}`",
        "",
        "| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            "| {beta:g} | {lam:g} | {cost:.1f} | {cost_inc:.3%} | {risk:.6f} | {risk_red:.3%} | {cvar:.6f} | {maxveh:.6f} | {vgini:.6f} | {egini:.6f} | {top:.3%} |".format(
                beta=row["beta"],
                lam=row["lambda_concentration"],
                cost=row["pyvrp_cost_mean"],
                cost_inc=row["cost_increase_pct"],
                risk=row["global_risk_mean"],
                risk_red=row["risk_reduction_pct"],
                cvar=row["global_cvar90_mean"],
                maxveh=row["max_vehicle_risk_mean"],
                vgini=row["vehicle_risk_gini_mean"],
                egini=row["edge_burden_gini_used_mean"],
                top=row["top10_burden_share_mean"],
            )
        )
    lines.extend(
        [
            "",
            "PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    out_dir = args.output_dir / args.batch_name
    out_dir.mkdir(parents=True, exist_ok=True)

    graph, scores_norm, labels = load_graph(args.risk_dir, args.year)
    del labels
    graph = largest_component(graph)
    fixed_depot = None
    fixed_customers = None
    if args.fixed_instance_meta is not None:
        fixed_meta = json.loads(args.fixed_instance_meta.read_text(encoding="utf-8"))
        fixed_depot = int(fixed_meta["depot"])
        fixed_customers = [int(node) for node in fixed_meta["customers"]]
    inst = build_instance(
        graph,
        scores_norm,
        args.num_customers,
        args.num_vehicles,
        args.capacity,
        args.customer_set,
        args.sample_seed,
        fixed_depot,
        fixed_customers,
        args.concentration_threshold,
        args.tail_risk_eta,
    )

    rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    betas = parse_float_csv(args.betas)
    lambdas = parse_float_csv(args.lambda_concentration)
    seeds = parse_int_csv(args.seeds)
    started = time.time()
    for beta in betas:
        lambda_values = [0.0] if abs(beta) <= EPS else lambdas
        for lambda_concentration in lambda_values:
            cost = inst.d_norm + beta * inst.q_tail_norm + lambda_concentration * inst.f_norm
            np.fill_diagonal(cost, 0.0)
            for seed in seeds:
                try:
                    result = solve_pyvrp(cost, inst, seed, args.max_runtime, args.scale)
                    rows.append(
                        posterior_metrics(
                            graph,
                            inst,
                            result,
                            beta,
                            lambda_concentration,
                            seed,
                        )
                    )
                except Exception as exc:  # noqa: BLE001 - validation records failures.
                    failures.append(
                        {
                            "beta": beta,
                            "lambda_concentration": lambda_concentration,
                            "seed": seed,
                            "error": repr(exc),
                        }
                    )

    summary = summarize(rows)
    meta = {
        "year": args.year,
        "risk_dir": str(args.risk_dir),
        "num_customers": args.num_customers,
        "num_vehicles": args.num_vehicles,
        "capacity": args.capacity,
        "customer_set": args.customer_set,
        "depot": inst.depot,
        "customers": inst.customers,
        "betas": betas,
        "lambda_concentration": lambdas,
        "tail_risk_eta": args.tail_risk_eta,
        "tail_risk_definition": "Q_tail=(1-eta)Q_sum+eta*Q_CVaR90",
        "concentration_threshold": args.concentration_threshold,
        "seeds": seeds,
        "max_runtime": args.max_runtime,
        "scale": args.scale,
        "fixed_instance_meta": str(args.fixed_instance_meta) if args.fixed_instance_meta else None,
        "elapsed_seconds": time.time() - started,
        "num_failures": len(failures),
    }

    write_csv(out_dir / "pyvrp_cvrp_detail.csv", rows)
    write_csv(out_dir / "pyvrp_cvrp_summary.csv", summary)
    (out_dir / "pyvrp_cvrp_failures.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out_dir / "pyvrp_cvrp_meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_report(out_dir / "pyvrp_cvrp_report.md", summary, meta)
    print(f"Wrote PyVRP CVRP validation to {out_dir}")


if __name__ == "__main__":
    main()
