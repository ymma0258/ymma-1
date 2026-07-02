"""Create B=20 baseline table, Pareto plots, and Budgeted Risk Scores."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


POOL_NAMES = {
    "GCN-only pool": "GCN",
    "TEG-low-only pool": "TEG-low",
    "Stable-Tail-only pool": "Stable-Tail-GNN",
    "three-model pool": "J-full",
    "three-model + multi-eta pool": "Three-model + multi-eta",
}
METRICS = {
    "common_global_risk_mean": ("CommonRisk", "Common risk"),
    "common_global_cvar90_mean": ("CVaR90", "CVaR90"),
    "load_global_risk_mean": ("LoadRisk", "Load risk"),
    "common_top10_burden_share_mean": ("Top10Share", "Top-10% burden share"),
}
WEIGHTS = {
    "common_global_risk_mean": 1.0,
    "common_global_cvar90_mean": 2.0,
    "load_global_risk_mean": 1.0,
    "common_top10_burden_share_mean": 0.5,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool-summary", type=Path, required=True)
    parser.add_argument("--weight-summary", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def add_brs(frame: pd.DataFrame, method_column: str) -> pd.DataFrame:
    """Normalize within each set-budget cell, then average weighted risk over B."""

    data = frame.copy()
    components = []
    for column, weight in WEIGHTS.items():
        group = data.groupby(["customer_set", "budget"])[column]
        low = group.transform("min")
        span = group.transform("max") - low
        norm_column = f"{column}_norm"
        data[norm_column] = np.where(span > 1e-12, (data[column] - low) / span, 0.0)
        components.append(weight * data[norm_column])
    data["budget_risk_component"] = sum(components)
    by_set = (
        data.groupby([method_column, "customer_set"], as_index=False)["budget_risk_component"]
        .mean()
        .rename(columns={"budget_risk_component": "BRS"})
    )
    overall = by_set.groupby(method_column, as_index=False)["BRS"].mean()
    overall["customer_set"] = "Overall"
    return pd.concat([by_set, overall], ignore_index=True)


def markdown_table(path: Path, title: str, frame: pd.DataFrame) -> None:
    columns = list(frame.columns)
    lines = [f"# {title}", "", "| " + " | ".join(columns) + " |", "|" + "---:|" * len(columns)]
    for _, row in frame.iterrows():
        values = []
        for column in columns:
            value = row[column]
            values.append(f"{value:.5f}" if isinstance(value, (float, np.floating)) else str(value))
        lines.append("| " + " | ".join(values) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def plot_curves(data: pd.DataFrame, output_dir: Path) -> None:
    colors = {
        "GCN": "#4C78A8",
        "TEG-low": "#F58518",
        "Stable-Tail-GNN": "#54A24B",
        "J-full": "#E45756",
        "Three-model + multi-eta": "#7A5195",
    }
    markers = ["o", "s", "^", "D", "P"]
    fig, axes = plt.subplots(2, 4, figsize=(17.5, 7.8), constrained_layout=True)
    for row_idx, customer_set in enumerate(["A", "B"]):
        for col_idx, (column, (_, ylabel)) in enumerate(METRICS.items()):
            ax = axes[row_idx, col_idx]
            for marker, method in zip(markers, POOL_NAMES.values()):
                group = data[
                    (data["method"] == method) & (data["customer_set"] == customer_set)
                ].sort_values("budget")
                ax.plot(
                    100.0 * group["cost_increase_pct_mean"],
                    group[column],
                    marker=marker,
                    linewidth=2.0,
                    markersize=6,
                    color=colors[method],
                    label=method,
                )
            ax.set_xlabel("Cost increase (%)")
            ax.set_ylabel(ylabel)
            ax.set_title(f"Set {customer_set}: {ylabel}")
            ax.grid(True, alpha=0.25)
    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(
        handles,
        labels,
        loc="center left",
        bbox_to_anchor=(1.005, 0.5),
        ncol=1,
        frameon=False,
    )
    fig.suptitle("Cost-risk trade-offs under B = 20%, 25%, and 30%", fontsize=15)
    fig.savefig(output_dir / "pareto_cost_risk_curves.png", dpi=300, bbox_inches="tight")
    fig.savefig(output_dir / "pareto_cost_risk_curves.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pools = pd.read_csv(args.pool_summary)
    pools = pools[pools["route_pool"].isin(POOL_NAMES)].copy()
    pools["method"] = pools["route_pool"].map(POOL_NAMES)
    pools.to_csv(args.output_dir / "pareto_curve_data.csv", index=False)

    b20 = pools[pools["budget"] == 0.20][
        ["method", "customer_set", "cost_increase_pct_mean", *METRICS]
    ].sort_values(["customer_set", "method"])
    b20.to_csv(args.output_dir / "budget20_baseline_table.csv", index=False)
    markdown_table(args.output_dir / "budget20_baseline_table.md", "B=20% Baseline Comparison", b20)

    pool_brs = add_brs(pools, "method").sort_values(["customer_set", "BRS"])
    pool_brs.to_csv(args.output_dir / "budgeted_risk_score.csv", index=False)
    markdown_table(args.output_dir / "budgeted_risk_score.md", "Budgeted Risk Score", pool_brs)

    weights = pd.read_csv(args.weight_summary)
    weight_brs = add_brs(weights, "weight_setting").sort_values(["customer_set", "BRS"])
    weight_brs.to_csv(args.output_dir / "j_weight_sensitivity_brs.csv", index=False)
    markdown_table(
        args.output_dir / "j_weight_sensitivity_brs.md",
        "J Weight Sensitivity BRS",
        weight_brs,
    )
    single_pools = pools[pools["method"].isin(["GCN", "TEG-low", "Stable-Tail-GNN"])].copy()
    weight_methods = weights.rename(columns={"weight_setting": "method"})
    comparable = pd.concat([single_pools, weight_methods], ignore_index=True, sort=False)
    comparable_brs = add_brs(comparable, "method").sort_values(["customer_set", "BRS"])
    comparable_brs.to_csv(
        args.output_dir / "j_weights_vs_single_pools_brs.csv", index=False
    )
    markdown_table(
        args.output_dir / "j_weights_vs_single_pools_brs.md",
        "J Weights versus Single-model Pools",
        comparable_brs,
    )
    plot_curves(pools, args.output_dir)
    print(f"Wrote budget-risk analysis to {args.output_dir}")


if __name__ == "__main__":
    main()
