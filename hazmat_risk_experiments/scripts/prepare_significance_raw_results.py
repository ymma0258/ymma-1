"""Create hierarchical raw results for paired downstream significance tests.

Selections are made independently for every model_seed x solver_seed pair.
This preserves the repeated-experiment hierarchy needed to aggregate the ten
solver seeds before testing across the ten model seeds.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

import numpy as np


EPS = 1e-12
METRIC_COLUMNS = {
    "common_risk": "common_global_risk",
    "cvar90": "common_global_cvar90",
    "load_risk": "load_global_risk",
    "top10share": "common_top10_burden_share",
}
J_WEIGHTS = {
    "cost": 1.0,
    "common_risk": 1.0,
    "cvar90": 2.0,
    "load_risk": 1.0,
    "top10share": 0.5,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--budgets", default="0.20,0.25,0.30")
    return parser.parse_args()


def parse_budgets(value: str) -> list[float]:
    return sorted({float(item.strip()) for item in value.split(",") if item.strip()})


def parse_source(value: str) -> tuple[str, int]:
    match = re.search(r"(?:^|_)(GCN|TEG-low|Stable-Tail-GNN)_seed(\d+)$", value)
    if match is None:
        raise ValueError(f"Cannot parse method/model seed from risk_source={value!r}")
    return match.group(1), int(match.group(2))


def read_candidates(path: Path) -> list[dict[str, object]]:
    numeric = {
        "beta",
        "lambda_concentration",
        "seed",
        "pyvrp_cost",
        "cost_increase_pct",
        *METRIC_COLUMNS.values(),
    }
    rows: list[dict[str, object]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for raw in csv.DictReader(handle):
            row: dict[str, object] = dict(raw)
            for key in numeric:
                row[key] = float(raw[key])
            row["solver_seed"] = int(float(raw["seed"]))
            row["method"], row["model_seed"] = parse_source(raw["risk_source"])
            rows.append(row)
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = list(rows[0]) if rows else []
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def minmax(value: float, values: np.ndarray) -> float:
    span = float(values.max() - values.min())
    return 0.0 if span <= EPS else (value - float(values.min())) / span


def raw_row(
    row: dict[str, object], budget: float, method: str, j_score: float | None = None
) -> dict[str, object]:
    return {
        "set": row["customer_set"],
        "budget": int(round(100 * budget)),
        "method": method,
        "model_seed": int(row["model_seed"]),
        "solver_seed": int(row["solver_seed"]),
        "cost_inc": 100.0 * float(row["cost_increase_pct"]),
        "common_risk": float(row["common_global_risk"]),
        "cvar90": float(row["common_global_cvar90"]),
        "load_risk": float(row["load_global_risk"]),
        "top10share": float(row["common_top10_burden_share"]),
        "j_score": "" if j_score is None else j_score,
        "risk_source": row["risk_source"],
    }


def risk_budget_rows(
    candidates: list[dict[str, object]], budgets: list[float]
) -> list[dict[str, object]]:
    groups: dict[tuple[str, str, int, int], list[dict[str, object]]] = defaultdict(list)
    for row in candidates:
        key = (
            str(row["customer_set"]),
            str(row["method"]),
            int(row["model_seed"]),
            int(row["solver_seed"]),
        )
        groups[key].append(row)
    result = []
    for (_, method, _, _), group in sorted(groups.items()):
        for budget in budgets:
            feasible = [row for row in group if float(row["cost_increase_pct"]) <= budget + EPS]
            if not feasible:
                raise ValueError(f"No feasible Risk@B route for method={method}, B={budget}")
            best = min(
                feasible,
                key=lambda row: (float(row["common_global_risk"]), float(row["pyvrp_cost"])),
            )
            result.append(raw_row(best, budget, method))
    return result


def j_reranking_rows(
    candidates: list[dict[str, object]], budgets: list[float]
) -> list[dict[str, object]]:
    groups: dict[tuple[str, int, int], list[dict[str, object]]] = defaultdict(list)
    for row in candidates:
        key = (str(row["customer_set"]), int(row["model_seed"]), int(row["solver_seed"]))
        groups[key].append(row)

    score_fields = {
        "cost": "pyvrp_cost",
        "common_risk": "common_global_risk",
        "cvar90": "common_global_cvar90",
        "load_risk": "load_global_risk",
        "top10share": "common_top10_burden_share",
    }
    result = []
    for group in groups.values():
        arrays = {
            name: np.asarray([float(row[column]) for row in group], dtype=float)
            for name, column in score_fields.items()
        }
        for budget in budgets:
            feasible = [row for row in group if float(row["cost_increase_pct"]) <= budget + EPS]
            if not feasible:
                raise ValueError(f"No feasible J route for B={budget}")
            scored = []
            for row in feasible:
                score = sum(
                    J_WEIGHTS[name] * minmax(float(row[column]), arrays[name])
                    for name, column in score_fields.items()
                )
                scored.append((score, float(row["pyvrp_cost"]), row))
            score, _, best = min(scored, key=lambda item: (item[0], item[1]))
            result.append(raw_row(best, budget, "J-reranking", score))
    return sorted(
        result,
        key=lambda row: (
            str(row["set"]),
            int(row["budget"]),
            int(row["model_seed"]),
            int(row["solver_seed"]),
        ),
    )


def validate_design(rows: list[dict[str, object]], expected_methods: set[str]) -> None:
    counts: dict[tuple[object, ...], set[int]] = defaultdict(set)
    for row in rows:
        counts[(row["set"], row["budget"], row["method"], row["model_seed"])].add(
            int(row["solver_seed"])
        )
    methods = {str(row["method"]) for row in rows}
    if methods != expected_methods:
        raise ValueError(f"Expected methods {expected_methods}, found {methods}")
    bad = {key: len(seeds) for key, seeds in counts.items() if len(seeds) != 10}
    if bad:
        raise ValueError(f"Expected 10 solver seeds per model seed; invalid groups: {bad}")


def main() -> None:
    args = parse_args()
    budgets = parse_budgets(args.budgets)
    candidates = read_candidates(args.candidates)
    risk_rows = risk_budget_rows(candidates, budgets)
    j_rows = j_reranking_rows(candidates, budgets)
    validate_design(risk_rows, {"GCN", "TEG-low", "Stable-Tail-GNN"})
    validate_design(j_rows, {"J-reranking"})
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.output_dir / "risk_budget_results_raw.csv", risk_rows)
    write_csv(args.output_dir / "j_reranking_results_raw.csv", j_rows)
    print(f"Risk@B rows: {len(risk_rows)}; J rows: {len(j_rows)}")


if __name__ == "__main__":
    main()
