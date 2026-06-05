"""Create additional risk-distribution figures 7-12."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs")
OUT_DIR = ROOT / "final_figures_stable_tail_gnn"
FIG_DIR = OUT_DIR / "figures"
TABLE_DIR = OUT_DIR / "tables"
MAIN_MODELS = ["GCN", "TEG-low", "Stable-Tail GNN", "Edge-GAT", "Weighted-GCN"]


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


def distribution_rows() -> list[dict[str, object]]:
    rows = read_csv(TABLE_DIR / "fig3_risk_distribution_data.csv")
    out: list[dict[str, object]] = []
    for row in rows:
        if row["risk_matrix"] not in MAIN_MODELS:
            continue
        converted: dict[str, object] = {"risk_matrix": row["risk_matrix"]}
        for key in ["mean", "p50", "p75", "p90", "p95", "p99", "max", "std", "tail_gap"]:
            converted[key] = float(row[key])
        out.append(converted)
    return out


def fig7_tail_quantile_comparison(rows: list[dict[str, object]]) -> None:
    metrics = ["p95", "p99", "tail_gap"]
    labels = ["P95", "P99", "TailGap"]
    models = [str(row["risk_matrix"]) for row in rows]
    x = np.arange(len(models))
    width = 0.24

    fig, ax = plt.subplots(figsize=(10.2, 5.4))
    for idx, metric in enumerate(metrics):
        ax.bar(
            x + (idx - 1) * width,
            [float(row[metric]) for row in rows],
            width,
            label=labels[idx],
        )

    ax.set_xticks(x)
    ax.set_xticklabels(models, rotation=18, ha="right")
    ax.set_title("Figure 7: Tail quantile comparison")
    ax.set_ylabel("Risk value")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(frameon=False, ncol=3)

    write_csv(
        TABLE_DIR / "fig7_quantile_curve_data.csv",
        [
            {
                "risk_matrix": row["risk_matrix"],
                "p95": row["p95"],
                "p99": row["p99"],
                "tail_gap": row["tail_gap"],
            }
            for row in rows
        ],
    )
    savefig(fig, "fig7_risk_quantile_curves")


def fig8_tail_bars(rows: list[dict[str, object]]) -> None:
    metrics = ["p95", "p99", "tail_gap"]
    labels = ["P95", "P99", "TailGap"]
    models = [str(row["risk_matrix"]) for row in rows]
    x = np.arange(len(models))
    width = 0.24

    fig, ax = plt.subplots(figsize=(10.5, 5.4))
    for idx, metric in enumerate(metrics):
        ax.bar(
            x + (idx - 1) * width,
            [float(row[metric]) for row in rows],
            width,
            label=labels[idx],
        )

    ax.set_xticks(x)
    ax.set_xticklabels(models, rotation=18, ha="right")
    ax.set_ylabel("Risk value")
    ax.set_title("Figure 8: Tail Risk Zoom")
    ax.legend(frameon=False, ncol=3)
    ax.grid(axis="y", alpha=0.25)
    write_csv(
        TABLE_DIR / "fig8_tail_zoom_data.csv",
        [
            {
                "risk_matrix": row["risk_matrix"],
                "p95": row["p95"],
                "p99": row["p99"],
                "tail_gap": row["tail_gap"],
            }
            for row in rows
        ],
    )
    savefig(fig, "fig8_tail_risk_zoom")


def risk_mode_rows() -> list[dict[str, object]]:
    mode_dirs = [
        ("raw", ROOT / "risk_matrices" / "teg_gnn_splitB_seed0_epochs20_raw"),
        ("floor_0.001", ROOT / "risk_matrices" / "teg_gnn_splitB_seed0_epochs20_floor_0p001"),
        ("floor_0.01", ROOT / "risk_matrices" / "teg_gnn_splitB_seed0_epochs20_floor_0p01"),
        ("floor_0.05", ROOT / "risk_matrices" / "teg_gnn_splitB_seed0_epochs20_floor_0p05"),
        ("positive_only", ROOT / "risk_matrices" / "teg_gnn_splitB_seed0_epochs20_positive_only"),
    ]
    diag_rows = {
        row["risk_version"]: row
        for row in read_csv(ROOT / "risk_matrices" / "risk_matrix_modes_2021" / "risk_matrix_diagnostics.csv")
    }
    out: list[dict[str, object]] = []
    for label, risk_dir in mode_dirs:
        data = np.load(risk_dir / "data_2021_edge_risk.npz")
        risks = np.asarray(data["R_ij"], dtype=float)
        diag = next(
            (
                row
                for version, row in diag_rows.items()
                if label.replace(".", "p") in version or (label == "raw" and version.endswith("raw"))
            ),
            {},
        )
        p95 = float(np.quantile(risks, 0.95))
        p99 = float(np.quantile(risks, 0.99))
        out.append(
            {
                "risk_mode": label,
                "zero_risk_ratio": float(diag.get("zero_risk_edge_ratio", np.mean(risks <= 1e-12))),
                "tail_gap": p99 - p95,
                "std": float(risks.std(ddof=0)),
                "p95": p95,
                "p99": p99,
                "max": float(risks.max()),
            }
        )
    return out


def fig9_floor_diagnostics(rows: list[dict[str, object]]) -> None:
    metrics = ["zero_risk_ratio", "tail_gap", "std"]
    labels = ["Zero-risk ratio", "TailGap", "Std"]
    modes = [str(row["risk_mode"]) for row in rows]
    x = np.arange(len(modes))

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.6), sharex=True)
    for ax, metric, label in zip(axes, metrics, labels):
        ax.plot(x, [float(row[metric]) for row in rows], marker="o", linewidth=0)
        ax.vlines(x, 0, [float(row[metric]) for row in rows], linewidth=2, alpha=0.65)
        ax.set_title(label)
        ax.set_xticks(x)
        ax.set_xticklabels(modes, rotation=28, ha="right")
        ax.grid(axis="y", alpha=0.25)

    axes[0].set_ylabel("Value")
    fig.suptitle("Figure 9: Exposure floor removes raw zero-risk degeneration", fontweight="bold")
    write_csv(TABLE_DIR / "fig9_floor_repair_data.csv", rows)
    savefig(fig, "fig9_raw_floor_repair")


def _scatter_p95_tailgap(ax: plt.Axes, rows: list[dict[str, object]], title: str) -> None:
    x_vals = [float(row["p95"]) for row in rows]
    y_vals = [float(row["tail_gap"]) for row in rows]
    x_min = min(x_vals) - 0.006
    x_max = max(x_vals) + 0.006
    y_min = min(y_vals) - 0.010
    y_max = max(0.355, max(y_vals) + 0.012)

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.axvspan(x_min, 0.08, ymin=(0.32 - y_min) / (y_max - y_min), ymax=1, color="#d62728", alpha=0.08)
    ax.text(
        x_min + 0.002,
        y_max - 0.004,
        "Ideal region",
        color="#9b1c1c",
        fontsize=8,
        va="top",
    )

    for row, x_val, y_val in zip(rows, x_vals, y_vals):
        model = str(row["risk_matrix"])
        if model == "Stable-Tail GNN":
            ax.scatter(x_val, y_val, s=180, marker="*", color="#d62728", zorder=4)
            ax.annotate(model, (x_val, y_val), xytext=(8, 8), textcoords="offset points", fontweight="bold")
        else:
            ax.scatter(x_val, y_val, s=75, alpha=0.86)
            ax.annotate(model, (x_val, y_val), xytext=(7, 5), textcoords="offset points", fontsize=8)

    ax.set_xlabel("P95 edge risk")
    ax.set_ylabel("TailGap = P99 - P95")
    ax.set_title(title)
    ax.grid(alpha=0.25)

    ax.annotate(
        "Lower P95",
        xy=(0.074, 0.266),
        xytext=(0.100, 0.266),
        arrowprops={"arrowstyle": "->", "lw": 1.2},
        ha="center",
        va="center",
        fontsize=9,
    )
    ax.annotate(
        "Higher TailGap",
        xy=(0.073, 0.336),
        xytext=(0.073, 0.279),
        arrowprops={"arrowstyle": "->", "lw": 1.2},
        ha="center",
        va="center",
        rotation=90,
        fontsize=9,
    )


def fig10_p95_tailgap_scatter(rows: list[dict[str, object]]) -> None:
    fig, ax = plt.subplots(figsize=(8.2, 5.8))
    _scatter_p95_tailgap(ax, rows, "Figure 10: P95-TailGap Scatter")
    write_csv(
        TABLE_DIR / "fig10_p95_tailgap_scatter_data.csv",
        [
            {
                "risk_matrix": row["risk_matrix"],
                "p95": row["p95"],
                "tail_gap": row["tail_gap"],
            }
            for row in rows
        ],
    )
    savefig(fig, "fig10_p95_tailgap_scatter")


def relative_to_gcn_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    gcn = next(row for row in rows if row["risk_matrix"] == "GCN")
    metrics = ["mean", "p95", "p99", "tail_gap"]
    out: list[dict[str, object]] = []

    for row in rows:
        if row["risk_matrix"] not in {"TEG-low", "Stable-Tail GNN"}:
            continue
        converted: dict[str, object] = {"risk_matrix": row["risk_matrix"]}
        for metric in metrics:
            base = float(gcn[metric])
            converted[metric] = (float(row[metric]) - base) / (base + 1e-12) * 100
        out.append(converted)

    return out


def _relative_change_bars(ax: plt.Axes, rows: list[dict[str, object]], title: str) -> None:
    metrics = ["mean", "p95", "p99", "tail_gap"]
    labels = ["Mean", "P95", "P99", "TailGap"]
    models = [str(row["risk_matrix"]) for row in rows]
    x = np.arange(len(labels))
    width = 0.34
    colors = ["#1f77b4", "#d62728"]

    for idx, row in enumerate(rows):
        ax.bar(
            x + (idx - 0.5) * width,
            [float(row[metric]) for metric in metrics],
            width,
            label=models[idx],
            color=colors[idx % len(colors)],
        )

    ax.axhline(0, color="black", linewidth=1)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Relative change vs GCN (%)")
    ax.set_title(title)
    ax.grid(axis="y", alpha=0.25)
    ax.legend(frameon=False)


def fig11_relative_change_vs_gcn(rows: list[dict[str, object]]) -> None:
    rel_rows = relative_to_gcn_rows(rows)
    fig, ax = plt.subplots(figsize=(8.6, 5.4))
    _relative_change_bars(ax, rel_rows, "Figure 11: Relative Change Compared with GCN")
    write_csv(TABLE_DIR / "fig11_relative_change_vs_gcn_data.csv", rel_rows)
    savefig(fig, "fig11_relative_change_vs_gcn")


def fig12_tail_selectivity_panels(rows: list[dict[str, object]]) -> None:
    rel_rows = relative_to_gcn_rows(rows)
    fig, axes = plt.subplots(1, 2, figsize=(14.5, 5.8))
    _scatter_p95_tailgap(axes[0], rows, "Figure 12-1: P95-TailGap Scatter")
    _relative_change_bars(axes[1], rel_rows, "Figure 12-2: Relative Change vs GCN")
    fig.suptitle("Figure 12: Tail Selectivity of Stable-Tail GNN", fontweight="bold")

    write_csv(
        TABLE_DIR / "fig12_tail_selectivity_panel_data.csv",
        [
            {
                "panel": "12-1_scatter",
                "risk_matrix": row["risk_matrix"],
                "p95": row["p95"],
                "tail_gap": row["tail_gap"],
            }
            for row in rows
        ]
        + [
            {
                "panel": "12-2_relative_change_vs_gcn",
                "risk_matrix": row["risk_matrix"],
                "mean_change_pct": row["mean"],
                "p95_change_pct": row["p95"],
                "p99_change_pct": row["p99"],
                "tail_gap_change_pct": row["tail_gap"],
            }
            for row in rel_rows
        ],
    )
    savefig(fig, "fig12_tail_selectivity_panels")


def append_summary() -> None:
    summary = OUT_DIR / "figure_results_summary.md"
    text = """

## Additional Risk Distribution Figures

### Figure 7: Tail quantile comparison
- Figure: `figures/fig7_risk_quantile_curves.png`
- Table: `tables/fig7_quantile_curve_data.csv`
- Purpose: compares P95, P99, and TailGap only.

### Figure 10: P95-TailGap scatter
- Figure: `figures/fig10_p95_tailgap_scatter.png`
- Table: `tables/fig10_p95_tailgap_scatter_data.csv`
- Purpose: highlights the low-P95/high-TailGap position of Stable-Tail GNN.

### Figure 11: Relative change compared with GCN
- Figure: `figures/fig11_relative_change_vs_gcn.png`
- Table: `tables/fig11_relative_change_vs_gcn_data.csv`
- Purpose: compares TEG-low and Stable-Tail GNN against GCN on Mean, P95, P99, and TailGap.

### Figure 12: Tail selectivity panels
- Figure: `figures/fig12_tail_selectivity_panels.png`
- Table: `tables/fig12_tail_selectivity_panel_data.csv`
- Purpose: combines the P95-TailGap scatter with relative change against GCN.
"""
    with summary.open("a", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
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

    rows = distribution_rows()
    # Figure 7 duplicated Figure 8 after narrowing both to P95/P99/TailGap, so
    # it is intentionally not regenerated.
    fig8_tail_bars(rows)
    fig9_floor_diagnostics(risk_mode_rows())
    fig10_p95_tailgap_scatter(rows)
    fig11_relative_change_vs_gcn(rows)
    fig12_tail_selectivity_panels(rows)
    append_summary()
    print(f"Wrote additional figures 8-12 to {OUT_DIR}")


if __name__ == "__main__":
    main()
