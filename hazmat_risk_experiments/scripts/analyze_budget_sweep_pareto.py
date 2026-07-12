"""Analyze budget sweeps, budget-free J selection, and route-pool Pareto quality."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


EPS = 1e-12
METHODS = ["GCN", "TEG-low", "Stable-Tail-GNN"]
RISK_COLUMNS = {
    "CommonRisk": "common_global_risk",
    "CVaR90": "common_global_cvar90",
    "LoadRisk": "load_global_risk",
    "Top10Share": "common_top10_burden_share",
}
J_WEIGHTS = {
    "cost_increase_pct": 1.0,
    "common_global_risk": 1.0,
    "common_global_cvar90": 2.0,
    "load_global_risk": 1.0,
    "common_top10_burden_share": 0.5,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--budgets", default="0.10,0.15,0.20,0.25,0.30,0.35,0.40")
    parser.add_argument("--auc-step", type=float, default=0.005)
    parser.add_argument("--auc-min-budget", type=float, default=0.10)
    parser.add_argument("--auc-max-budget", type=float, default=0.40)
    return parser.parse_args()


def parse_source(value: str) -> tuple[str, int]:
    match = re.search(r"(?:^|_)(GCN|TEG-low|Stable-Tail-GNN)_seed(\d+)$", value)
    if match is None:
        raise ValueError(f"Cannot parse source: {value}")
    return match.group(1), int(match.group(2))


def load_candidates(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    parsed = frame["risk_source"].map(parse_source)
    frame["method"] = parsed.map(lambda item: item[0])
    frame["model_seed"] = parsed.map(lambda item: item[1])
    frame["solver_seed"] = frame["seed"].astype(int)
    return frame


def minmax(values: pd.Series) -> pd.Series:
    span = float(values.max() - values.min())
    if span <= EPS:
        return pd.Series(np.zeros(len(values)), index=values.index)
    return (values - float(values.min())) / span


def select_at_budgets(
    candidates: pd.DataFrame, budgets: list[float], metric: str
) -> pd.DataFrame:
    rows = []
    keys = ["method", "customer_set", "model_seed", "solver_seed"]
    for key, group in candidates.groupby(keys, sort=True):
        for budget in budgets:
            feasible = group[group["cost_increase_pct"] <= budget + EPS]
            if feasible.empty:
                raise ValueError(f"No feasible route for {key}, B={budget}")
            best = feasible.sort_values([metric, "pyvrp_cost"], kind="stable").iloc[0]
            row = best.to_dict()
            row.update(
                {
                    "method": key[0],
                    "customer_set": key[1],
                    "model_seed": key[2],
                    "solver_seed": key[3],
                    "budget": budget,
                    "selection_metric": metric,
                }
            )
            rows.append(row)
    return pd.DataFrame(rows)


def hierarchical_summary(raw: pd.DataFrame, value: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    model_seed = (
        raw.groupby(
            ["method", "customer_set", "budget", "model_seed"], as_index=False
        )[[value, "cost_increase_pct"]]
        .mean()
    )
    summary = (
        model_seed.groupby(["method", "customer_set", "budget"], as_index=False)
        .agg(
            value_mean=(value, "mean"),
            value_std=(value, "std"),
            cost_increase_mean=("cost_increase_pct", "mean"),
            model_seeds=("model_seed", "nunique"),
        )
    )
    return model_seed, summary


def budget_curve_metrics(summary: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    scored = summary.copy()
    cell_best = scored.groupby(["customer_set", "budget"])["value_mean"].transform("min")
    scored["is_winner"] = np.isclose(scored["value_mean"], cell_best, rtol=0, atol=1e-12)
    rows = []
    for (method, customer_set), group in scored.groupby(["method", "customer_set"]):
        group = group.sort_values("budget")
        x = group["budget"].to_numpy(float)
        y = group["value_mean"].to_numpy(float)
        rows.append(
            {
                "method": method,
                "customer_set": customer_set,
                "budget_points": len(group),
                "wins": int(group["is_winner"].sum()),
                "win_rate": float(group["is_winner"].mean()),
                "AUBRC": float(np.trapz(y, x)),
                "normalized_AUBRC": float(np.trapz(y, x) / (x[-1] - x[0])),
                "average_risk_at_B": float(y.mean()),
            }
        )
    by_set = pd.DataFrame(rows)
    overall = (
        by_set.groupby("method", as_index=False)
        .agg(
            set_A_win_rate=("win_rate", lambda values: float(values.iloc[0])),
            AUBRC=("AUBRC", "mean"),
            normalized_AUBRC=("normalized_AUBRC", "mean"),
            average_risk_at_B=("average_risk_at_B", "mean"),
        )
    )
    set_b = by_set[by_set["customer_set"] == "B"].set_index("method")["win_rate"]
    overall["set_A_win_rate"] = overall["method"].map(
        by_set[by_set["customer_set"] == "A"].set_index("method")["win_rate"]
    )
    overall["set_B_win_rate"] = overall["method"].map(set_b)
    return by_set, overall


def budget_free_j(candidates: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows = []
    keys = ["method", "customer_set", "model_seed", "solver_seed"]
    for key, group in candidates.groupby(keys, sort=True):
        normalized = pd.DataFrame(index=group.index)
        for column in J_WEIGHTS:
            normalized[column] = minmax(group[column])
        score = sum(J_WEIGHTS[column] * normalized[column] for column in J_WEIGHTS)
        best_idx = score.sort_values(kind="stable").index[0]
        best = group.loc[best_idx].to_dict()
        best.update(
            {
                "method": key[0],
                "customer_set": key[1],
                "model_seed": key[2],
                "solver_seed": key[3],
                "J_score": float(score.loc[best_idx]),
            }
        )
        rows.append(best)
    raw = pd.DataFrame(rows)
    metrics = ["cost_increase_pct", *RISK_COLUMNS.values()]
    model_seed = raw.groupby(
        ["method", "customer_set", "model_seed"], as_index=False
    )[metrics].mean()
    summary = model_seed.groupby(["method", "customer_set"], as_index=False)[metrics].mean()
    return raw, summary


def nondominated_mask(values: np.ndarray) -> np.ndarray:
    keep = np.ones(values.shape[0], dtype=bool)
    for idx, point in enumerate(values):
        if not keep[idx]:
            continue
        dominated = np.all(values <= point + EPS, axis=1) & np.any(values < point - EPS, axis=1)
        dominated[idx] = False
        if dominated.any():
            keep[idx] = False
    return keep


def pareto_statistics(candidates: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    objectives = ["cost_increase_pct", *RISK_COLUMNS.values()]
    rows = []
    pareto_rows = []
    for (method, customer_set), group in candidates.groupby(["method", "customer_set"]):
        unique = group.drop_duplicates(subset=["routes", *objectives]).copy()
        mask = nondominated_mask(unique[objectives].to_numpy(float))
        pareto = unique.loc[mask].copy()
        pareto["method"] = method
        pareto["customer_set"] = customer_set
        pareto_rows.append(pareto)
        rows.append(
            {
                "method": method,
                "customer_set": customer_set,
                "unique_routes": len(unique),
                "pareto_routes": len(pareto),
                "pareto_share": len(pareto) / len(unique),
                "cost_increase_mean": float(pareto["cost_increase_pct"].mean()),
                "common_risk_mean": float(pareto["common_global_risk"].mean()),
                "cvar90_mean": float(pareto["common_global_cvar90"].mean()),
                "load_risk_mean": float(pareto["load_global_risk"].mean()),
                "top10_share_mean": float(pareto["common_top10_burden_share"].mean()),
            }
        )
    return pd.concat(pareto_rows, ignore_index=True), pd.DataFrame(rows)


def pareto_overall(pareto_routes: pd.DataFrame, summary: pd.DataFrame) -> pd.DataFrame:
    counts = (
        summary.groupby("method", as_index=False)[["unique_routes", "pareto_routes"]]
        .sum()
    )
    counts["pareto_share"] = counts["pareto_routes"] / counts["unique_routes"]
    means = pareto_routes.groupby("method", as_index=False).agg(
        cost_increase_mean=("cost_increase_pct", "mean"),
        common_risk_mean=("common_global_risk", "mean"),
        cvar90_mean=("common_global_cvar90", "mean"),
        load_risk_mean=("load_global_risk", "mean"),
        top10_share_mean=("common_top10_burden_share", "mean"),
    )
    return counts.merge(means, on="method", how="left")


def risk_cost_auc(
    candidates: pd.DataFrame, min_budget: float, max_budget: float, step: float
) -> tuple[pd.DataFrame, pd.DataFrame]:
    budgets = np.round(
        np.arange(min_budget, max_budget + step / 2.0, step), 10
    ).tolist()
    curve_parts = []
    auc_rows = []
    for label, metric in list(RISK_COLUMNS.items())[:3]:
        raw = select_at_budgets(candidates, budgets, metric)
        _, summary = hierarchical_summary(raw, metric)
        summary["metric"] = label
        curve_parts.append(summary)
        for (method, customer_set), group in summary.groupby(["method", "customer_set"]):
            group = group.sort_values("budget")
            x = group["budget"].to_numpy(float)
            y = group["value_mean"].to_numpy(float)
            auc_rows.append(
                {
                    "method": method,
                    "customer_set": customer_set,
                    "metric": label,
                    "AUC_10_to_40pct": float(np.trapz(y, x)),
                    "normalized_AUC": float(np.trapz(y, x) / (max_budget - min_budget)),
                }
            )
    return pd.concat(curve_parts, ignore_index=True), pd.DataFrame(auc_rows)


def write_report(
    path: Path,
    overall: pd.DataFrame,
    budget_free: pd.DataFrame,
    pareto: pd.DataFrame,
    auc: pd.DataFrame,
) -> None:
    lines = [
        "# Budget Sweep and Pareto Pool Evaluation",
        "",
        "## B-sweep summary",
        "",
        "| Model | Set A Win Rate | Set B Win Rate | Mean AUBRC | Average Risk@B |",
        "|---|---:|---:|---:|---:|",
    ]
    for _, row in overall.iterrows():
        lines.append(
            f"| {row['method']} | {row['set_A_win_rate']:.1%} | {row['set_B_win_rate']:.1%} | "
            f"{row['AUBRC']:.5f} | {row['average_risk_at_B']:.4f} |"
        )
    lines.extend(
        [
            "",
            "## Budget-free J selection",
            "",
            "J = D_norm + CommonRisk_norm + 2 CVaR90_norm + LoadRisk_norm + 0.5 Top10Share_norm.",
            "",
            "| Model | Set | CostInc | CommonRisk | CVaR90 | LoadRisk | Top10Share |",
            "|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for _, row in budget_free.iterrows():
        lines.append(
            f"| {row['method']} | {row['customer_set']} | {row['cost_increase_pct']:.2%} | "
            f"{row['common_global_risk']:.4f} | {row['common_global_cvar90']:.5f} | "
            f"{row['load_global_risk']:.4f} | {row['common_top10_burden_share']:.2%} |"
        )
    lines.extend(
        [
            "",
            "## Five-objective Pareto routes",
            "",
            "| Model | Set | Unique routes | Pareto routes | Share | CommonRisk | CVaR90 | LoadRisk |",
            "|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for _, row in pareto.iterrows():
        lines.append(
            f"| {row['method']} | {row['customer_set']} | {int(row['unique_routes'])} | "
            f"{int(row['pareto_routes'])} | {row['pareto_share']:.1%} | "
            f"{row['common_risk_mean']:.4f} | {row['cvar90_mean']:.5f} | {row['load_risk_mean']:.4f} |"
        )
    lines.extend(
        [
            "",
            "## Risk-cost AUC (10%-40%)",
            "",
            "| Model | Set | Metric | AUC | Normalized AUC |",
            "|---|---|---|---:|---:|",
        ]
    )
    for _, row in auc.iterrows():
        lines.append(
            f"| {row['method']} | {row['customer_set']} | {row['metric']} | "
            f"{row['AUC_10_to_40pct']:.6f} | {row['normalized_AUC']:.5f} |"
        )
    lines.extend(
        [
            "",
            "注：三模型使用相同 beta 候选网格和 common evaluator。Risk@B 与 AUC 均先在每个 model_seed × solver_seed 内选择，再对 10 个 solver seeds 和 10 个 model seeds 分层聚合。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def plot_budget_sweep(summary: pd.DataFrame, output_dir: Path) -> None:
    colors = {"GCN": "#4C78A8", "TEG-low": "#F58518", "Stable-Tail-GNN": "#54A24B"}
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), constrained_layout=True)
    for ax, customer_set in zip(axes, ["A", "B"]):
        for method in METHODS:
            group = summary[
                (summary["method"] == method) & (summary["customer_set"] == customer_set)
            ].sort_values("budget")
            ax.plot(100 * group["budget"], group["value_mean"], marker="o", label=method, color=colors[method])
        ax.set_title(f"Set {customer_set}")
        ax.set_xlabel("Budget B (%)")
        ax.set_ylabel("Risk@B (CommonRisk)")
        ax.grid(alpha=0.25)
    axes[1].legend(frameon=False)
    fig.savefig(output_dir / "budget_sweep_common_risk.png", dpi=300, bbox_inches="tight")
    fig.savefig(output_dir / "budget_sweep_common_risk.pdf", bbox_inches="tight")
    plt.close(fig)


def plot_auc_curves(curves: pd.DataFrame, output_dir: Path) -> None:
    colors = {"GCN": "#4C78A8", "TEG-low": "#F58518", "Stable-Tail-GNN": "#54A24B"}
    fig, axes = plt.subplots(2, 3, figsize=(14, 7.5), constrained_layout=True)
    for row_idx, customer_set in enumerate(["A", "B"]):
        for col_idx, metric in enumerate(["CommonRisk", "CVaR90", "LoadRisk"]):
            ax = axes[row_idx, col_idx]
            for method in METHODS:
                group = curves[
                    (curves["method"] == method)
                    & (curves["customer_set"] == customer_set)
                    & (curves["metric"] == metric)
                ].sort_values("budget")
                ax.plot(100 * group["budget"], group["value_mean"], label=method, color=colors[method])
            ax.set_title(f"Set {customer_set}: {metric}")
            ax.set_xlabel("Cost budget (%)")
            ax.set_ylabel(metric)
            ax.grid(alpha=0.25)
    axes[0, 2].legend(frameon=False)
    fig.savefig(output_dir / "risk_cost_auc_curves.png", dpi=300, bbox_inches="tight")
    fig.savefig(output_dir / "risk_cost_auc_curves.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    candidates = load_candidates(args.candidates)
    budgets = sorted({float(item) for item in args.budgets.split(",") if item.strip()})

    sweep_raw = select_at_budgets(candidates, budgets, "common_global_risk")
    sweep_seed, sweep_summary = hierarchical_summary(sweep_raw, "common_global_risk")
    sweep_by_set, sweep_overall = budget_curve_metrics(sweep_summary)
    sweep_raw.to_csv(args.output_dir / "budget_sweep_raw.csv", index=False)
    sweep_seed.to_csv(args.output_dir / "budget_sweep_model_seed.csv", index=False)
    sweep_summary.to_csv(args.output_dir / "budget_sweep_summary.csv", index=False)
    sweep_by_set.to_csv(args.output_dir / "budget_sweep_metrics_by_set.csv", index=False)
    sweep_overall.to_csv(args.output_dir / "budget_sweep_metrics_overall.csv", index=False)

    free_raw, free_summary = budget_free_j(candidates)
    free_raw.to_csv(args.output_dir / "budget_free_j_raw.csv", index=False)
    free_summary.to_csv(args.output_dir / "budget_free_j_summary.csv", index=False)

    pareto_routes, pareto_summary = pareto_statistics(candidates)
    pareto_routes.to_csv(args.output_dir / "pareto_nondominated_routes.csv", index=False)
    pareto_summary.to_csv(args.output_dir / "pareto_nondominated_summary.csv", index=False)

    auc_curves, auc_summary = risk_cost_auc(
        candidates, args.auc_min_budget, args.auc_max_budget, args.auc_step
    )
    auc_curves.to_csv(args.output_dir / "risk_cost_auc_curve_data.csv", index=False)
    auc_summary.to_csv(args.output_dir / "risk_cost_auc_summary.csv", index=False)
    (
        auc_summary.groupby(["method", "metric"], as_index=False)[
            ["AUC_10_to_40pct", "normalized_AUC"]
        ]
        .mean()
        .to_csv(args.output_dir / "risk_cost_auc_overall.csv", index=False)
    )
    pareto_overall(pareto_routes, pareto_summary).to_csv(
        args.output_dir / "pareto_nondominated_overall.csv", index=False
    )

    write_report(
        args.output_dir / "budget_sweep_pareto_report.md",
        sweep_overall,
        free_summary,
        pareto_summary,
        auc_summary,
    )
    plot_budget_sweep(sweep_summary, args.output_dir)
    plot_auc_curves(auc_curves, args.output_dir)
    print(f"Wrote budget sweep and Pareto analysis to {args.output_dir}")


if __name__ == "__main__":
    main()
