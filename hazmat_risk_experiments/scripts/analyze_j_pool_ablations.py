"""Run objective-term and route-pool ablations on cached route evaluations.

The objective ablation uses the three-model route pool.  The route-pool
ablation uses J-full.  Every selection is subject to CostInc <= B and all
candidate routes have already been evaluated on the same common risk matrix.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import evaluate_route_pool_budget as budget_eval  # noqa: E402


METRICS = [
    "common_global_risk",
    "common_global_cvar90",
    "load_global_risk",
    "common_top10_burden_share",
]

OBJECTIVES = {
    "J-common": {
        "cost": 0.0,
        "common_risk": 1.0,
        "cvar90": 0.0,
        "load_risk": 0.0,
        "top10_share": 0.0,
    },
    "J-common+cvar": {
        "cost": 0.0,
        "common_risk": 1.0,
        "cvar90": 2.0,
        "load_risk": 0.0,
        "top10_share": 0.0,
    },
    "J-common+load": {
        "cost": 0.0,
        "common_risk": 1.0,
        "cvar90": 0.0,
        "load_risk": 1.0,
        "top10_share": 0.0,
    },
    "J-common+top10": {
        "cost": 0.0,
        "common_risk": 1.0,
        "cvar90": 0.0,
        "load_risk": 0.0,
        "top10_share": 0.5,
    },
    "J-full": {
        "cost": 0.0,
        "common_risk": 1.0,
        "cvar90": 2.0,
        "load_risk": 1.0,
        "top10_share": 0.5,
    },
}

WEIGHT_SENSITIVITY = {
    "J-balanced": {"cost": 0.0, "common_risk": 1.0, "cvar90": 2.0, "load_risk": 1.0, "top10_share": 0.5},
    "J-risk": {"cost": 0.0, "common_risk": 2.0, "cvar90": 2.0, "load_risk": 1.0, "top10_share": 0.5},
    "J-tail": {"cost": 0.0, "common_risk": 1.0, "cvar90": 3.0, "load_risk": 1.0, "top10_share": 0.5},
    "J-load": {"cost": 0.0, "common_risk": 1.0, "cvar90": 2.0, "load_risk": 2.0, "top10_share": 0.5},
    "J-conc": {"cost": 0.0, "common_risk": 1.0, "cvar90": 2.0, "load_risk": 1.0, "top10_share": 1.0},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--three-model-candidates", type=Path, required=True)
    parser.add_argument("--multi-eta-candidates", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--budgets", default="0.20,0.25,0.30")
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, object]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows: list[dict[str, object]] = []
        for raw in csv.DictReader(handle):
            row: dict[str, object] = dict(raw)
            for key in row:
                if key not in {"risk_source", "customer_set", "run_dir", "routes"}:
                    try:
                        row[key] = float(str(row[key]))
                    except ValueError:
                        pass
            row["seed"] = int(float(str(row["seed"])))
            rows.append(row)
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields: list[str] = []
    for row in rows:
        for field in row:
            if field not in fields:
                fields.append(field)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, object]], group_field: str) -> list[dict[str, object]]:
    groups: dict[tuple[str, str, float], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[(str(row[group_field]), str(row["customer_set"]), float(row["budget"]))].append(row)
    result: list[dict[str, object]] = []
    for (name, customer_set, budget), group in sorted(groups.items()):
        out: dict[str, object] = {
            group_field: name,
            "customer_set": customer_set,
            "budget": budget,
            "runs": len(group),
            "cost_increase_pct_mean": float(
                np.mean([float(row["cost_increase_pct"]) for row in group])
            ),
        }
        for metric in METRICS:
            values = np.asarray([float(row[metric]) for row in group], dtype=float)
            out[f"{metric}_mean"] = float(values.mean())
            out[f"{metric}_std"] = float(values.std(ddof=1)) if values.size > 1 else 0.0
        result.append(out)
    return result


def overall_summary(
    rows: list[dict[str, object]], group_field: str
) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[str(row[group_field])].append(row)
    result = []
    for name, group in sorted(groups.items()):
        out: dict[str, object] = {group_field: name, "cells": len(group)}
        for metric in METRICS:
            out[f"{metric}_mean"] = float(
                np.mean([float(row[f"{metric}_mean"]) for row in group])
            )
        result.append(out)
    return result


def objective_balance(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    """Average relative gap to the best objective in each set-budget cell."""

    cells: dict[tuple[str, float], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        cells[(str(row["customer_set"]), float(row["budget"]))].append(row)
    gaps: dict[str, list[float]] = defaultdict(list)
    for group in cells.values():
        best = {
            metric: min(float(row[f"{metric}_mean"]) for row in group)
            for metric in METRICS
        }
        for row in group:
            gap = np.mean(
                [
                    (float(row[f"{metric}_mean"]) - best[metric]) / best[metric]
                    for metric in METRICS
                ]
            )
            gaps[str(row["objective"])].append(float(gap))
    return [
        {
            "objective": objective,
            "cells": len(values),
            "mean_relative_gap_to_cell_best": float(np.mean(values)),
        }
        for objective, values in sorted(gaps.items())
    ]


def markdown_table(path: Path, title: str, rows: list[dict[str, object]], name_field: str) -> None:
    lines = [
        f"# {title}",
        "",
        "| Method | Set | B | CostInc | CommonRisk | CVaR90 | LoadRisk | Top10Share |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {name} | {customer_set} | {budget:.0%} | {cost:.2%} | {risk:.4f} | {cvar:.5f} | {load:.4f} | {top:.2%} |".format(
                name=row[name_field],
                customer_set=row["customer_set"],
                budget=float(row["budget"]),
                cost=float(row["cost_increase_pct_mean"]),
                risk=float(row["common_global_risk_mean"]),
                cvar=float(row["common_global_cvar90_mean"]),
                load=float(row["load_global_risk_mean"]),
                top=float(row["common_top10_burden_share_mean"]),
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    budgets = budget_eval.parse_float_list(args.budgets)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    three_model = read_csv(args.three_model_candidates)
    multi_eta = read_csv(args.multi_eta_candidates)

    # Recompute one shared baseline after merging pools.
    all_rows = budget_eval.assign_cost_increase(three_model + multi_eta)
    three_sources = {str(row["risk_source"]) for row in three_model}
    three_model = [row for row in all_rows if str(row["risk_source"]) in three_sources]

    objective_detail: list[dict[str, object]] = []
    for objective, weights in OBJECTIVES.items():
        for row in budget_eval.rerank_pool(three_model, budgets, weights):
            objective_detail.append({"objective": objective, **row})
    objective_summary = summarize(objective_detail, "objective")
    objective_overall = overall_summary(objective_summary, "objective")
    balance_summary = objective_balance(objective_summary)

    pools = {
        "GCN-only pool": [row for row in three_model if "_GCN_seed" in str(row["risk_source"])],
        "TEG-low-only pool": [row for row in three_model if "TEG-low" in str(row["risk_source"])],
        "Stable-Tail-only pool": [
            row for row in three_model if "Stable-Tail-GNN" in str(row["risk_source"])
        ],
        "three-model pool": three_model,
        "three-model + multi-eta pool": all_rows,
    }
    pool_detail: list[dict[str, object]] = []
    for pool_name, rows in pools.items():
        for row in budget_eval.rerank_pool(rows, budgets, OBJECTIVES["J-full"]):
            pool_detail.append({"route_pool": pool_name, **row})
    pool_summary = summarize(pool_detail, "route_pool")
    pool_overall = overall_summary(pool_summary, "route_pool")

    weight_detail: list[dict[str, object]] = []
    for weight_name, weights in WEIGHT_SENSITIVITY.items():
        for row in budget_eval.rerank_pool(all_rows, budgets, weights):
            weight_detail.append({"weight_setting": weight_name, **row})
    weight_summary = summarize(weight_detail, "weight_setting")
    weight_overall = overall_summary(weight_summary, "weight_setting")

    write_csv(args.output_dir / "j_ablation_detail.csv", objective_detail)
    write_csv(args.output_dir / "j_ablation_summary.csv", objective_summary)
    write_csv(args.output_dir / "j_ablation_overall.csv", objective_overall)
    write_csv(args.output_dir / "j_ablation_balance.csv", balance_summary)
    write_csv(args.output_dir / "route_pool_ablation_detail.csv", pool_detail)
    write_csv(args.output_dir / "route_pool_ablation_summary.csv", pool_summary)
    write_csv(args.output_dir / "route_pool_ablation_overall.csv", pool_overall)
    write_csv(args.output_dir / "j_weight_sensitivity_detail.csv", weight_detail)
    write_csv(args.output_dir / "j_weight_sensitivity_summary.csv", weight_summary)
    write_csv(args.output_dir / "j_weight_sensitivity_overall.csv", weight_overall)
    markdown_table(
        args.output_dir / "j_ablation_summary.md",
        "J Objective Ablation",
        objective_summary,
        "objective",
    )
    markdown_table(
        args.output_dir / "route_pool_ablation_summary.md",
        "Route Pool Ablation",
        pool_summary,
        "route_pool",
    )
    markdown_table(
        args.output_dir / "j_weight_sensitivity_summary.md",
        "J Weight Sensitivity",
        weight_summary,
        "weight_setting",
    )
    print(f"Wrote J and route-pool ablations to {args.output_dir}")


if __name__ == "__main__":
    main()
