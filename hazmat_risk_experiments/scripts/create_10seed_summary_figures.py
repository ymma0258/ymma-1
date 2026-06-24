"""Create core 10seed paper figures from organized 10seed table data."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FINAL_ROOT = ROOT / "outputs" / "final_figures_stable_tail_gnn_10seed"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final-root", type=Path, default=DEFAULT_FINAL_ROOT)
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def save(fig: plt.Figure, fig_dir: Path, name: str) -> None:
    fig.tight_layout()
    fig.savefig(fig_dir / f"{name}.png", dpi=300, bbox_inches="tight")
    fig.savefig(fig_dir / f"{name}.svg", bbox_inches="tight")
    plt.close(fig)


def add_box(ax, xy, text, width=0.18, height=0.12, color="#e8f1ff"):
    x, y = xy
    rect = plt.Rectangle(
        (x - width / 2, y - height / 2),
        width,
        height,
        facecolor=color,
        edgecolor="#2f5597",
        linewidth=1.5,
        joinstyle="round",
    )
    ax.add_patch(rect)
    ax.text(x, y, text, ha="center", va="center", fontsize=9, wrap=True)


def add_arrow(ax, start, end):
    ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="->", linewidth=1.4, color="#404040"))


def fig1(fig_dir: Path) -> None:
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
        if idx:
            add_arrow(ax, (xs[idx - 1] + 0.07, 0.55), (x - 0.07, 0.55))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Overall Experimental Framework (10seed)", fontsize=14, fontweight="bold")
    save(fig, fig_dir, "fig1_overall_experiment_framework_10seed")


def fig2(fig_dir: Path) -> None:
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
    save(fig, fig_dir, "fig2_stable_tail_gnn_structure_10seed")


def fig3_7_10(table_dir: Path, fig_dir: Path) -> None:
    rows = read_csv(table_dir / "risk_distribution_summary_10seed.csv")
    keep = ["GCN", "Weighted-GCN", "Edge-GAT", "TEG-low", "Stable-Tail GNN", "Fusion-rho0.25", "Ensemble-4"]
    rows = [row for row in rows if row["model"] in keep]

    fig, ax = plt.subplots(figsize=(11, 5.2))
    x = np.arange(len(rows))
    width = 0.22
    for idx, metric in enumerate(["p95", "p99", "tail_gap"]):
        vals = [float(row[f"{metric}_mean"]) for row in rows]
        errs = [float(row[f"{metric}_std"]) for row in rows]
        ax.bar(x + (idx - 1) * width, vals, width, yerr=errs, capsize=3, label=metric.upper() if metric != "tail_gap" else "TailGap")
    ax.set_xticks(x)
    ax.set_xticklabels([row["model"] for row in rows], rotation=20, ha="right")
    ax.set_ylabel("Edge risk")
    ax.set_title("Tail quantile comparison (10seed mean +/- std)")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(frameon=False)
    save(fig, fig_dir, "fig7_tail_quantile_comparison_10seed")

    fig, ax = plt.subplots(figsize=(7.0, 5.8))
    for row in rows:
        marker = "*" if row["model"] == "Stable-Tail GNN" else "o"
        size = 180 if row["model"] == "Stable-Tail GNN" else 70
        ax.scatter(float(row["p95_mean"]), float(row["tail_gap_mean"]), s=size, marker=marker, label=row["model"], alpha=0.9)
        ax.text(float(row["p95_mean"]) + 0.001, float(row["tail_gap_mean"]) + 0.001, row["model"], fontsize=8)
    ax.set_xlabel("P95 edge risk")
    ax.set_ylabel("TailGap = P99 - P95")
    ax.set_title("P95-TailGap tail selectivity (10seed)")
    ax.grid(alpha=0.25)
    save(fig, fig_dir, "fig10_p95_tailgap_scatter_10seed")

    fig, ax = plt.subplots(figsize=(11, 5.5))
    x = np.arange(len(rows))
    ax.bar(x - 0.2, [float(row["mean_mean"]) for row in rows], 0.4, label="Mean")
    ax.bar(x + 0.2, [float(row["std_mean"]) for row in rows], 0.4, label="Std")
    ax.set_xticks(x)
    ax.set_xticklabels([row["model"] for row in rows], rotation=20, ha="right")
    ax.set_ylabel("Edge risk")
    ax.set_title("Risk distribution level and dispersion (10seed)")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(frameon=False)
    save(fig, fig_dir, "fig3_risk_matrix_distribution_10seed")


def fig4(table_dir: Path, fig_dir: Path) -> None:
    rows = [row for row in read_csv(table_dir / "fig4_od_path_comparison_data_10seed.csv") if row["method"] == "CVaR-risk"]
    order = ["GCN", "TEG-low", "Stable-Tail GNN", "Edge-GAT", "Weighted-GCN", "Fusion-rho0.25", "Ensemble-4"]
    rows = [next(row for row in rows if row["model"] == model) for model in order if any(row["model"] == model for row in rows)]
    metrics = [
        ("total_risk_reduction_mean", "Total Risk"),
        ("cvar90_reduction_mean", "CVaR90"),
        ("maxrisk_reduction_mean", "MaxRisk"),
        ("re_reduction_mean", "RE"),
    ]
    fig, ax = plt.subplots(figsize=(12, 5.5))
    x = np.arange(len(rows))
    width = 0.18
    for idx, (metric, label) in enumerate(metrics):
        ax.bar(x + (idx - 1.5) * width, [100 * float(row[metric]) for row in rows], width, label=label)
    ax.set_xticks(x)
    ax.set_xticklabels([row["model"] for row in rows], rotation=20, ha="right")
    ax.set_ylabel("Reduction (%)")
    ax.set_title("OD CVaR-risk downstream reductions (10seed)")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(frameon=False, ncol=4)
    save(fig, fig_dir, "fig4_od_path_comparison_10seed")


def fig5(table_dir: Path, fig_dir: Path) -> None:
    rows = read_csv(table_dir / "fig5_pyvrp_beta_curve_data_10seed.csv")
    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    for customer_set in ["A", "B"]:
        subset = sorted([row for row in rows if row["customer_set"] == customer_set], key=lambda row: float(row["beta"]))
        ax.errorbar(
            [100 * float(row["cost_increase_mean"]) for row in subset],
            [100 * float(row["risk_reduction_mean"]) for row in subset],
            xerr=[100 * float(row["cost_increase_std"]) for row in subset],
            yerr=[100 * float(row["risk_reduction_std"]) for row in subset],
            marker="o",
            capsize=3,
            label=f"Set {customer_set}",
        )
        for row in subset:
            ax.text(100 * float(row["cost_increase_mean"]), 100 * float(row["risk_reduction_mean"]), f"b={float(row['beta']):g}", fontsize=8)
    ax.set_xlabel("Cost increase (%)")
    ax.set_ylabel("Global risk reduction (%)")
    ax.set_title("PyVRP beta cost-risk tradeoff (10seed)")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)
    save(fig, fig_dir, "fig5_pyvrp_beta_tradeoff_10seed")


def fig6(table_dir: Path, fig_dir: Path) -> None:
    rows = read_csv(table_dir / "fig6_concentration_improvement_data_10seed.csv")
    metrics = [
        ("risk_improvement_mean", "Risk"),
        ("cvar90_improvement_mean", "CVaR90"),
        ("edge_gini_improvement_mean", "Edge Gini"),
        ("top10_share_improvement_mean", "Top10 Share"),
        ("extra_cost_percentage_points_mean", "Extra Cost pp"),
    ]
    fig, ax = plt.subplots(figsize=(9, 5.2))
    x = np.arange(len(rows))
    width = 0.15
    for idx, (metric, label) in enumerate(metrics):
        ax.bar(x + (idx - 2) * width, [100 * float(row[metric]) for row in rows], width, label=label)
    ax.set_xticks(x)
    ax.set_xticklabels([f"Set {row['customer_set']}" for row in rows])
    ax.set_ylabel("Improvement / extra cost (percentage points)")
    ax.set_title("Concentration-aware lambda=1 improvement over lambda=0 (10seed)")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(frameon=False, ncol=3)
    save(fig, fig_dir, "fig6_concentration_aware_improvement_10seed")


def main() -> None:
    args = parse_args()
    table_dir = args.final_root / "tables"
    fig_dir = args.final_root / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    fig1(fig_dir)
    fig2(fig_dir)
    fig3_7_10(table_dir, fig_dir)
    fig4(table_dir, fig_dir)
    fig5(table_dir, fig_dir)
    fig6(table_dir, fig_dir)
    print(f"Wrote 10seed summary figures to {fig_dir}")


if __name__ == "__main__":
    main()
