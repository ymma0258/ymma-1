"""Run the isolated Stable-Tail v1/v2 three-seed screening experiment.

The experiment never writes to the formal model/risk/output directories. It
trains four controlled configurations, exports each exact checkpoint, and can
then run fixed-OD and fixed-CVRP downstream validation.
"""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
PYTHON = sys.executable
DEFAULT_ROOT = ROOT / "outputs_10seed" / "stable_tail_v2_pretest_3seed"
DEFAULT_ZIP = Path(r"D:\城市危险化学品运输车辆轨迹数据.zip")
FIXED_OD = ROOT / "outputs_10seed" / "od_paths" / "fixed_od_pairs_150.csv"
COMMON_RISK = (
    ROOT / "outputs_10seed" / "risk_matrices" / "common_ensemble4_10seed_floor_0p01"
)
META_A = (
    ROOT
    / "outputs_10seed"
    / "pyvrp_cvrp"
    / "fixed_instances_10seed"
    / "setA"
    / "pyvrp_cvrp_meta.json"
)
META_B = (
    ROOT
    / "outputs_10seed"
    / "pyvrp_cvrp"
    / "fixed_instances_10seed"
    / "setB"
    / "pyvrp_cvrp_meta.json"
)


@dataclass(frozen=True)
class Configuration:
    name: str
    val_fraction: float
    selection: str
    gate_normalized: bool = False
    feature_standardization: bool = False
    edge_normalization: str = "per_year"


CONFIGS = [
    Configuration("st_v1", 0.0, "last"),
    Configuration("st_v1_best", 0.2, "best"),
    Configuration("st_v2", 0.2, "best", gate_normalized=True),
    Configuration(
        "st_v2_std",
        0.2,
        "best",
        gate_normalized=True,
        feature_standardization=True,
        edge_normalization="shared_train",
    ),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--zip", type=Path, default=DEFAULT_ZIP)
    parser.add_argument("--seeds", default="0,1,2")
    parser.add_argument("--solver-seeds", default="0,1,2")
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--max-runtime", type=float, default=10.0)
    parser.add_argument(
        "--stages",
        default="train,export,od,pyvrp,summarize",
        help="Comma-separated: train,export,od,pyvrp,summarize.",
    )
    return parser.parse_args()


def run(command: list[str]) -> None:
    print("[cmd]", subprocess.list2cmdline(command), flush=True)
    subprocess.run(command, check=True)


def seeds(value: str) -> list[int]:
    return [int(item.strip()) for item in value.split(",") if item.strip()]


def model_stem(config: Configuration, seed: int, epochs: int) -> str:
    return f"gcn_teg_concat_splitB_seed{seed}_epochs{epochs}_{config.name}_3seed"


def risk_dir(root: Path, config: Configuration, seed: int, epochs: int) -> Path:
    return root / "risk_matrices" / f"{model_stem(config, seed, epochs)}_floor_0p01"


def train_stage(args: argparse.Namespace) -> None:
    model_root = args.root / "models"
    model_root.mkdir(parents=True, exist_ok=True)
    for config in CONFIGS:
        command = [
            PYTHON,
            "-B",
            str(SCRIPT_DIR / "run_model_experiments.py"),
            "--zip",
            str(args.zip),
            "--output-dir",
            str(model_root),
            "--checkpoint-dir",
            str(model_root / "checkpoints"),
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
            str(config.val_fraction),
            "--checkpoint-selection",
            config.selection,
            "--checkpoint-min-recall",
            "0.2223",
            "--checkpoint-max-high-fn",
            "0.7777",
            "--edge-normalization",
            config.edge_normalization,
            "--experiment-tag",
            f"{config.name}_3seed",
            "--batch-name",
            f"{config.name}_splitB_3seed",
        ]
        if config.gate_normalized:
            command.append("--gate-normalized")
        if config.feature_standardization:
            command.append("--feature-standardization")
        run(command)


def export_stage(args: argparse.Namespace) -> None:
    checkpoint_root = args.root / "models" / "checkpoints"
    output_root = args.root / "risk_matrices"
    output_root.mkdir(parents=True, exist_ok=True)
    for config in CONFIGS:
        for seed in seeds(args.seeds):
            checkpoint = checkpoint_root / f"{model_stem(config, seed, args.epochs)}.pt"
            if not checkpoint.exists():
                raise FileNotFoundError(checkpoint)
            run(
                [
                    PYTHON,
                    "-B",
                    str(SCRIPT_DIR / "export_risk_matrix.py"),
                    "--zip",
                    str(args.zip),
                    "--output-dir",
                    str(output_root),
                    "--checkpoint",
                    str(checkpoint),
                    "--risk-mode",
                    "exposure_floor",
                    "--exposure-delta",
                    "0.01",
                    "--experiment-tag",
                    f"{config.name}_3seed",
                ]
            )


def source_args(args: argparse.Namespace) -> list[str]:
    return [
        f"{config.name}_seed{seed}={risk_dir(args.root, config, seed, args.epochs)}"
        for config in CONFIGS
        for seed in seeds(args.seeds)
    ]


def od_stage(args: argparse.Namespace) -> None:
    run(
        [
            PYTHON,
            "-B",
            str(SCRIPT_DIR / "compare_model_od_paths.py"),
            *source_args(args),
            "--pairs",
            str(FIXED_OD),
            "--output-dir",
            str(args.root / "od_paths"),
            "--batch-name",
            "stable_tail_v2_fixed150_3seed",
            "--k-paths",
            "50",
            "--cvar-alpha",
            "0.9",
            "--re-threshold",
            "p75",
        ]
    )


def pyvrp_stage(args: argparse.Namespace) -> None:
    output_root = args.root / "pyvrp_cvrp"
    batch = "stable_tail_v2_beta1_3seed"
    run(
        [
            PYTHON,
            "-B",
            str(SCRIPT_DIR / "compare_model_pyvrp.py"),
            *source_args(args),
            "--output-dir",
            str(output_root),
            "--meta-a",
            str(META_A),
            "--meta-b",
            str(META_B),
            "--customer-sets",
            "A,B",
            "--betas",
            "0,1.0",
            "--seeds",
            args.solver_seeds,
            "--max-runtime",
            str(args.max_runtime),
            "--batch-name",
            batch,
        ]
    )
    run_dirs: list[str] = []
    for config in CONFIGS:
        for seed in seeds(args.seeds):
            label = f"{config.name}_seed{seed}"
            for customer_set in ("A", "B"):
                directory = output_root / f"{batch}_{customer_set}_{label}"
                run_dirs.append(f"{label}={directory}")
    run(
        [
            PYTHON,
            "-B",
            str(SCRIPT_DIR / "common_evaluate_pyvrp_routes.py"),
            *run_dirs,
            "--common-risk-dir",
            str(COMMON_RISK),
            "--output-dir",
            str(output_root),
            "--batch-name",
            "stable_tail_v2_common_eval_3seed",
            "--beta",
            "1.0",
            "--lambda-concentration",
            "0",
        ]
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


def summarize_stage(args: argparse.Namespace) -> None:
    summary_root = args.root / "summary"
    summary_root.mkdir(parents=True, exist_ok=True)
    node_rows: list[dict[str, object]] = []
    risk_rows: list[dict[str, object]] = []
    for config in CONFIGS:
        node_values: dict[str, list[float]] = {
            key: [] for key in ("mae", "pr_auc_high", "recall_6_8", "high_fn_rate")
        }
        risk_values: dict[str, list[float]] = {
            key: [] for key in ("risk_mean", "risk_p95", "risk_p99", "tail_gap")
        }
        epochs: list[float] = []
        for seed in seeds(args.seeds):
            model_json = args.root / "models" / f"{model_stem(config, seed, args.epochs)}.json"
            model_payload = json.loads(model_json.read_text(encoding="utf-8"))
            metrics = model_payload["metrics"]["data_2021_test"]
            for key in node_values:
                node_values[key].append(float(metrics[key]))
            epochs.append(float(model_payload["best_epoch"]))

            export = json.loads(
                (risk_dir(args.root, config, seed, args.epochs) / "export_summary.json").read_text(
                    encoding="utf-8"
                )
            )["risk_summaries"]["data_2021"]
            risk_values["risk_mean"].append(float(export["risk_mean"]))
            risk_values["risk_p95"].append(float(export["risk_p95"]))
            risk_values["risk_p99"].append(float(export["risk_p99"]))
            risk_values["tail_gap"].append(
                float(export["risk_p99"]) - float(export["risk_p95"])
            )
        node_row: dict[str, object] = {"configuration": config.name, "runs": len(epochs)}
        node_row["best_epoch_mean"], node_row["best_epoch_std"] = mean_std(epochs)
        for key, values in node_values.items():
            node_row[f"{key}_mean"], node_row[f"{key}_std"] = mean_std(values)
        node_rows.append(node_row)
        risk_row: dict[str, object] = {"configuration": config.name, "runs": len(epochs)}
        for key, values in risk_values.items():
            risk_row[f"{key}_mean"], risk_row[f"{key}_std"] = mean_std(values)
        risk_rows.append(risk_row)

    od_rows_raw = read_csv(
        args.root / "od_paths" / "stable_tail_v2_fixed150_3seed" / "model_od_summary.csv"
    )
    od_rows: list[dict[str, object]] = []
    for config in CONFIGS:
        selected = [
            row
            for row in od_rows_raw
            if row["method"] == "CVaR-risk"
            and row["risk_source"].startswith(f"{config.name}_seed")
        ]
        out: dict[str, object] = {"configuration": config.name, "runs": len(selected)}
        for source, target in (
            ("hop_increase_pct_mean", "hop_increase"),
            ("total_risk_aggregate_reduction", "total_risk_reduction"),
            ("cvar90_aggregate_reduction", "cvar90_reduction"),
            ("max_risk_aggregate_reduction", "maxrisk_reduction"),
            ("re_aggregate_reduction", "re_reduction"),
        ):
            out[f"{target}_mean"], out[f"{target}_std"] = mean_std(
                [float(row[source]) for row in selected]
            )
        od_rows.append(out)

    common_rows_raw = read_csv(
        args.root
        / "pyvrp_cvrp"
        / "stable_tail_v2_common_eval_3seed"
        / "common_route_summary.csv"
    )
    pyvrp_rows: list[dict[str, object]] = []
    for config in CONFIGS:
        for customer_set in ("A", "B"):
            selected = [
                row
                for row in common_rows_raw
                if row["customer_set"] == customer_set
                and row["risk_source"].startswith(f"{config.name}_seed")
            ]
            out = {
                "configuration": config.name,
                "customer_set": customer_set,
                "model_seeds": len(selected),
            }
            for source, target in (
                ("common_global_risk_mean", "global_risk"),
                ("common_global_cvar90_mean", "cvar90"),
                ("common_max_vehicle_risk_mean", "max_vehicle_risk"),
                ("common_edge_burden_gini_used_mean", "edge_gini"),
                ("common_top10_burden_share_mean", "top10_share"),
            ):
                out[f"{target}_mean"], out[f"{target}_std"] = mean_std(
                    [float(row[source]) for row in selected]
                )
            pyvrp_rows.append(out)

    write_csv(summary_root / "node_summary_3seed.csv", node_rows)
    write_csv(summary_root / "risk_distribution_summary_3seed.csv", risk_rows)
    write_csv(summary_root / "od_summary_3seed.csv", od_rows)
    write_csv(summary_root / "pyvrp_common_summary_3seed.csv", pyvrp_rows)

    lines = ["# Stable-Tail v1/v2 Three-Seed Screening", ""]
    node_by_name = {row["configuration"]: row for row in node_rows}
    risk_by_name = {row["configuration"]: row for row in risk_rows}
    od_by_name = {row["configuration"]: row for row in od_rows}
    py_by_key = {(row["configuration"], row["customer_set"]): row for row in pyvrp_rows}
    lines += [
        "| Configuration | MAE | PR-AUC | Recall | P95 | P99 | TailGap | OD risk red. | OD CVaR90 red. | OD MaxRisk red. | Set A common risk | Set B common risk | Pass |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|",
    ]
    decision_rows: list[dict[str, object]] = []
    for config in CONFIGS:
        node = node_by_name[config.name]
        risk = risk_by_name[config.name]
        od = od_by_name[config.name]
        set_a = py_by_key[(config.name, "A")]
        set_b = py_by_key[(config.name, "B")]
        checks = {
            "MAE<=1.2089": float(node["mae_mean"]) <= 1.2089,
            "PR-AUC>=0.3716": float(node["pr_auc_high_mean"]) >= 0.3716,
            "Recall>=0.2423": float(node["recall_6_8_mean"]) >= 0.2423,
            "P95>=0.075": float(risk["risk_p95_mean"]) >= 0.075,
            "P99>=0.420": float(risk["risk_p99_mean"]) >= 0.420,
            "TailGap>=0.350": float(risk["tail_gap_mean"]) >= 0.350,
            "ODRisk>=0.8501": float(od["total_risk_reduction_mean"]) >= 0.8501,
            "ODCVaR90>=0.9005": float(od["cvar90_reduction_mean"]) >= 0.9005,
            "ODMaxRisk>=0.9078": float(od["maxrisk_reduction_mean"]) >= 0.9078,
            "SetA_Risk<3.1467": float(set_a["global_risk_mean"]) < 3.1467,
            "SetB_Risk<4.0353": float(set_b["global_risk_mean"]) < 4.0353,
            "SetA_Gini<=0.7546": float(set_a["edge_gini_mean"]) <= 0.7546,
            "SetB_Gini<=0.7777": float(set_b["edge_gini_mean"]) <= 0.7777,
        }
        failed = [name for name, ok in checks.items() if not ok]
        passed = not failed
        decision_rows.append(
            {
                "configuration": config.name,
                "passed": passed,
                "passed_count": sum(checks.values()),
                "criterion_count": len(checks),
                "failed_criteria": "; ".join(failed),
            }
        )
        lines.append(
            "| {name} | {mae:.4f} | {pr:.4f} | {rec:.4f} | {p95:.4f} | {p99:.4f} | {gap:.4f} | {risk_red:.2%} | {cvar:.2%} | {maxrisk:.2%} | {set_a:.4f} | {set_b:.4f} | {passed} |".format(
                name=config.name,
                mae=float(node["mae_mean"]),
                pr=float(node["pr_auc_high_mean"]),
                rec=float(node["recall_6_8_mean"]),
                p95=float(risk["risk_p95_mean"]),
                p99=float(risk["risk_p99_mean"]),
                gap=float(risk["tail_gap_mean"]),
                risk_red=float(od["total_risk_reduction_mean"]),
                cvar=float(od["cvar90_reduction_mean"]),
                maxrisk=float(od["maxrisk_reduction_mean"]),
                set_a=float(set_a["global_risk_mean"]),
                set_b=float(set_b["global_risk_mean"]),
                passed="YES" if passed else "NO",
            )
        )
    (summary_root / "screening_report_3seed.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    write_csv(summary_root / "screening_decision_3seed.csv", decision_rows)


def main() -> None:
    args = parse_args()
    args.root.mkdir(parents=True, exist_ok=True)
    requested = {item.strip() for item in args.stages.split(",") if item.strip()}
    stages = {
        "train": train_stage,
        "export": export_stage,
        "od": od_stage,
        "pyvrp": pyvrp_stage,
        "summarize": summarize_stage,
    }
    unknown = requested - stages.keys()
    if unknown:
        raise ValueError(f"Unknown stages: {sorted(unknown)}")
    for name, function in stages.items():
        if name in requested:
            print(f"\n=== {name} ===", flush=True)
            function(args)


if __name__ == "__main__":
    main()
