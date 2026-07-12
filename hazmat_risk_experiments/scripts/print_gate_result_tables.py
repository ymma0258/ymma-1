"""Print compact Markdown tables from the gate comparison package."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = (
    Path(__file__).resolve().parents[1]
    / "outputs_10seed"
    / "pyvrp_cvrp"
    / "paper_model_comparison_with_gate_10seed"
)
ORDER = [
    "GraphSAGE",
    "GraphSAGE-TEG-Concat",
    "GraphSAGE-TEG-Gate",
    "SGFormer-adapted",
    "SGFormer-TEG-Concat",
    "SGFormer-TEG-Gate",
    "Stable-Tail GNN",
]


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def f(value: object, digits: int = 4) -> str:
    return f"{float(value):.{digits}f}"


def pct(value: object) -> str:
    return f"{100 * float(value):.1f}%"


def print_core() -> None:
    rows = {row["model"]: row for row in read_csv("all_models_summary.csv")}
    print("CORE")
    print(
        "| Model | Macro-F1 | Set A Risk@20 | Set A AUBRC | Set B Risk@20 | Set B AUBRC |"
    )
    print("|---|---:|---:|---:|---:|---:|")
    for model in ORDER:
        row = rows[model]
        print(
            f"| {model} | {f(row['macro_f1'])} | "
            f"{f(row['set_a_risk20'])} | {f(row['set_a_common_risk_aubrc'])} | "
            f"{f(row['set_b_risk20'])} | {f(row['set_b_common_risk_aubrc'])} |"
        )


def print_aubrc() -> None:
    auc = read_csv("cost_risk_aubrc_summary.csv")
    win = read_csv("budget_win_rates.csv")
    for customer_set in ("A", "B"):
        print(f"\nAUBRC {customer_set}")
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


def print_sig() -> None:
    print("\nGATE_SIG")
    print(
        "| Set | Metric | Target | Reference | Ref-target | Relative | Holm p | Sig |"
    )
    print("|---|---|---|---|---:|---:|---:|---|")
    wanted = {"common_risk_aubrc", "average_common_risk_at_b", "load_risk_aubrc"}
    for row in read_csv("gate_pairwise_significance.csv"):
        if row["metric"] not in wanted:
            continue
        if row["reference_model"] not in {
            "SGFormer-TEG-Concat",
            "GraphSAGE-TEG-Concat",
            "Stable-Tail GNN",
        }:
            continue
        print(
            f"| {row['customer_set']} | {row['metric']} | {row['target_model']} | "
            f"{row['reference_model']} | {f(row['reference_minus_target_mean'])} | "
            f"{pct(row['relative_improvement'])} | {f(row['holm_p'])} | "
            f"{row['significant_0p05']} |"
        )


def main() -> None:
    print_core()
    print_aubrc()
    print_sig()


if __name__ == "__main__":
    main()
