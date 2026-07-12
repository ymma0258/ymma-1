"""Create B=20 baseline table, Pareto plots, and Budgeted Risk Scores."""

from __future__ import annotations

import argparse
import re
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
    parser.add_argument("--pool-detail", type=Path, required=True)
    parser.add_argument("--weight-summary", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def route_source(value: str) -> str:
    if re.search(r"(?:^|_)GCN_seed\d+$", value):
        return "GCN"
    if "TEG-low" in value:
        return "TEG-low"
    if "Stable-Tail-GNN" in value or "Stable-Tail-eta" in value:
        return "Stable-Tail-GNN"
    raise ValueError(f"Unknown route source: {value}")


def write_bjr_source_statistics(detail: pd.DataFrame, output_dir: Path) -> None:
    selected = detail[detail["route_pool"] == "three-model + multi-eta pool"].copy()
    selected["route_source"] = selected["risk_source"].map(route_source)
    total = len(selected)
    if total != 60:
        raise ValueError(f"Expected 60 Multi-BJR selections, found {total}")
    stats = (
        selected.groupby("route_source", as_index=False)
        .agg(
            selected_count=("risk_source", "size"),
            common_risk_mean=("common_global_risk", "mean"),
            cvar90_mean=("common_global_cvar90", "mean"),
            load_risk_mean=("load_global_risk", "mean"),
        )
        .set_index("route_source")
        .reindex(["GCN", "TEG-low", "Stable-Tail-GNN"])
        .reset_index()
    )
    stats["share"] = stats["selected_count"] / total
    stats = stats[
        [
            "route_source",
            "selected_count",
            "share",
            "common_risk_mean",
            "cvar90_mean",
            "load_risk_mean",
        ]
    ]
    stats.to_csv(output_dir / "bjr_route_source_statistics.csv", index=False)
    lines = [
        "# Multi-BJR Route-source Statistics",
        "",
        "| 路线来源 | 被 BJR 选中次数 | 占比 | 平均 CommonRisk | 平均 CVaR90 | 平均 LoadRisk |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for _, row in stats.iterrows():
        lines.append(
            f"| {row['route_source']} | {int(row['selected_count'])} | {row['share']:.1%} | "
            f"{row['common_risk_mean']:.4f} | {row['cvar90_mean']:.5f} | "
            f"{row['load_risk_mean']:.4f} |"
        )
    lines.extend(
        [
            "",
            "注：",
            "",
            "1. BJR 指 Budget-constrained J Reranking；所有候选路线均使用同一公共风险矩阵重新评价。",
            "2. 统计样本为 Set A/B × B={20%,25%,30%} × 10 个求解种子，共 60 次最终选择。",
            "3. Stable-Tail-GNN 包含基础 Stable-Tail 路线及 eta=0.3/0.5/0.7 的尾部增强路线。",
            "4. 三项风险指标均为越低越好；占比反映候选路线互补性，不代表模型训练样本比例。",
            "5. 各来源平均风险是对该来源实际被选中路线的条件均值，受 Set 与预算构成影响；来源间的公平效果比较应以固定 J 的路线池消融表为准。",
        ]
    )
    (output_dir / "bjr_route_source_statistics.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def write_bjr_pool_ablation(pools: pd.DataFrame, output_dir: Path) -> None:
    definitions = {
        "GCN-only pool": (
            "GCN-BJR",
            "只用 GCN 路线",
            "固定 J: (1,2,1,0.5)",
            "GCN 路线池效果",
        ),
        "TEG-low-only pool": (
            "TEG-BJR",
            "只用 TEG-low 路线",
            "固定 J: (1,2,1,0.5)",
            "TEG-low 路线池效果",
        ),
        "Stable-Tail-only pool": (
            "Stable-BJR",
            "只用 Stable-Tail 路线",
            "固定 J: (1,2,1,0.5)",
            "Stable-Tail 路线池效果",
        ),
        "three-model + multi-eta pool": (
            "Multi-BJR",
            "三模型 + 多 eta 路线",
            "固定 J: (1,2,1,0.5)",
            "多源候选路线互补效果",
        ),
    }
    ablation = pools[pools["route_pool"].isin(definitions)].copy()
    ablation["setting"] = ablation["route_pool"].map(lambda name: definitions[name][0])
    ablation["candidate_pool"] = ablation["route_pool"].map(lambda name: definitions[name][1])
    ablation["selection_rule"] = ablation["route_pool"].map(lambda name: definitions[name][2])
    ablation["evidence"] = ablation["route_pool"].map(lambda name: definitions[name][3])
    detail_columns = [
        "setting",
        "candidate_pool",
        "selection_rule",
        "evidence",
        "customer_set",
        "budget",
        "cost_increase_pct_mean",
        *METRICS,
    ]
    ablation[detail_columns].to_csv(
        output_dir / "bjr_pool_source_ablation_detail.csv", index=False
    )
    overall = (
        ablation.groupby(
            ["setting", "candidate_pool", "selection_rule", "evidence"], as_index=False
        )[["cost_increase_pct_mean", *METRICS]]
        .mean()
    )
    order = ["GCN-BJR", "TEG-BJR", "Stable-BJR", "Multi-BJR"]
    overall["_order"] = overall["setting"].map({name: idx for idx, name in enumerate(order)})
    overall = overall.sort_values("_order").drop(columns="_order")
    overall.to_csv(output_dir / "bjr_pool_source_ablation_overall.csv", index=False)

    lines = [
        "# BJR Route-pool Source Ablation",
        "",
        "## 实验设置",
        "",
        "| 设置 | 候选池 | 选择规则 | 证明内容 |",
        "|---|---|---|---|",
    ]
    for _, row in overall.iterrows():
        lines.append(
            f"| {row['setting']} | {row['candidate_pool']} | {row['selection_rule']} | {row['evidence']} |"
        )
    lines.extend(
        [
            "",
            "## 总体结果（Set A/B 与三个预算等权平均）",
            "",
            "| 设置 | CostInc | CommonRisk | CVaR90 | LoadRisk | Top10Share |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for _, row in overall.iterrows():
        lines.append(
            f"| {row['setting']} | {row['cost_increase_pct_mean']:.2%} | "
            f"{row['common_global_risk_mean']:.4f} | {row['common_global_cvar90_mean']:.5f} | "
            f"{row['load_global_risk_mean']:.4f} | {row['common_top10_burden_share_mean']:.2%} |"
        )
    lines.extend(
        [
            "",
            "注：四组实验使用完全相同的预算约束、公共评价矩阵、归一化方式和 J 权重；唯一变化是候选路线池来源。",
        ]
    )
    (output_dir / "bjr_pool_source_ablation.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


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
    detail = pd.read_csv(args.pool_detail)
    write_bjr_source_statistics(detail, args.output_dir)
    write_bjr_pool_ablation(pools, args.output_dir)
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
