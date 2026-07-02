"""Run the downstream extension experiments without retraining models.

The script keeps the 10seed extension results separate from the main 10seed
package. It reuses existing Split-B risk matrices and fixed CVRP instances:

1. beta sensitivity for GCN / TEG-low / Stable-Tail.
2. tail-aware path risk for Stable-Tail.
3. concentration-aware CVRP for Stable-Tail plus lambda=1 checks for GCN/TEG-low.
4. tail-aware + concentration-aware combinations for Stable-Tail.

All route sets are evaluated again with the same common reference risk matrix so
cross-model comparisons stay on one risk scale.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
COMPARE_PYVRP = SCRIPT_DIR / "compare_model_pyvrp.py"
COMMON_EVAL = SCRIPT_DIR / "common_evaluate_pyvrp_routes.py"
TAIL_EXPORT = SCRIPT_DIR / "export_tail_enhanced_risk_matrix.py"

DEFAULT_ROOT = Path(r"D:\PyVRP-main\hazmat_risk_experiments")
DEFAULT_OUTPUTS = DEFAULT_ROOT / "outputs_10seed"
DEFAULT_COMMON_RISK = DEFAULT_OUTPUTS / "risk_matrices" / "common_ensemble4_10seed_floor_0p01"
DEFAULT_META_A = DEFAULT_OUTPUTS / "pyvrp_cvrp" / "fixed_instances_10seed" / "setA" / "pyvrp_cvrp_meta.json"
DEFAULT_META_B = DEFAULT_OUTPUTS / "pyvrp_cvrp" / "fixed_instances_10seed" / "setB" / "pyvrp_cvrp_meta.json"
DEFAULT_PYTHON = Path(r"D:\PyVRP-main\PyVRP-main\.venv\Scripts\python.exe")

MODEL_SPECS = {
    "GCN": "gcn_splitB_seed{seed}_epochs50_10seed_floor_0p01",
    "TEG-low": "teg_gnn_splitB_seed{seed}_epochs50_teg_low_tail_10seed_floor_0p01",
    "Stable-Tail-GNN": "gcn_teg_concat_splitB_seed{seed}_epochs50_10seed_floor_0p01",
}
EPS = 1e-12


def parse_list(value: str, cast=str) -> list:
    return [cast(item.strip()) for item in value.split(",") if item.strip()]


def safe_name(value: str) -> str:
    return (
        value.replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
        .replace(".", "p")
        .replace("+", "plus")
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outputs-root", type=Path, default=DEFAULT_OUTPUTS)
    parser.add_argument("--common-risk-dir", type=Path, default=DEFAULT_COMMON_RISK)
    parser.add_argument("--meta-a", type=Path, default=DEFAULT_META_A)
    parser.add_argument("--meta-b", type=Path, default=DEFAULT_META_B)
    parser.add_argument(
        "--python-executable",
        type=Path,
        default=DEFAULT_PYTHON if DEFAULT_PYTHON.exists() else Path(sys.executable),
        help="Python interpreter with PyVRP installed.",
    )
    parser.add_argument("--stages", default="beta,tail,concentration")
    parser.add_argument("--model-seeds", default="0,1,2,3,4,5,6,7,8,9")
    parser.add_argument("--pyvrp-seeds", default="0,1,2,3,4,5,6,7,8,9")
    parser.add_argument("--max-runtime", type=float, default=10.0)
    parser.add_argument("--tail-etas", default="0.1,0.2,0.3,0.4,0.5")
    parser.add_argument("--tail-betas", default="0,1.0,2.0")
    parser.add_argument("--combo-tail-eta", type=float, default=0.7)
    parser.add_argument(
        "--combo-specs",
        default="2.0:1.0,2.0:2.0,3.0:1.0",
        help="Comma-separated beta:lambda pairs for combo stage.",
    )
    parser.add_argument("--combo-batch-name", default="extension_tail_concentration_combo_10seed")
    parser.add_argument(
        "--combo-common-name",
        default="extension_tail_concentration_combo_common_10seed",
    )
    parser.add_argument("--beta-values", default="0,0.5,1.0,1.5,2.0,3.0")
    parser.add_argument("--lambda-values", default="0,0.5,1.0,2.0")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
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


def write_md_table(path: Path, rows: list[dict[str, object]], title: str) -> None:
    if not rows:
        path.write_text(f"# {title}\n\nNo rows.\n", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    lines = [f"# {title}", "", "| " + " | ".join(fields) + " |", "|" + "---|" * len(fields)]
    for row in rows:
        values = []
        for field in fields:
            value = row[field]
            if isinstance(value, float):
                values.append(f"{value:.6f}")
            else:
                values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    path.write_text("\n".join(lines), encoding="utf-8")


def run_command(cmd: list[str], dry_run: bool) -> None:
    print(" ".join(cmd))
    if dry_run:
        return
    completed = subprocess.run(cmd, text=True, check=False)
    if completed.returncode != 0:
        raise RuntimeError(f"Command failed with return code {completed.returncode}: {' '.join(cmd)}")


def model_risk_dir(outputs_root: Path, model: str, seed: int) -> Path:
    return outputs_root / "risk_matrices" / MODEL_SPECS[model].format(seed=seed)


def tail_name(eta: float, seed: int) -> str:
    eta_label = f"{eta:.2f}".rstrip("0").rstrip(".").replace(".", "p")
    return f"stable_tail_eta{eta_label}_splitB_seed{seed}_10seed_floor_0p01"


def run_compare_chunk(
    args: argparse.Namespace,
    label: str,
    risk_dir: Path,
    batch_name: str,
    betas: str,
    lambdas: str,
    tail_risk_eta: float = 0.0,
) -> Path:
    pyvrp_root = args.outputs_root / "pyvrp_cvrp"
    chunk_summary = pyvrp_root / batch_name / "model_pyvrp_summary.csv"
    if chunk_summary.exists() and not args.force:
        print(f"[skip] {chunk_summary}")
        return pyvrp_root / batch_name
    cmd = [
        str(args.python_executable),
        "-B",
        str(COMPARE_PYVRP),
        f"{label}={risk_dir}",
        "--output-dir",
        str(pyvrp_root),
        "--meta-a",
        str(args.meta_a),
        "--meta-b",
        str(args.meta_b),
        "--customer-sets",
        "A,B",
        "--betas",
        betas,
        "--lambda-concentration",
        lambdas,
        "--tail-risk-eta",
        str(tail_risk_eta),
        "--seeds",
        args.pyvrp_seeds,
        "--max-runtime",
        str(args.max_runtime),
        "--batch-name",
        batch_name,
    ]
    run_command(cmd, args.dry_run)
    return pyvrp_root / batch_name


def merge_chunk_summaries(batch_dir: Path, chunk_dirs: Iterable[Path]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for chunk_dir in chunk_dirs:
        summary_path = chunk_dir / "model_pyvrp_summary.csv"
        if summary_path.exists():
            rows.extend(read_csv(summary_path))
    write_csv(batch_dir / "model_pyvrp_summary.csv", rows)
    return rows


def route_run_list(batch_dir: Path, summary_rows: list[dict[str, object]]) -> Path:
    sources: dict[str, Path] = {}
    for row in summary_rows:
        label = str(row["risk_source"])
        run_name = str(row["run_name"])
        customer_set = str(row["customer_set"])
        # Keep set in the label because Set A and Set B use different fixed instances.
        sources[f"{customer_set}_{label}"] = batch_dir.parent / run_name
    rows = [{"label": label, "run_dir": str(path)} for label, path in sorted(sources.items())]
    path = batch_dir / "common_eval_run_list.csv"
    write_csv(path, rows)
    return path


def run_common_eval(
    args: argparse.Namespace,
    batch_dir: Path,
    summary_rows: list[dict[str, object]],
    batch_name: str,
    betas: str,
) -> Path:
    run_list = route_run_list(batch_dir, summary_rows)
    common_dir = args.outputs_root / "pyvrp_cvrp" / batch_name
    common_summary = common_dir / "common_route_summary.csv"
    if common_summary.exists() and not args.force:
        print(f"[skip] {common_summary}")
        return common_dir
    cmd = [
        str(args.python_executable),
        "-B",
        str(COMMON_EVAL),
        "--run-list",
        str(run_list),
        "--common-risk-dir",
        str(args.common_risk_dir),
        "--output-dir",
        str(args.outputs_root / "pyvrp_cvrp"),
        "--batch-name",
        batch_name,
        "--betas",
        betas,
    ]
    run_command(cmd, args.dry_run)
    return common_dir


def parse_source(source: str) -> tuple[str, int | None]:
    clean = source
    if clean.startswith("A_") or clean.startswith("B_"):
        clean = clean[2:]
    for model in ["Stable-Tail-GNN", "TEG-low", "GCN"]:
        prefix = f"{model}_seed"
        if clean.startswith(prefix):
            return model, int(clean[len(prefix) :])
    if clean.startswith("Stable-Tail-eta"):
        left, _, seed_part = clean.partition("_seed")
        return left, int(seed_part) if seed_part else None
    if "_seed" in clean:
        left, _, seed_part = clean.rpartition("_seed")
        try:
            return left, int(seed_part)
        except ValueError:
            return clean, None
    return clean, None


def parse_combo_specs(value: str) -> list[tuple[float, float]]:
    combos: list[tuple[float, float]] = []
    for item in value.split(","):
        text = item.strip()
        if not text:
            continue
        if ":" not in text:
            raise ValueError(f"Combo spec must use beta:lambda, got {text!r}")
        beta, lam = text.split(":", 1)
        combos.append((float(beta), float(lam)))
    return combos


def mean_std(values: list[float]) -> tuple[float, float]:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return math.nan, math.nan
    return float(arr.mean()), float(arr.std(ddof=1)) if arr.size > 1 else 0.0


def summarize_common_beta(common_dir: Path, self_rows: list[dict[str, object]], out_prefix: str) -> list[dict[str, object]]:
    common_rows = read_csv(common_dir / "common_route_summary.csv")
    self_lookup: dict[tuple[str, str, float, float], float] = {}
    for row in self_rows:
        key = (
            str(row["risk_source"]),
            str(row["customer_set"]),
            float(row["beta"]),
            float(row.get("lambda_concentration", 0.0)),
        )
        self_lookup[key] = float(row.get("cost_increase_pct", 0.0))

    per_seed: list[dict[str, object]] = []
    base_risk: dict[tuple[str, str], float] = {}
    for row in common_rows:
        model, model_seed = parse_source(str(row["risk_source"]))
        beta = float(row["beta"])
        lam = float(row.get("lambda_concentration", 0.0))
        customer_set = str(row["customer_set"])
        if abs(beta) < 1e-9 and abs(lam) < 1e-9:
            base_risk[(str(row["risk_source"]), customer_set)] = float(
                row["common_global_risk_mean"]
            )
        cost_key = (str(row["risk_source"])[2:], customer_set, beta, lam)
        per_seed.append(
            {
                "model": model,
                "model_seed": model_seed,
                "customer_set": customer_set,
                "beta": beta,
                "lambda_concentration": lam,
                "cost_increase_pct": self_lookup.get(cost_key, math.nan),
                "common_global_risk": float(row["common_global_risk_mean"]),
                "common_global_cvar90": float(row["common_global_cvar90_mean"]),
                "common_max_vehicle_risk": float(row["common_max_vehicle_risk_mean"]),
                "common_edge_burden_gini_used": float(row["common_edge_burden_gini_used_mean"]),
                "common_top10_burden_share": float(row["common_top10_burden_share_mean"]),
            }
        )
    for row in per_seed:
        key = (
            f"{row['customer_set']}_{row['model']}_seed{row['model_seed']}",
            str(row["customer_set"]),
        )
        base = base_risk.get(key, math.nan)
        row["common_risk_reduction_pct"] = (base - float(row["common_global_risk"])) / (base + EPS)

    grouped: dict[tuple[str, str, float, float], list[dict[str, object]]] = defaultdict(list)
    for row in per_seed:
        grouped[
            (
                str(row["model"]),
                str(row["customer_set"]),
                float(row["beta"]),
                float(row["lambda_concentration"]),
            )
        ].append(row)

    summary: list[dict[str, object]] = []
    metrics = [
        "cost_increase_pct",
        "common_risk_reduction_pct",
        "common_global_risk",
        "common_global_cvar90",
        "common_max_vehicle_risk",
        "common_edge_burden_gini_used",
        "common_top10_burden_share",
    ]
    for (model, customer_set, beta, lam), group in sorted(grouped.items()):
        out: dict[str, object] = {
            "model": model,
            "customer_set": customer_set,
            "beta": beta,
            "lambda_concentration": lam,
            "model_seeds": len(group),
        }
        for metric in metrics:
            avg, std = mean_std([float(row[metric]) for row in group])
            out[f"{metric}_mean"] = avg
            out[f"{metric}_std"] = std
        summary.append(out)

    write_csv(common_dir / f"{out_prefix}_per_seed.csv", per_seed)
    write_csv(common_dir / f"{out_prefix}_summary.csv", summary)
    write_md_table(common_dir / f"{out_prefix}_summary.md", summary, out_prefix.replace("_", " ").title())
    return summary


def summarize_lambda_improvements(common_dir: Path, self_rows: list[dict[str, object]], out_prefix: str) -> list[dict[str, object]]:
    common_rows = read_csv(common_dir / "common_route_summary.csv")
    self_cost: dict[tuple[str, str, float, float], float] = {}
    for row in self_rows:
        self_cost[
            (
                str(row["risk_source"]),
                str(row["customer_set"]),
                float(row["beta"]),
                float(row.get("lambda_concentration", 0.0)),
            )
        ] = float(row.get("cost_increase_pct", 0.0))

    by_key: dict[tuple[str, str, float, float], dict[str, str]] = {}
    for row in common_rows:
        by_key[
            (
                str(row["risk_source"]),
                str(row["customer_set"]),
                float(row["beta"]),
                float(row.get("lambda_concentration", 0.0)),
            )
        ] = row

    rows: list[dict[str, object]] = []
    for key, row in by_key.items():
        source, customer_set, beta, lam = key
        if abs(beta - 1.0) > 1e-9 or abs(lam) < 1e-9:
            continue
        base = by_key.get((source, customer_set, beta, 0.0))
        if base is None:
            continue
        model, model_seed = parse_source(source)
        rows.append(
            {
                "model": model,
                "model_seed": model_seed,
                "customer_set": customer_set,
                "lambda_concentration": lam,
                "risk_improvement_pct": (
                    float(base["common_global_risk_mean"]) - float(row["common_global_risk_mean"])
                )
                / (float(base["common_global_risk_mean"]) + EPS),
                "cvar90_improvement_pct": (
                    float(base["common_global_cvar90_mean"]) - float(row["common_global_cvar90_mean"])
                )
                / (float(base["common_global_cvar90_mean"]) + EPS),
                "max_vehicle_risk_improvement_pct": (
                    float(base["common_max_vehicle_risk_mean"]) - float(row["common_max_vehicle_risk_mean"])
                )
                / (float(base["common_max_vehicle_risk_mean"]) + EPS),
                "edge_gini_improvement_pct": (
                    float(base["common_edge_burden_gini_used_mean"]) - float(row["common_edge_burden_gini_used_mean"])
                )
                / (float(base["common_edge_burden_gini_used_mean"]) + EPS),
                "top10_share_improvement_pct": (
                    float(base["common_top10_burden_share_mean"]) - float(row["common_top10_burden_share_mean"])
                )
                / (float(base["common_top10_burden_share_mean"]) + EPS),
                "extra_cost_percentage_points": self_cost.get((source[2:], customer_set, beta, lam), math.nan)
                - self_cost.get((source[2:], customer_set, beta, 0.0), math.nan),
            }
        )

    grouped: dict[tuple[str, str, float], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["model"]), str(row["customer_set"]), float(row["lambda_concentration"]))].append(row)

    summary: list[dict[str, object]] = []
    metrics = [
        "risk_improvement_pct",
        "cvar90_improvement_pct",
        "max_vehicle_risk_improvement_pct",
        "edge_gini_improvement_pct",
        "top10_share_improvement_pct",
        "extra_cost_percentage_points",
    ]
    for (model, customer_set, lam), group in sorted(grouped.items()):
        out: dict[str, object] = {
            "model": model,
            "customer_set": customer_set,
            "lambda_concentration": lam,
            "model_seeds": len(group),
        }
        for metric in metrics:
            avg, std = mean_std([float(row[metric]) for row in group])
            out[f"{metric}_mean"] = avg
            out[f"{metric}_std"] = std
        summary.append(out)

    write_csv(common_dir / f"{out_prefix}_per_seed.csv", rows)
    write_csv(common_dir / f"{out_prefix}_summary.csv", summary)
    write_md_table(common_dir / f"{out_prefix}_summary.md", summary, out_prefix.replace("_", " ").title())
    return summary


def export_tail_risk(args: argparse.Namespace, eta: float, seed: int) -> Path:
    out_name = tail_name(eta, seed)
    out_dir = args.outputs_root / "risk_matrices" / out_name
    if (out_dir / "export_summary.json").exists() and not args.force:
        print(f"[skip] {out_dir}")
        return out_dir
    cmd = [
        str(args.python_executable),
        "-B",
        str(TAIL_EXPORT),
        "--base-risk-dir",
        str(model_risk_dir(args.outputs_root, "Stable-Tail-GNN", seed)),
        "--eta",
        str(eta),
        "--output-dir",
        str(args.outputs_root / "risk_matrices"),
        "--name",
        out_name,
    ]
    run_command(cmd, args.dry_run)
    return out_dir


def stage_beta(args: argparse.Namespace) -> None:
    seeds = parse_list(args.model_seeds, int)
    batch_root = args.outputs_root / "pyvrp_cvrp" / "extension_beta_sensitivity_10seed"
    batch_root.mkdir(parents=True, exist_ok=True)
    chunk_dirs = []
    for model in ["GCN", "TEG-low", "Stable-Tail-GNN"]:
        for seed in seeds:
            label = f"{model}_seed{seed}"
            batch_name = f"extension_beta_sensitivity_10seed_{safe_name(label)}"
            chunk_dirs.append(
                run_compare_chunk(
                    args,
                    label,
                    model_risk_dir(args.outputs_root, model, seed),
                    batch_name,
                    args.beta_values,
                    "0",
                )
            )
    rows = merge_chunk_summaries(batch_root, chunk_dirs)
    common_dir = run_common_eval(
        args,
        batch_root,
        rows,
        "extension_beta_sensitivity_common_10seed",
        args.beta_values,
    )
    if args.dry_run:
        return
    summarize_common_beta(common_dir, rows, "extension_beta_sensitivity_common")


def stage_tail(args: argparse.Namespace) -> None:
    seeds = parse_list(args.model_seeds, int)
    etas = parse_list(args.tail_etas, float)
    batch_root = args.outputs_root / "pyvrp_cvrp" / "extension_tail_aware_path_risk_10seed"
    batch_root.mkdir(parents=True, exist_ok=True)
    chunk_dirs = []
    for eta in etas:
        for seed in seeds:
            risk_dir = export_tail_risk(args, eta, seed)
            eta_label = f"{eta:.2f}".rstrip("0").rstrip(".")
            label = f"Stable-Tail-eta{eta_label}_seed{seed}"
            batch_name = f"extension_tail_aware_10seed_{safe_name(label)}"
            chunk_dirs.append(
                run_compare_chunk(args, label, risk_dir, batch_name, args.tail_betas, "0")
            )
    rows = merge_chunk_summaries(batch_root, chunk_dirs)
    common_dir = run_common_eval(
        args,
        batch_root,
        rows,
        "extension_tail_aware_common_10seed",
        args.tail_betas,
    )
    if args.dry_run:
        return
    summarize_common_beta(common_dir, rows, "extension_tail_aware_common")


def stage_concentration(args: argparse.Namespace) -> None:
    seeds = parse_list(args.model_seeds, int)
    batch_root = args.outputs_root / "pyvrp_cvrp" / "extension_concentration_aware_10seed"
    batch_root.mkdir(parents=True, exist_ok=True)
    chunk_dirs = []
    for seed in seeds:
        stable_label = f"Stable-Tail-GNN_seed{seed}"
        chunk_dirs.append(
            run_compare_chunk(
                args,
                stable_label,
                model_risk_dir(args.outputs_root, "Stable-Tail-GNN", seed),
                f"extension_concentration_10seed_{safe_name(stable_label)}",
                "0,1.0",
                args.lambda_values,
            )
        )
        for model in ["GCN", "TEG-low"]:
            label = f"{model}_seed{seed}"
            chunk_dirs.append(
                run_compare_chunk(
                    args,
                    label,
                    model_risk_dir(args.outputs_root, model, seed),
                    f"extension_concentration_lambda1_10seed_{safe_name(label)}",
                    "0,1.0",
                    "0,1.0",
                )
            )
    rows = merge_chunk_summaries(batch_root, chunk_dirs)
    common_dir = run_common_eval(
        args,
        batch_root,
        rows,
        "extension_concentration_common_10seed",
        "1.0",
    )
    if args.dry_run:
        return
    summarize_common_beta(common_dir, rows, "extension_concentration_common")
    summarize_lambda_improvements(common_dir, rows, "extension_concentration_improvements")


def stage_combo(args: argparse.Namespace) -> None:
    seeds = parse_list(args.model_seeds, int)
    eta = args.combo_tail_eta
    combos = parse_combo_specs(args.combo_specs)
    batch_root = args.outputs_root / "pyvrp_cvrp" / args.combo_batch_name
    batch_root.mkdir(parents=True, exist_ok=True)
    chunk_dirs = []
    for seed in seeds:
        risk_dir = model_risk_dir(args.outputs_root, "Stable-Tail-GNN", seed)
        for beta, lam in combos:
            label = f"Stable-Tail-combo-eta{eta:g}-b{beta:g}-l{lam:g}_seed{seed}"
            batch_name = f"{args.combo_batch_name}_{safe_name(label)}"
            chunk_dirs.append(
                run_compare_chunk(
                    args,
                    label,
                    risk_dir,
                    batch_name,
                    f"0,{beta:g}",
                    f"{lam:g}",
                    tail_risk_eta=eta,
                )
            )
    rows = merge_chunk_summaries(batch_root, chunk_dirs)
    common_dir = run_common_eval(
        args,
        batch_root,
        rows,
        args.combo_common_name,
        ",".join(["0"] + [f"{beta:g}" for beta, _ in combos]),
    )
    if args.dry_run:
        return
    summarize_common_beta(common_dir, rows, "extension_tail_concentration_combo_common")


def main() -> None:
    args = parse_args()
    stages = set(parse_list(args.stages, str))
    if "beta" in stages:
        stage_beta(args)
    if "tail" in stages:
        stage_tail(args)
    if "concentration" in stages:
        stage_concentration(args)
    if "combo" in stages:
        stage_combo(args)


if __name__ == "__main__":
    main()
