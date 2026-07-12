"""Focused SGFormer-TEG-Gate vs Stable-Tail GNN analysis."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
from scipy.stats import wilcoxon


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import train_risk_model as training  # noqa: E402
import analyze_paper_model_comparison as paper  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs_10seed"
GATE_DIR = OUTPUTS / "pyvrp_cvrp" / "paper_model_comparison_with_gate_10seed"
RISK_DIR = (
    OUTPUTS
    / "risk_matrices"
    / "sgformer_teg_gate_splitB_seed0_epochs50_paper_teg_gate_fusions_10seed_floor_0p01"
)
CHECKPOINT_DIR = OUTPUTS / "models" / "checkpoints"
OUT_DIR = OUTPUTS / "pyvrp_cvrp" / "paper_model_comparison_with_gate_focus_10seed"

TARGET = "SGFormer-TEG-Gate"
REFERENCE = "Stable-Tail GNN"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=GATE_DIR)
    parser.add_argument("--risk-dir", type=Path, default=RISK_DIR)
    parser.add_argument("--checkpoint-dir", type=Path, default=CHECKPOINT_DIR)
    parser.add_argument("--output-dir", type=Path, default=OUT_DIR)
    parser.add_argument("--benchmark-repeats", type=int, default=50)
    parser.add_argument("--benchmark-warmup", type=int, default=10)
    parser.add_argument("--bootstrap-samples", type=int, default=10000)
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
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


def paired_test(
    target_values: np.ndarray,
    reference_values: np.ndarray,
    samples: int,
    seed: int,
) -> dict[str, float | bool]:
    diff = reference_values - target_values
    try:
        p_value = float(wilcoxon(diff, alternative="two-sided").pvalue)
    except ValueError:
        p_value = 1.0
    low, high = paper.bootstrap_ci(diff, samples, seed=seed)
    return {
        "target_mean": float(target_values.mean()),
        "reference_mean": float(reference_values.mean()),
        "reference_minus_target_mean": float(diff.mean()),
        "relative_improvement": float(diff.mean() / (reference_values.mean() + 1e-12)),
        "bootstrap_ci_low": low,
        "bootstrap_ci_high": high,
        "wilcoxon_p": p_value,
        "effect_size_dz": float(diff.mean() / (diff.std(ddof=1) + 1e-12)),
    }


def aubrc_significance(input_dir: Path, samples: int) -> list[dict[str, object]]:
    rows = read_csv(input_dir / "cost_risk_aubrc_detail.csv")
    keyed = {
        (row["model"], int(row["model_seed"]), row["customer_set"]): row for row in rows
    }
    metrics = [
        "common_risk_aubrc",
        "cvar90_aubrc",
        "load_risk_aubrc",
    ]
    result: list[dict[str, object]] = []
    for metric in metrics:
        block: list[dict[str, object]] = []
        p_values: list[float] = []
        for customer_set in ("A", "B"):
            target = np.asarray(
                [
                    float(keyed[(TARGET, seed, customer_set)][metric])
                    for seed in range(10)
                ],
                dtype=float,
            )
            reference = np.asarray(
                [
                    float(keyed[(REFERENCE, seed, customer_set)][metric])
                    for seed in range(10)
                ],
                dtype=float,
            )
            out = {
                "scope": f"Set {customer_set}",
                "metric": metric,
                **paired_test(target, reference, samples, seed=20260711),
            }
            block.append(out)
            p_values.append(float(out["wilcoxon_p"]))

        for seed in range(10):
            target_avg = np.mean(
                [
                    float(keyed[(TARGET, seed, customer_set)][metric])
                    for customer_set in ("A", "B")
                ]
            )
            reference_avg = np.mean(
                [
                    float(keyed[(REFERENCE, seed, customer_set)][metric])
                    for customer_set in ("A", "B")
                ]
            )
            if seed == 0:
                target_avg_values = []
                reference_avg_values = []
            target_avg_values.append(target_avg)
            reference_avg_values.append(reference_avg)
        out = {
            "scope": "Average(A,B)",
            "metric": metric,
            **paired_test(
                np.asarray(target_avg_values, dtype=float),
                np.asarray(reference_avg_values, dtype=float),
                samples,
                seed=20260712,
            ),
        }
        block.append(out)
        p_values.append(float(out["wilcoxon_p"]))

        for row, p_adj in zip(block, paper.holm_adjust(p_values)):
            row["holm_p"] = p_adj
            row["significant_0p05"] = p_adj < 0.05
            result.append(row)
    return result


def risk20_significance(input_dir: Path, samples: int) -> list[dict[str, object]]:
    rows = read_csv(input_dir / "fixed_budget_risk_detail.csv")
    keyed = {
        (row["model"], int(row["model_seed"]), row["customer_set"], float(row["budget"])): row
        for row in rows
    }
    metrics = [
        "common_global_risk_mean",
        "common_global_cvar90_mean",
        "load_global_risk_mean",
        "common_top10_burden_share_mean",
    ]
    result: list[dict[str, object]] = []
    for metric in metrics:
        block: list[dict[str, object]] = []
        p_values: list[float] = []
        for customer_set in ("A", "B"):
            target = np.asarray(
                [
                    float(keyed[(TARGET, seed, customer_set, 0.20)][metric])
                    for seed in range(10)
                ],
                dtype=float,
            )
            reference = np.asarray(
                [
                    float(keyed[(REFERENCE, seed, customer_set, 0.20)][metric])
                    for seed in range(10)
                ],
                dtype=float,
            )
            out = {
                "scope": f"Set {customer_set}",
                "budget": 0.20,
                "metric": metric,
                **paired_test(target, reference, samples, seed=20260713),
            }
            block.append(out)
            p_values.append(float(out["wilcoxon_p"]))

        target_avg_values = []
        reference_avg_values = []
        for seed in range(10):
            target_avg_values.append(
                np.mean(
                    [
                        float(keyed[(TARGET, seed, customer_set, 0.20)][metric])
                        for customer_set in ("A", "B")
                    ]
                )
            )
            reference_avg_values.append(
                np.mean(
                    [
                        float(keyed[(REFERENCE, seed, customer_set, 0.20)][metric])
                        for customer_set in ("A", "B")
                    ]
                )
            )
        out = {
            "scope": "Average(A,B)",
            "budget": 0.20,
            "metric": metric,
            **paired_test(
                np.asarray(target_avg_values, dtype=float),
                np.asarray(reference_avg_values, dtype=float),
                samples,
                seed=20260714,
            ),
        }
        block.append(out)
        p_values.append(float(out["wilcoxon_p"]))

        for row, p_adj in zip(block, paper.holm_adjust(p_values)):
            row["holm_p"] = p_adj
            row["significant_0p05"] = p_adj < 0.05
            result.append(row)
    return result


def summary_subset(input_dir: Path) -> list[dict[str, object]]:
    auc_rows = read_csv(input_dir / "cost_risk_aubrc_summary.csv")
    fixed_rows = read_csv(input_dir / "fixed_budget_risk_summary.csv")
    result: list[dict[str, object]] = []
    for model in (TARGET, REFERENCE):
        for customer_set in ("A", "B"):
            auc = next(
                row
                for row in auc_rows
                if row["model"] == model and row["customer_set"] == customer_set
            )
            fixed = next(
                row
                for row in fixed_rows
                if row["model"] == model
                and row["customer_set"] == customer_set
                and abs(float(row["budget"]) - 0.20) < 1e-12
            )
            result.append(
                {
                    "model": model,
                    "customer_set": customer_set,
                    "common_risk_aubrc": float(auc["common_risk_aubrc_mean"]),
                    "cvar90_aubrc": float(auc["cvar90_aubrc_mean"]),
                    "load_risk_aubrc": float(auc["load_risk_aubrc_mean"]),
                    "risk20": float(fixed["common_global_risk_mean_mean"]),
                    "cvar90_20": float(fixed["common_global_cvar90_mean_mean"]),
                    "load_risk20": float(fixed["load_global_risk_mean_mean"]),
                    "top10_share20": float(fixed["common_top10_burden_share_mean_mean"]),
                    "edge_gini20": float(fixed["common_edge_burden_gini_used_mean_mean"]),
                    "max_vehicle_risk20": float(fixed["common_max_vehicle_risk_mean_mean"]),
                }
            )
    return result


def checkpoint_path(model: str, checkpoint_dir: Path) -> Path:
    if model == TARGET:
        return checkpoint_dir / "sgformer_teg_gate_splitB_seed0_epochs50_paper_teg_gate_fusions_10seed.pt"
    if model == REFERENCE:
        return checkpoint_dir / "stable_tail_gnn_splitB_seed0_epochs50_paper_comparison_10seed.pt"
    raise ValueError(model)


def load_model_from_checkpoint(path: Path) -> tuple[training.RiskModel, dict[str, object], int]:
    checkpoint = torch.load(path, map_location="cpu", weights_only=False)
    config = dict(checkpoint["model_config"])
    model = training.RiskModel(**config)
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()
    param_count = int(sum(param.numel() for param in model.parameters()))
    return model, config, param_count


def synthetic_graph(config: dict[str, object], risk_dir: Path) -> training.GraphData:
    node_npz = np.load(risk_dir / "data_2021_node_risk.npz")
    edge_npz = np.load(risk_dir / "data_2021_edge_risk.npz")
    num_nodes = int(node_npz["scores"].shape[0])
    x = torch.randn(num_nodes, int(config["in_dim"]), dtype=torch.float32)
    y = torch.ones(num_nodes, dtype=torch.long)
    edge_index = torch.as_tensor(
        np.stack([edge_npz["src"], edge_npz["dst"]], axis=0),
        dtype=torch.long,
    )
    edge_weight = torch.as_tensor(edge_npz["w_norm"], dtype=torch.float32)
    return training.GraphData(
        year="synthetic_data_2021_shape",
        x=x,
        y=y,
        edge_index=edge_index,
        edge_weight=edge_weight,
        labeled_idx=np.arange(num_nodes),
    )


def time_call(fn, repeats: int, warmup: int) -> tuple[float, float]:
    for _ in range(warmup):
        fn()
    values = []
    for _ in range(repeats):
        start = time.perf_counter()
        fn()
        values.append((time.perf_counter() - start) * 1000.0)
    arr = np.asarray(values, dtype=float)
    return float(arr.mean()), float(arr.std(ddof=1)) if arr.size > 1 else 0.0


def complexity_rows(args: argparse.Namespace) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    torch.set_num_threads(1)
    for model_name in (TARGET, REFERENCE):
        path = checkpoint_path(model_name, args.checkpoint_dir)
        model, config, param_count = load_model_from_checkpoint(path)
        graph = synthetic_graph(config, args.risk_dir)
        labels = torch.randint(0, training.NUM_CLASSES, (graph.x.shape[0],), dtype=torch.long)

        with torch.no_grad():
            forward_mean, forward_std = time_call(
                lambda: model(graph),
                repeats=args.benchmark_repeats,
                warmup=args.benchmark_warmup,
            )

        optimizer = torch.optim.SGD(model.parameters(), lr=0.0)

        def train_step() -> None:
            optimizer.zero_grad(set_to_none=True)
            logits = model(graph)
            loss = torch.nn.functional.cross_entropy(logits, labels)
            loss.backward()

        train_step_mean, train_step_std = time_call(
            train_step,
            repeats=max(10, args.benchmark_repeats // 5),
            warmup=max(3, args.benchmark_warmup // 2),
        )
        rows.append(
            {
                "model": model_name,
                "seed_for_checkpoint": 0,
                "parameters": param_count,
                "checkpoint_size_mb": path.stat().st_size / (1024.0 * 1024.0),
                "hidden_dim": config["hidden_dim"],
                "in_dim": config["in_dim"],
                "benchmark_nodes": int(graph.x.shape[0]),
                "benchmark_edges": int(graph.edge_index.shape[1]),
                "cpu_threads": torch.get_num_threads(),
                "forward_ms_mean": forward_mean,
                "forward_ms_std": forward_std,
                "train_step_ms_mean": train_step_mean,
                "train_step_ms_std": train_step_std,
                "gpu_peak_memory_mb": "",
                "gpu_peak_memory_note": "not available; experiment ran in current CPU-only benchmark without CUDA memory logging",
            }
        )
    keyed = {row["model"]: row for row in rows}
    if TARGET in keyed and REFERENCE in keyed:
        keyed[TARGET]["param_ratio_vs_stable"] = (
            float(keyed[TARGET]["parameters"]) / float(keyed[REFERENCE]["parameters"])
        )
        keyed[TARGET]["forward_time_ratio_vs_stable"] = (
            float(keyed[TARGET]["forward_ms_mean"]) / float(keyed[REFERENCE]["forward_ms_mean"])
        )
        keyed[TARGET]["train_step_time_ratio_vs_stable"] = (
            float(keyed[TARGET]["train_step_ms_mean"]) / float(keyed[REFERENCE]["train_step_ms_mean"])
        )
        keyed[REFERENCE]["param_ratio_vs_stable"] = 1.0
        keyed[REFERENCE]["forward_time_ratio_vs_stable"] = 1.0
        keyed[REFERENCE]["train_step_time_ratio_vs_stable"] = 1.0
    return rows


def write_report(
    path: Path,
    summary: list[dict[str, object]],
    aubrc_sig: list[dict[str, object]],
    risk20_sig: list[dict[str, object]],
    complexity: list[dict[str, object]],
) -> None:
    def fmt(value: object, digits: int = 4) -> str:
        if value == "":
            return ""
        return f"{float(value):.{digits}f}"

    def pct(value: object) -> str:
        return f"{100 * float(value):.2f}%"

    lines = [
        "# SGFormer-TEG-Gate vs Stable-Tail GNN focused analysis",
        "",
        "Positive `reference - target` means SGFormer-TEG-Gate is lower/better.",
        "",
        "## AUBRC / Risk@20 / burden summary",
        "",
        "| Model | Set | Common AUBRC | CVaR AUBRC | LoadRisk AUBRC | Risk@20 | CVaR@20 | LoadRisk@20 | Top10 share@20 |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            f"| {row['model']} | {row['customer_set']} | {fmt(row['common_risk_aubrc'])} | "
            f"{fmt(row['cvar90_aubrc'])} | {fmt(row['load_risk_aubrc'])} | "
            f"{fmt(row['risk20'])} | {fmt(row['cvar90_20'])} | "
            f"{fmt(row['load_risk20'])} | {pct(row['top10_share20'])} |"
        )

    lines.extend(
        [
            "",
            "## Paired significance: AUBRC",
            "",
            "| Scope | Metric | Gate mean | Stable mean | Stable - Gate | Relative | 95% CI | Holm p | Sig |",
            "|---|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in aubrc_sig:
        lines.append(
            f"| {row['scope']} | {row['metric']} | {fmt(row['target_mean'])} | "
            f"{fmt(row['reference_mean'])} | {fmt(row['reference_minus_target_mean'])} | "
            f"{pct(row['relative_improvement'])} | "
            f"[{fmt(row['bootstrap_ci_low'])}, {fmt(row['bootstrap_ci_high'])}] | "
            f"{fmt(row['holm_p'])} | {row['significant_0p05']} |"
        )

    lines.extend(
        [
            "",
            "## Paired significance: B=20%",
            "",
            "| Scope | Metric | Gate mean | Stable mean | Stable - Gate | Relative | 95% CI | Holm p | Sig |",
            "|---|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in risk20_sig:
        lines.append(
            f"| {row['scope']} | {row['metric']} | {fmt(row['target_mean'])} | "
            f"{fmt(row['reference_mean'])} | {fmt(row['reference_minus_target_mean'])} | "
            f"{pct(row['relative_improvement'])} | "
            f"[{fmt(row['bootstrap_ci_low'])}, {fmt(row['bootstrap_ci_high'])}] | "
            f"{fmt(row['holm_p'])} | {row['significant_0p05']} |"
        )

    lines.extend(
        [
            "",
            "## Complexity proxy",
            "",
            "CPU benchmark uses the actual exported 2021 graph shape (5261 nodes, 7647 directed edges), synthetic node features with checkpoint in_dim, one CPU thread, and seed-0 checkpoints.",
            "",
            "| Model | Params | Checkpoint MB | Forward ms | Train-step ms | Param ratio | Forward ratio | Step ratio | GPU memory |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in complexity:
        lines.append(
            f"| {row['model']} | {int(row['parameters'])} | {fmt(row['checkpoint_size_mb'], 3)} | "
            f"{fmt(row['forward_ms_mean'], 3)} ± {fmt(row['forward_ms_std'], 3)} | "
            f"{fmt(row['train_step_ms_mean'], 3)} ± {fmt(row['train_step_ms_std'], 3)} | "
            f"{fmt(row['param_ratio_vs_stable'], 3)} | "
            f"{fmt(row['forward_time_ratio_vs_stable'], 3)} | "
            f"{fmt(row['train_step_time_ratio_vs_stable'], 3)} | not logged |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- SGFormer-TEG-Gate is competitive and improves Set B Common/LoadRisk AUBRC relative to Stable-Tail GNN, but Holm-corrected paired tests do not show significance at 0.05.",
            "- SGFormer-TEG-Gate has substantially more parameters and slower CPU forward/step proxy than Stable-Tail GNN, so Stable-Tail GNN remains the more efficient main model unless Set-B-specific performance is prioritized.",
            "- GPU peak memory was not logged in the original run; reporting it requires a rerun with CUDA memory instrumentation.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary = summary_subset(args.input_dir)
    aubrc_sig = aubrc_significance(args.input_dir, args.bootstrap_samples)
    risk20_sig = risk20_significance(args.input_dir, args.bootstrap_samples)
    complexity = complexity_rows(args)

    write_csv(args.output_dir / "sgformer_gate_vs_stable_summary.csv", summary)
    write_csv(args.output_dir / "sgformer_gate_vs_stable_aubrc_significance.csv", aubrc_sig)
    write_csv(args.output_dir / "sgformer_gate_vs_stable_risk20_significance.csv", risk20_sig)
    write_csv(args.output_dir / "sgformer_gate_vs_stable_complexity.csv", complexity)
    write_report(
        args.output_dir / "sgformer_gate_vs_stable_report.md",
        summary,
        aubrc_sig,
        risk20_sig,
        complexity,
    )
    integrity = {
        "summary_rows": len(summary),
        "aubrc_significance_rows": len(aubrc_sig),
        "risk20_significance_rows": len(risk20_sig),
        "complexity_rows": len(complexity),
        "target": TARGET,
        "reference": REFERENCE,
    }
    (args.output_dir / "integrity.json").write_text(
        json.dumps(integrity, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote focused analysis to {args.output_dir}")
    print(json.dumps(integrity, ensure_ascii=False))


if __name__ == "__main__":
    main()
