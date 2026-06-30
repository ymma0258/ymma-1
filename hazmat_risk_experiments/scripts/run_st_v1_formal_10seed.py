"""Run the isolated formal 10seed pipeline for the selected ST-v1 model."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
PYTHON = sys.executable
OUTPUT_ROOT = ROOT / "outputs_10seed" / "st_v1_formal_10seed"
ZIP_PATH = Path(r"D:\城市危险化学品运输车辆轨迹数据.zip")
SEEDS = "0,1,2,3,4,5,6,7,8,9"
FIXED_OD = ROOT / "outputs_10seed" / "od_paths" / "fixed_od_pairs_150.csv"
COMMON_RISK = ROOT / "outputs_10seed" / "risk_matrices" / "common_ensemble4_10seed_floor_0p01"
FIXED_INSTANCES = ROOT / "outputs_10seed" / "pyvrp_cvrp" / "fixed_instances_10seed"
TAG = "st_v1_formal_10seed"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=OUTPUT_ROOT)
    parser.add_argument("--zip", type=Path, default=ZIP_PATH)
    parser.add_argument("--seeds", default=SEEDS)
    parser.add_argument("--solver-seeds", default=SEEDS)
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--max-runtime", type=float, default=10.0)
    parser.add_argument(
        "--stages",
        default="train,export,od,pyvrp,tc_lite,load_aware,summarize",
    )
    return parser.parse_args()


def parse_seeds(value: str) -> list[int]:
    return [int(item.strip()) for item in value.split(",") if item.strip()]


def run(command: list[str]) -> None:
    print("[cmd]", subprocess.list2cmdline(command), flush=True)
    subprocess.run(command, check=True)


def stem(seed: int, epochs: int) -> str:
    return f"gcn_teg_concat_splitB_seed{seed}_epochs{epochs}_{TAG}"


def risk_dir(args: argparse.Namespace, seed: int) -> Path:
    return args.root / "risk_matrices" / f"{stem(seed, args.epochs)}_floor_0p01"


def sources(args: argparse.Namespace) -> list[str]:
    return [f"ST-v1_seed{seed}={risk_dir(args, seed)}" for seed in parse_seeds(args.seeds)]


def train_stage(args: argparse.Namespace) -> None:
    out = args.root / "models"
    run(
        [
            PYTHON,
            "-B",
            str(SCRIPT_DIR / "run_model_experiments.py"),
            "--zip",
            str(args.zip),
            "--output-dir",
            str(out),
            "--checkpoint-dir",
            str(out / "checkpoints"),
            "--models",
            "gcn_teg_concat",
            "--splits",
            "B",
            "--seeds",
            args.seeds,
            "--epochs",
            str(args.epochs),
            "--alpha-ord",
            "0.3",
            "--alpha-hr",
            "0.5",
            "--alpha-topk",
            "0.1",
            "--topk-frac",
            "0.2",
            "--split-b-val-fraction",
            "0",
            "--checkpoint-selection",
            "last",
            "--edge-normalization",
            "per_year",
            "--experiment-tag",
            TAG,
            "--batch-name",
            "st_v1_node_eval_10seed",
        ]
    )


def export_stage(args: argparse.Namespace) -> None:
    out = args.root / "risk_matrices"
    for seed in parse_seeds(args.seeds):
        run(
            [
                PYTHON,
                "-B",
                str(SCRIPT_DIR / "export_risk_matrix.py"),
                "--zip",
                str(args.zip),
                "--output-dir",
                str(out),
                "--checkpoint",
                str(args.root / "models" / "checkpoints" / f"{stem(seed, args.epochs)}.pt"),
                "--risk-mode",
                "exposure_floor",
                "--exposure-delta",
                "0.01",
                "--experiment-tag",
                TAG,
            ]
        )


def od_stage(args: argparse.Namespace) -> None:
    run(
        [
            PYTHON,
            "-B",
            str(SCRIPT_DIR / "compare_model_od_paths.py"),
            *sources(args),
            "--pairs",
            str(FIXED_OD),
            "--output-dir",
            str(args.root / "od_paths"),
            "--batch-name",
            "st_v1_fixed150_10seed",
            "--k-paths",
            "50",
            "--cvar-alpha",
            "0.9",
            "--re-threshold",
            "p75",
        ]
    )


def compare_pyvrp(
    args: argparse.Namespace,
    batch: str,
    betas: str,
    lam: str,
    tail_eta: float,
) -> None:
    run(
        [
            PYTHON,
            "-B",
            str(SCRIPT_DIR / "compare_model_pyvrp.py"),
            *sources(args),
            "--output-dir",
            str(args.root / "pyvrp_cvrp"),
            "--meta-a",
            str(FIXED_INSTANCES / "setA" / "pyvrp_cvrp_meta.json"),
            "--meta-b",
            str(FIXED_INSTANCES / "setB" / "pyvrp_cvrp_meta.json"),
            "--customer-sets",
            "A,B",
            "--betas",
            betas,
            "--lambda-concentration",
            lam,
            "--tail-risk-eta",
            str(tail_eta),
            "--seeds",
            args.solver_seeds,
            "--max-runtime",
            str(args.max_runtime),
            "--batch-name",
            batch,
        ]
    )


def run_dirs(args: argparse.Namespace, batch: str) -> list[str]:
    result: list[str] = []
    for seed in parse_seeds(args.seeds):
        label = f"ST-v1_seed{seed}"
        for customer_set in ("A", "B"):
            directory = args.root / "pyvrp_cvrp" / f"{batch}_{customer_set}_{label}"
            result.append(f"{label}={directory}")
    return result


def common_eval(
    args: argparse.Namespace,
    source_batch: str,
    output_batch: str,
    beta: float,
    lam: float,
) -> None:
    run(
        [
            PYTHON,
            "-B",
            str(SCRIPT_DIR / "common_evaluate_pyvrp_routes.py"),
            *run_dirs(args, source_batch),
            "--common-risk-dir",
            str(COMMON_RISK),
            "--output-dir",
            str(args.root / "pyvrp_cvrp"),
            "--batch-name",
            output_batch,
            "--beta",
            str(beta),
            "--lambda-concentration",
            str(lam),
        ]
    )


def pyvrp_stage(args: argparse.Namespace) -> None:
    batch = "st_v1_beta1_10seed"
    compare_pyvrp(args, batch, "0,1.0", "0", 0.0)
    common_eval(args, batch, "st_v1_beta1_common_10seed", 1.0, 0.0)


def tc_lite_stage(args: argparse.Namespace) -> None:
    batch = "st_v1_tc_lite_eta0p7_b1p5_l1_10seed"
    compare_pyvrp(args, batch, "0,1.5", "1", 0.7)
    common_eval(args, batch, "st_v1_tc_lite_common_10seed", 1.5, 1.0)


def load_eval(
    args: argparse.Namespace,
    source_batch: str,
    output_batch: str,
    beta: float,
    lam: float,
) -> None:
    run(
        [
            PYTHON,
            "-B",
            str(SCRIPT_DIR / "common_evaluate_load_aware_routes.py"),
            *run_dirs(args, source_batch),
            "--common-risk-dir",
            str(COMMON_RISK),
            "--output-dir",
            str(args.root / "pyvrp_cvrp"),
            "--batch-name",
            output_batch,
            "--betas",
            str(beta),
            "--lambda-concentration",
            str(lam),
        ]
    )


def load_aware_stage(args: argparse.Namespace) -> None:
    load_eval(args, "st_v1_beta1_10seed", "st_v1_beta1_load_aware_common_10seed", 1.0, 0.0)
    load_eval(
        args,
        "st_v1_tc_lite_eta0p7_b1p5_l1_10seed",
        "st_v1_tc_lite_load_aware_common_10seed",
        1.5,
        1.0,
    )


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def mean_std(values: list[float]) -> tuple[float, float]:
    return statistics.mean(values), statistics.stdev(values) if len(values) > 1 else 0.0


def aggregate_by_set(
    rows: list[dict[str, str]], metric_map: dict[str, str]
) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for customer_set in ("A", "B"):
        selected = [row for row in rows if row["customer_set"] == customer_set]
        out: dict[str, object] = {"customer_set": customer_set, "model_seeds": len(selected)}
        for source, target in metric_map.items():
            out[f"{target}_mean"], out[f"{target}_std"] = mean_std(
                [float(row[source]) for row in selected]
            )
        result.append(out)
    return result


def summarize_stage(args: argparse.Namespace) -> None:
    out = args.root / "summary"
    out.mkdir(parents=True, exist_ok=True)
    node_values: dict[str, list[float]] = {
        key: []
        for key in (
            "macro_f1",
            "weighted_f1",
            "mae",
            "qwk",
            "recall_6_8",
            "precision_6_8",
            "pr_auc_high",
            "high_fn_rate",
        )
    }
    risk_values: dict[str, list[float]] = {
        key: []
        for key in (
            "risk_mean",
            "risk_p50",
            "risk_p75",
            "risk_p90",
            "risk_p95",
            "risk_p99",
            "risk_max",
        )
    }
    for seed in parse_seeds(args.seeds):
        model = json.loads(
            (args.root / "models" / f"{stem(seed, args.epochs)}.json").read_text(encoding="utf-8")
        )
        metrics = model["metrics"]["data_2021_test"]
        for key in node_values:
            node_values[key].append(float(metrics[key]))
        risk = json.loads(
            (risk_dir(args, seed) / "export_summary.json").read_text(encoding="utf-8")
        )["risk_summaries"]["data_2021"]
        for key in risk_values:
            risk_values[key].append(float(risk[key]))
    node_row: dict[str, object] = {"model": "ST-v1", "runs": 10}
    for key, values in node_values.items():
        node_row[f"{key}_mean"], node_row[f"{key}_std"] = mean_std(values)
    risk_row: dict[str, object] = {"model": "ST-v1", "runs": 10}
    for key, values in risk_values.items():
        risk_row[f"{key}_mean"], risk_row[f"{key}_std"] = mean_std(values)
    gaps = [p99 - p95 for p99, p95 in zip(risk_values["risk_p99"], risk_values["risk_p95"])]
    risk_row["tail_gap_mean"], risk_row["tail_gap_std"] = mean_std(gaps)
    write_csv(out / "node_risk_summary_10seed.csv", [node_row])
    write_csv(out / "risk_distribution_summary_10seed.csv", [risk_row])

    od_raw = read_csv(args.root / "od_paths" / "st_v1_fixed150_10seed" / "model_od_summary.csv")
    od_selected = [row for row in od_raw if row["method"] == "CVaR-risk"]
    od_row: dict[str, object] = {"model": "ST-v1", "model_seeds": len(od_selected)}
    for source, target in (
        ("hop_increase_pct_mean", "hop_increase"),
        ("total_risk_aggregate_reduction", "total_risk_reduction"),
        ("cvar90_aggregate_reduction", "cvar90_reduction"),
        ("max_risk_aggregate_reduction", "maxrisk_reduction"),
        ("re_aggregate_reduction", "re_reduction"),
    ):
        od_row[f"{target}_mean"], od_row[f"{target}_std"] = mean_std(
            [float(row[source]) for row in od_selected]
        )
    write_csv(out / "od_fixed150_summary_10seed.csv", [od_row])

    common_map = {
        "common_global_risk_mean": "global_risk",
        "common_global_cvar90_mean": "cvar90",
        "common_max_vehicle_risk_mean": "max_vehicle_risk",
        "common_edge_burden_gini_used_mean": "edge_gini",
        "common_top10_burden_share_mean": "top10_share",
    }
    beta_common = aggregate_by_set(
        read_csv(args.root / "pyvrp_cvrp" / "st_v1_beta1_common_10seed" / "common_route_summary.csv"),
        common_map,
    )
    tc_common = aggregate_by_set(
        read_csv(args.root / "pyvrp_cvrp" / "st_v1_tc_lite_common_10seed" / "common_route_summary.csv"),
        common_map,
    )
    for row in beta_common:
        row["method"] = "beta1"
    for row in tc_common:
        row["method"] = "TC-lite eta0.7 beta1.5 lambda1"
    write_csv(out / "pyvrp_common_summary_10seed.csv", beta_common + tc_common)

    self_rows: list[dict[str, object]] = []
    for method, batch, target_beta in (
        ("beta1", "st_v1_beta1_10seed", 1.0),
        (
            "TC-lite eta0.7 beta1.5 lambda1",
            "st_v1_tc_lite_eta0p7_b1p5_l1_10seed",
            1.5,
        ),
    ):
        raw = read_csv(args.root / "pyvrp_cvrp" / batch / "model_pyvrp_summary.csv")
        for customer_set in ("A", "B"):
            selected = [
                row
                for row in raw
                if row["customer_set"] == customer_set
                and abs(float(row["beta"]) - target_beta) < 1e-9
            ]
            item: dict[str, object] = {
                "method": method,
                "customer_set": customer_set,
                "model_seeds": len(selected),
            }
            for source, target in (
                ("cost_increase_pct", "cost_increase"),
                ("risk_reduction_pct", "risk_reduction"),
                ("global_risk_mean", "self_global_risk"),
                ("global_cvar90_mean", "self_cvar90"),
                ("edge_burden_gini_used_mean", "self_edge_gini"),
                ("top10_burden_share_mean", "self_top10_share"),
            ):
                item[f"{target}_mean"], item[f"{target}_std"] = mean_std(
                    [float(row[source]) for row in selected]
                )
            self_rows.append(item)
    write_csv(out / "pyvrp_self_summary_10seed.csv", self_rows)

    load_map = {
        "load_global_risk_mean": "load_global_risk",
        "load_cvar90_mean": "load_cvar90",
        "load_max_vehicle_risk_mean": "load_max_vehicle_risk",
        "load_edge_burden_gini_used_mean": "load_edge_gini",
        "load_top10_burden_share_mean": "load_top10_share",
    }
    beta_load = aggregate_by_set(
        read_csv(
            args.root
            / "pyvrp_cvrp"
            / "st_v1_beta1_load_aware_common_10seed"
            / "load_aware_summary.csv"
        ),
        load_map,
    )
    tc_load = aggregate_by_set(
        read_csv(
            args.root
            / "pyvrp_cvrp"
            / "st_v1_tc_lite_load_aware_common_10seed"
            / "load_aware_summary.csv"
        ),
        load_map,
    )
    for row in beta_load:
        row["method"] = "beta1"
    for row in tc_load:
        row["method"] = "TC-lite eta0.7 beta1.5 lambda1"
    write_csv(out / "load_aware_common_summary_10seed.csv", beta_load + tc_load)

    lines = [
        "# ST-v1 Formal 10seed Results",
        "",
        f"- Node MAE: {node_row['mae_mean']:.4f} +/- {node_row['mae_std']:.4f}",
        f"- Node PR-AUC: {node_row['pr_auc_high_mean']:.4f} +/- {node_row['pr_auc_high_std']:.4f}",
        f"- Recall@6-8: {node_row['recall_6_8_mean']:.4f} +/- {node_row['recall_6_8_std']:.4f}",
        f"- Risk P95/P99/TailGap: {risk_row['risk_p95_mean']:.4f} / {risk_row['risk_p99_mean']:.4f} / {risk_row['tail_gap_mean']:.4f}",
        f"- OD total-risk/CVaR90/MaxRisk reduction: {od_row['total_risk_reduction_mean']:.2%} / {od_row['cvar90_reduction_mean']:.2%} / {od_row['maxrisk_reduction_mean']:.2%}",
        "",
        "## PyVRP Self Evaluation",
        "",
        "| Method | Set | Cost increase | Risk reduction | Global risk | CVaR90 | Edge Gini | Top10 share |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in self_rows:
        lines.append(
            "| {method} | {set_name} | {cost:.2%} | {red:.2%} | {risk:.4f} | {cvar:.4f} | {gini:.4f} | {top:.2%} |".format(
                method=row["method"],
                set_name=row["customer_set"],
                cost=float(row["cost_increase_mean"]),
                red=float(row["risk_reduction_mean"]),
                risk=float(row["self_global_risk_mean"]),
                cvar=float(row["self_cvar90_mean"]),
                gini=float(row["self_edge_gini_mean"]),
                top=float(row["self_top10_share_mean"]),
            )
        )
    lines += [
        "",
        "## Common Evaluation",
        "",
        "| Method | Set | Global risk | CVaR90 | Max vehicle risk | Edge Gini | Top10 share |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in beta_common + tc_common:
        lines.append(
            "| {method} | {set_name} | {risk:.4f} | {cvar:.4f} | {maxrisk:.4f} | {gini:.4f} | {top:.2%} |".format(
                method=row["method"],
                set_name=row["customer_set"],
                risk=float(row["global_risk_mean"]),
                cvar=float(row["cvar90_mean"]),
                maxrisk=float(row["max_vehicle_risk_mean"]),
                gini=float(row["edge_gini_mean"]),
                top=float(row["top10_share_mean"]),
            )
        )
    lines += [
        "",
        "## Load-Aware Common Evaluation",
        "",
        "| Method | Set | Load risk | Load CVaR90 | Max vehicle load risk | Load edge Gini | Load Top10 share |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in beta_load + tc_load:
        lines.append(
            "| {method} | {set_name} | {risk:.4f} | {cvar:.4f} | {maxrisk:.4f} | {gini:.4f} | {top:.2%} |".format(
                method=row["method"],
                set_name=row["customer_set"],
                risk=float(row["load_global_risk_mean"]),
                cvar=float(row["load_cvar90_mean"]),
                maxrisk=float(row["load_max_vehicle_risk_mean"]),
                gini=float(row["load_edge_gini_mean"]),
                top=float(row["load_top10_share_mean"]),
            )
        )
    (out / "st_v1_formal_results_10seed.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    args.root.mkdir(parents=True, exist_ok=True)
    stages = {
        "train": train_stage,
        "export": export_stage,
        "od": od_stage,
        "pyvrp": pyvrp_stage,
        "tc_lite": tc_lite_stage,
        "load_aware": load_aware_stage,
        "summarize": summarize_stage,
    }
    requested = {item.strip() for item in args.stages.split(",") if item.strip()}
    unknown = requested - stages.keys()
    if unknown:
        raise ValueError(f"Unknown stages: {sorted(unknown)}")
    for name, function in stages.items():
        if name in requested:
            print(f"\n=== {name} ===", flush=True)
            function(args)


if __name__ == "__main__":
    main()
