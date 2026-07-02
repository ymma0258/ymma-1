"""Hierarchical paired tests for Risk@B and J-reranking experiments."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import ttest_rel, wilcoxon


METRICS = ["common_risk", "cvar90", "load_risk", "top10share"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--risk-raw", type=Path, required=True)
    parser.add_argument("--j-raw", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--budgets", default="25,30")
    parser.add_argument("--n-boot", type=int, default=10000)
    parser.add_argument("--bootstrap-seed", type=int, default=42)
    return parser.parse_args()


def holm_bonferroni(p_values: np.ndarray) -> np.ndarray:
    p_values = np.asarray(p_values, dtype=float)
    order = np.argsort(p_values)
    adjusted = np.empty(p_values.size, dtype=float)
    previous = 0.0
    for rank, idx in enumerate(order):
        current = max(previous, (p_values.size - rank) * p_values[idx])
        adjusted[idx] = min(current, 1.0)
        previous = adjusted[idx]
    return adjusted


def bootstrap_ci(
    values: np.ndarray, n_boot: int, alpha: float, rng: np.random.Generator
) -> tuple[float, float]:
    samples = rng.choice(values, size=(n_boot, values.size), replace=True).mean(axis=1)
    return tuple(np.quantile(samples, [alpha / 2.0, 1.0 - alpha / 2.0]))


def aggregate_solver_seeds(df: pd.DataFrame) -> pd.DataFrame:
    keys = ["set", "budget", "method", "model_seed"]
    counts = df.groupby(keys)["solver_seed"].nunique()
    if not bool((counts == 10).all()):
        raise ValueError(f"Every model-seed cell must contain 10 solver seeds:\n{counts[counts != 10]}")
    result = df.groupby(keys, as_index=False)[METRICS + ["cost_inc"]].mean()
    model_counts = result.groupby(["set", "budget", "method"])["model_seed"].nunique()
    if not bool((model_counts == 10).all()):
        raise ValueError(f"Every method cell must contain 10 model seeds:\n{model_counts}")
    return result


def paired_compare(
    seed_df: pd.DataFrame,
    set_name: str,
    budget: int,
    method: str,
    baseline: str,
    metric: str,
    n_boot: int,
    rng: np.random.Generator,
) -> dict[str, object]:
    sub = seed_df[
        (seed_df["set"] == set_name)
        & (seed_df["budget"] == budget)
        & (seed_df["method"].isin([method, baseline]))
    ]
    wide = sub.pivot(index="model_seed", columns="method", values=metric).dropna()
    if set(wide.columns) != {method, baseline} or len(wide) != 10:
        raise ValueError(
            f"Incomplete pair: set={set_name}, B={budget}, {method} vs {baseline}, metric={metric}"
        )
    method_values = wide[method].to_numpy(dtype=float)
    baseline_values = wide[baseline].to_numpy(dtype=float)
    delta = baseline_values - method_values
    if np.allclose(delta, 0.0):
        p_wilcoxon = 1.0
        p_ttest = 1.0
    else:
        p_wilcoxon = float(wilcoxon(delta, alternative="two-sided").pvalue)
        p_ttest = float(ttest_rel(baseline_values, method_values).pvalue)
    delta_std = float(np.std(delta, ddof=1))
    ci_low, ci_high = bootstrap_ci(delta, n_boot, 0.05, rng)
    baseline_mean = float(np.mean(baseline_values))
    method_mean = float(np.mean(method_values))
    mean_delta = float(np.mean(delta))
    return {
        "set": set_name,
        "budget": budget,
        "metric": metric,
        "method": method,
        "baseline": baseline,
        "n_model_seeds": len(delta),
        "baseline_mean": baseline_mean,
        "method_mean": method_mean,
        "mean_delta": mean_delta,
        "relative_improve_pct": 100.0 * mean_delta / baseline_mean,
        "ci95_low": ci_low,
        "ci95_high": ci_high,
        "p_wilcoxon": p_wilcoxon,
        "p_ttest": p_ttest,
        "cohen_dz": mean_delta / delta_std if delta_std > 0 else np.nan,
        "wins": int(np.sum(delta > 0)),
        "ties": int(np.sum(np.isclose(delta, 0.0))),
    }


def write_main_markdown(path: Path, risk_stats: pd.DataFrame, j_stats: pd.DataFrame) -> None:
    lines = [
        "# Hierarchical Significance Tests",
        "",
        "Tests use n=10 paired model-seed means after averaging the 10 solver seeds within each model seed.",
        "",
        "## Risk@B: Stable-Tail-GNN vs baselines",
        "",
        "| Set | B | Baseline | Reduction | 95% CI of delta | Wilcoxon p_adj | Cohen dz |",
        "|---|---:|---|---:|---:|---:|---:|",
    ]
    for _, row in risk_stats.iterrows():
        lines.append(
            f"| {row['set']} | {int(row['budget'])}% | {row['baseline']} | "
            f"{row['relative_improve_pct']:.2f}% | [{row['ci95_low']:.4f}, {row['ci95_high']:.4f}] | "
            f"{row['p_wilcoxon_adj']:.4f} | {row['cohen_dz']:.3f} |"
        )
    lines.extend(
        [
            "",
            "## J-reranking vs Stable-Tail-GNN",
            "",
            "| Set | B | Metric | Stable-Tail | J-reranking | Reduction | p_adj | Cohen dz |",
            "|---|---:|---|---:|---:|---:|---:|---:|",
        ]
    )
    main_j = j_stats[j_stats["baseline"] == "Stable-Tail-GNN"]
    for _, row in main_j.iterrows():
        lines.append(
            f"| {row['set']} | {int(row['budget'])}% | {row['metric']} | "
            f"{row['baseline_mean']:.4f} | {row['method_mean']:.4f} | "
            f"{row['relative_improve_pct']:.2f}% | {row['p_wilcoxon_adj']:.4f} | "
            f"{row['cohen_dz']:.3f} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    budgets = [int(item.strip()) for item in args.budgets.split(",") if item.strip()]
    risk_raw = pd.read_csv(args.risk_raw)
    j_raw = pd.read_csv(args.j_raw)
    combined = pd.concat([risk_raw, j_raw], ignore_index=True)
    seed_df = aggregate_solver_seeds(combined)
    rng = np.random.default_rng(args.bootstrap_seed)

    risk_results = []
    for set_name in ["A", "B"]:
        for budget in budgets:
            for baseline in ["GCN", "TEG-low"]:
                risk_results.append(
                    paired_compare(
                        seed_df,
                        set_name,
                        budget,
                        "Stable-Tail-GNN",
                        baseline,
                        "common_risk",
                        args.n_boot,
                        rng,
                    )
                )
    risk_stats = pd.DataFrame(risk_results)
    risk_stats["p_wilcoxon_adj"] = holm_bonferroni(risk_stats["p_wilcoxon"].to_numpy())

    j_results = []
    for set_name in ["A", "B"]:
        for budget in budgets:
            for metric in METRICS:
                for baseline in ["Stable-Tail-GNN", "GCN", "TEG-low"]:
                    j_results.append(
                        paired_compare(
                            seed_df,
                            set_name,
                            budget,
                            "J-reranking",
                            baseline,
                            metric,
                            args.n_boot,
                            rng,
                        )
                    )
    j_stats = pd.DataFrame(j_results)
    j_stats["p_wilcoxon_adj"] = holm_bonferroni(j_stats["p_wilcoxon"].to_numpy())

    args.output_dir.mkdir(parents=True, exist_ok=True)
    seed_df.to_csv(args.output_dir / "model_seed_aggregated_results.csv", index=False)
    risk_stats.to_csv(
        args.output_dir / "riskB_significance_stable_vs_baselines.csv", index=False
    )
    j_stats.to_csv(args.output_dir / "j_reranking_significance.csv", index=False)
    write_main_markdown(args.output_dir / "significance_main_table.md", risk_stats, j_stats)
    print(f"Risk@B tests: {len(risk_stats)}; J tests: {len(j_stats)}")


if __name__ == "__main__":
    main()
