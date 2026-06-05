"""Summarize model experiment CSV output into a Markdown report."""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path


DEFAULT_INPUT = Path(
    r"D:\PyVRP-main\hazmat_risk_experiments\outputs\models\small_formal_seed0_e20_summary.csv"
)


METRICS = [
    "macro_f1",
    "mae",
    "qwk",
    "recall_6_8",
    "precision_6_8",
    "pr_auc_high",
    "high_fn_rate",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=None)
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def metric_value(row: dict[str, str], metric: str) -> float:
    value = row.get(f"{metric}_mean", "")
    if value == "":
        return float("nan")
    return float(value)


def fmt(value: float) -> str:
    if math.isnan(value):
        return "NA"
    return f"{value:.4f}"


def best_row(rows: list[dict[str, str]], metric: str, higher_is_better: bool) -> dict[str, str]:
    valid = [row for row in rows if not math.isnan(metric_value(row, metric))]
    if not valid:
        return {}
    return max(valid, key=lambda row: metric_value(row, metric)) if higher_is_better else min(
        valid, key=lambda row: metric_value(row, metric)
    )


def markdown_report(rows: list[dict[str, str]], input_path: Path) -> str:
    test_rows = [row for row in rows if row["eval_split"].endswith("_test")]
    by_split: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in test_rows:
        by_split[row["split"]].append(row)

    lines = [
        "# Small Formal Model Comparison Report",
        "",
        f"Source: `{input_path}`",
        "",
        "This is a short 20-epoch, seed-0 stability run. It verifies the experimental pipeline and gives an initial trend, but it is not a final multi-seed result.",
        "",
        "## Test Metrics By Split",
        "",
    ]

    for split in sorted(by_split):
        lines.extend(
            [
                f"### Split {split}",
                "",
                "| Model | Macro-F1 | MAE | QWK | Recall@6-8 | Precision@6-8 | PR-AUC high | High FN rate |",
                "|---|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in sorted(by_split[split], key=lambda item: item["model"]):
            lines.append(
                "| {model} | {macro} | {mae} | {qwk} | {recall} | {precision} | {prauc} | {fn} |".format(
                    model=row["model"],
                    macro=fmt(metric_value(row, "macro_f1")),
                    mae=fmt(metric_value(row, "mae")),
                    qwk=fmt(metric_value(row, "qwk")),
                    recall=fmt(metric_value(row, "recall_6_8")),
                    precision=fmt(metric_value(row, "precision_6_8")),
                    prauc=fmt(metric_value(row, "pr_auc_high")),
                    fn=fmt(metric_value(row, "high_fn_rate")),
                )
            )
        lines.append("")

        best_macro = best_row(by_split[split], "macro_f1", True)
        best_mae = best_row(by_split[split], "mae", False)
        best_qwk = best_row(by_split[split], "qwk", True)
        best_recall = best_row(by_split[split], "recall_6_8", True)

        lines.extend(
            [
                "Initial bests:",
                f"- Macro-F1: `{best_macro.get('model', 'NA')}` ({fmt(metric_value(best_macro, 'macro_f1')) if best_macro else 'NA'}).",
                f"- MAE: `{best_mae.get('model', 'NA')}` ({fmt(metric_value(best_mae, 'mae')) if best_mae else 'NA'}).",
                f"- QWK: `{best_qwk.get('model', 'NA')}` ({fmt(metric_value(best_qwk, 'qwk')) if best_qwk else 'NA'}).",
                f"- Recall@6-8: `{best_recall.get('model', 'NA')}` ({fmt(metric_value(best_recall, 'recall_6_8')) if best_recall else 'NA'}).",
                "",
            ]
        )

    lines.extend(
        [
            "## Notes",
            "",
            "- This report uses only one seed, so all standard deviations are zero in the source summary.",
            "- The next formal step should run multiple seeds and more epochs before drawing paper-level conclusions.",
            "- The current result is useful for checking whether the training code, splits, and metrics behave sensibly.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    output = args.output or args.input.with_name(args.input.stem + "_report.md")
    rows = read_rows(args.input)
    output.write_text(markdown_report(rows, args.input), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()

