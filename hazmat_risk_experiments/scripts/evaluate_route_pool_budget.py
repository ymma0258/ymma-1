"""Evaluate and rerank a PyVRP route pool under explicit cost budgets.

This script does not modify the PyVRP optimizer. It re-evaluates saved routes
with one common risk matrix, computes load-aware metrics, and selects the best
route among candidates whose cost increase is within each requested budget.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import common_evaluate_load_aware_routes as load_eval  # noqa: E402
import common_evaluate_pyvrp_routes as common_eval  # noqa: E402
import validate_pyvrp_cvrp as pyvrp_eval  # noqa: E402


EPS = 1e-12
METRIC_COLUMNS = {
    "common_risk": "common_global_risk",
    "cvar90": "common_global_cvar90",
    "cvar95": "common_global_cvar95",
    "load_risk": "load_global_risk",
    "load_cvar90": "load_cvar90",
    "edge_gini": "common_edge_burden_gini_used",
    "top10_share": "common_top10_burden_share",
}
DEFAULT_WEIGHTS = {
    "cost": 1.0,
    "common_risk": 1.0,
    "cvar90": 2.0,
    "load_risk": 1.0,
    "top10_share": 0.5,
}


def parse_label_dir(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("run dirs must use label=path")
    label, path = value.split("=", 1)
    return label.strip(), Path(path.strip())


def parse_float_list(value: str) -> list[float]:
    values = []
    for item in value.split(","):
        if not item.strip():
            continue
        number = float(item)
        values.append(number / 100.0 if number > 1 else number)
    return sorted(set(values))


def parse_weights(value: str) -> dict[str, float]:
    weights = dict(DEFAULT_WEIGHTS)
    for item in value.split(","):
        if not item.strip():
            continue
        name, raw = item.split("=", 1)
        name = name.strip()
        if name not in weights:
            raise ValueError(f"Unknown objective weight: {name}")
        weights[name] = float(raw)
    return weights


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dirs", nargs="*", type=parse_label_dir)
    parser.add_argument("--run-list", type=Path, default=None)
    parser.add_argument("--common-risk-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--batch-name", default="route_pool_budget")
    parser.add_argument(
        "--budgets",
        default="0.25,0.30",
        help="Maximum CostInc constraints (fractions or percentages).",
    )
    parser.add_argument(
        "--objective-weights",
        default="cost=1,common_risk=1,cvar90=2,load_risk=1,top10_share=0.5",
    )
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
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


def load_sources(args: argparse.Namespace) -> list[tuple[str, Path]]:
    sources = list(args.run_dirs)
    if args.run_list is not None:
        for row in read_csv(args.run_list):
            sources.append((row["label"], Path(row["run_dir"])))
    if not sources:
        raise ValueError("Provide positional label=path run dirs or --run-list.")
    return sources


def assign_cost_increase(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    """Attach cost increase using the shared beta=0 baseline per set and seed."""

    grouped: dict[tuple[str, int], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["customer_set"]), int(row["seed"]))].append(row)
    result: list[dict[str, object]] = []
    for group in grouped.values():
        baselines = [
            float(row["pyvrp_cost"])
            for row in group
            if abs(float(row["beta"])) <= EPS
            and abs(float(row["lambda_concentration"])) <= EPS
        ]
        base_cost = min(baselines) if baselines else min(float(row["pyvrp_cost"]) for row in group)
        for original in group:
            row = dict(original)
            row["baseline_cost"] = base_cost
            row["cost_increase_pct"] = (float(row["pyvrp_cost"]) - base_cost) / max(base_cost, EPS)
            result.append(row)
    return result


def budget_metric_best(
    rows: list[dict[str, object]], budgets: list[float]
) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str, int], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["risk_source"]), str(row["customer_set"]), int(row["seed"]))].append(row)
    selected: list[dict[str, object]] = []
    for (source, customer_set, seed), group in sorted(grouped.items()):
        for budget in budgets:
            feasible = [row for row in group if float(row["cost_increase_pct"]) <= budget + EPS]
            for selector, metric in METRIC_COLUMNS.items():
                if not feasible:
                    continue
                best = min(feasible, key=lambda row: (float(row[metric]), float(row["pyvrp_cost"])))
                selected.append(
                    {
                        "risk_source": source,
                        "customer_set": customer_set,
                        "seed": seed,
                        "budget": budget,
                        "selector": selector,
                        "selected_value": float(best[metric]),
                        **{key: value for key, value in best.items() if key != "routes"},
                    }
                )
    return selected


def minmax(value: float, values: np.ndarray) -> float:
    span = float(values.max() - values.min())
    return 0.0 if span <= EPS else (value - float(values.min())) / span


def rerank_pool(
    rows: list[dict[str, object]], budgets: list[float], weights: dict[str, float]
) -> list[dict[str, object]]:
    grouped: dict[tuple[str, int], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["customer_set"]), int(row["seed"]))].append(row)
    selected: list[dict[str, object]] = []
    score_fields = {
        "cost": "pyvrp_cost",
        "common_risk": "common_global_risk",
        "cvar90": "common_global_cvar90",
        "load_risk": "load_global_risk",
        "top10_share": "common_top10_burden_share",
    }
    for (customer_set, seed), group in sorted(grouped.items()):
        # Fit normalization once on the complete route pool.  This keeps J for
        # a route invariant when B changes from 25% to 30%.
        arrays = {
            name: np.asarray([float(row[column]) for row in group], dtype=float)
            for name, column in score_fields.items()
        }
        for budget in budgets:
            feasible = [row for row in group if float(row["cost_increase_pct"]) <= budget + EPS]
            if not feasible:
                continue
            scored = []
            for row in feasible:
                components = {
                    name: minmax(float(row[column]), arrays[name])
                    for name, column in score_fields.items()
                }
                score = sum(weights[name] * components[name] for name in score_fields)
                scored.append((score, float(row["pyvrp_cost"]), row))
            score, _, best = min(scored, key=lambda item: (item[0], item[1]))
            best_components = {
                f"{name}_norm": minmax(float(best[column]), arrays[name])
                for name, column in score_fields.items()
            }
            selected.append(
                {
                    "customer_set": customer_set,
                    "seed": seed,
                    "budget": budget,
                    "rerank_score": score,
                    **best_components,
                    **best,
                }
            )
    return selected


def summarize_budget(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str, float, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[
            (
                str(row["risk_source"]),
                str(row["customer_set"]),
                float(row["budget"]),
                str(row["selector"]),
            )
        ].append(row)
    summary = []
    for (source, customer_set, budget, selector), group in sorted(grouped.items()):
        values = np.asarray([float(row["selected_value"]) for row in group], dtype=float)
        costs = np.asarray([float(row["cost_increase_pct"]) for row in group], dtype=float)
        summary.append(
            {
                "risk_source": source,
                "customer_set": customer_set,
                "budget": budget,
                "selector": selector,
                "runs": len(group),
                "value_mean": float(values.mean()),
                "value_std": float(values.std(ddof=1)) if values.size > 1 else 0.0,
                "selected_cost_increase_mean": float(costs.mean()),
            }
        )
    return summary


def main_table(summary: list[dict[str, object]]) -> list[dict[str, object]]:
    lookup = {
        (str(row["risk_source"]), str(row["customer_set"]), round(float(row["budget"]), 2), str(row["selector"])): row
        for row in summary
    }
    groups = sorted({(str(row["risk_source"]), str(row["customer_set"])) for row in summary})
    columns = [
        ("common_risk_at_20", 0.20, "common_risk"),
        ("cvar90_at_25", 0.25, "cvar90"),
        ("load_risk_at_30", 0.30, "load_risk"),
        ("edge_gini_at_25", 0.25, "edge_gini"),
        ("top10_share_at_25", 0.25, "top10_share"),
    ]
    rows = []
    for source, customer_set in groups:
        out: dict[str, object] = {"risk_source": source, "customer_set": customer_set}
        for name, budget, selector in columns:
            row = lookup.get((source, customer_set, budget, selector))
            out[name] = float(row["value_mean"]) if row is not None else math.nan
        rows.append(out)
    return rows


def write_report(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# Cost-Constrained Route Risk",
        "",
        "Routes are re-evaluated on one common matrix. Risk@B is the minimum risk among routes with CostInc <= B. PyVRP itself is not modified.",
        "",
        "| Method | Set | Common Risk @20% | CVaR90 @25% | Load Risk @30% | Edge Gini @25% | Top10 Share @25% |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {risk_source} | {customer_set} | {common_risk_at_20:.6f} | {cvar90_at_25:.6f} | {load_risk_at_30:.6f} | {edge_gini_at_25:.6f} | {top10_share_at_25:.3%} |".format(**row)
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    budgets = parse_float_list(args.budgets)
    weights = parse_weights(args.objective_weights)
    out_dir = args.output_dir / args.batch_name
    out_dir.mkdir(parents=True, exist_ok=True)
    graph, scores_norm, _ = pyvrp_eval.load_graph(args.common_risk_dir, "data_2021")
    graph = pyvrp_eval.largest_component(graph)

    candidates: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    seen: set[tuple[object, ...]] = set()
    for label, run_dir in load_sources(args):
        try:
            meta = json.loads((run_dir / "pyvrp_cvrp_meta.json").read_text(encoding="utf-8"))
            inst = pyvrp_eval.build_instance(
                graph,
                scores_norm,
                int(meta["num_customers"]),
                int(meta["num_vehicles"]),
                int(meta["capacity"]),
                str(meta["customer_set"]),
                0,
                int(meta["depot"]),
                [int(node) for node in meta["customers"]],
            )
            for row in read_csv(run_dir / "pyvrp_cvrp_detail.csv"):
                key = (label, meta["customer_set"], row["beta"], row.get("lambda_concentration", "0"), row["seed"], row["routes"])
                if key in seen:
                    continue
                seen.add(key)
                routes = json.loads(row["routes"])
                candidates.append(
                    {
                        "risk_source": label,
                        "customer_set": str(meta["customer_set"]),
                        "run_dir": str(run_dir),
                        "beta": float(row["beta"]),
                        "lambda_concentration": float(row.get("lambda_concentration", 0.0)),
                        "seed": int(row["seed"]),
                        "pyvrp_cost": float(row["pyvrp_cost"]),
                        "routes": row["routes"],
                        **common_eval.metrics_for_sequences(graph, inst, routes),
                        **load_eval.metrics(graph, inst, routes),
                    }
                )
        except Exception as exc:  # noqa: BLE001
            failures.append({"risk_source": label, "run_dir": str(run_dir), "error": repr(exc)})

    candidates = assign_cost_increase(candidates)
    metric_best = budget_metric_best(candidates, budgets)
    metric_summary = summarize_budget(metric_best)
    table = main_table(metric_summary)
    reranked = rerank_pool(candidates, budgets, weights)
    write_csv(out_dir / "route_pool_candidates.csv", candidates)
    write_csv(out_dir / "budget_metric_best.csv", metric_best)
    write_csv(out_dir / "budget_metric_summary.csv", metric_summary)
    write_csv(out_dir / "budget_main_table.csv", table)
    write_csv(out_dir / "route_pool_reranked.csv", reranked)
    write_report(out_dir / "budget_main_table.md", table)
    (out_dir / "failures.json").write_text(json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / "meta.json").write_text(
        json.dumps(
            {
                "common_risk_dir": str(args.common_risk_dir),
                "budgets": budgets,
                "objective_weights": weights,
                "budget_definition": "Risk@B = min(CommonRisk | CostInc <= B)",
                "rerank_definition": "J = D_norm + beta1*CommonRisk_norm + beta2*CVaR90_norm + beta3*LoadRisk_norm + beta4*Top10Share_norm",
                "definition": "posterior common/load-aware route-pool reranking; PyVRP optimizer unchanged",
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote budget-constrained route evaluation to {out_dir}")
    print(f"Candidates: {len(candidates)}; reranked: {len(reranked)}; failures: {len(failures)}")


if __name__ == "__main__":
    main()
