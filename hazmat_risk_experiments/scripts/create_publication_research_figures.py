"""Create a compact, publication-ready figure set from formal 10-seed outputs.

The script intentionally reads only the organized 10-seed paper tables. It does
not use legacy 5-seed or exploratory result folders.
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FINAL = ROOT / "outputs" / "final_figures_stable_tail_gnn_10seed"
PAPER = FINAL / "paper_results"
TABLES = FINAL / "tables"
OUT = FINAL / "publication_figures"

BLUE = "#0072B2"
ORANGE = "#D55E00"
GREEN = "#009E73"
PURPLE = "#6F4C9B"
SKY = "#56B4E9"
GOLD = "#E69F00"
GRAY = "#777777"
LIGHT = "#E8E8E8"
MODEL_COLORS = {
    "GCN": BLUE,
    "Weighted-GCN": GOLD,
    "Edge-GAT": GREEN,
    "TEG-low": PURPLE,
    "Stable-Tail GNN": ORANGE,
    "Fusion-rho0.25": SKY,
    "Ensemble-4": GRAY,
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def configure_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "DejaVu Sans"],
            "font.size": 9,
            "axes.titlesize": 10.5,
            "axes.labelsize": 9.5,
            "axes.linewidth": 0.8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "xtick.labelsize": 8.5,
            "ytick.labelsize": 8.5,
            "legend.fontsize": 8.5,
            "figure.dpi": 120,
            "savefig.facecolor": "white",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
        }
    )


def save(fig: plt.Figure, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.png", dpi=600, bbox_inches="tight", pad_inches=0.04)
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", pad_inches=0.04)
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)


def panel_label(ax: plt.Axes, label: str) -> None:
    ax.text(-0.13, 1.06, label, transform=ax.transAxes, fontsize=11, fontweight="bold")


def research_framework() -> None:
    fig, ax = plt.subplots(figsize=(7.15, 3.25))
    ax.set_axis_off()
    boxes = [
        (0.04, 0.63, 0.18, 0.20, "Trajectory graph\n2020 / 2021", "Data"),
        (0.29, 0.63, 0.18, 0.20, "Stable-Tail GNN\nnode-risk learning", "Model"),
        (0.54, 0.63, 0.18, 0.20, "Edge risk $R_{ij}$\nexposure floor", "Risk matrix"),
        (0.79, 0.63, 0.18, 0.20, "OD paths\nCVaR validation", "Path level"),
        (0.29, 0.20, 0.18, 0.20, "PyVRP-CVRP\nfixed instances", "Route level"),
        (0.54, 0.20, 0.18, 0.20, "Posterior burden\nconcentration", "Fairness"),
        (0.79, 0.20, 0.18, 0.20, "Cost-risk-fairness\ntrade-off", "Decision"),
    ]
    colors = ["#EAF3F8", "#FCEDE7", "#FFF4D6", "#E8F3EC", "#EFEAF7", "#E8F3EC", "#FCEDE7"]
    for (x, y, w, h, text, stage), color in zip(boxes, colors):
        rect = mpl.patches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.012",
            facecolor=color, edgecolor="#4A4A4A", linewidth=0.9,
        )
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h * 0.57, text, ha="center", va="center", fontsize=8.5)
        ax.text(x + w / 2, y - 0.035, stage, ha="center", va="top", fontsize=7.5, color="#555555")

    arrows = [
        ((0.22, 0.73), (0.29, 0.73)),
        ((0.47, 0.73), (0.54, 0.73)),
        ((0.72, 0.73), (0.79, 0.73)),
        ((0.88, 0.62), (0.88, 0.42)),
        ((0.47, 0.30), (0.54, 0.30)),
        ((0.72, 0.30), (0.79, 0.30)),
    ]
    for start, end in arrows:
        ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "-|>", "lw": 1.1, "color": "#4A4A4A"})
    ax.annotate(
        "", xy=(0.38, 0.42), xytext=(0.63, 0.62),
        arrowprops={"arrowstyle": "-|>", "lw": 1.1, "color": "#4A4A4A", "connectionstyle": "arc3,rad=0.13"},
    )
    ax.text(0.05, 0.06, "Formal protocol: Split B | model seeds 0-9 | solver seeds 0-9 | common evaluation", fontsize=8, color="#444444")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    save(fig, "fig01_research_framework")


def data_profile() -> None:
    rows = read_csv(PAPER / "01_data_statistics" / "audit_summary.csv")
    years = [row["year"].replace("data_", "") for row in rows]
    x = np.arange(len(rows))
    fig, axes = plt.subplots(1, 2, figsize=(7.15, 2.75), gridspec_kw={"wspace": 0.32})

    node_counts = np.array([int(row["node_count"]) for row in rows])
    edge_counts = np.array([int(row["edge_count"]) for row in rows])
    width = 0.34
    axes[0].bar(x - width / 2, node_counts, width, color=BLUE, label="Nodes")
    axes[0].bar(x + width / 2, edge_counts, width, color=SKY, label="Directed edges")
    for offset, values in [(-width / 2, node_counts), (width / 2, edge_counts)]:
        for xx, val in zip(x + offset, values):
            axes[0].text(xx, val + 130, f"{val:,}", ha="center", va="bottom", fontsize=8)
    axes[0].set_xticks(x, years)
    axes[0].set_ylim(0, max(edge_counts) * 1.18)
    axes[0].set_ylabel("Count")
    axes[0].set_title("Graph scale")
    axes[0].legend(frameon=False, loc="upper left")
    axes[0].grid(axis="y", color=LIGHT, linewidth=0.7)
    panel_label(axes[0], "a")

    labeled = np.array([int(row["labeled_count"]) for row in rows])
    high = np.array([int(row["high_risk_count_6_8"]) for row in rows])
    axes[1].bar(x - width / 2, labeled, width, color=GREEN, label="Labeled")
    axes[1].bar(x + width / 2, high, width, color=ORANGE, label="High risk (6-8)")
    for offset, values in [(-width / 2, labeled), (width / 2, high)]:
        for xx, val in zip(x + offset, values):
            axes[1].text(xx, val + 8, str(val), ha="center", va="bottom", fontsize=8)
    axes[1].set_xticks(x, years)
    axes[1].set_ylim(0, max(labeled) * 1.24)
    axes[1].set_ylabel("Number of nodes")
    axes[1].set_title("Label scarcity and tail samples")
    axes[1].legend(frameon=False, loc="upper left")
    axes[1].grid(axis="y", color=LIGHT, linewidth=0.7)
    panel_label(axes[1], "b")
    save(fig, "fig02_data_profile")


def node_model_performance() -> None:
    source = ROOT / "outputs_10seed" / "model_comparison_overview_10seed" / "node_eval_selected_models_10seed.csv"
    rows = [r for r in read_csv(source) if r["table"] == "main_formal_baselines" and r["split"] == "B"]
    order = ["GCN", "Weighted-GCN", "Edge-GAT", "TEG-low", "Stable-Tail GNN"]
    rows = [next(r for r in rows if r["model"] == name) for name in order]
    summary_files = {
        "GCN": ("formal_graph_models_A_B_s0_9_e50_10seed_summary.csv", "gcn"),
        "Weighted-GCN": ("formal_graph_models_A_B_s0_9_e50_10seed_summary.csv", "weighted_gcn"),
        "Edge-GAT": ("formal_graph_models_A_B_s0_9_e50_10seed_summary.csv", "edge_gat"),
        "TEG-low": ("teg_loss_teg_low_tail_s0_9_e50_10seed_summary.csv", "teg_gnn"),
        "Stable-Tail GNN": ("gcn_stabilized_teg_s0_9_e50_10seed_summary.csv", "gcn_teg_concat"),
    }
    summaries: dict[str, dict[str, str]] = {}
    for model, (filename, source_model) in summary_files.items():
        candidates = read_csv(ROOT / "outputs_10seed" / "models" / filename)
        summaries[model] = next(
            r for r in candidates
            if r["model"] == source_model and r["split"] == "B" and r["eval_split"] == "data_2021_test"
        )
    metrics = [("mae", "MAE", False), ("pr_auc_high", "High-risk PR-AUC", True),
               ("recall_6_8", "Recall@6-8", True), ("high_fn_rate", "High-risk FN rate", False)]
    fig, axes = plt.subplots(2, 2, figsize=(7.15, 5.0), gridspec_kw={"hspace": 0.48, "wspace": 0.32})
    y = np.arange(len(rows))
    colors = [MODEL_COLORS[name] for name in order]
    for idx, (ax, (field, title, higher)) in enumerate(zip(axes.flat, metrics)):
        values = [float(summaries[name][f"{field}_mean"]) for name in order]
        errors = [float(summaries[name][f"{field}_std"]) for name in order]
        ax.barh(y, values, xerr=errors, color=colors, height=0.65, capsize=2.5, error_kw={"lw": 0.8})
        ax.set_yticks(y, order if idx % 2 == 0 else [])
        ax.invert_yaxis()
        ax.set_title(title + ("  (higher is better)" if higher else "  (lower is better)"), loc="left")
        ax.grid(axis="x", color=LIGHT, linewidth=0.7)
        ax.set_axisbelow(True)
        span = max(values) - min(values)
        pad = max(span * 0.05, max(values) * 0.01)
        for yy, value, error in zip(y, values, errors):
            ax.text(value + error + pad, yy, f"{value:.3f}", va="center", fontsize=7.8)
        ax.set_xlim(0, max(v + e for v, e in zip(values, errors)) * 1.18)
        panel_label(ax, chr(ord("a") + idx))
    fig.text(0.5, 0.015, "Formal Split B test set; bars show mean +/- SD over 10 model seeds", ha="center", fontsize=8, color="#555555")
    save(fig, "fig03_node_model_performance")


def edge_risk_tail() -> None:
    rows = read_csv(TABLES / "risk_distribution_summary_10seed.csv")
    order = ["GCN", "Weighted-GCN", "Edge-GAT", "TEG-low", "Stable-Tail GNN", "Fusion-rho0.25", "Ensemble-4"]
    rows = [next(r for r in rows if r["model"] == name) for name in order]
    y = np.arange(len(rows))
    fig, ax = plt.subplots(figsize=(7.15, 3.75))
    specs = [("p95", "P95", "o", BLUE), ("p99", "P99", "s", GREEN), ("tail_gap", "Tail gap", "D", ORANGE)]
    offsets = [-0.18, 0, 0.18]
    for (metric, label, marker, color), offset in zip(specs, offsets):
        vals = np.array([float(r[f"{metric}_mean"]) for r in rows])
        errs = np.array([float(r[f"{metric}_std"]) for r in rows])
        ax.errorbar(vals, y + offset, xerr=errs, fmt=marker, ms=5, color=color, capsize=2.5, lw=1, label=label)
    ax.set_yticks(y, order)
    ax.invert_yaxis()
    ax.set_xlabel("Edge-risk value")
    ax.set_title("Tail selectivity of the inferred edge-risk matrix", loc="left")
    ax.grid(axis="x", color=LIGHT, linewidth=0.7)
    ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.12))
    ax.text(0.99, 0.98, "Mean +/- SD across 10 model seeds", transform=ax.transAxes, ha="right", va="top", fontsize=8, color="#555555")
    save(fig, "fig04_edge_risk_tail_distribution")


def od_tradeoff() -> None:
    rows = [r for r in read_csv(TABLES / "fig4_od_path_comparison_data_10seed.csv") if r["method"] == "CVaR-risk"]
    rename = {"Stable-Tail-GNN": "Stable-Tail GNN", "Fusion-rho025": "Fusion-rho0.25"}
    for row in rows:
        row["model"] = rename.get(row["model"], row["model"])
    order = ["GCN", "Weighted-GCN", "Edge-GAT", "TEG-low", "Stable-Tail GNN", "Fusion-rho0.25", "Ensemble-4"]
    rows = [next(r for r in rows if r["model"] == name) for name in order]
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    for row in rows:
        model = row["model"]
        x = 100 * float(row["hop_increase_mean"])
        y = 100 * float(row["total_risk_reduction_mean"])
        ax.errorbar(
            x, y, xerr=100 * float(row["hop_increase_std"]), yerr=100 * float(row["total_risk_reduction_std"]),
            fmt="o", ms=7 if model == "Stable-Tail GNN" else 5, color=MODEL_COLORS[model], capsize=2.5, lw=1,
        )
        dx, dy = (0.09, 0.18)
        if model in {"Edge-GAT", "GCN"}:
            dy = -0.45
        ax.text(x + dx, y + dy, model, fontsize=7.8)
    ax.set_xlabel("Hop increase (%)")
    ax.set_ylabel("Total-risk reduction (%)")
    ax.set_title("OD path safety-efficiency trade-off (fixed 150 OD pairs)", loc="left")
    ax.grid(color=LIGHT, linewidth=0.7)
    ax.text(0.02, 0.03, "Preferred direction", transform=ax.transAxes, fontsize=8, color="#555555")
    ax.annotate("", xy=(0.16, 0.18), xytext=(0.28, 0.08), xycoords="axes fraction", arrowprops={"arrowstyle": "->", "color": "#555555"})
    save(fig, "fig05_od_path_tradeoff")


def pyvrp_beta_tradeoff() -> None:
    rows = read_csv(TABLES / "fig5_pyvrp_beta_curve_data_10seed.csv")
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    for customer_set, color, marker in [("A", BLUE, "o"), ("B", ORANGE, "s")]:
        subset = sorted([r for r in rows if r["customer_set"] == customer_set], key=lambda r: float(r["beta"]))
        xs = np.array([100 * float(r["cost_increase_mean"]) for r in subset])
        ys = np.array([100 * float(r["risk_reduction_mean"]) for r in subset])
        ax.errorbar(
            xs, ys,
            xerr=[100 * float(r["cost_increase_std"]) for r in subset],
            yerr=[100 * float(r["risk_reduction_std"]) for r in subset],
            color=color, marker=marker, ms=5, capsize=2.5, lw=1.4, label=f"Customer set {customer_set}",
        )
        for x, y, row in zip(xs, ys, subset):
            ax.annotate(rf"$\beta$={float(row['beta']):g}", (x, y), xytext=(3, 5), textcoords="offset points", fontsize=7.3)
    ax.set_xlabel("Cost increase over shortest-route baseline (%)")
    ax.set_ylabel("Global-risk reduction (%)")
    ax.set_title("PyVRP cost-risk frontier", loc="left")
    ax.grid(color=LIGHT, linewidth=0.7)
    ax.legend(frameon=False, loc="lower right")
    save(fig, "fig06_pyvrp_beta_tradeoff")


def concentration_effect() -> None:
    rows = read_csv(TABLES / "fig6_concentration_improvement_data_10seed.csv")
    metrics = [
        ("risk_improvement", "Global risk"),
        ("cvar90_improvement", "CVaR90"),
        ("max_vehicle_risk_improvement", "Max vehicle risk"),
        ("edge_gini_improvement", "Edge Gini"),
        ("top10_share_improvement", "Top-10% burden share"),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(7.15, 3.3), gridspec_kw={"width_ratios": [2.2, 1], "wspace": 0.38})
    y = np.arange(len(metrics))
    offsets = [-0.14, 0.14]
    for row, offset, color, marker in zip(rows, offsets, [BLUE, ORANGE], ["o", "s"]):
        vals = [100 * float(row[f"{field}_mean"]) for field, _ in metrics]
        errs = [100 * float(row[f"{field}_std"]) for field, _ in metrics]
        axes[0].errorbar(vals, y + offset, xerr=errs, fmt=marker, color=color, ms=5, capsize=2.5, lw=1, label=f"Set {row['customer_set']}")
    axes[0].axvline(0, color="#555555", lw=0.8)
    axes[0].set_yticks(y, [label for _, label in metrics])
    axes[0].invert_yaxis()
    axes[0].set_xlabel("Improvement from concentration penalty (%)")
    axes[0].set_title(r"Safety and fairness ($\lambda$: 0 $\rightarrow$ 1)", loc="left")
    axes[0].grid(axis="x", color=LIGHT, linewidth=0.7)
    axes[0].legend(frameon=False, loc="lower right")
    panel_label(axes[0], "a")

    sets = [f"Set {r['customer_set']}" for r in rows]
    vals = [100 * float(r["extra_cost_percentage_points_mean"]) for r in rows]
    errs = [100 * float(r["extra_cost_percentage_points_std"]) for r in rows]
    bars = axes[1].bar(sets, vals, yerr=errs, capsize=3, color=[BLUE, ORANGE], width=0.58)
    axes[1].set_ylabel("Extra cost (percentage points)")
    axes[1].set_title("Cost of concentration control", loc="left")
    axes[1].grid(axis="y", color=LIGHT, linewidth=0.7)
    for bar, val in zip(bars, vals):
        axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.7, f"{val:.1f}", ha="center", fontsize=8)
    panel_label(axes[1], "b")
    save(fig, "fig07_concentration_effect")


def main() -> None:
    configure_style()
    research_framework()
    data_profile()
    node_model_performance()
    edge_risk_tail()
    od_tradeoff()
    pyvrp_beta_tradeoff()
    concentration_effect()
    print(f"Wrote publication figures to {OUT}")


if __name__ == "__main__":
    main()
