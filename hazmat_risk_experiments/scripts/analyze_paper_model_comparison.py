"""Build the final paper comparison from node, OD, and common PyVRP results."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import wilcoxon


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs_10seed"
DEFAULT_NODE = (
    OUTPUTS
    / "models"
    / "paper_comparison_tables_10seed"
    / "node_risk_eval_with_high_fn_paper_10seed.csv"
)
DEFAULT_ABLATION = (
    OUTPUTS
    / "models"
    / "paper_comparison_tables_10seed"
    / "node_risk_ablation_with_high_fn_paper_10seed.csv"
)
DEFAULT_STRONG_NODE = (
    OUTPUTS / "models" / "paper_strong_baselines_splitB_10seed_summary.csv"
)
DEFAULT_OD = (
    OUTPUTS
    / "od_paths"
    / "paper_model_od_comparison_10seed"
    / "od_seed_robustness_by_model_10seed.csv"
)
DEFAULT_STRONG_OD = (
    OUTPUTS
    / "od_paths"
    / "paper_strong_od_comparison_10seed"
    / "od_seed_robustness_by_model_10seed.csv"
)
DEFAULT_SELF = (
    OUTPUTS
    / "pyvrp_cvrp"
    / "paper_model_pyvrp_budget_sweep_10seed"
    / "model_pyvrp_summary.csv"
)
DEFAULT_STRONG_SELF = (
    OUTPUTS
    / "pyvrp_cvrp"
    / "paper_strong_pyvrp_budget_sweep_10seed"
    / "model_pyvrp_summary.csv"
)
DEFAULT_COMMON = (
    OUTPUTS
    / "pyvrp_cvrp"
    / "paper_all_models_common_eval_10seed"
    / "common_route_summary.csv"
)
DEFAULT_LOAD = (
    OUTPUTS
    / "pyvrp_cvrp"
    / "paper_all_models_load_eval_10seed"
    / "load_aware_summary.csv"
)
DEFAULT_OUT = (
    OUTPUTS / "pyvrp_cvrp" / "paper_model_comparison_final_10seed"
)
STABLE = "Stable-Tail GNN"
MODEL_DISPLAY = {
    "GCN (paper)": "GCN",
    "GAT": "GAT",
    "GraphSAGE": "GraphSAGE",
    "TEG-only": "TEG-only",
    "Stable-Tail w/o Tail Loss": "Stable-Tail w/o Tail Loss",
    "Stable-Tail GNN (paper)": STABLE,
    "SGFormer-adapted": "SGFormer-adapted",
    "Gradformer-adapted": "Gradformer-adapted",
}
MODEL_ORDER = [
    "GCN",
    "GAT",
    "GraphSAGE",
    "SGFormer-adapted",
    "Gradformer-adapted",
    "TEG-only",
    "Stable-Tail w/o Tail Loss",
    STABLE,
]
METRICS = [
    "common_global_risk_mean",
    "common_global_cvar90_mean",
    "common_global_cvar95_mean",
    "common_max_edge_risk_mean",
    "common_high_risk_edge_hits_mean",
    "common_max_vehicle_risk_mean",
    "common_max_vehicle_cvar90_mean",
    "common_edge_burden_gini_used_mean",
    "common_top10_burden_share_mean",
    "load_global_risk_mean",
    "load_cvar90_mean",
    "load_cvar95_mean",
    "load_max_vehicle_risk_mean",
    "load_edge_burden_gini_used_mean",
    "load_top10_burden_share_mean",
]
BUDGETS = tuple(value / 100 for value in range(10, 41, 5))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--node", type=Path, default=DEFAULT_NODE)
    parser.add_argument("--ablation", type=Path, default=DEFAULT_ABLATION)
    parser.add_argument("--strong-node", type=Path, default=DEFAULT_STRONG_NODE)
    parser.add_argument("--od", type=Path, default=DEFAULT_OD)
    parser.add_argument("--strong-od", type=Path, default=DEFAULT_STRONG_OD)
    parser.add_argument("--self-summary", type=Path, default=DEFAULT_SELF)
    parser.add_argument("--strong-self-summary", type=Path, default=DEFAULT_STRONG_SELF)
    parser.add_argument("--common-summary", type=Path, default=DEFAULT_COMMON)
    parser.add_argument("--load-summary", type=Path, default=DEFAULT_LOAD)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--bootstrap-samples", type=int, default=10000)
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
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


def split_source(value: str, common: bool = False) -> tuple[str, int]:
    if common:
        match = re.match(r"^[AB]_(.+)_seed(\d+)$", value)
    else:
        match = re.match(r"^(.+)_seed(\d+)$", value)
    if not match:
        raise ValueError(f"Cannot parse risk source: {value}")
    return MODEL_DISPLAY[match.group(1)], int(match.group(2))


def mean_std(values: list[float]) -> tuple[float, float]:
    arr = np.asarray(values, dtype=float)
    return float(arr.mean()), float(arr.std(ddof=1)) if arr.size > 1 else 0.0


def bootstrap_ci(values: np.ndarray, samples: int, seed: int = 20260705) -> tuple[float, float]:
    if values.size == 0:
        return np.nan, np.nan
    rng = np.random.default_rng(seed)
    draws = rng.choice(values, size=(samples, values.size), replace=True).mean(axis=1)
    low, high = np.quantile(draws, [0.025, 0.975])
    return float(low), float(high)


def holm_adjust(p_values: list[float]) -> list[float]:
    order = np.argsort(p_values)
    adjusted = np.ones(len(p_values), dtype=float)
    running = 0.0
    count = len(p_values)
    for rank, idx in enumerate(order):
        running = max(running, min(1.0, (count - rank) * p_values[idx]))
        adjusted[idx] = running
    return adjusted.tolist()


def load_joined(
    self_rows: list[dict[str, str]],
    common_rows: list[dict[str, str]],
    load_rows: list[dict[str, str]],
) -> list[dict[str, object]]:
    costs: dict[tuple[str, int, str, float], dict[str, str]] = {}
    for row in self_rows:
        model, model_seed = split_source(row["risk_source"])
        key = (model, model_seed, row["customer_set"], float(row["beta"]))
        costs[key] = row

    load_by_key: dict[tuple[str, int, str, float], dict[str, str]] = {}
    for row in load_rows:
        model, model_seed = split_source(row["risk_source"], common=True)
        key = (model, model_seed, row["customer_set"], float(row["beta"]))
        load_by_key[key] = row

    joined: list[dict[str, object]] = []
    for row in common_rows:
        model, model_seed = split_source(row["risk_source"], common=True)
        key = (model, model_seed, row["customer_set"], float(row["beta"]))
        cost = costs.get(key)
        if cost is None:
            raise KeyError(f"No matching cost row for {key}")
        load = load_by_key.get(key)
        if load is None:
            raise KeyError(f"No matching load-risk row for {key}")
        joined.append(
            {
                "model": model,
                "model_seed": model_seed,
                "customer_set": row["customer_set"],
                "beta": float(row["beta"]),
                "cost_increase": float(cost["cost_increase_pct"]),
                **{
                    metric: float(row[metric])
                    if metric.startswith("common_")
                    else float(load[metric])
                    for metric in METRICS
                },
            }
        )
    return joined


def select_budgets(joined: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, int, str], list[dict[str, object]]] = defaultdict(list)
    for row in joined:
        grouped[(str(row["model"]), int(row["model_seed"]), str(row["customer_set"]))].append(row)

    selected: list[dict[str, object]] = []
    for (model, seed, customer_set), candidates in sorted(grouped.items()):
        for budget in BUDGETS:
            feasible = [row for row in candidates if float(row["cost_increase"]) <= budget + 1e-12]
            if not feasible:
                continue
            best = min(feasible, key=lambda row: float(row["common_global_risk_mean"]))
            selected.append(
                {
                    "model": model,
                    "model_seed": seed,
                    "customer_set": customer_set,
                    "budget": budget,
                    "selected_beta": best["beta"],
                    "cost_increase": best["cost_increase"],
                    **{metric: best[metric] for metric in METRICS},
                }
            )
    return selected


def summarize_budgets(selected: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str, float], list[dict[str, object]]] = defaultdict(list)
    for row in selected:
        grouped[(str(row["model"]), str(row["customer_set"]), float(row["budget"]))].append(row)
    result: list[dict[str, object]] = []
    for (model, customer_set, budget), rows in sorted(grouped.items()):
        out: dict[str, object] = {
            "model": model,
            "customer_set": customer_set,
            "budget": budget,
            "model_seed_runs": len(rows),
        }
        for metric in ["cost_increase", *METRICS]:
            avg, std = mean_std([float(row[metric]) for row in rows])
            out[f"{metric}_mean"] = avg
            out[f"{metric}_std"] = std
        result.append(out)
    return result


def significance(selected: list[dict[str, object]], samples: int) -> list[dict[str, object]]:
    keyed = {
        (str(row["model"]), int(row["model_seed"]), str(row["customer_set"]), float(row["budget"])): row
        for row in selected
    }
    result: list[dict[str, object]] = []
    for customer_set in ("A", "B"):
        for budget in BUDGETS:
            block: list[dict[str, object]] = []
            p_values: list[float] = []
            for baseline in MODEL_ORDER[:-1]:
                base = np.asarray(
                    [float(keyed[(baseline, seed, customer_set, budget)]["common_global_risk_mean"]) for seed in range(10)]
                )
                stable = np.asarray(
                    [float(keyed[(STABLE, seed, customer_set, budget)]["common_global_risk_mean"]) for seed in range(10)]
                )
                diff = base - stable  # Positive means Stable-Tail is safer.
                try:
                    p_value = float(wilcoxon(diff, alternative="two-sided").pvalue)
                except ValueError:
                    p_value = 1.0
                low, high = bootstrap_ci(diff, samples)
                row = {
                    "customer_set": customer_set,
                    "budget": budget,
                    "baseline": baseline,
                    "comparison": STABLE,
                    "baseline_minus_stable_mean": float(diff.mean()),
                    "relative_risk_reduction": float(diff.mean() / (base.mean() + 1e-12)),
                    "bootstrap_ci_low": low,
                    "bootstrap_ci_high": high,
                    "wilcoxon_p": p_value,
                    "effect_size_dz": float(
                        diff.mean() / (diff.std(ddof=1) + 1e-12)
                    ),
                }
                block.append(row)
                p_values.append(p_value)
            adjusted = holm_adjust(p_values)
            for row, p_adj in zip(block, adjusted):
                row["holm_p"] = p_adj
                row["significant_0p05"] = p_adj < 0.05
                result.append(row)
    return result


def targeted_significance(
    selected: list[dict[str, object]], samples: int
) -> list[dict[str, object]]:
    keyed = {
        (str(row["model"]), int(row["model_seed"]), str(row["customer_set"]), float(row["budget"])): row
        for row in selected
    }
    result: list[dict[str, object]] = []
    baselines = ["GraphSAGE", "TEG-only", "Stable-Tail w/o Tail Loss"]
    metrics = [
        "common_global_risk_mean",
        "common_global_cvar90_mean",
        "common_global_cvar95_mean",
    ]
    for customer_set in ("A", "B"):
        for budget in BUDGETS:
            for metric in metrics:
                block: list[dict[str, object]] = []
                p_values: list[float] = []
                for baseline in baselines:
                    base = np.asarray(
                        [float(keyed[(baseline, seed, customer_set, budget)][metric]) for seed in range(10)]
                    )
                    stable = np.asarray(
                        [float(keyed[(STABLE, seed, customer_set, budget)][metric]) for seed in range(10)]
                    )
                    diff = base - stable
                    try:
                        p_value = float(wilcoxon(diff, alternative="two-sided").pvalue)
                    except ValueError:
                        p_value = 1.0
                    low, high = bootstrap_ci(diff, samples, seed=20260707)
                    block.append(
                        {
                            "customer_set": customer_set,
                            "budget": budget,
                            "metric": metric,
                            "baseline": baseline,
                            "comparison": STABLE,
                            "baseline_minus_stable_mean": float(diff.mean()),
                            "relative_reduction": float(diff.mean() / (base.mean() + 1e-12)),
                            "bootstrap_ci_low": low,
                            "bootstrap_ci_high": high,
                            "effect_size_dz": float(
                                diff.mean() / (diff.std(ddof=1) + 1e-12)
                            ),
                            "wilcoxon_p": p_value,
                        }
                    )
                    p_values.append(p_value)
                for row, p_adj in zip(block, holm_adjust(p_values)):
                    row["holm_p"] = p_adj
                    row["significant_0p05"] = p_adj < 0.05
                    result.append(row)
    return result


def beta_one_summary(joined: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in joined:
        if abs(float(row["beta"]) - 1.0) < 1e-12:
            grouped[(str(row["model"]), str(row["customer_set"]))].append(row)
    result: list[dict[str, object]] = []
    for (model, customer_set), rows in sorted(grouped.items()):
        out: dict[str, object] = {"model": model, "customer_set": customer_set, "model_seed_runs": len(rows)}
        for metric in ["cost_increase", *METRICS]:
            avg, std = mean_std([float(row[metric]) for row in rows])
            out[f"{metric}_mean"] = avg
            out[f"{metric}_std"] = std
        result.append(out)
    return result


def strong_node_table(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    labels = {
        "sgformer_adapted": "SGFormer-adapted",
        "gradformer_adapted": "Gradformer-adapted",
    }
    for row in rows:
        if row["split"] != "B" or row["eval_split"] != "data_2021_test":
            continue
        result.append(
            {
                "model": labels[row["model"]],
                "Macro-F1": f"{float(row['macro_f1_mean']):.4f}",
                "MAE": f"{float(row['mae_mean']):.4f}",
                "QWK": f"{float(row['qwk_mean']):.4f}",
                "Recall@6-8": f"{float(row['recall_6_8_mean']):.4f}",
                "PR-AUC": f"{float(row['pr_auc_high_mean']):.4f}",
                "High FN": f"{float(row['high_fn_rate_mean']):.4f}",
            }
        )
    return result


def lower_envelope_auc(
    rows: list[dict[str, object]], metric: str, max_budget: float = 0.40
) -> float:
    points = sorted(
        (max(0.0, float(row["cost_increase"])), float(row[metric])) for row in rows
    )
    baseline = min(value for cost, value in points if cost <= 1e-12)
    breakpoints: list[tuple[float, float]] = [(0.0, baseline)]
    best = baseline
    for cost, value in points:
        if cost > max_budget:
            continue
        best = min(best, value)
        breakpoints.append((cost, best))
    breakpoints.append((max_budget, best))
    breakpoints.sort()

    # Right-continuous step integral of the best observed feasible candidate.
    auc = 0.0
    current = baseline
    previous = 0.0
    for cost, value in breakpoints[1:]:
        auc += (cost - previous) * current
        previous = cost
        current = min(current, value)
    if previous < max_budget:
        auc += (max_budget - previous) * current
    return auc / max_budget


def cost_risk_auc(joined: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    grouped: dict[tuple[str, int, str], list[dict[str, object]]] = defaultdict(list)
    for row in joined:
        grouped[(str(row["model"]), int(row["model_seed"]), str(row["customer_set"]))].append(row)
    detail: list[dict[str, object]] = []
    for (model, seed, customer_set), rows in sorted(grouped.items()):
        detail.append(
            {
                "model": model,
                "model_seed": seed,
                "customer_set": customer_set,
                "max_budget": 0.40,
                "common_risk_aubrc": lower_envelope_auc(rows, "common_global_risk_mean"),
                "cvar90_aubrc": lower_envelope_auc(rows, "common_global_cvar90_mean"),
                "cvar95_aubrc": lower_envelope_auc(rows, "common_global_cvar95_mean"),
                "load_risk_aubrc": lower_envelope_auc(rows, "load_global_risk_mean"),
                "load_cvar90_aubrc": lower_envelope_auc(rows, "load_cvar90_mean"),
                "load_cvar95_aubrc": lower_envelope_auc(rows, "load_cvar95_mean"),
                "max_vehicle_risk_aubrc": lower_envelope_auc(
                    rows, "common_max_vehicle_risk_mean"
                ),
                "max_vehicle_cvar90_aubrc": lower_envelope_auc(
                    rows, "common_max_vehicle_cvar90_mean"
                ),
            }
        )
    grouped_detail: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in detail:
        grouped_detail[(str(row["model"]), str(row["customer_set"]))].append(row)
    summary: list[dict[str, object]] = []
    for (model, customer_set), rows in sorted(grouped_detail.items()):
        out: dict[str, object] = {
            "model": model,
            "customer_set": customer_set,
            "model_seed_runs": len(rows),
            "max_budget": 0.40,
        }
        for metric in (
            "common_risk_aubrc",
            "cvar90_aubrc",
            "cvar95_aubrc",
            "load_risk_aubrc",
            "load_cvar90_aubrc",
            "load_cvar95_aubrc",
            "max_vehicle_risk_aubrc",
            "max_vehicle_cvar90_aubrc",
        ):
            avg, std = mean_std([float(row[metric]) for row in rows])
            out[f"{metric}_mean"] = avg
            out[f"{metric}_std"] = std
        summary.append(out)
    return detail, summary


def budget_win_rates(selected: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[int, str, float], list[dict[str, object]]] = defaultdict(list)
    for row in selected:
        grouped[(int(row["model_seed"]), str(row["customer_set"]), float(row["budget"]))].append(row)
    wins = {(model, customer_set): 0 for model in MODEL_ORDER for customer_set in ("A", "B")}
    comparisons = {(model, customer_set): 0 for model in MODEL_ORDER for customer_set in ("A", "B")}
    risk_values: dict[tuple[str, str], list[float]] = defaultdict(list)
    for (_seed, customer_set, _budget), rows in grouped.items():
        best = min(float(row["common_global_risk_mean"]) for row in rows)
        for row in rows:
            model = str(row["model"])
            key = (model, customer_set)
            comparisons[key] += 1
            risk_values[key].append(float(row["common_global_risk_mean"]))
            if abs(float(row["common_global_risk_mean"]) - best) <= 1e-12:
                wins[key] += 1
    result: list[dict[str, object]] = []
    for model in MODEL_ORDER:
        for customer_set in ("A", "B"):
            key = (model, customer_set)
            result.append(
                {
                    "model": model,
                    "customer_set": customer_set,
                    "wins": wins[key],
                    "comparisons": comparisons[key],
                    "win_rate": wins[key] / max(1, comparisons[key]),
                    "average_common_risk_at_b": float(np.mean(risk_values[key])),
                }
            )
    return result


def all_model_summary(
    node_rows: list[dict[str, str]],
    ablation_rows: list[dict[str, str]],
    od_rows: list[dict[str, str]],
    budget_rows: list[dict[str, object]],
    auc_rows: list[dict[str, object]],
    win_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    """Build one publication-ready row per model across upstream and downstream tests."""
    node_by_model = {str(row["model"]): row for row in node_rows}
    for row in ablation_rows:
        model = str(row["model"])
        if model in MODEL_ORDER:
            node_by_model[model] = row
    od_by_model = {
        (MODEL_DISPLAY.get(str(row["model"]), str(row["model"])), str(row["method"])): row
        for row in od_rows
    }
    budget_by_key = {
        (str(row["model"]), str(row["customer_set"]), float(row["budget"])): row
        for row in budget_rows
    }
    auc_by_key = {
        (str(row["model"]), str(row["customer_set"])): row for row in auc_rows
    }
    win_by_key = {
        (str(row["model"]), str(row["customer_set"])): row for row in win_rows
    }
    result: list[dict[str, object]] = []
    for model in MODEL_ORDER:
        node = node_by_model[model]
        od = od_by_model[(model, "CVaR-risk")]
        out: dict[str, object] = {
            "model": model,
            "macro_f1": node["Macro-F1"],
            "mae": node["MAE"],
            "qwk": node["QWK"],
            "pr_auc": node["PR-AUC"],
            "recall_at_6_8": node["Recall@6-8"],
            "high_fn": node["High FN"],
            "od_hop_increase": od["hop_increase_mean"],
            "od_total_risk_reduction": od["total_risk_reduction_mean"],
            "od_cvar90_reduction": od["cvar90_reduction_mean"],
        }
        for customer_set in ("A", "B"):
            prefix = f"set_{customer_set.lower()}"
            budget20 = budget_by_key[(model, customer_set, 0.20)]
            auc = auc_by_key[(model, customer_set)]
            wins = win_by_key[(model, customer_set)]
            out.update(
                {
                    f"{prefix}_risk20": budget20["common_global_risk_mean_mean"],
                    f"{prefix}_cvar90_20": budget20["common_global_cvar90_mean_mean"],
                    f"{prefix}_cvar95_20": budget20["common_global_cvar95_mean_mean"],
                    f"{prefix}_max_edge_risk20": budget20["common_max_edge_risk_mean_mean"],
                    f"{prefix}_high_risk_edge_hits20": budget20[
                        "common_high_risk_edge_hits_mean_mean"
                    ],
                    f"{prefix}_load_risk20": budget20["load_global_risk_mean_mean"],
                    f"{prefix}_load_cvar90_20": budget20["load_cvar90_mean_mean"],
                    f"{prefix}_load_cvar95_20": budget20["load_cvar95_mean_mean"],
                    f"{prefix}_top10_share20": budget20["common_top10_burden_share_mean_mean"],
                    f"{prefix}_edge_gini20": budget20["common_edge_burden_gini_used_mean_mean"],
                    f"{prefix}_max_vehicle_risk20": budget20["common_max_vehicle_risk_mean_mean"],
                    f"{prefix}_max_vehicle_cvar90_20": budget20[
                        "common_max_vehicle_cvar90_mean_mean"
                    ],
                    f"{prefix}_win_rate_10_40": wins["win_rate"],
                    f"{prefix}_average_risk_at_b": wins["average_common_risk_at_b"],
                    f"{prefix}_common_risk_aubrc": auc["common_risk_aubrc_mean"],
                    f"{prefix}_cvar90_aubrc": auc["cvar90_aubrc_mean"],
                    f"{prefix}_cvar95_aubrc": auc["cvar95_aubrc_mean"],
                    f"{prefix}_load_risk_aubrc": auc["load_risk_aubrc_mean"],
                    f"{prefix}_load_cvar90_aubrc": auc["load_cvar90_aubrc_mean"],
                    f"{prefix}_load_cvar95_aubrc": auc["load_cvar95_aubrc_mean"],
                    f"{prefix}_max_vehicle_risk_aubrc": auc[
                        "max_vehicle_risk_aubrc_mean"
                    ],
                    f"{prefix}_max_vehicle_cvar90_aubrc": auc[
                        "max_vehicle_cvar90_aubrc_mean"
                    ],
                }
            )
        result.append(out)
    return result


def auc_significance(
    detail: list[dict[str, object]], samples: int
) -> list[dict[str, object]]:
    keyed = {
        (str(row["model"]), int(row["model_seed"]), str(row["customer_set"])): row
        for row in detail
    }
    result: list[dict[str, object]] = []
    for customer_set in ("A", "B"):
        block: list[dict[str, object]] = []
        p_values: list[float] = []
        for baseline in MODEL_ORDER[:-1]:
            base = np.asarray(
                [float(keyed[(baseline, seed, customer_set)]["common_risk_aubrc"]) for seed in range(10)]
            )
            stable = np.asarray(
                [float(keyed[(STABLE, seed, customer_set)]["common_risk_aubrc"]) for seed in range(10)]
            )
            diff = base - stable
            p_value = float(wilcoxon(diff, alternative="two-sided").pvalue)
            low, high = bootstrap_ci(diff, samples, seed=20260706)
            row = {
                "customer_set": customer_set,
                "baseline": baseline,
                "comparison": STABLE,
                "baseline_minus_stable_aubrc_mean": float(diff.mean()),
                "relative_aubrc_reduction": float(diff.mean() / (base.mean() + 1e-12)),
                "bootstrap_ci_low": low,
                "bootstrap_ci_high": high,
                "wilcoxon_p": p_value,
            }
            block.append(row)
            p_values.append(p_value)
        for row, p_adj in zip(block, holm_adjust(p_values)):
            row["holm_p"] = p_adj
            row["significant_0p05"] = p_adj < 0.05
            result.append(row)
    return result


def write_report(
    path: Path,
    node_rows: list[dict[str, str]],
    ablation_rows: list[dict[str, str]],
    od_rows: list[dict[str, str]],
    budget_rows: list[dict[str, object]],
    sig_rows: list[dict[str, object]],
    auc_rows: list[dict[str, object]],
    win_rows: list[dict[str, object]],
    auc_sig_rows: list[dict[str, object]],
) -> None:
    lines = [
        "# Paper model comparison: final 10-seed results",
        "",
        "All downstream cross-model risk values below use the same common reference risk matrix.",
        "",
        "## Node-risk evaluation (Split B)",
        "",
        "| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in node_rows:
        lines.append(
            f"| {row['model']} | {row['Macro-F1']} | {row['MAE']} | {row['QWK']} | "
            f"{row['Recall@6-8']} | {row['PR-AUC']} | {row['High FN']} |"
        )
    lines.extend(["", "## Structure and loss ablation", "", "| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |", "|---|---:|---:|---:|---:|---:|---:|"])
    for row in ablation_rows:
        lines.append(
            f"| {row['model']} | {row['Macro-F1']} | {row['MAE']} | {row['QWK']} | "
            f"{row['Recall@6-8']} | {row['PR-AUC']} | {row['High FN']} |"
        )

    lines.extend(
        [
            "",
            "## Fixed-budget common-risk comparison",
            "",
            "| Set | Budget | Model | Cost inc. | Common risk | CVaR90 | CVaR95 | Max edge risk |",
            "|---|---:|---|---:|---:|---:|---:|---:|",
        ]
    )
    for customer_set in ("A", "B"):
        for budget in (0.20, 0.25, 0.30):
            rows = [row for row in budget_rows if row["customer_set"] == customer_set and row["budget"] == budget]
            for row in sorted(rows, key=lambda item: MODEL_ORDER.index(str(item["model"]))):
                lines.append(
                    f"| {customer_set} | {budget:.0%} | {row['model']} | "
                    f"{float(row['cost_increase_mean']):.2%} | {float(row['common_global_risk_mean_mean']):.4f} | "
                    f"{float(row['common_global_cvar90_mean_mean']):.4f} | "
                    f"{float(row['common_global_cvar95_mean_mean']):.4f} | "
                    f"{float(row['common_max_edge_risk_mean_mean']):.4f} |"
                )

    lines.extend(
        [
            "",
            "## Extended downstream metrics at B=20%",
            "",
            "| Set | Model | LoadRisk | Load CVaR90 | Load CVaR95 | Max vehicle risk | Max vehicle CVaR90 | Top10 burden share | Edge burden Gini |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for customer_set in ("A", "B"):
        rows = [row for row in budget_rows if row["customer_set"] == customer_set and row["budget"] == 0.20]
        for row in sorted(rows, key=lambda item: MODEL_ORDER.index(str(item["model"]))):
            lines.append(
                f"| {customer_set} | {row['model']} | {float(row['load_global_risk_mean_mean']):.4f} | "
                f"{float(row['load_cvar90_mean_mean']):.4f} | "
                f"{float(row['load_cvar95_mean_mean']):.4f} | "
                f"{float(row['common_max_vehicle_risk_mean_mean']):.4f} | "
                f"{float(row['common_max_vehicle_cvar90_mean_mean']):.4f} | "
                f"{float(row['common_top10_burden_share_mean_mean']):.2%} | "
                f"{float(row['common_edge_burden_gini_used_mean_mean']):.4f} |"
            )

    lines.extend(["", "## OD path validation (CVaR-risk)", "", "| Model | Hop inc. | Total risk reduction | CVaR90 reduction |", "|---|---:|---:|---:|"])
    for row in od_rows:
        if row["method"] == "CVaR-risk":
            lines.append(
                f"| {MODEL_DISPLAY.get(row['model'], row['model'])} | {float(row['hop_increase_mean']):.2%} | "
                f"{float(row['total_risk_reduction_mean']):.2%} | {float(row['cvar90_reduction_mean']):.2%} |"
            )

    lines.extend(
        [
            "",
            "## Cost-risk AUBRC over 0-40% budget",
            "",
            "Lower is better; each curve is the lower envelope of observed beta candidates.",
            "",
            "| Set | Model | Common risk AUBRC | CVaR90 AUBRC | CVaR95 AUBRC | LoadRisk AUBRC | Load CVaR90 AUBRC | Max-vehicle risk AUBRC | Max-vehicle CVaR90 AUBRC |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for customer_set in ("A", "B"):
        rows = [row for row in auc_rows if row["customer_set"] == customer_set]
        for row in sorted(rows, key=lambda item: MODEL_ORDER.index(str(item["model"]))):
            lines.append(
                f"| {customer_set} | {row['model']} | {float(row['common_risk_aubrc_mean']):.4f} | "
                f"{float(row['cvar90_aubrc_mean']):.4f} | {float(row['cvar95_aubrc_mean']):.4f} | "
                f"{float(row['load_risk_aubrc_mean']):.4f} | {float(row['load_cvar90_aubrc_mean']):.4f} | "
                f"{float(row['max_vehicle_risk_aubrc_mean']):.4f} | "
                f"{float(row['max_vehicle_cvar90_aubrc_mean']):.4f} |"
            )

    lines.extend(["", "## Budget sweep: 10%-40%", "", "A win is the lowest common risk for the same model seed, customer set, and budget.", "", "| Set | Model | Wins | Comparisons | Win rate | Average Risk@B |", "|---|---|---:|---:|---:|---:|"])
    for row in win_rows:
        lines.append(
            f"| {row['customer_set']} | {row['model']} | {row['wins']} | {row['comparisons']} | "
            f"{float(row['win_rate']):.2%} | {float(row['average_common_risk_at_b']):.4f} |"
        )

    lines.extend(["", "## AUBRC paired significance", "", "Positive difference means Stable-Tail GNN has lower AUBRC.", "", "| Set | Baseline | Baseline - Stable | Relative reduction | 95% CI | Holm p |", "|---|---|---:|---:|---:|---:|"])
    for row in auc_sig_rows:
        lines.append(
            f"| {row['customer_set']} | {row['baseline']} | {float(row['baseline_minus_stable_aubrc_mean']):.4f} | "
            f"{float(row['relative_aubrc_reduction']):.2%} | [{float(row['bootstrap_ci_low']):.4f}, "
            f"{float(row['bootstrap_ci_high']):.4f}] | {float(row['holm_p']):.4g} |"
        )

    lines.extend(["", "## Paired significance at Risk@20", "", "Positive difference means Stable-Tail GNN has lower common risk.", "", "| Set | Baseline | Baseline - Stable | Relative reduction | 95% CI | Holm p |", "|---|---|---:|---:|---:|---:|"])
    for row in sig_rows:
        if float(row["budget"]) == 0.20:
            lines.append(
                f"| {row['customer_set']} | {row['baseline']} | {float(row['baseline_minus_stable_mean']):.4f} | "
                f"{float(row['relative_risk_reduction']):.2%} | [{float(row['bootstrap_ci_low']):.4f}, "
                f"{float(row['bootstrap_ci_high']):.4f}] | {float(row['holm_p']):.4g} |"
            )

    lines.extend(
        [
            "",
            "## Interpretation guardrails",
            "",
            "- Node classification and downstream route safety are related but distinct objectives.",
            "- Cross-model route claims must use the common-risk tables, not each model's self-evaluation scale.",
            "- The budget selector chooses the lowest-common-risk observed beta candidate feasible under each cost budget.",
            "- Statistical tests pair identical model-seed indices; bootstrap intervals use 10,000 resamples by default.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    node_rows = read_csv(args.node)
    node_rows.extend(strong_node_table(read_csv(args.strong_node)))
    ablation_rows = read_csv(args.ablation)
    od_rows = [*read_csv(args.od), *read_csv(args.strong_od)]
    self_rows = [*read_csv(args.self_summary), *read_csv(args.strong_self_summary)]
    common_rows = read_csv(args.common_summary)
    load_rows = read_csv(args.load_summary)
    joined = load_joined(self_rows, common_rows, load_rows)
    selected = select_budgets(joined)
    budget_summary = summarize_budgets(selected)
    sig_rows = significance(selected, args.bootstrap_samples)
    targeted_sig_rows = targeted_significance(selected, args.bootstrap_samples)
    beta1_rows = beta_one_summary(joined)
    auc_detail, auc_summary = cost_risk_auc(joined)
    win_rows = budget_win_rates(selected)
    auc_sig_rows = auc_significance(auc_detail, args.bootstrap_samples)
    model_summary = all_model_summary(
        node_rows, ablation_rows, od_rows, budget_summary, auc_summary, win_rows
    )

    write_csv(
        args.output_dir / "upstream_node_metrics_all_models.csv",
        [
            {
                key: row[key]
                for key in (
                    "model",
                    "macro_f1",
                    "mae",
                    "qwk",
                    "pr_auc",
                    "recall_at_6_8",
                    "high_fn",
                )
            }
            for row in model_summary
        ],
    )
    write_csv(args.output_dir / "all_models_summary.csv", model_summary)
    write_csv(args.output_dir / "common_cost_risk_joined.csv", joined)
    write_csv(args.output_dir / "fixed_budget_risk_detail.csv", selected)
    write_csv(args.output_dir / "fixed_budget_risk_summary.csv", budget_summary)
    write_csv(
        args.output_dir / "extended_downstream_metrics_10_40.csv",
        budget_summary,
    )
    write_csv(args.output_dir / "paired_significance_holm.csv", sig_rows)
    write_csv(
        args.output_dir / "targeted_common_cvar_significance.csv",
        targeted_sig_rows,
    )
    write_csv(args.output_dir / "beta1_common_comparison.csv", beta1_rows)
    write_csv(args.output_dir / "cost_risk_aubrc_detail.csv", auc_detail)
    write_csv(args.output_dir / "cost_risk_aubrc_summary.csv", auc_summary)
    write_csv(args.output_dir / "budget_win_rates.csv", win_rows)
    write_csv(args.output_dir / "auc_paired_significance_holm.csv", auc_sig_rows)
    write_report(
        args.output_dir / "final_comparison_report.md",
        node_rows,
        ablation_rows,
        od_rows,
        budget_summary,
        sig_rows,
        auc_summary,
        win_rows,
        auc_sig_rows,
    )
    integrity = {
        "node_rows": len(node_rows),
        "ablation_rows": len(ablation_rows),
        "od_rows": len(od_rows),
        "self_rows": len(self_rows),
        "common_rows": len(common_rows),
        "load_rows": len(load_rows),
        "joined_rows": len(joined),
        "fixed_budget_detail_rows": len(selected),
        "fixed_budget_summary_rows": len(budget_summary),
        "significance_rows": len(sig_rows),
        "targeted_significance_rows": len(targeted_sig_rows),
        "cost_risk_auc_detail_rows": len(auc_detail),
        "cost_risk_auc_summary_rows": len(auc_summary),
        "auc_significance_rows": len(auc_sig_rows),
        "all_models_summary_rows": len(model_summary),
        "models": sorted({str(row["model"]) for row in joined}),
        "model_seeds": sorted({int(row["model_seed"]) for row in joined}),
        "customer_sets": sorted({str(row["customer_set"]) for row in joined}),
        "betas": sorted({float(row["beta"]) for row in joined}),
    }
    (args.output_dir / "integrity.json").write_text(
        json.dumps(integrity, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote final comparison package to {args.output_dir}")
    print(json.dumps(integrity, ensure_ascii=False))


if __name__ == "__main__":
    main()
