"""Create final paper figures for the Stable-Tail GNN experiments."""

from __future__ import annotations

import csv
import math
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs")
OUT_DIR = ROOT / "final_figures_stable_tail_gnn"
TABLE_DIR = OUT_DIR / "tables"
FIG_DIR = OUT_DIR / "figures"


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


def savefig(fig: plt.Figure, name: str) -> None:
    fig.tight_layout()
    fig.savefig(FIG_DIR / f"{name}.png", dpi=300, bbox_inches="tight")
    fig.savefig(FIG_DIR / f"{name}.svg", bbox_inches="tight")
    plt.close(fig)


def add_box(ax, xy, text, width=0.18, height=0.12, color="#e8f1ff"):
    x, y = xy
    rect = plt.Rectangle(
        (x - width / 2, y - height / 2),
        width,
        height,
        facecolor=color,
        edgecolor="#2f5597",
        linewidth=1.6,
        joinstyle="round",
    )
    ax.add_patch(rect)
    ax.text(x, y, text, ha="center", va="center", fontsize=9, wrap=True)


def add_arrow(ax, start, end):
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops=dict(arrowstyle="->", linewidth=1.5, color="#404040"),
    )


def fig1_framework() -> None:
    fig, ax = plt.subplots(figsize=(13, 3.6))
    ax.set_axis_off()
    steps = [
        "Vehicle\ntrajectory graph",
        "Stable-Tail\nGNN",
        "Node risk\nS_i",
        "floor_0.01\nedge risk R_ij",
        "OD path\nCVaR validation",
        "PyVRP-CVRP\ndownstream",
        "Risk / cost /\nfairness metrics",
    ]
    xs = np.linspace(0.08, 0.92, len(steps))
    colors = ["#e8f1ff", "#e8f6ef", "#fff2cc", "#fce4d6", "#e2f0d9", "#ddebf7", "#f4cccc"]
    for idx, (x, step) in enumerate(zip(xs, steps)):
        add_box(ax, (x, 0.55), step, width=0.13, height=0.22, color=colors[idx])
        if idx > 0:
            add_arrow(ax, (xs[idx - 1] + 0.07, 0.55), (x - 0.07, 0.55))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Overall Experimental Framework", fontsize=14, fontweight="bold")
    savefig(fig, "fig1_overall_experiment_framework")


def fig2_model_structure() -> None:
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.set_axis_off()
    add_box(ax, (0.5, 0.88), "Node features X", width=0.22, height=0.10, color="#fff2cc")
    add_box(ax, (0.28, 0.68), "GCN branch\nstable representation", width=0.24, height=0.13, color="#e8f1ff")
    add_box(ax, (0.72, 0.68), "TEG branch\nX + edge_attribute", width=0.24, height=0.13, color="#e8f6ef")
    add_box(ax, (0.28, 0.48), "H_gcn", width=0.16, height=0.10, color="#ddebf7")
    add_box(ax, (0.72, 0.48), "H_teg", width=0.16, height=0.10, color="#d9ead3")
    add_box(ax, (0.5, 0.30), "[H_gcn || H_teg]", width=0.24, height=0.10, color="#fce4d6")
    add_box(ax, (0.5, 0.15), "MLP classifier\np_i,1 ... p_i,8", width=0.25, height=0.12, color="#eadcf8")
    add_box(ax, (0.5, 0.02), "S_i and P_high", width=0.22, height=0.08, color="#f4cccc")
    add_arrow(ax, (0.45, 0.83), (0.32, 0.75))
    add_arrow(ax, (0.55, 0.83), (0.68, 0.75))
    add_arrow(ax, (0.28, 0.61), (0.28, 0.54))
    add_arrow(ax, (0.72, 0.61), (0.72, 0.54))
    add_arrow(ax, (0.34, 0.45), (0.43, 0.34))
    add_arrow(ax, (0.66, 0.45), (0.57, 0.34))
    add_arrow(ax, (0.5, 0.25), (0.5, 0.21))
    add_arrow(ax, (0.5, 0.09), (0.5, 0.06))
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.05, 1)
    ax.set_title("Stable-Tail GNN Model Structure", fontsize=14, fontweight="bold")
    savefig(fig, "fig2_stable_tail_gnn_structure")


def fig3_risk_distribution() -> None:
    dist_rows = read_csv(ROOT / "risk_matrices" / "risk_distribution_model_compare_2021" / "risk_distribution_summary.csv")
    mode_rows = read_csv(ROOT / "risk_matrices" / "risk_matrix_modes_2021" / "risk_matrix_diagnostics.csv")
    for row in dist_rows:
        row["tail_gap"] = float(row["p99"]) - float(row["p95"])
    models = [row["risk_matrix"] for row in dist_rows]
    fig, axes = plt.subplots(2, 1, figsize=(14.5, 9.2))

    quantile_metrics = ["p90", "p95", "p99", "max"]
    quantile_labels = ["P90", "P95", "P99", "Max"]
    x = np.arange(len(models))
    width = 0.18
    for i, metric in enumerate(quantile_metrics):
        axes[0].bar(
            x + (i - 1.5) * width,
            [float(row[metric]) for row in dist_rows],
            width,
            label=quantile_labels[i],
        )
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(models, rotation=22, ha="right")
    axes[0].set_ylabel("Edge risk R_ij")
    axes[0].set_title("Figure 3-1: Risk quantile bars")
    axes[0].grid(axis="y", alpha=0.25)
    axes[0].legend(frameon=False, fontsize=9, ncol=4)

    tail_metrics = ["tail_gap", "std", "mean"]
    tail_labels = ["TailGap (P99-P95)", "Std", "Mean"]
    width = 0.22
    for i, metric in enumerate(tail_metrics):
        axes[1].bar(
            x + (i - 1) * width,
            [float(row[metric]) for row in dist_rows],
            width,
            label=tail_labels[i].replace("\n", " "),
        )
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(models, rotation=22, ha="right")
    axes[1].set_ylabel("Risk value")
    axes[1].set_title("Figure 3-2: Tail concentration bars")
    axes[1].legend(frameon=False, fontsize=8)
    axes[1].grid(axis="y", alpha=0.25)

    mode_keep = [
        row
        for row in mode_rows
        if any(key in row["risk_version"] for key in ["raw", "floor_0p001", "floor_0p01", "floor_0p05"])
        and "positive_only" not in row["risk_version"]
    ]
    labels = []
    zero = []
    p75 = []
    p90 = []
    for row in mode_keep:
        version = row["risk_version"]
        if version.endswith("raw"):
            label = "raw"
        elif "floor_0p001" in version:
            label = "floor_0.001"
        elif "floor_0p01" in version:
            label = "floor_0.01"
        elif "floor_0p05" in version:
            label = "floor_0.05"
        else:
            continue
        labels.append(label)
        zero.append(float(row["zero_risk_edge_ratio"]))
        p75.append(float(row["risk_p75"]))
        p90.append(float(row["risk_p90"]))
    order = ["raw", "floor_0.001", "floor_0.01", "floor_0.05"]
    idx = [labels.index(label) for label in order if label in labels]
    labels = [labels[i] for i in idx]
    zero = [zero[i] for i in idx]
    p75 = [p75[i] for i in idx]
    p90 = [p90[i] for i in idx]
    xx = np.arange(len(labels))
    axes[1].bar(xx - 0.2, zero, 0.4, label="Zero-risk ratio")
    axes[1].bar(xx + 0.2, p90, 0.4, label="Risk P90")
    axes[1].set_xticks(xx)
    axes[1].set_xticklabels(labels, rotation=15, ha="right")
    axes[1].set_title("Raw degeneration and exposure floor")
    axes[1].set_ylabel("Ratio / risk value")
    axes[1].legend(frameon=False)

    write_csv(TABLE_DIR / "fig3_risk_distribution_data.csv", dist_rows)
    write_csv(
        TABLE_DIR / "fig3_tail_concentration_data.csv",
        [
            {
                "risk_matrix": row["risk_matrix"],
                "mean": row["mean"],
                "std": row["std"],
                "p95": row["p95"],
                "p99": row["p99"],
                "tail_gap": row["tail_gap"],
                "max": row["max"],
            }
            for row in dist_rows
        ],
    )
    write_csv(
        TABLE_DIR / "fig3_floor_diagnostics_data.csv",
        [
            {"risk_mode": labels[i], "zero_risk_ratio": zero[i], "risk_p75": p75[i], "risk_p90": p90[i]}
            for i in range(len(labels))
        ],
    )
    savefig(fig, "fig3_risk_matrix_distribution")


def fig4_od_path_comparison() -> None:
    cvar = read_csv(ROOT / "od_paths" / "od_formal_floor001_p50_k50_cached_floor_0p01_a0p9_l0_p75" / "od_path_summary.csv")
    conc = read_csv(ROOT / "od_paths" / "od_formal_floor001_p50_k50_cached_floor_0p01_a0p9_l1_p75" / "od_path_summary.csv")
    rows = []
    for label, source_rows in [("CVaR-risk", cvar), ("CVaR+Concentration", conc)]:
        row = next(item for item in source_rows if item["method"] == "CVaR-risk" or item["method"] == "CVaR+Concentration")
        if label == "CVaR+Concentration":
            row = next(item for item in source_rows if item["method"] == "CVaR+Concentration")
        else:
            row = next(item for item in source_rows if item["method"] == "CVaR-risk")
        rows.append(
            {
                "method": label,
                "hop_increase": float(row["hop_increase_pct_mean"]),
                "total_risk_reduction": float(row["total_risk_aggregate_reduction"]),
                "cvar90_reduction": float(row["cvar90_aggregate_reduction"]),
                "re_reduction": float(row["re_aggregate_reduction"]),
            }
        )
    metrics = ["hop_increase", "total_risk_reduction", "cvar90_reduction", "re_reduction"]
    labels = ["Hop inc.", "Total risk red.", "CVaR90 red.", "RE red."]
    x = np.arange(len(metrics))
    width = 0.35
    fig, ax = plt.subplots(figsize=(9, 5))
    for i, row in enumerate(rows):
        ax.bar(x + (i - 0.5) * width, [row[m] * 100 for m in metrics], width, label=row["method"])
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=10)
    ax.set_ylabel("Percent (%)")
    ax.set_title("OD path validation: tail risk and concentration")
    ax.legend(frameon=False)
    ax.axhline(0, color="#666666", linewidth=0.8)
    write_csv(TABLE_DIR / "fig4_od_path_comparison_data.csv", rows)
    savefig(fig, "fig4_od_path_comparison")


def fig5_beta_tradeoff() -> None:
    rows = read_csv(ROOT / "pyvrp_cvrp" / "stable_tail_pyvrp50_beta_curve_fixedAB" / "model_pyvrp_summary.csv")
    data = {}
    for set_name in ["A", "B"]:
        data[set_name] = sorted(
            [row for row in rows if row["customer_set"] == set_name],
            key=lambda row: float(row["beta"]),
        )
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
    for set_name, marker in [("A", "o"), ("B", "s")]:
        subset = data[set_name]
        axes[0].plot(
            [float(row["cost_increase_pct"]) * 100 for row in subset],
            [float(row["risk_reduction_pct"]) * 100 for row in subset],
            marker=marker,
            label=f"Set {set_name}",
        )
        axes[1].plot(
            [float(row["beta"]) for row in subset],
            [float(row["global_cvar90_mean"]) for row in subset],
            marker=marker,
            label=f"Set {set_name}",
        )
        axes[2].plot(
            [float(row["beta"]) for row in subset],
            [float(row["edge_burden_gini_used_mean"]) for row in subset],
            marker=marker,
            label=f"Set {set_name}",
        )
    axes[0].set_xlabel("Cost increase (%)")
    axes[0].set_ylabel("Risk reduction (%)")
    axes[0].set_title("Cost-risk tradeoff")
    axes[1].set_xlabel("Beta")
    axes[1].set_ylabel("Global CVaR90")
    axes[1].set_title("Beta vs CVaR90")
    axes[2].set_xlabel("Beta")
    axes[2].set_ylabel("Edge Burden Gini")
    axes[2].set_title("Beta vs edge burden")
    for ax in axes:
        ax.grid(alpha=0.25)
        ax.legend(frameon=False)
    write_csv(TABLE_DIR / "fig5_pyvrp_beta_curve_data.csv", rows)
    savefig(fig, "fig5_pyvrp_beta_tradeoff")


def fig6_concentration_improvement() -> None:
    rows = read_csv(ROOT / "pyvrp_cvrp" / "common_eval_concat_concentration_lambda0_1_ensemble4" / "common_route_summary.csv")
    by_set = {}
    for set_name in ["A", "B"]:
        subset = [row for row in rows if row["customer_set"] == set_name]
        by_set[set_name] = {float(row["lambda_concentration"]): row for row in subset}
    metrics = [
        ("common_global_risk_mean", "Global risk"),
        ("common_global_cvar90_mean", "CVaR90"),
        ("common_edge_burden_gini_used_mean", "Edge Gini"),
        ("common_top10_burden_share_mean", "Top10 share"),
    ]
    out_rows = []
    for set_name, items in by_set.items():
        base = items[0.0]
        method = items[1.0]
        row = {"customer_set": set_name}
        for key, label in metrics:
            improvement = (float(base[key]) - float(method[key])) / max(float(base[key]), 1e-12)
            row[label] = improvement
        out_rows.append(row)
    x = np.arange(len(metrics))
    width = 0.35
    fig, ax = plt.subplots(figsize=(9, 5))
    for i, row in enumerate(out_rows):
        ax.bar(
            x + (i - 0.5) * width,
            [row[label] * 100 for _, label in metrics],
            width,
            label=f"Set {row['customer_set']}",
        )
    ax.set_xticks(x)
    ax.set_xticklabels([label for _, label in metrics], rotation=10)
    ax.set_ylabel("Improvement from lambda=0 to lambda=1 (%)")
    ax.set_title("Concentration-aware cost improvement")
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.25)
    write_csv(TABLE_DIR / "fig6_concentration_improvement_data.csv", out_rows)
    savefig(fig, "fig6_concentration_aware_improvement")


def write_summary() -> None:
    text = """# Final Figures and Result Files

本目录汇总 Stable-Tail GNN 最终实验的 6 张论文图和配套结果表。

## 图 1：整体实验框架图
- 文件：`figures/fig1_overall_experiment_framework.png`
- 内容：车辆轨迹图数据 -> Stable-Tail GNN -> 节点风险 -> floor_0.01 边风险矩阵 -> OD 路径验证 -> PyVRP-CVRP 下游验证 -> 风险/成本/公平性评价。

## 图 2：模型结构图
- 文件：`figures/fig2_stable_tail_gnn_structure.png`
- 内容：GCN 稳定分支与 TEG 轨迹暴露门控分支 concat 融合，输出 1-8 风险概率、S_i 和 P_high。

## 图 3：风险矩阵分布图
- 文件：`figures/fig3_risk_matrix_distribution.png`
- 表格：`tables/fig3_risk_distribution_data.csv`、`tables/fig3_floor_diagnostics_data.csv`
- 结论：TEG-low 的 P99 和 Std 更高，说明尾部敏感；raw 矩阵零风险边比例约 93.15%，floor_0.01 将零风险比例降为 0。

## 图 4：OD 路径对比图
- 文件：`figures/fig4_od_path_comparison.png`
- 表格：`tables/fig4_od_path_comparison_data.csv`
- 结论：CVaR-risk 在少量 Hop 增加下显著降低 Total Risk、CVaR90 和 RE；CVaR+Concentration 进一步降低 RE，但 Hop 代价更高。

## 图 5：PyVRP beta 成本-风险折中曲线
- 文件：`figures/fig5_pyvrp_beta_tradeoff.png`
- 表格：`tables/fig5_pyvrp_beta_curve_data.csv`
- 结论：beta 增大时 Risk Reduction 上升、CVaR90 下降，Edge Burden Gini 总体下降，体现成本-风险折中。

## 图 6：concentration-aware lambda 改善图
- 文件：`figures/fig6_concentration_aware_improvement.png`
- 表格：`tables/fig6_concentration_improvement_data.csv`
- 结论：lambda=1 相比 lambda=0 能降低 Global Risk、CVaR90、Edge Burden Gini 和 Top10% Burden Share，支持边负担公平扩展。
"""
    (OUT_DIR / "figure_results_summary.md").write_text(text, encoding="utf-8")


def main() -> None:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
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
    fig1_framework()
    fig2_model_structure()
    fig3_risk_distribution()
    fig4_od_path_comparison()
    fig5_beta_tradeoff()
    fig6_concentration_improvement()
    write_summary()
    print(f"Wrote final figures to {OUT_DIR}")


if __name__ == "__main__":
    main()
