#!/usr/bin/env python3
"""Build a validated snapshot of every current 10-seed model result."""

from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs_10seed"
REPORT_DIR = OUTPUTS / "all_model_results_current"

EXPECTED_MODELS = {
    "GAT",
    "GCN",
    "GraphSAGE",
    "Stable-Tail GNN",
    "TEG-only",
    "Gradformer-adapted",
    "SGFormer-adapted",
    "GraphSAGE-TEG-Concat",
    "SGFormer-TEG-Concat",
    "GraphSAGE-TEG-Gate",
    "SGFormer-TEG-Gate",
    "Stable-Tail-Gate",
    "Stable-Tail w/o Tail Loss",
}

NODE_FILES = (
    "paper_main_comparison_splitB_10seed_summary.csv",
    "paper_stable_tail_gate_splitB_10seed_summary.csv",
    "paper_stable_tail_no_tail_loss_splitB_10seed_summary.csv",
    "paper_strong_baselines_splitB_10seed_summary.csv",
    "paper_teg_concat_fusions_splitB_10seed_summary.csv",
    "paper_teg_gate_fusions_splitB_10seed_summary.csv",
)

OD_BATCHES = (
    "paper_model_od_comparison_10seed",
    "paper_stable_tail_gate_od_10seed",
    "paper_strong_od_comparison_10seed",
    "paper_teg_concat_fusion_od_10seed",
    "paper_teg_gate_fusion_od_10seed",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        raise RuntimeError(f"Refusing to write empty result table: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0])
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def normalized_model(row: dict[str, str]) -> str:
    model = row.get("paper_model_name") or row.get("model") or ""
    aliases = {
        "GCN (paper)": "GCN",
        "Stable-Tail GNN (paper)": "Stable-Tail GNN",
    }
    model = aliases.get(model, model)
    if row.get("experiment_tag") == "paper_no_tail_loss_10seed":
        return "Stable-Tail w/o Tail Loss"
    return model


def require_models(rows: Iterable[dict[str, str]], context: str) -> None:
    actual = {row["model"] for row in rows}
    if actual != EXPECTED_MODELS:
        missing = sorted(EXPECTED_MODELS - actual)
        extra = sorted(actual - EXPECTED_MODELS)
        raise RuntimeError(f"{context}: model mismatch; missing={missing}, extra={extra}")


def collect_node_results() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    all_rows: list[dict[str, str]] = []
    model_dir = OUTPUTS / "models"
    for name in NODE_FILES:
        source = model_dir / name
        for row in read_csv(source):
            model = normalized_model(row)
            output = {"source_file": str(source.relative_to(ROOT))}
            output.update(row)
            output["model"] = model
            output["paper_model_name"] = model
            all_rows.append(output)

    require_models(all_rows, "node all-split results")
    if len(all_rows) != 4 * len(EXPECTED_MODELS):
        raise RuntimeError("Node results must contain four evaluation splits per model")
    split_counts = {
        model: len({row["eval_split"] for row in all_rows if row["model"] == model})
        for model in EXPECTED_MODELS
    }
    if set(split_counts.values()) != {4} or any(row["runs"] != "10" for row in all_rows):
        raise RuntimeError("Node all-split results must contain four unique 10-seed rows per model")

    test_rows = [row for row in all_rows if row["eval_split"] == "data_2021_test"]
    require_models(test_rows, "node test results")
    if len(test_rows) != len(EXPECTED_MODELS):
        raise RuntimeError("Node results must contain one 10-seed row per model")
    return (
        sorted(test_rows, key=lambda row: row["model"].casefold()),
        sorted(all_rows, key=lambda row: (row["model"].casefold(), row["eval_split"])),
    )


def collect_od_results() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    od_root = OUTPUTS / "od_paths"
    for batch in OD_BATCHES:
        source = od_root / batch / "od_seed_robustness_by_model_10seed.csv"
        for row in read_csv(source):
            output = {"model": normalized_model(row), "source_file": str(source.relative_to(ROOT))}
            output.update(row)
            output["model"] = normalized_model(output)
            rows.append(output)

    require_models(rows, "OD results")
    pairs = {(row["model"], row["method"]) for row in rows}
    expected_pairs = {(model, method) for model in EXPECTED_MODELS for method in ("CVaR-risk", "Hop-shortest")}
    if pairs != expected_pairs or len(rows) != len(expected_pairs):
        raise RuntimeError("OD results must contain both methods exactly once for every model")
    if any(row["model_seed_runs"] != "10" for row in rows):
        raise RuntimeError("OD results must contain 10 model seeds per row")
    return sorted(rows, key=lambda row: (row["model"].casefold(), row["method"]))


def collect_budget_results() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    root = OUTPUTS / "pyvrp_cvrp" / "paper_budget_sweep_10seed"
    ab_source = root / "budget_sweep_ab_average.csv"
    set_source = root / "budget_sweep_summary.csv"
    ab_rows = read_csv(ab_source)
    set_rows = read_csv(set_source)
    require_models(ab_rows, "budget A/B average")
    require_models(set_rows, "budget by customer set")
    if len(ab_rows) != 13 or len(set_rows) != 26:
        raise RuntimeError("Budget results must contain 13 A/B rows and 26 per-set rows")
    return ab_rows, set_rows


def collect_all_budget_by_set(formal_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    calibration_source = (
        OUTPUTS
        / "pyvrp_cvrp"
        / "stable_tail_calibration_budget_sweep_10seed"
        / "calibration_summary.csv"
    )
    calibration_rows = read_csv(calibration_source)
    if len(calibration_rows) != 34:
        raise RuntimeError(f"Expected 34 calibration budget rows, found {len(calibration_rows)}")

    metric_fields = [
        "avg_risk_at_b_mean",
        "avg_risk_at_b_std",
        "common_aubrc_mean",
        "common_aubrc_std",
        "cvar90_aubrc_mean",
        "cvar90_aubrc_std",
        "cvar95_aubrc_mean",
        "cvar95_aubrc_std",
        "load_cvar90_aubrc_mean",
        "load_cvar90_aubrc_std",
        "max_vehicle_cvar90_aubrc_mean",
        "max_vehicle_cvar90_aubrc_std",
    ]
    rows: list[dict[str, str]] = []
    formal_source = OUTPUTS / "pyvrp_cvrp" / "paper_budget_sweep_10seed" / "budget_sweep_summary.csv"
    for row in formal_rows:
        output = {
            "model": row["model"],
            "model_type": "formal_trained_model",
            "customer_set": row["customer_set"],
            "method": "trained_model",
            "alpha": "",
            "rho": "",
        }
        output.update({field: row[field] for field in metric_fields})
        output["core_score"] = ""
        output["source_file"] = str(formal_source.relative_to(ROOT))
        rows.append(output)
    for row in calibration_rows:
        output = {
            "model": row["model"],
            "model_type": "stable_tail_postprocess",
            "customer_set": row["customer_set"],
            "method": row["method"],
            "alpha": row["alpha"],
            "rho": row["rho"],
        }
        output.update({field: row[field] for field in metric_fields})
        output["core_score"] = row["core_score"]
        output["source_file"] = str(calibration_source.relative_to(ROOT))
        rows.append(output)

    models = {row["model"] for row in rows}
    counts = {customer_set: sum(row["customer_set"] == customer_set for row in rows) for customer_set in ("A", "B")}
    if len(models) != 30 or counts != {"A": 30, "B": 30} or len(rows) != 60:
        raise RuntimeError(f"Combined budget coverage mismatch: models={len(models)}, counts={counts}, rows={len(rows)}")
    return sorted(rows, key=lambda row: (row["customer_set"], row["model"].casefold()))


def collect_all_od_results(
    formal_rows: list[dict[str, str]], calibration_rows: list[dict[str, str]]
) -> list[dict[str, str]]:
    metric_fields = [
        "model_seed_runs",
        "hop_increase_mean",
        "hop_increase_std",
        "hop_increase_mean_std",
        "total_risk_reduction_mean",
        "total_risk_reduction_std",
        "total_risk_reduction_mean_std",
        "cvar90_reduction_mean",
        "cvar90_reduction_std",
        "cvar90_reduction_mean_std",
        "maxrisk_reduction_mean",
        "maxrisk_reduction_std",
        "maxrisk_reduction_mean_std",
        "re_reduction_mean",
        "re_reduction_std",
        "re_reduction_mean_std",
    ]
    rows: list[dict[str, str]] = []
    calibration_source = (
        OUTPUTS
        / "od_paths"
        / "stable_tail_calibration_od_10seed"
        / "od_seed_robustness_by_model_10seed.csv"
    )
    for model_type, source_rows in (
        ("formal_trained_model", formal_rows),
        ("stable_tail_postprocess", calibration_rows),
    ):
        for row in source_rows:
            output = {
                "model": row["model"],
                "model_type": model_type,
                "method": row["method"],
            }
            output.update({field: row[field] for field in metric_fields})
            output["source_file"] = (
                row.get("source_file", "")
                if model_type == "formal_trained_model"
                else str(calibration_source.relative_to(ROOT))
            )
            rows.append(output)
    pairs = {(row["model"], row["method"]) for row in rows}
    if len(rows) != 60 or len({row["model"] for row in rows}) != 30 or len(pairs) != 60:
        raise RuntimeError("Combined OD results must contain 30 models x 2 methods")
    return sorted(rows, key=lambda row: (row["model"].casefold(), row["method"]))


def model_inventory(all_budget_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    models = {(row["model"], row["model_type"]) for row in all_budget_rows}
    return [
        {
            "model": model,
            "model_type": model_type,
            "node_prediction": "available" if model_type == "formal_trained_model" else "not_applicable_postprocess",
            "pyvrp_set_a": "available",
            "pyvrp_set_b": "available",
            "od_validation": "available",
        }
        for model, model_type in sorted(models, key=lambda item: item[0].casefold())
    ]


def calibration_state() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    risk_root = OUTPUTS / "risk_matrices"
    meta_paths = sorted(risk_root.glob("stable_tail_*/calibration_meta.json"))
    if len(meta_paths) != 170:
        raise RuntimeError(f"Expected 170 calibration exports, found {len(meta_paths)}")
    schemas = {json.loads(path.read_text(encoding="utf-8"))["schema_version"] for path in meta_paths}
    if schemas != {3}:
        raise RuntimeError(f"Calibration exports are not uniformly schema v3: {sorted(schemas)}")
    latest_risk_mtime = max(path.stat().st_mtime for path in meta_paths)

    calibration_od = (
        OUTPUTS
        / "od_paths"
        / "stable_tail_calibration_od_10seed"
        / "od_seed_robustness_by_model_10seed.csv"
    )
    calibration_od_rows = read_csv(calibration_od)
    if len(calibration_od_rows) != 34:
        raise RuntimeError(f"Expected 34 calibration OD rows, found {len(calibration_od_rows)}")
    if calibration_od.stat().st_mtime < latest_risk_mtime:
        raise RuntimeError("Calibration OD result is older than the schema-v3 risk matrices")

    failures = calibration_od.with_name("model_od_failures.json")
    if json.loads(failures.read_text(encoding="utf-8")) != []:
        raise RuntimeError("Calibration OD run contains failures")

    calibration_outputs = {
        "calibration_pyvrp": OUTPUTS / "pyvrp_cvrp" / "stable_tail_calibration_pyvrp_10seed" / "stable_tail_calibration_pyvrp_summary_10seed.csv",
        "calibration_common_route": OUTPUTS / "pyvrp_cvrp" / "stable_tail_calibration_common_eval_10seed" / "common_route_summary.csv",
        "calibration_load_aware": OUTPUTS / "pyvrp_cvrp" / "stable_tail_calibration_load_eval_10seed" / "load_aware_summary.csv",
        "calibration_budget_sweep": OUTPUTS / "pyvrp_cvrp" / "stable_tail_calibration_budget_sweep_10seed" / "calibration_summary.csv",
    }
    statuses = [
        {
            "result_group": "primary_node_test",
            "status": "valid",
            "rows": "13",
            "reason": "one 10-seed data_2021_test aggregate per formal model",
        },
        {
            "result_group": "primary_budget_sweep",
            "status": "valid",
            "rows": "13 A/B + 26 per-set",
            "reason": "all 13 formal models present",
        },
        {
            "result_group": "primary_od_validation",
            "status": "valid",
            "rows": "26",
            "reason": "13 models x 2 methods, each with 10 seeds",
        },
        {
            "result_group": "calibration_risk_matrices",
            "status": "valid",
            "rows": "170",
            "reason": "17 configurations x 10 seeds; all schema v3",
        },
        {
            "result_group": "calibration_od_validation",
            "status": "valid",
            "rows": "34",
            "reason": "17 configurations x 2 methods; newer than schema-v3 exports; no failures",
        },
    ]
    for group, path in calibration_outputs.items():
        stale = not path.exists() or path.stat().st_mtime < latest_risk_mtime
        statuses.append(
            {
                "result_group": group,
                "status": "stale" if stale else "valid",
                "rows": str(len(read_csv(path))) if path.exists() else "0",
                "reason": "older than schema-v3 calibration risk matrices" if stale else "fresh",
            }
        )
    return calibration_od_rows, statuses


def f(value: str, digits: int = 4) -> str:
    return f"{float(value):.{digits}f}"


def mean_std(row: dict[str, str], metric: str, digits: int = 4) -> str:
    return f"{f(row[f'{metric}_mean'], digits)} +/- {f(row[f'{metric}_std'], digits)}"


def budget_by_set_report(
    rows: list[dict[str, str]],
    title: str = "Model budget results by customer set",
    table_name: str = "all_model_budget_by_set_results.csv",
) -> str:
    lines = [
        f"# {title}",
        "",
        f"Generated: {datetime.now().astimezone().isoformat(timespec='seconds')}",
        "",
        "All values are 10-seed mean +/- standard deviation. No A/B averages are used.",
    ]
    for customer_set in ("A", "B"):
        lines += [
            "",
            f"## Set {customer_set}",
            "",
            "Lower is better for every risk metric.",
            "",
            "| Model | Avg risk@B | Common AUBRC | CVaR90 AUBRC | CVaR95 AUBRC | Load CVaR90 | Max-vehicle CVaR90 |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
        set_rows = [row for row in rows if row["customer_set"] == customer_set]
        for row in sorted(set_rows, key=lambda item: float(item["avg_risk_at_b_mean"])):
            lines.append(
                f"| {row['model']} | {mean_std(row, 'avg_risk_at_b')} | "
                f"{mean_std(row, 'common_aubrc')} | {mean_std(row, 'cvar90_aubrc', 5)} | "
                f"{mean_std(row, 'cvar95_aubrc', 5)} | {mean_std(row, 'load_cvar90_aubrc', 5)} | "
                f"{mean_std(row, 'max_vehicle_cvar90_aubrc', 5)} |"
            )
    lines += [
        "",
        f"Complete machine-readable table: `{table_name}`.",
        "",
    ]
    return "\n".join(lines)


def markdown_report(
    node_rows: list[dict[str, str]],
    budget_rows: list[dict[str, str]],
    od_rows: list[dict[str, str]],
    calibration_od_rows: list[dict[str, str]],
    statuses: list[dict[str, str]],
) -> str:
    lines = [
        "# Current model result snapshot",
        "",
        f"Generated: {datetime.now().astimezone().isoformat(timespec='seconds')}",
        "",
        "Only current, validated aggregates are ranked below. Stale calibration downstream files are listed in the status table and excluded from comparisons.",
        "",
        "## Result status",
        "",
        "| Result group | Status | Rows | Reason |",
        "|---|---:|---:|---|",
    ]
    lines.extend(
        f"| {row['result_group']} | {row['status']} | {row['rows']} | {row['reason']} |"
        for row in statuses
    )

    lines += [
        "",
        "## Node prediction (data_2021_test, 10 seeds)",
        "",
        "| Model | Macro-F1 | MAE | QWK | High recall | High PR-AUC | High FN rate |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in sorted(node_rows, key=lambda item: float(item["macro_f1_mean"]), reverse=True):
        lines.append(
            f"| {row['model']} | {f(row['macro_f1_mean'])} | {f(row['mae_mean'])} | "
            f"{f(row['qwk_mean'])} | {f(row['recall_6_8_mean'])} | "
            f"{f(row['pr_auc_high_mean'])} | {f(row['high_fn_rate_mean'])} |"
        )

    lines += [
        "",
        "## PyVRP budget sweep (A/B average, 10 seeds)",
        "",
        "Lower is better for every risk column.",
        "",
        "| Model | Avg risk@B | Common AUBRC | CVaR90 AUBRC | CVaR95 AUBRC | Load CVaR90 | Max-vehicle CVaR90 | Core rank |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in sorted(budget_rows, key=lambda item: float(item["rank_by_core_risk"])):
        lines.append(
            f"| {row['model']} | {f(row['avg_risk_at_b_ab_mean'])} | {f(row['common_aubrc_ab_mean'])} | "
            f"{f(row['cvar90_aubrc_ab_mean'], 5)} | {f(row['cvar95_aubrc_ab_mean'], 5)} | "
            f"{f(row['load_cvar90_aubrc_ab_mean'], 5)} | {f(row['max_vehicle_cvar90_aubrc_ab_mean'], 5)} | "
            f"{f(row['rank_by_core_risk'], 2)} |"
        )

    lines += [
        "",
        "## OD validation (CVaR-risk, 10 seeds)",
        "",
        "Risk reductions are benefits; hop increase is routing cost.",
        "",
        "| Model | Hop increase | Total-risk reduction | CVaR90 reduction | Max-risk reduction | RE reduction |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    cvar_od = [row for row in od_rows if row["method"] == "CVaR-risk"]
    for row in sorted(cvar_od, key=lambda item: float(item["total_risk_reduction_mean"]), reverse=True):
        lines.append(
            f"| {row['model']} | {f(row['hop_increase_mean'])} | {f(row['total_risk_reduction_mean'])} | "
            f"{f(row['cvar90_reduction_mean'])} | {f(row['maxrisk_reduction_mean'])} | "
            f"{f(row['re_reduction_mean'])} |"
        )

    lines += [
        "",
        "## Stable-Tail calibration OD (schema v3, CVaR-risk, 10 seeds)",
        "",
        "| Configuration | Hop increase | Total-risk reduction | CVaR90 reduction | Max-risk reduction | RE reduction |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    calibration_cvar = [row for row in calibration_od_rows if row["method"] == "CVaR-risk"]
    for row in sorted(calibration_cvar, key=lambda item: float(item["total_risk_reduction_mean"]), reverse=True):
        lines.append(
            f"| {row['model']} | {f(row['hop_increase_mean'])} | {f(row['total_risk_reduction_mean'])} | "
            f"{f(row['cvar90_reduction_mean'])} | {f(row['maxrisk_reduction_mean'])} | "
            f"{f(row['re_reduction_mean'])} |"
        )

    lines += [
        "",
        "## Complete tables",
        "",
        "- `all_model_node_all_splits_results.csv`: all four node evaluation splits, means, and standard deviations.",
        "- `all_model_node_test_results.csv`: the data_2021_test subset used in the comparison above.",
        "- `all_model_budget_ab_results.csv`: all A/B-average budget metrics.",
        "- `all_model_budget_by_set_results.csv`: all A and B metrics with standard deviations.",
        "- `all_model_od_results.csv`: both OD methods and all means/standard deviations.",
        "- `stable_tail_calibration_od_results_v3.csv`: all 17 calibration configurations and both OD methods.",
        "- `all_30_models_budget_by_set_results.csv`: 13 formal models plus 17 post-processing configurations, split by Set A/B.",
        "- `all_30_models_od_results.csv`: OD results for all 30 models/configurations and both routing methods.",
        "- `all_30_models_inventory.csv`: result availability for every model/configuration.",
        "- `result_status.csv`: validity and freshness audit.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    node_rows, node_all_rows = collect_node_results()
    od_rows = collect_od_results()
    budget_ab_rows, budget_set_rows = collect_budget_results()
    calibration_od_rows, statuses = calibration_state()
    all_budget_rows = collect_all_budget_by_set(budget_set_rows)
    all_od_rows = collect_all_od_results(od_rows, calibration_od_rows)
    inventory_rows = model_inventory(all_budget_rows)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(REPORT_DIR / "all_model_node_all_splits_results.csv", node_all_rows)
    write_csv(REPORT_DIR / "all_model_node_test_results.csv", node_rows)
    write_csv(REPORT_DIR / "all_model_budget_ab_results.csv", budget_ab_rows)
    write_csv(REPORT_DIR / "all_model_budget_by_set_results.csv", budget_set_rows)
    write_csv(REPORT_DIR / "all_model_od_results.csv", od_rows)
    write_csv(REPORT_DIR / "stable_tail_calibration_od_results_v3.csv", calibration_od_rows)
    write_csv(REPORT_DIR / "all_30_models_budget_by_set_results.csv", all_budget_rows)
    write_csv(REPORT_DIR / "all_30_models_od_results.csv", all_od_rows)
    write_csv(REPORT_DIR / "all_30_models_inventory.csv", inventory_rows)
    write_csv(REPORT_DIR / "result_status.csv", statuses)
    report = markdown_report(node_rows, budget_ab_rows, od_rows, calibration_od_rows, statuses)
    (REPORT_DIR / "all_model_results.md").write_text(report, encoding="utf-8")
    set_report = budget_by_set_report(budget_set_rows)
    (REPORT_DIR / "all_model_budget_results_by_set.md").write_text(set_report, encoding="utf-8")
    all_set_report = budget_by_set_report(
        all_budget_rows,
        title="All 30 model/configuration budget results by customer set",
        table_name="all_30_models_budget_by_set_results.csv",
    )
    (REPORT_DIR / "all_30_models_results_by_set.md").write_text(all_set_report, encoding="utf-8")
    print(f"Wrote validated report to {REPORT_DIR}")


if __name__ == "__main__":
    main()
