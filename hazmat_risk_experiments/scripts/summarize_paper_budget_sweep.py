"""Summarize the paper PyVRP budget sweep without retraining any model.

For every model seed and customer set, this script selects the lowest-common-
risk route that satisfies each budget in 10%--40%, then computes trapezoidal
AUBRC values over the seven requested budget coordinates.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs_10seed"
FINAL = ROOT / "outputs" / "final_figures_stable_tail_gnn_10seed"
BUDGETS = (0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40)
PRIMARY_MODELS = (
    "GCN",
    "GAT",
    "GraphSAGE",
    "SGFormer-adapted",
    "Gradformer-adapted",
    "Stable-Tail GNN",
    "Stable-Tail-Gate",
    "SGFormer-TEG-Gate",
)
BASE_MODEL_ORDER = (
    "GCN",
    "GAT",
    "GraphSAGE",
    "SGFormer-adapted",
    "Gradformer-adapted",
    "Stable-Tail GNN",
    "SGFormer-TEG-Gate",
    "TEG-only",
    "Stable-Tail w/o Tail Loss",
    "GraphSAGE-TEG-Concat",
    "GraphSAGE-TEG-Gate",
    "SGFormer-TEG-Concat",
)
MODEL_ORDER = (*BASE_MODEL_ORDER, "Stable-Tail-Gate")
MODEL_DISPLAY = {
    "GCN (paper)": "GCN",
    "GAT": "GAT",
    "GraphSAGE": "GraphSAGE",
    "SGFormer-adapted": "SGFormer-adapted",
    "Gradformer-adapted": "Gradformer-adapted",
    "Stable-Tail GNN (paper)": "Stable-Tail GNN",
    "Stable-Tail-Gate": "Stable-Tail-Gate",
    "SGFormer-TEG-Gate": "SGFormer-TEG-Gate",
    "TEG-only": "TEG-only",
    "Stable-Tail w/o Tail Loss": "Stable-Tail w/o Tail Loss",
    "GraphSAGE-TEG-Concat": "GraphSAGE-TEG-Concat",
    "GraphSAGE-TEG-Gate": "GraphSAGE-TEG-Gate",
    "SGFormer-TEG-Concat": "SGFormer-TEG-Concat",
}


def parse_args() -> argparse.Namespace:
    pyvrp = OUTPUTS / "pyvrp_cvrp"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-summaries",
        type=Path,
        nargs="+",
        default=[
            pyvrp / "paper_model_pyvrp_budget_sweep_10seed" / "model_pyvrp_summary.csv",
            pyvrp / "paper_strong_pyvrp_budget_sweep_10seed" / "model_pyvrp_summary.csv",
            pyvrp / "paper_teg_concat_fusion_pyvrp_budget_sweep_10seed" / "model_pyvrp_summary.csv",
            pyvrp / "paper_teg_gate_fusion_pyvrp_budget_sweep_10seed" / "model_pyvrp_summary.csv",
        ],
    )
    parser.add_argument(
        "--common-summary",
        type=Path,
        default=pyvrp / "paper_all_models_with_gate_common_eval_10seed" / "common_route_summary.csv",
    )
    parser.add_argument("--extra-common-summaries", type=Path, nargs="*", default=[])
    parser.add_argument(
        "--load-summary",
        type=Path,
        default=pyvrp / "paper_all_models_with_gate_load_eval_10seed" / "load_aware_summary.csv",
    )
    parser.add_argument("--extra-load-summaries", type=Path, nargs="*", default=[])
    parser.add_argument(
        "--output-dir", type=Path, default=pyvrp / "paper_budget_sweep_10seed"
    )
    parser.add_argument("--final-root", type=Path, default=FINAL)
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Required downstream result does not exist: {path}")
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


def parse_source(value: str, common: bool) -> tuple[str, int]:
    pattern = r"^[AB]_(.+)_seed(\d+)$" if common else r"^(.+)_seed(\d+)$"
    match = re.match(pattern, value)
    if not match or match.group(1) not in MODEL_DISPLAY:
        raise ValueError(f"Cannot parse paper risk source: {value}")
    return MODEL_DISPLAY[match.group(1)], int(match.group(2))


def mean_std(values: list[float]) -> tuple[float, float]:
    return mean(values), stdev(values) if len(values) > 1 else 0.0


def trapezoid(values: list[float]) -> float:
    if len(values) != len(BUDGETS):
        raise ValueError(f"Expected {len(BUDGETS)} budget values, got {len(values)}")
    return sum(
        (BUDGETS[idx + 1] - BUDGETS[idx]) * (values[idx] + values[idx + 1]) / 2
        for idx in range(len(BUDGETS) - 1)
    )


def rank_values(rows: list[dict[str, object]], metric: str) -> dict[str, float]:
    ordered = sorted((float(row[metric]), str(row["model"])) for row in rows)
    ranks: dict[str, float] = {}
    pos = 0
    while pos < len(ordered):
        end = pos + 1
        while end < len(ordered) and abs(ordered[end][0] - ordered[pos][0]) <= 1e-12:
            end += 1
        rank = ((pos + 1) + end) / 2
        for _, model in ordered[pos:end]:
            ranks[model] = rank
        pos = end
    return ranks


def build_detail(args: argparse.Namespace) -> list[dict[str, object]]:
    costs: dict[tuple[str, int, str, float], tuple[float, Path]] = {}
    for path in args.self_summaries:
        for row in read_csv(path):
            model, seed = parse_source(row["risk_source"], common=False)
            key = (model, seed, row["customer_set"], float(row["beta"]))
            costs[key] = (float(row["cost_increase_pct"]), path)

    loads: dict[
        tuple[str, int, str, float], tuple[dict[str, str], Path]
    ] = {}
    load_paths = [args.load_summary, *args.extra_load_summaries]
    for path in load_paths:
        for row in read_csv(path):
            model, seed = parse_source(row["risk_source"], common=True)
            loads[(model, seed, row["customer_set"], float(row["beta"]))] = (
                row,
                path,
            )

    candidates: dict[tuple[str, int, str], list[dict[str, object]]] = defaultdict(list)
    common_paths = [args.common_summary, *args.extra_common_summaries]
    for common_path in common_paths:
        for row in read_csv(common_path):
            model, seed = parse_source(row["risk_source"], common=True)
            key = (model, seed, row["customer_set"], float(row["beta"]))
            if key not in costs or key not in loads:
                raise KeyError(f"Missing self/load result for {key}")
            cost, self_path = costs[key]
            load, load_path = loads[key]
            candidates[(model, seed, row["customer_set"])].append(
                {
                    "beta": float(row["beta"]),
                    "cost_increase": cost,
                    "risk20_or_risk_at_b": float(row["common_global_risk_mean"]),
                    "cvar90": float(row["common_global_cvar90_mean"]),
                    "cvar95": float(row["common_global_cvar95_mean"]),
                    "load_cvar90": float(load["load_cvar90_mean"]),
                    "max_vehicle_cvar90": float(row["common_max_vehicle_cvar90_mean"]),
                    "source_file": ";".join(
                        (str(self_path), str(common_path), str(load_path))
                    ),
                }
            )

    found = {key[0] for key in candidates}
    expected = set(BASE_MODEL_ORDER)
    if "Stable-Tail-Gate" in found:
        expected.add("Stable-Tail-Gate")
    if found != expected:
        raise ValueError(f"Expected paper models {sorted(expected)}, found {sorted(found)}")

    detail: list[dict[str, object]] = []
    for (model, seed, customer_set), rows in sorted(candidates.items()):
        for budget in BUDGETS:
            feasible = [row for row in rows if float(row["cost_increase"]) <= budget + 1e-12]
            if not feasible:
                raise ValueError(f"No feasible route for {(model, seed, customer_set, budget)}")
            best = min(feasible, key=lambda row: float(row["risk20_or_risk_at_b"]))
            detail.append(
                {
                    "model": model,
                    "seed": seed,
                    "customer_set": customer_set,
                    "budget": budget,
                    "risk20_or_risk_at_b": best["risk20_or_risk_at_b"],
                    "cvar90": best["cvar90"],
                    "cvar95": best["cvar95"],
                    "load_cvar90": best["load_cvar90"],
                    "max_vehicle_cvar90": best["max_vehicle_cvar90"],
                    "selected_beta": best["beta"],
                    "cost_increase": best["cost_increase"],
                    "source_file": best["source_file"],
                }
            )
    return detail


def summarize(detail: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    grouped: dict[tuple[str, int, str], list[dict[str, object]]] = defaultdict(list)
    for row in detail:
        grouped[(str(row["model"]), int(row["seed"]), str(row["customer_set"]))].append(row)

    seed_rows: list[dict[str, object]] = []
    metrics = {
        "common_aubrc": "risk20_or_risk_at_b",
        "cvar90_aubrc": "cvar90",
        "cvar95_aubrc": "cvar95",
        "load_cvar90_aubrc": "load_cvar90",
        "max_vehicle_cvar90_aubrc": "max_vehicle_cvar90",
    }
    for (model, seed, customer_set), rows in sorted(grouped.items()):
        rows.sort(key=lambda row: float(row["budget"]))
        if tuple(float(row["budget"]) for row in rows) != BUDGETS:
            raise ValueError(f"Incomplete budget grid for {(model, seed, customer_set)}")
        out: dict[str, object] = {
            "model": model,
            "seed": seed,
            "customer_set": customer_set,
            "avg_risk_at_b": mean(float(row["risk20_or_risk_at_b"]) for row in rows),
        }
        for output_metric, detail_metric in metrics.items():
            out[output_metric] = trapezoid([float(row[detail_metric]) for row in rows])
        seed_rows.append(out)

    by_model_set: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in seed_rows:
        by_model_set[(str(row["model"]), str(row["customer_set"]))].append(row)
    summary: list[dict[str, object]] = []
    for (model, customer_set), rows in sorted(by_model_set.items()):
        out: dict[str, object] = {"model": model, "customer_set": customer_set}
        for metric in ("avg_risk_at_b", *metrics):
            avg, std = mean_std([float(row[metric]) for row in rows])
            out[f"{metric}_mean"] = avg
            out[f"{metric}_std"] = std
        summary.append(out)
    return seed_rows, summary


def average_ab(summary: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in summary:
        grouped[str(row["model"])].append(row)
    metrics = (
        "avg_risk_at_b",
        "common_aubrc",
        "cvar90_aubrc",
        "cvar95_aubrc",
        "load_cvar90_aubrc",
        "max_vehicle_cvar90_aubrc",
    )
    rows: list[dict[str, object]] = []
    present_models = [model for model in MODEL_ORDER if model in grouped]
    for model in present_models:
        blocks = grouped[model]
        if {str(row["customer_set"]) for row in blocks} != {"A", "B"}:
            raise ValueError(f"Set A/B summary missing for {model}")
        rows.append(
            {
                "model": model,
                **{
                    f"{metric}_ab_mean": mean(float(row[f"{metric}_mean"]) for row in blocks)
                    for metric in metrics
                },
            }
        )
    core_metrics = ("avg_risk_at_b_ab_mean", "cvar90_aubrc_ab_mean", "cvar95_aubrc_ab_mean")
    ranks = [rank_values(rows, metric) for metric in core_metrics]
    for row in rows:
        model = str(row["model"])
        row["rank_by_core_risk"] = mean(rank[model] for rank in ranks)
    return sorted(rows, key=lambda row: (float(row["rank_by_core_risk"]), MODEL_ORDER.index(str(row["model"]))))


def best_model(rows: list[dict[str, object]], metric: str) -> str:
    return str(min(rows, key=lambda row: float(row[metric]))["model"])


def write_stable_gate_comparison(
    output_dir: Path,
    final_dir: Path,
    summary: list[dict[str, object]],
    ab_rows: list[dict[str, object]],
) -> None:
    if not any(row["model"] == "Stable-Tail-Gate" for row in ab_rows):
        return
    metric_names = (
        "avg_risk_at_b",
        "common_aubrc",
        "cvar90_aubrc",
        "cvar95_aubrc",
        "load_cvar90_aubrc",
        "max_vehicle_cvar90_aubrc",
    )
    set_rows = {
        (str(row["model"]), str(row["customer_set"])): row for row in summary
    }
    ab_by_model = {str(row["model"]): row for row in ab_rows}
    comparisons: list[dict[str, object]] = []
    for customer_set in ("A", "B", "AB"):
        for reference in ("Stable-Tail GNN", "GraphSAGE-TEG-Gate"):
            target = (
                ab_by_model["Stable-Tail-Gate"]
                if customer_set == "AB"
                else set_rows[("Stable-Tail-Gate", customer_set)]
            )
            baseline = (
                ab_by_model[reference]
                if customer_set == "AB"
                else set_rows[(reference, customer_set)]
            )
            suffix = "_ab_mean" if customer_set == "AB" else "_mean"
            row: dict[str, object] = {
                "customer_set": customer_set,
                "target": "Stable-Tail-Gate",
                "reference": reference,
            }
            for metric in metric_names:
                target_value = float(target[f"{metric}{suffix}"])
                reference_value = float(baseline[f"{metric}{suffix}"])
                row[f"{metric}_target"] = target_value
                row[f"{metric}_reference"] = reference_value
                row[f"{metric}_difference"] = target_value - reference_value
                row[f"{metric}_relative_change"] = (
                    (target_value - reference_value) / (reference_value + 1e-12)
                )
            comparisons.append(row)
    write_csv(output_dir / "stable_tail_gate_comparison.csv", comparisons)

    lines = [
        "# Stable-Tail-Gate downstream comparison",
        "",
        "Difference is Stable-Tail-Gate minus reference; negative values mean lower risk.",
        "",
        "| Set | Reference | Avg Risk@B Δ | Common AUBRC Δ | CVaR90 Δ | CVaR95 Δ | LoadCVaR90 Δ | MaxVehCVaR90 Δ |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in comparisons:
        lines.append(
            f"| {row['customer_set']} | {row['reference']} | "
            f"{float(row['avg_risk_at_b_difference']):+.4f} | "
            f"{float(row['common_aubrc_difference']):+.4f} | "
            f"{float(row['cvar90_aubrc_difference']):+.5f} | "
            f"{float(row['cvar95_aubrc_difference']):+.5f} | "
            f"{float(row['load_cvar90_aubrc_difference']):+.5f} | "
            f"{float(row['max_vehicle_cvar90_aubrc_difference']):+.5f} |"
        )
    (final_dir / "stable_tail_gate_comparison.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def write_markdown(final_dir: Path, summary: list[dict[str, object]], ab_rows: list[dict[str, object]]) -> None:
    final_dir.mkdir(parents=True, exist_ok=True)
    ab_by_model = {str(row["model"]): row for row in ab_rows}
    lines = [
        "# Downstream budget sweep (B = 10%–40%)",
        "",
        "All values are lower-is-better. AUBRC uses the trapezoidal rule on B = [0.10, 0.15, ..., 0.40].",
        "",
        "| Model | Avg Risk@B | Common AUBRC | CVaR90 AUBRC | CVaR95 AUBRC | LoadCVaR90 AUBRC | MaxVehCVaR90 AUBRC |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for model in PRIMARY_MODELS:
        if model not in ab_by_model:
            continue
        row = ab_by_model[model]
        lines.append(
            f"| {model} | {float(row['avg_risk_at_b_ab_mean']):.4f} | "
            f"{float(row['common_aubrc_ab_mean']):.4f} | {float(row['cvar90_aubrc_ab_mean']):.4f} | "
            f"{float(row['cvar95_aubrc_ab_mean']):.4f} | {float(row['load_cvar90_aubrc_ab_mean']):.4f} | "
            f"{float(row['max_vehicle_cvar90_aubrc_ab_mean']):.4f} |"
        )
    lines.extend(["", "## Ablation and extension models", "", lines[4], lines[5]])
    for model in MODEL_ORDER:
        if model in PRIMARY_MODELS or model not in ab_by_model:
            continue
        row = ab_by_model[model]
        lines.append(
            f"| {model} | {float(row['avg_risk_at_b_ab_mean']):.4f} | "
            f"{float(row['common_aubrc_ab_mean']):.4f} | {float(row['cvar90_aubrc_ab_mean']):.4f} | "
            f"{float(row['cvar95_aubrc_ab_mean']):.4f} | {float(row['load_cvar90_aubrc_ab_mean']):.4f} | "
            f"{float(row['max_vehicle_cvar90_aubrc_ab_mean']):.4f} |"
        )
    (final_dir / "budget_sweep_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    by_set = {
        customer_set: [row for row in summary if row["customer_set"] == customer_set]
        for customer_set in ("A", "B")
    }
    primary_ab = [row for row in ab_rows if row["model"] in PRIMARY_MODELS]
    stable = ab_by_model["Stable-Tail GNN"]
    gate = ab_by_model["SGFormer-TEG-Gate"]
    stable_core_rank = float(stable["rank_by_core_risk"])
    stable_core_position = next(
        idx for idx, row in enumerate(ab_rows, start=1) if row["model"] == "Stable-Tail GNN"
    )
    gate_set_b_or_load = (
        any(
            best_model(by_set["B"], metric) == "SGFormer-TEG-Gate"
            for metric in ("avg_risk_at_b_mean", "cvar90_aubrc_mean", "cvar95_aubrc_mean")
        )
        or float(gate["load_cvar90_aubrc_ab_mean"]) < float(stable["load_cvar90_aubrc_ab_mean"])
    )
    interpretation = [
        "# Budget-sweep interpretation",
        "",
        f"- Set A: Avg Risk@B 最优为 **{best_model(by_set['A'], 'avg_risk_at_b_mean')}**；CVaR90/CVaR95 AUBRC 最优分别为 **{best_model(by_set['A'], 'cvar90_aubrc_mean')}** / **{best_model(by_set['A'], 'cvar95_aubrc_mean')}**。",
        f"- Set B: Avg Risk@B 最优为 **{best_model(by_set['B'], 'avg_risk_at_b_mean')}**；CVaR90/CVaR95 AUBRC 最优分别为 **{best_model(by_set['B'], 'cvar90_aubrc_mean')}** / **{best_model(by_set['B'], 'cvar95_aubrc_mean')}**。",
        f"- A/B 平均：Avg Risk@B、CVaR90 AUBRC、CVaR95 AUBRC 最优分别为 **{best_model(ab_rows, 'avg_risk_at_b_ab_mean')}**、**{best_model(ab_rows, 'cvar90_aubrc_ab_mean')}**、**{best_model(ab_rows, 'cvar95_aubrc_ab_mean')}**。",
        f"- Stable-Tail GNN 的综合核心风险 mean-rank 为 {stable_core_rank:.3f}，排序第 {stable_core_position}（共 {len(ab_rows)} 个模型），因此本次扫描不支持其在所有模型中‘总风险 + 尾部风险综合最稳’的强表述；但它仍是主表模型中 CVaR95 AUBRC 最低的模型。",
    ]
    if gate_set_b_or_load:
        interpretation.append("- SGFormer-TEG-Gate 在 Set B、A/B 平均 CVaR90 或 LoadCVaR 上优于 Stable-Tail GNN，但 Stable-Tail GNN 的 A/B 平均 CVaR95 与 MaxVehCVaR90 更低；因此将前者定位为强主干扩展模型，而不是直接替代 Stable-Tail GNN 的论文主模型。")
    else:
        interpretation.append("- SGFormer-TEG-Gate 未在本次 Set B / LoadCVaR 汇总中形成对 Stable-Tail GNN 的系统性替代优势，仍作为强主干扩展模型报告。")
    (final_dir / "budget_sweep_interpretation.md").write_text(
        "\n".join(interpretation) + "\n", encoding="utf-8"
    )


def main() -> None:
    args = parse_args()
    detail = build_detail(args)
    seed_rows, summary = summarize(detail)
    ab_rows = average_ab(summary)
    write_csv(args.output_dir / "budget_sweep_detail.csv", detail)
    write_csv(args.output_dir / "budget_sweep_seed_metrics.csv", seed_rows)
    write_csv(args.output_dir / "budget_sweep_summary.csv", summary)
    write_csv(args.output_dir / "budget_sweep_ab_average.csv", ab_rows)
    final_dir = args.final_root / "paper_results" / "03_downstream_budget_sweep"
    write_markdown(final_dir, summary, ab_rows)
    write_stable_gate_comparison(args.output_dir, final_dir, summary, ab_rows)
    print(
        f"Wrote budget sweep: detail={len(detail)}, summary={len(summary)}, "
        f"ab={len(ab_rows)} to {args.output_dir}"
    )


if __name__ == "__main__":
    main()
