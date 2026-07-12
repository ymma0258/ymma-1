"""Build the 12-model paper comparison including TEG-gated fusion models."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.stats import wilcoxon

import analyze_paper_model_comparison as base
import analyze_fusion_model_comparison as concat


OUTPUTS = base.OUTPUTS
DEFAULT_GATE_NODE = (
    OUTPUTS / "models" / "paper_teg_gate_fusions_splitB_10seed_summary.csv"
)
DEFAULT_GATE_OD = (
    OUTPUTS
    / "od_paths"
    / "paper_teg_gate_fusion_od_10seed"
    / "od_seed_robustness_by_model_10seed.csv"
)
DEFAULT_GATE_SELF = (
    OUTPUTS
    / "pyvrp_cvrp"
    / "paper_teg_gate_fusion_pyvrp_budget_sweep_10seed"
    / "model_pyvrp_summary.csv"
)
DEFAULT_COMMON_WITH_GATE = (
    OUTPUTS
    / "pyvrp_cvrp"
    / "paper_all_models_with_gate_common_eval_10seed"
    / "common_route_summary.csv"
)
DEFAULT_LOAD_WITH_GATE = (
    OUTPUTS
    / "pyvrp_cvrp"
    / "paper_all_models_with_gate_load_eval_10seed"
    / "load_aware_summary.csv"
)
DEFAULT_OUT = OUTPUTS / "pyvrp_cvrp" / "paper_model_comparison_with_gate_10seed"

MODEL_DISPLAY = {
    **concat.FUSION_MODEL_DISPLAY,
    "SGFormer-TEG-Gate": "SGFormer-TEG-Gate",
    "GraphSAGE-TEG-Gate": "GraphSAGE-TEG-Gate",
}

MODEL_ORDER = [
    "GCN",
    "GAT",
    "GraphSAGE",
    "GraphSAGE-TEG-Concat",
    "GraphSAGE-TEG-Gate",
    "SGFormer-adapted",
    "SGFormer-TEG-Concat",
    "SGFormer-TEG-Gate",
    "Gradformer-adapted",
    "TEG-only",
    "Stable-Tail w/o Tail Loss",
    base.STABLE,
]

PAIRWISE_TARGETS = [
    ("SGFormer-TEG-Gate", "SGFormer-TEG-Concat", "Gate vs concat"),
    ("SGFormer-TEG-Gate", "SGFormer-adapted", "TEG gated enhancement over SGFormer"),
    ("SGFormer-TEG-Gate", base.STABLE, "Gate vs current main model"),
    ("GraphSAGE-TEG-Gate", "GraphSAGE-TEG-Concat", "Gate vs concat"),
    ("GraphSAGE-TEG-Gate", "GraphSAGE", "TEG gated enhancement over GraphSAGE"),
    ("GraphSAGE-TEG-Gate", base.STABLE, "Gate vs current main model"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--node", type=Path, default=base.DEFAULT_NODE)
    parser.add_argument("--ablation", type=Path, default=base.DEFAULT_ABLATION)
    parser.add_argument("--strong-node", type=Path, default=base.DEFAULT_STRONG_NODE)
    parser.add_argument("--concat-node", type=Path, default=concat.DEFAULT_FUSION_NODE)
    parser.add_argument("--gate-node", type=Path, default=DEFAULT_GATE_NODE)
    parser.add_argument("--od", type=Path, default=base.DEFAULT_OD)
    parser.add_argument("--strong-od", type=Path, default=base.DEFAULT_STRONG_OD)
    parser.add_argument("--concat-od", type=Path, default=concat.DEFAULT_FUSION_OD)
    parser.add_argument("--gate-od", type=Path, default=DEFAULT_GATE_OD)
    parser.add_argument("--self-summary", type=Path, default=base.DEFAULT_SELF)
    parser.add_argument("--strong-self-summary", type=Path, default=base.DEFAULT_STRONG_SELF)
    parser.add_argument("--concat-self-summary", type=Path, default=concat.DEFAULT_FUSION_SELF)
    parser.add_argument("--gate-self-summary", type=Path, default=DEFAULT_GATE_SELF)
    parser.add_argument("--common-summary", type=Path, default=DEFAULT_COMMON_WITH_GATE)
    parser.add_argument("--load-summary", type=Path, default=DEFAULT_LOAD_WITH_GATE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--bootstrap-samples", type=int, default=10000)
    return parser.parse_args()


def install_globals() -> None:
    base.MODEL_DISPLAY.clear()
    base.MODEL_DISPLAY.update(MODEL_DISPLAY)
    base.MODEL_ORDER[:] = MODEL_ORDER


def gate_node_table(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    labels = {
        "sgformer_teg_gate": "SGFormer-TEG-Gate",
        "graphsage_teg_gate": "GraphSAGE-TEG-Gate",
    }
    for row in rows:
        if row["split"] != "B" or row["eval_split"] != "data_2021_test":
            continue
        result.append(
            {
                "model": labels[row["model"]],
                "Macro-F1": f"{float(row['macro_f1_mean']):.4f}",
                "MAE": f"{float(row['mae_mean']):.4f}",
                "QWK": f"{float(row['qwk_mean']):.4f}",
                "Recall@6-8": f"{float(row['recall_6_8_mean']):.4f}",
                "PR-AUC": f"{float(row['pr_auc_high_mean']):.4f}",
                "High FN": f"{float(row['high_fn_rate_mean']):.4f}",
            }
        )
    return result


def paired_wilcoxon(diff: np.ndarray) -> float:
    try:
        return float(wilcoxon(diff, alternative="two-sided").pvalue)
    except ValueError:
        return 1.0


def average_risk_at_budget_detail(
    selected: list[dict[str, object]],
) -> list[dict[str, object]]:
    grouped: dict[tuple[str, int, str], list[float]] = {}
    for row in selected:
        key = (str(row["model"]), int(row["model_seed"]), str(row["customer_set"]))
        grouped.setdefault(key, []).append(float(row["common_global_risk_mean"]))
    return [
        {
            "model": model,
            "model_seed": seed,
            "customer_set": customer_set,
            "average_common_risk_at_b": float(np.mean(values)),
        }
        for (model, seed, customer_set), values in sorted(grouped.items())
    ]


def gate_pairwise_significance(
    auc_detail: list[dict[str, object]],
    avg_risk_detail: list[dict[str, object]],
    samples: int,
) -> list[dict[str, object]]:
    auc_keyed = {
        (str(row["model"]), int(row["model_seed"]), str(row["customer_set"])): row
        for row in auc_detail
    }
    avg_keyed = {
        (str(row["model"]), int(row["model_seed"]), str(row["customer_set"])): row
        for row in avg_risk_detail
    }
    metric_sources = [
        ("common_risk_aubrc", auc_keyed),
        ("cvar90_aubrc", auc_keyed),
        ("load_risk_aubrc", auc_keyed),
        ("average_common_risk_at_b", avg_keyed),
    ]
    rows: list[dict[str, object]] = []
    for customer_set in ("A", "B"):
        for metric, keyed in metric_sources:
            block: list[dict[str, object]] = []
            p_values: list[float] = []
            for target, reference, purpose in PAIRWISE_TARGETS:
                target_values = np.asarray(
                    [
                        float(keyed[(target, seed, customer_set)][metric])
                        for seed in range(10)
                    ],
                    dtype=float,
                )
                reference_values = np.asarray(
                    [
                        float(keyed[(reference, seed, customer_set)][metric])
                        for seed in range(10)
                    ],
                    dtype=float,
                )
                diff = reference_values - target_values
                p_value = paired_wilcoxon(diff)
                low, high = base.bootstrap_ci(diff, samples, seed=20260711)
                block.append(
                    {
                        "customer_set": customer_set,
                        "metric": metric,
                        "target_model": target,
                        "reference_model": reference,
                        "purpose": purpose,
                        "reference_minus_target_mean": float(diff.mean()),
                        "relative_improvement": float(
                            diff.mean() / (reference_values.mean() + 1e-12)
                        ),
                        "bootstrap_ci_low": low,
                        "bootstrap_ci_high": high,
                        "wilcoxon_p": p_value,
                        "effect_size_dz": float(
                            diff.mean() / (diff.std(ddof=1) + 1e-12)
                        ),
                    }
                )
                p_values.append(p_value)
            for row, p_adj in zip(block, base.holm_adjust(p_values)):
                row["holm_p"] = p_adj
                row["significant_0p05"] = p_adj < 0.05
                rows.append(row)
    return rows


def append_gate_report(path: Path, pairwise_rows: list[dict[str, object]]) -> None:
    lines = [
        "",
        "## Gate-targeted paired significance",
        "",
        "Positive `reference - target` means the target model is lower/better. Holm correction is applied within each Set × metric block over the six targeted Gate comparisons.",
        "",
        "| Set | Metric | Target | Reference | Reference - target | Relative | 95% CI | Holm p |",
        "|---|---|---|---|---:|---:|---:|---:|",
    ]
    for row in pairwise_rows:
        lines.append(
            f"| {row['customer_set']} | {row['metric']} | {row['target_model']} | "
            f"{row['reference_model']} | {float(row['reference_minus_target_mean']):.4f} | "
            f"{float(row['relative_improvement']):.2%} | "
            f"[{float(row['bootstrap_ci_low']):.4f}, {float(row['bootstrap_ci_high']):.4f}] | "
            f"{float(row['holm_p']):.4g} |"
        )
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def main() -> None:
    install_globals()
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    node_rows = base.read_csv(args.node)
    node_rows.extend(base.strong_node_table(base.read_csv(args.strong_node)))
    node_rows.extend(concat.fusion_node_table(base.read_csv(args.concat_node)))
    node_rows.extend(gate_node_table(base.read_csv(args.gate_node)))
    ablation_rows = base.read_csv(args.ablation)
    od_rows = [
        *base.read_csv(args.od),
        *base.read_csv(args.strong_od),
        *base.read_csv(args.concat_od),
        *base.read_csv(args.gate_od),
    ]
    self_rows = [
        *base.read_csv(args.self_summary),
        *base.read_csv(args.strong_self_summary),
        *base.read_csv(args.concat_self_summary),
        *base.read_csv(args.gate_self_summary),
    ]
    common_rows = base.read_csv(args.common_summary)
    load_rows = base.read_csv(args.load_summary)

    joined = base.load_joined(self_rows, common_rows, load_rows)
    selected = base.select_budgets(joined)
    budget_summary = base.summarize_budgets(selected)
    sig_rows = base.significance(selected, args.bootstrap_samples)
    targeted_sig_rows = base.targeted_significance(selected, args.bootstrap_samples)
    beta1_rows = base.beta_one_summary(joined)
    auc_detail, auc_summary = base.cost_risk_auc(joined)
    win_rows = base.budget_win_rates(selected)
    auc_sig_rows = base.auc_significance(auc_detail, args.bootstrap_samples)
    avg_risk_detail = average_risk_at_budget_detail(selected)
    gate_sig_rows = gate_pairwise_significance(
        auc_detail, avg_risk_detail, args.bootstrap_samples
    )
    model_summary = base.all_model_summary(
        node_rows, ablation_rows, od_rows, budget_summary, auc_summary, win_rows
    )

    base.write_csv(
        args.output_dir / "upstream_node_metrics_all_models.csv",
        [
            {
                key: row[key]
                for key in (
                    "model",
                    "macro_f1",
                    "mae",
                    "qwk",
                    "pr_auc",
                    "recall_at_6_8",
                    "high_fn",
                )
            }
            for row in model_summary
        ],
    )
    base.write_csv(args.output_dir / "all_models_summary.csv", model_summary)
    base.write_csv(args.output_dir / "common_cost_risk_joined.csv", joined)
    base.write_csv(args.output_dir / "fixed_budget_risk_detail.csv", selected)
    base.write_csv(args.output_dir / "fixed_budget_risk_summary.csv", budget_summary)
    base.write_csv(args.output_dir / "extended_downstream_metrics_10_40.csv", budget_summary)
    base.write_csv(args.output_dir / "paired_significance_holm.csv", sig_rows)
    base.write_csv(args.output_dir / "targeted_common_cvar_significance.csv", targeted_sig_rows)
    base.write_csv(args.output_dir / "beta1_common_comparison.csv", beta1_rows)
    base.write_csv(args.output_dir / "cost_risk_aubrc_detail.csv", auc_detail)
    base.write_csv(args.output_dir / "cost_risk_aubrc_summary.csv", auc_summary)
    base.write_csv(args.output_dir / "budget_win_rates.csv", win_rows)
    base.write_csv(args.output_dir / "auc_paired_significance_holm.csv", auc_sig_rows)
    base.write_csv(args.output_dir / "average_risk_at_budget_detail.csv", avg_risk_detail)
    base.write_csv(args.output_dir / "gate_pairwise_significance.csv", gate_sig_rows)

    report_path = args.output_dir / "final_comparison_report.md"
    base.write_report(
        report_path,
        node_rows,
        ablation_rows,
        od_rows,
        budget_summary,
        sig_rows,
        auc_summary,
        win_rows,
        auc_sig_rows,
    )
    append_gate_report(report_path, gate_sig_rows)

    integrity = {
        "node_rows": len(node_rows),
        "ablation_rows": len(ablation_rows),
        "od_rows": len(od_rows),
        "self_rows": len(self_rows),
        "common_rows": len(common_rows),
        "load_rows": len(load_rows),
        "joined_rows": len(joined),
        "fixed_budget_detail_rows": len(selected),
        "fixed_budget_summary_rows": len(budget_summary),
        "significance_rows": len(sig_rows),
        "targeted_significance_rows": len(targeted_sig_rows),
        "cost_risk_auc_detail_rows": len(auc_detail),
        "cost_risk_auc_summary_rows": len(auc_summary),
        "auc_significance_rows": len(auc_sig_rows),
        "gate_pairwise_significance_rows": len(gate_sig_rows),
        "all_models_summary_rows": len(model_summary),
        "models": MODEL_ORDER,
        "model_seeds": sorted({int(row["model_seed"]) for row in joined}),
        "customer_sets": sorted({str(row["customer_set"]) for row in joined}),
        "betas": sorted({float(row["beta"]) for row in joined}),
    }
    (args.output_dir / "integrity.json").write_text(
        json.dumps(integrity, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote gate comparison package to {args.output_dir}")
    print(json.dumps(integrity, ensure_ascii=False))


if __name__ == "__main__":
    main()
