"""Create paper-ready node-risk evaluation tables with High FN rate."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
SOURCE = OUTPUTS / "models" / "gcn_stabilized_teg_s0_4_e50_summary.csv"
SOURCE_OUT_DIR = OUTPUTS / "models" / "node_risk_eval_tables"
PAPER_OUT_DIR = OUTPUTS / "final_figures_stable_tail_gnn" / "paper_results" / "02_model_results"

MODEL_ORDER = [
    ("gcn", "GCN"),
    ("teg_gnn", "TEG-low"),
    ("gcn_teg_concat", "Stable-Tail GNN"),
    ("gcn_teg_residual_fixed", "Residual fixed"),
    ("gcn_teg_residual_learnable", "Residual learnable"),
]

METRICS = [
    ("macro_f1_mean", "Macro-F1"),
    ("mae_mean", "MAE"),
    ("qwk_mean", "QWK"),
    ("recall_6_8_mean", "Recall@6-8"),
    ("pr_auc_high_mean", "PR-AUC"),
    ("high_fn_rate_mean", "High FN"),
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def fmt(value: str) -> str:
    return f"{float(value):.4f}"


def build_tables() -> tuple[list[dict[str, object]], dict[str, list[dict[str, object]]]]:
    source_rows = read_rows(SOURCE)
    by_key = {
        (row["model"], row["split"], row["eval_split"]): row
        for row in source_rows
        if row["eval_split"] == "data_2021_test"
    }

    all_rows: list[dict[str, object]] = []
    split_tables: dict[str, list[dict[str, object]]] = {"A": [], "B": []}
    for split in ["A", "B"]:
        for model_key, model_name in MODEL_ORDER:
            src = by_key[(model_key, split, "data_2021_test")]
            out = {
                "split": split,
                "model": model_name,
                "source_model": model_key,
                "source_file": str(SOURCE),
            }
            for src_col, dst_col in METRICS:
                out[dst_col] = fmt(src[src_col])
                out[f"{dst_col}_raw"] = float(src[src_col])
            all_rows.append(out)
            split_tables[split].append(
                {
                    "Model": model_name,
                    **{dst_col: fmt(src[src_col]) for src_col, dst_col in METRICS},
                }
            )
    return all_rows, split_tables


def write_markdown(path: Path, split_tables: dict[str, list[dict[str, object]]]) -> None:
    lines: list[str] = []
    for split, title_no in [("A", 2), ("B", 3)]:
        lines.extend(
            [
                f"## Table {title_no}. Split {split} node-risk evaluation results",
                "",
                "| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |",
                "|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in split_tables[split]:
            lines.append(
                "| {Model} | {Macro-F1} | {MAE} | {QWK} | {Recall@6-8} | {PR-AUC} | {High FN} |".format(
                    **row
                )
            )
        lines.append("")
    lines.extend(
        [
            "Notes:",
            "",
            "- `High FN` is the high-risk false-negative rate for labels 6-8.",
            "- Values are computed from `gcn_stabilized_teg_s0_4_e50_summary.csv`, `eval_split=data_2021_test`, and rounded to four decimals.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    all_rows, split_tables = build_tables()
    for out_dir in [SOURCE_OUT_DIR, PAPER_OUT_DIR]:
        write_csv(out_dir / "node_risk_eval_with_high_fn.csv", all_rows)
        write_csv(out_dir / "node_risk_eval_splitA_with_high_fn.csv", split_tables["A"])
        write_csv(out_dir / "node_risk_eval_splitB_with_high_fn.csv", split_tables["B"])
        write_markdown(out_dir / "node_risk_eval_with_high_fn.md", split_tables)
    print(f"Wrote node-risk evaluation tables to {SOURCE_OUT_DIR}")
    print(f"Mirrored node-risk evaluation tables to {PAPER_OUT_DIR}")


if __name__ == "__main__":
    main()
