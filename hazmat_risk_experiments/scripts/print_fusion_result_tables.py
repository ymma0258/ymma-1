"""Print compact Markdown tables from the fusion comparison package."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = (
    Path(__file__).resolve().parents[1]
    / "outputs_10seed"
    / "pyvrp_cvrp"
    / "paper_model_comparison_with_fusion_10seed"
)
ORDER = [
    "GCN",
    "GAT",
    "GraphSAGE",
    "GraphSAGE-TEG-Concat",
    "SGFormer-adapted",
    "SGFormer-TEG-Concat",
    "Gradformer-adapted",
    "TEG-only",
    "Stable-Tail w/o Tail Loss",
    "Stable-Tail GNN",
]


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def f(value: object, digits: int = 4) -> str:
    return f"{float(value):.{digits}f}"


def pct(value: object) -> str:
    return f"{100 * float(value):.1f}%"


def print_upstream() -> None:
    rows = {row["model"]: row for row in read_csv("all_models_summary.csv")}
    print("UPSTREAM")
    print("| Model | Macro-F1 | MAE | QWK | PR-AUC | Recall@6-8 | High FN |")
    print("|---|---:|---:|---:|---:|---:|---:|")
    for model in ORDER:
        row = rows[model]
        print(
            f"| {model} | {f(row['macro_f1'])} | {f(row['mae'])} | "
            f"{f(row['qwk'])} | {f(row['pr_auc'])} | "
            f"{f(row['recall_at_6_8'])} | {f(row['high_fn'])} |"
        )


def print_fixed() -> None:
    rows = read_csv("fixed_budget_risk_summary.csv")
    for customer_set in ("A", "B"):
        print(f"\nFIXED {customer_set}")
        print(
            "| Model | Risk@20 | CVaR@20 | Risk@25 | CVaR@25 | Risk@30 | CVaR@30 |"
        )
        print("|---|---:|---:|---:|---:|---:|---:|")
        for model in ORDER:
            vals = {
                float(row["budget"]): row
                for row in rows
                if row["model"] == model and row["customer_set"] == customer_set
            }
            print(
                f"| {model} | "
                f"{f(vals[0.20]['common_global_risk_mean_mean'])} | "
                f"{f(vals[0.20]['common_global_cvar90_mean_mean'])} | "
                f"{f(vals[0.25]['common_global_risk_mean_mean'])} | "
                f"{f(vals[0.25]['common_global_cvar90_mean_mean'])} | "
                f"{f(vals[0.30]['common_global_risk_mean_mean'])} | "
                f"{f(vals[0.30]['common_global_cvar90_mean_mean'])} |"
            )


def print_b20_extended() -> None:
    rows = read_csv("fixed_budget_risk_summary.csv")
    for customer_set in ("A", "B"):
        print(f"\nB20EXT {customer_set}")
        print("| Model | LoadRisk | Top10 share | Edge Gini | Max vehicle risk |")
        print("|---|---:|---:|---:|---:|")
        for model in ORDER:
            row = next(
                row
                for row in rows
                if row["model"] == model
                and row["customer_set"] == customer_set
                and abs(float(row["budget"]) - 0.20) < 1e-9
            )
            print(
                f"| {model} | {f(row['load_global_risk_mean_mean'])} | "
                f"{pct(row['common_top10_burden_share_mean_mean'])} | "
                f"{f(row['common_edge_burden_gini_used_mean_mean'])} | "
                f"{f(row['common_max_vehicle_risk_mean_mean'])} |"
            )


def print_aubrc_win() -> None:
    auc = read_csv("cost_risk_aubrc_summary.csv")
    win = read_csv("budget_win_rates.csv")
    for customer_set in ("A", "B"):
        print(f"\nAUBRCWIN {customer_set}")
        print(
            "| Model | Win rate | Avg Risk@B | Common AUBRC | CVaR AUBRC | LoadRisk AUBRC |"
        )
        print("|---|---:|---:|---:|---:|---:|")
        for model in ORDER:
            auc_row = next(
                row
                for row in auc
                if row["model"] == model and row["customer_set"] == customer_set
            )
            win_row = next(
                row
                for row in win
                if row["model"] == model and row["customer_set"] == customer_set
            )
            print(
                f"| {model} | {pct(win_row['win_rate'])} | "
                f"{f(win_row['average_common_risk_at_b'])} | "
                f"{f(auc_row['common_risk_aubrc_mean'])} | "
                f"{f(auc_row['cvar90_aubrc_mean'])} | "
                f"{f(auc_row['load_risk_aubrc_mean'])} |"
            )


def main() -> None:
    print_upstream()
    print_fixed()
    print_b20_extended()
    print_aubrc_win()


if __name__ == "__main__":
    main()
