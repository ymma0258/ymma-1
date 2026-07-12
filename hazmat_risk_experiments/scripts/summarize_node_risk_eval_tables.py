"""Create paper-ready node-risk evaluation tables with High FN rate.

The paper uses two related, but not identical, model comparison tables:

* a main node-risk table, where GCN/Weighted-GCN/Edge-GAT are read from the
  formal baseline run and Stable-Tail GNN is read from the stabilized-TEG run;
* an ablation table, where all rows come from the stabilized-TEG run so the
  architecture/loss variants are compared under the same low-tail setting.

Keeping those sources separate avoids silently reporting a low-tail GCN as the
formal GCN baseline.
"""

from __future__ import annotations

import csv
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
SOURCE = OUTPUTS / "models" / "gcn_stabilized_teg_s0_4_e50_summary.csv"
SOURCE_OUT_DIR = OUTPUTS / "models" / "node_risk_eval_tables"
PAPER_OUT_DIR = OUTPUTS / "final_figures_stable_tail_gnn" / "paper_results" / "02_model_results"

LEGACY_MODEL_ORDER = [
    ("gcn", "GCN"),
    ("teg_gnn", "TEG-low"),
    ("gcn_teg_concat", "Stable-Tail GNN"),
    ("gcn_teg_residual_fixed", "Residual fixed"),
    ("gcn_teg_residual_learnable", "Residual learnable"),
]

MAIN_MODEL_SOURCES = [
    ("mlp", "MLP", "mlp"),
    ("gcn", "GCN", "formal"),
    ("weighted_gcn", "Weighted-GCN", "formal"),
    ("edge_gat", "Edge-GAT", "formal"),
    ("teg_gnn", "TEG-low", "teg_low"),
    ("gcn_teg_concat", "Stable-Tail GNN", "stable"),
]

ABLATION_MODEL_SOURCES = [
    ("gcn", "GCN low-tail setting", "stable"),
    ("teg_gnn", "TEG-low", "stable"),
    ("gcn_teg_concat", "Stable-Tail GNN", "stable"),
    ("gcn_teg_residual_fixed", "Residual fixed", "stable"),
    ("gcn_teg_residual_learnable", "Residual learnable", "stable"),
]

PAPER_MAIN_MODEL_SOURCES = [
    ("gcn", "GCN", "paper"),
    ("gat", "GAT", "paper"),
    ("graphsage", "GraphSAGE", "paper"),
    ("sgformer_adapted", "SGFormer-adapted", "strong"),
    ("gradformer_adapted", "Gradformer-adapted", "strong"),
    ("stable_tail_gnn", "Stable-Tail GNN", "paper"),
]

PAPER_ABLATION_MODEL_SOURCES = [
    ("gcn", "GCN-only branch", "paper"),
    ("teg_only", "TEG-only", "paper"),
    ("stable_tail_gnn", "Stable-Tail w/o Tail Loss", "no_tail"),
    ("stable_tail_gnn", "Stable-Tail GNN", "paper"),
]

PAPER_EXTENDED_MODEL_SOURCES = [
    ("graphsage_teg_concat", "GraphSAGE-TEG-Concat", "fusion"),
    ("sgformer_teg_concat", "SGFormer-TEG-Concat", "fusion"),
    ("graphsage_teg_gate", "GraphSAGE-TEG-Gate", "gate"),
    ("sgformer_teg_gate", "SGFormer-TEG-Gate", "gate"),
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--formal-source", type=Path)
    parser.add_argument("--teg-low-source", type=Path)
    parser.add_argument("--stable-source", type=Path)
    parser.add_argument("--mlp-source", type=Path)
    parser.add_argument("--paper-source", type=Path)
    parser.add_argument("--no-tail-source", type=Path)
    parser.add_argument("--strong-source", type=Path)
    parser.add_argument("--fusion-source", type=Path)
    parser.add_argument("--gate-source", type=Path)
    parser.add_argument("--source-out-dir", type=Path, default=SOURCE_OUT_DIR)
    parser.add_argument("--paper-out-dir", type=Path, default=PAPER_OUT_DIR)
    parser.add_argument("--suffix", default="")
    parser.add_argument("--note-label", default="gcn_stabilized_teg_s0_4_e50_summary.csv")
    return parser.parse_args()


def row_keyed_by_model(source: Path) -> dict[tuple[str, str, str], dict[str, str]]:
    source_rows = read_rows(source)
    return {
        (row["model"], row["split"], row["eval_split"]): row
        for row in source_rows
        if row["eval_split"] == "data_2021_test"
    }


def metric_value(row: dict[str, str], src_col: str) -> float:
    if src_col == "high_fn_rate_mean" and src_col not in row:
        return 1.0 - float(row["recall_6_8_mean"])
    return float(row[src_col])


def build_table_from_sources(
    source_maps: dict[str, tuple[Path, dict[tuple[str, str, str], dict[str, str]]]],
    model_sources: list[tuple[str, str, str]],
    table_name: str,
) -> tuple[list[dict[str, object]], dict[str, list[dict[str, object]]]]:
    all_rows: list[dict[str, object]] = []
    split_tables: dict[str, list[dict[str, object]]] = {"A": [], "B": []}
    for split in ["A", "B"]:
        for model_key, model_name, source_key in model_sources:
            if source_key not in source_maps:
                continue
            source_path, by_key = source_maps[source_key]
            src = by_key.get((model_key, split, "data_2021_test"))
            if src is None:
                continue
            out = {
                "table": table_name,
                "split": split,
                "model": model_name,
                "source_model": model_key,
                "source_file": str(source_path),
            }
            for src_col, dst_col in METRICS:
                value = metric_value(src, src_col)
                out[dst_col] = f"{value:.4f}"
                out[f"{dst_col}_raw"] = value
            all_rows.append(out)
            split_tables[split].append(
                {
                    "Model": model_name,
                    **{
                        dst_col: f"{metric_value(src, src_col):.4f}"
                        for src_col, dst_col in METRICS
                    },
                }
            )
    return all_rows, split_tables


def build_legacy_tables(
    source: Path,
) -> tuple[list[dict[str, object]], dict[str, list[dict[str, object]]]]:
    by_key = row_keyed_by_model(source)

    all_rows: list[dict[str, object]] = []
    split_tables: dict[str, list[dict[str, object]]] = {"A": [], "B": []}
    for split in ["A", "B"]:
        for model_key, model_name in LEGACY_MODEL_ORDER:
            src = by_key[(model_key, split, "data_2021_test")]
            out = {
                "table": "legacy_stabilized_teg",
                "split": split,
                "model": model_name,
                "source_model": model_key,
                "source_file": str(source),
            }
            for src_col, dst_col in METRICS:
                value = metric_value(src, src_col)
                out[dst_col] = f"{value:.4f}"
                out[f"{dst_col}_raw"] = value
            all_rows.append(out)
            split_tables[split].append(
                {
                    "Model": model_name,
                    **{
                        dst_col: f"{metric_value(src, src_col):.4f}"
                        for src_col, dst_col in METRICS
                    },
                }
            )
    return all_rows, split_tables


def write_markdown(
    path: Path,
    split_tables: dict[str, list[dict[str, object]]],
    note_label: str,
    title_prefix: str = "node-risk evaluation results",
) -> None:
    lines: list[str] = []
    for split, title_no in [("A", 2), ("B", 3)]:
        lines.extend(
            [
                f"## Table {title_no}. Split {split} {title_prefix}",
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
            f"- Values are computed from `{note_label}`, `eval_split=data_2021_test`, and rounded to four decimals.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    suffix = args.suffix

    if args.paper_source:
        sources = {
            "paper": (args.paper_source, row_keyed_by_model(args.paper_source))
        }
        if args.no_tail_source:
            sources["no_tail"] = (
                args.no_tail_source,
                row_keyed_by_model(args.no_tail_source),
            )
        for key, path in [
            ("strong", args.strong_source),
            ("fusion", args.fusion_source),
            ("gate", args.gate_source),
        ]:
            if path:
                sources[key] = (path, row_keyed_by_model(path))
        all_rows, split_tables = build_table_from_sources(
            sources, PAPER_MAIN_MODEL_SOURCES, "paper_main_comparison"
        )
        ablation_rows, ablation_tables = build_table_from_sources(
            sources, PAPER_ABLATION_MODEL_SOURCES, "paper_stable_tail_ablation"
        )
        extended_rows, extended_tables = build_table_from_sources(
            sources, PAPER_EXTENDED_MODEL_SOURCES, "paper_extended_fusion_comparison"
        )
    elif args.formal_source or args.stable_source or args.teg_low_source or args.mlp_source:
        sources: dict[str, tuple[Path, dict[tuple[str, str, str], dict[str, str]]]] = {}
        if args.formal_source:
            sources["formal"] = (args.formal_source, row_keyed_by_model(args.formal_source))
        if args.stable_source:
            sources["stable"] = (args.stable_source, row_keyed_by_model(args.stable_source))
        if args.teg_low_source:
            sources["teg_low"] = (args.teg_low_source, row_keyed_by_model(args.teg_low_source))
        elif args.stable_source:
            sources["teg_low"] = sources["stable"]
        if args.mlp_source:
            sources["mlp"] = (args.mlp_source, row_keyed_by_model(args.mlp_source))

        all_rows, split_tables = build_table_from_sources(
            sources, MAIN_MODEL_SOURCES, "main_formal_baselines"
        )
        ablation_rows: list[dict[str, object]] = []
        ablation_tables: dict[str, list[dict[str, object]]] = {"A": [], "B": []}
        if "stable" in sources:
            ablation_rows, ablation_tables = build_table_from_sources(
                sources, ABLATION_MODEL_SOURCES, "stable_tail_ablation"
            )
        extended_rows, extended_tables = [], {"A": [], "B": []}
    else:
        all_rows, split_tables = build_legacy_tables(args.source)
        ablation_rows = []
        ablation_tables = {"A": [], "B": []}
        extended_rows = []
        extended_tables = {"A": [], "B": []}

    for out_dir in [args.source_out_dir, args.paper_out_dir]:
        write_csv(out_dir / f"node_risk_eval_with_high_fn{suffix}.csv", all_rows)
        write_csv(out_dir / f"node_risk_eval_splitA_with_high_fn{suffix}.csv", split_tables["A"])
        write_csv(out_dir / f"node_risk_eval_splitB_with_high_fn{suffix}.csv", split_tables["B"])
        write_markdown(out_dir / f"node_risk_eval_with_high_fn{suffix}.md", split_tables, args.note_label)
        if ablation_rows:
            write_csv(out_dir / f"node_risk_ablation_with_high_fn{suffix}.csv", ablation_rows)
            write_csv(
                out_dir / f"node_risk_ablation_splitA_with_high_fn{suffix}.csv",
                ablation_tables["A"],
            )
            write_csv(
                out_dir / f"node_risk_ablation_splitB_with_high_fn{suffix}.csv",
                ablation_tables["B"],
            )
            write_markdown(
                out_dir / f"node_risk_ablation_with_high_fn{suffix}.md",
                ablation_tables,
                args.note_label,
                title_prefix="Stable-Tail ablation results",
            )
        if extended_rows:
            write_csv(out_dir / f"node_risk_extended_with_high_fn{suffix}.csv", extended_rows)
            write_csv(out_dir / f"node_risk_extended_splitA_with_high_fn{suffix}.csv", extended_tables["A"])
            write_csv(out_dir / f"node_risk_extended_splitB_with_high_fn{suffix}.csv", extended_tables["B"])
            write_markdown(out_dir / f"node_risk_extended_with_high_fn{suffix}.md", extended_tables, args.note_label, title_prefix="extended fusion comparison results")
    print(f"Wrote node-risk evaluation tables to {args.source_out_dir}")
    print(f"Mirrored node-risk evaluation tables to {args.paper_out_dir}")


if __name__ == "__main__":
    main()
