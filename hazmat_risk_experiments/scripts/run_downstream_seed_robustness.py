"""Run downstream seed-robustness checks for the final Stable-Tail study.

This script reuses exported Split-B risk matrices for model seeds 0..4. It can
run three lightweight robustness layers:

1. Fixed-OD downstream validation over the same 150 OD pairs.
2. PyVRP-CVRP-50 beta=1 robustness for GCN, TEG-low, and Stable-Tail GNN.
3. Stable-Tail concentration-aware lambda=1 robustness against lambda=0.
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path
from statistics import mean, stdev


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
OUTPUTS = ROOT / "outputs"
RISK_ROOT = OUTPUTS / "risk_matrices"
OD_OUT = OUTPUTS / "od_paths" / "seed_robustness_splitB_fixed150"
PYVRP_OUT = OUTPUTS / "pyvrp_cvrp"
PAPER_SEED_OUT = OUTPUTS / "final_figures_stable_tail_gnn" / "paper_results" / "09_seed_robustness"
COMPARE_PYVRP = SCRIPT_DIR / "compare_model_pyvrp.py"
SEED_LABEL = ""

if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import compare_model_od_paths  # noqa: E402


MODEL_DIRS = {
    "GCN": "gcn_splitB_seed{seed}_epochs50_floor_0p01",
    "TEG-low": "teg_gnn_splitB_seed{seed}_epochs50_teg_low_tail_floor_0p01",
    "Stable-Tail GNN": "gcn_teg_concat_splitB_seed{seed}_epochs50_floor_0p01",
}

LABEL_SAFE = {
    "GCN": "GCN",
    "TEG-low": "TEG-low",
    "Stable-Tail GNN": "Stable-Tail-GNN",
}

OD_METRICS = {
    "hop_increase": "hop_increase_pct_mean",
    "total_risk_reduction": "total_risk_aggregate_reduction",
    "cvar90_reduction": "cvar90_aggregate_reduction",
    "maxrisk_reduction": "max_risk_aggregate_reduction",
    "re_reduction": "re_aggregate_reduction",
}

PYVRP_METRICS = {
    "cost_increase": "cost_increase_pct",
    "global_risk": "global_risk_mean",
    "risk_reduction": "risk_reduction_pct",
    "cvar90": "global_cvar90_mean",
    "max_vehicle_risk": "max_vehicle_risk_mean",
    "edge_burden_gini": "edge_burden_gini_used_mean",
    "top10_share": "top10_burden_share_mean",
}

CONC_IMPROVEMENT_METRICS = {
    "risk_improvement": ("global_risk_mean", True),
    "cvar90_improvement": ("global_cvar90_mean", True),
    "max_vehicle_risk_improvement": ("max_vehicle_risk_mean", True),
    "edge_gini_improvement": ("edge_burden_gini_used_mean", True),
    "top10_share_improvement": ("top10_burden_share_mean", True),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outputs-root", type=Path, default=OUTPUTS)
    parser.add_argument(
        "--paper-root",
        type=Path,
        default=OUTPUTS / "final_figures_stable_tail_gnn" / "paper_results",
    )
    parser.add_argument("--seed-label", default="")
    parser.add_argument("--gcn-pattern", default=MODEL_DIRS["GCN"])
    parser.add_argument("--teg-low-pattern", default=MODEL_DIRS["TEG-low"])
    parser.add_argument("--stable-tail-pattern", default=MODEL_DIRS["Stable-Tail GNN"])
    parser.add_argument("--seeds", default="0,1,2,3,4")
    parser.add_argument("--run-od", action="store_true")
    parser.add_argument("--run-pyvrp", action="store_true")
    parser.add_argument("--run-concentration", action="store_true")
    parser.add_argument("--max-runtime", type=float, default=10.0)
    parser.add_argument("--pyvrp-seeds", default="0,1,2,3,4")
    return parser.parse_args()


def parse_seed_csv(value: str) -> list[int]:
    return [int(item.strip()) for item in value.split(",") if item.strip()]


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    ensure_dir(path.parent)
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


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def risk_dir(model: str, seed: int) -> Path:
    return RISK_ROOT / MODEL_DIRS[model].format(seed=seed)


def source_label(model: str, seed: int) -> str:
    return f"{LABEL_SAFE[model]}_seed{seed}"


def parse_source(label: str) -> tuple[str, int]:
    model_safe, seed_text = label.rsplit("_seed", 1)
    display = next(model for model, safe in LABEL_SAFE.items() if safe == model_safe)
    return display, int(seed_text)


def validate_sources(seeds: list[int], models: list[str]) -> list[tuple[str, str, int, Path]]:
    sources: list[tuple[str, str, int, Path]] = []
    missing: list[str] = []
    for model in models:
        for seed in seeds:
            path = risk_dir(model, seed)
            if not path.exists():
                missing.append(str(path))
            else:
                sources.append((source_label(model, seed), model, seed, path))
    if missing:
        raise FileNotFoundError("Missing risk dirs:\n" + "\n".join(missing))
    return sources


def mean_std(values: list[float]) -> tuple[float, float]:
    if not values:
        return 0.0, 0.0
    return mean(values), stdev(values) if len(values) > 1 else 0.0


def format_mean_std(value: float, std: float, pct: bool = True) -> str:
    if pct:
        return f"{value:.3%} +/- {std:.3%}"
    return f"{value:.6f} +/- {std:.6f}"


def aggregate_rows(
    rows: list[dict[str, object]],
    group_keys: list[str],
    metrics: dict[str, str],
    source_key: str = "risk_source",
    pct_metrics: set[str] | None = None,
) -> list[dict[str, object]]:
    if pct_metrics is None:
        pct_metrics = set(metrics)
    grouped: dict[tuple[object, ...], list[dict[str, object]]] = {}
    for row in rows:
        key = tuple(row[group_key] for group_key in group_keys)
        grouped.setdefault(key, []).append(row)

    out_rows: list[dict[str, object]] = []
    for key, group in sorted(grouped.items(), key=lambda item: item[0]):
        out: dict[str, object] = dict(zip(group_keys, key))
        out["model_seed_runs"] = len(group)
        for out_name, src_name in metrics.items():
            vals = [float(row[src_name]) for row in group]
            avg, sd = mean_std(vals)
            out[f"{out_name}_mean"] = avg
            out[f"{out_name}_std"] = sd
            out[f"{out_name}_mean_std"] = format_mean_std(avg, sd, pct=out_name in pct_metrics)
        out_rows.append(out)
    return out_rows


def write_markdown_table(path: Path, title: str, rows: list[dict[str, object]], columns: list[tuple[str, str]]) -> None:
    lines = [f"# {title}", ""]
    lines.append("| " + " | ".join(label for label, _ in columns) + " |")
    lines.append("|" + "|".join("---" for _ in columns) + "|")
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(key, "")) for _, key in columns) + " |")
    path.write_text("\n".join(lines), encoding="utf-8")


def run_od(seeds: list[int]) -> None:
    out_dir = ensure_dir(OD_OUT)
    sources = validate_sources(seeds, ["GCN", "TEG-low", "Stable-Tail GNN"])
    pairs = compare_model_od_paths.read_pairs(compare_model_od_paths.DEFAULT_PAIRS)
    path_cache = compare_model_od_paths.build_path_cache(sources[0][3], "data_2021", pairs, 50)

    detail_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    metas: list[dict[str, object]] = []

    for label, model, seed, path in sources:
        print(f"[od] {label}")
        rows, source_failures, meta = compare_model_od_paths.run_source(
            label,
            path,
            "data_2021",
            pairs,
            50,
            0.90,
            "p75",
            path_cache,
        )
        for row in rows:
            row["model"] = model
            row["model_seed"] = seed
        detail_rows.extend(rows)
        failures.extend(source_failures)
        metas.append(meta)
        for row in compare_model_od_paths.summarize_source(rows, label):
            row["model"] = model
            row["model_seed"] = seed
            summary_rows.append(row)

    write_csv(out_dir / "od_seed_robustness_detail.csv", detail_rows)
    write_csv(out_dir / "od_seed_robustness_by_seed.csv", summary_rows)
    cvar_rows = [row for row in summary_rows if row.get("method") == "CVaR-risk"]
    by_model = aggregate_rows(cvar_rows, ["model"], OD_METRICS)
    write_csv(out_dir / "od_seed_robustness_by_model.csv", by_model)
    write_markdown_table(
        out_dir / "od_seed_robustness_by_model.md",
        "OD downstream seed robustness",
        by_model,
        [
            ("Model", "model"),
            ("Hop inc.", "hop_increase_mean_std"),
            ("Total Risk red.", "total_risk_reduction_mean_std"),
            ("CVaR90 red.", "cvar90_reduction_mean_std"),
            ("MaxRisk red.", "maxrisk_reduction_mean_std"),
            ("RE red.", "re_reduction_mean_std"),
        ],
    )
    (out_dir / "od_seed_robustness_failures.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out_dir / "od_seed_robustness_meta.json").write_text(
        json.dumps(
            {
                "pairs": str(compare_model_od_paths.DEFAULT_PAIRS),
                "num_pairs": len(pairs),
                "year": "data_2021",
                "k_paths": 50,
                "cvar_alpha": 0.90,
                "risk_mode": "floor_0.01",
                "split": "B",
                "model_seeds": seeds,
                "sources": metas,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    mirror_to_paper(out_dir, "od")


def run_compare_pyvrp(
    batch_name: str,
    sources: list[tuple[str, str, int, Path]],
    lambda_concentration: str,
    max_runtime: float,
    pyvrp_seeds: str,
) -> Path:
    args = [
        sys.executable,
        "-B",
        str(COMPARE_PYVRP),
        "--output-dir",
        str(PYVRP_OUT),
        "--betas",
        "0,1.0",
        "--lambda-concentration",
        lambda_concentration,
        "--seeds",
        pyvrp_seeds,
        "--max-runtime",
        str(max_runtime),
        "--batch-name",
        batch_name,
    ]
    for label, _, _, path in sources:
        args.append(f"{label}={path}")
    print(f"[pyvrp batch] {batch_name} sources={len(sources)} lambda={lambda_concentration}")
    subprocess.run(args, check=True)
    return PYVRP_OUT / batch_name


def aggregate_pyvrp_main(batch_dir: Path) -> None:
    src = batch_dir / "model_pyvrp_summary.csv"
    rows = read_csv(src)
    parsed: list[dict[str, object]] = []
    for row in rows:
        if abs(float(row["beta"]) - 1.0) > 1e-12 or abs(float(row.get("lambda_concentration", 0.0))) > 1e-12:
            continue
        model, seed = parse_source(row["risk_source"])
        out = dict(row)
        out["model"] = model
        out["model_seed"] = seed
        parsed.append(out)
    write_csv(batch_dir / "pyvrp_seed_robustness_by_seed.csv", parsed)
    by_set_model = aggregate_rows(
        parsed,
        ["customer_set", "model"],
        PYVRP_METRICS,
        pct_metrics={"cost_increase", "risk_reduction", "top10_share"},
    )
    write_csv(batch_dir / "pyvrp_seed_robustness_by_set_model.csv", by_set_model)
    write_markdown_table(
        batch_dir / "pyvrp_seed_robustness_by_set_model.md",
        "PyVRP-CVRP-50 seed robustness",
        by_set_model,
        [
            ("Set", "customer_set"),
            ("Model", "model"),
            ("Cost inc.", "cost_increase_mean_std"),
            ("Global Risk", "global_risk_mean_std"),
            ("Risk red.", "risk_reduction_mean_std"),
            ("CVaR90", "cvar90_mean_std"),
            ("Max Vehicle Risk", "max_vehicle_risk_mean_std"),
            ("Edge Gini", "edge_burden_gini_mean_std"),
            ("Top10 Share", "top10_share_mean_std"),
        ],
    )
    mirror_to_paper(batch_dir, "pyvrp")


def run_pyvrp(seeds: list[int], max_runtime: float, pyvrp_seeds: str) -> None:
    sources = validate_sources(seeds, ["GCN", "TEG-low", "Stable-Tail GNN"])
    suffix = f"_{SEED_LABEL}" if SEED_LABEL else ""
    batch_dir = run_compare_pyvrp(
        f"seed_robustness_pyvrp50_beta1_splitB{suffix}",
        sources,
        "0",
        max_runtime,
        pyvrp_seeds,
    )
    aggregate_pyvrp_main(batch_dir)


def aggregate_concentration(batch_dir: Path) -> None:
    src = batch_dir / "model_pyvrp_summary.csv"
    rows = read_csv(src)
    grouped: dict[tuple[str, int, str], dict[float, dict[str, str]]] = {}
    for row in rows:
        if abs(float(row["beta"]) - 1.0) > 1e-12:
            continue
        model, seed = parse_source(row["risk_source"])
        key = (model, seed, row["customer_set"])
        grouped.setdefault(key, {})[float(row.get("lambda_concentration", 0.0))] = row

    improvement_rows: list[dict[str, object]] = []
    for (model, seed, customer_set), by_lambda in sorted(grouped.items()):
        if 0.0 not in by_lambda or 1.0 not in by_lambda:
            continue
        base = by_lambda[0.0]
        conc = by_lambda[1.0]
        out: dict[str, object] = {
            "model": model,
            "model_seed": seed,
            "customer_set": customer_set,
        }
        for out_name, (metric, lower_is_better) in CONC_IMPROVEMENT_METRICS.items():
            base_val = float(base[metric])
            conc_val = float(conc[metric])
            out[out_name] = (base_val - conc_val) / (base_val + 1e-12) if lower_is_better else 0.0
        out["extra_cost_percentage_points"] = float(conc["cost_increase_pct"]) - float(base["cost_increase_pct"])
        improvement_rows.append(out)

    write_csv(batch_dir / "stable_tail_lambda1_improvement_by_seed.csv", improvement_rows)
    metrics = {key: key for key in list(CONC_IMPROVEMENT_METRICS) + ["extra_cost_percentage_points"]}
    by_set = aggregate_rows(improvement_rows, ["customer_set", "model"], metrics)
    write_csv(batch_dir / "stable_tail_lambda1_improvement_by_set.csv", by_set)
    write_markdown_table(
        batch_dir / "stable_tail_lambda1_improvement_by_set.md",
        "Stable-Tail concentration-aware lambda=1 robustness",
        by_set,
        [
            ("Set", "customer_set"),
            ("Model", "model"),
            ("Risk improvement", "risk_improvement_mean_std"),
            ("CVaR90 improvement", "cvar90_improvement_mean_std"),
            ("Max vehicle improvement", "max_vehicle_risk_improvement_mean_std"),
            ("Edge Gini improvement", "edge_gini_improvement_mean_std"),
            ("Top10 improvement", "top10_share_improvement_mean_std"),
            ("Extra cost p.p.", "extra_cost_percentage_points_mean_std"),
        ],
    )
    mirror_to_paper(batch_dir, "concentration")


def run_concentration(seeds: list[int], max_runtime: float, pyvrp_seeds: str) -> None:
    sources = validate_sources(seeds, ["Stable-Tail GNN"])
    suffix = f"_{SEED_LABEL}" if SEED_LABEL else ""
    batch_dir = run_compare_pyvrp(
        f"seed_robustness_stable_tail_concentration_splitB{suffix}",
        sources,
        "0,1",
        max_runtime,
        pyvrp_seeds,
    )
    aggregate_concentration(batch_dir)


def mirror_to_paper(src_dir: Path, prefix: str) -> None:
    dst_dir = ensure_dir(PAPER_SEED_OUT / prefix)
    for src in src_dir.glob("*"):
        if src.is_file() and src.suffix.lower() in {".csv", ".json", ".md"}:
            dst = dst_dir / src.name
            dst.write_bytes(src.read_bytes())


def main() -> None:
    args = parse_args()
    global OUTPUTS, RISK_ROOT, OD_OUT, PYVRP_OUT, PAPER_SEED_OUT, SEED_LABEL, MODEL_DIRS
    SEED_LABEL = args.seed_label
    MODEL_DIRS = {
        "GCN": args.gcn_pattern,
        "TEG-low": args.teg_low_pattern,
        "Stable-Tail GNN": args.stable_tail_pattern,
    }
    OUTPUTS = args.outputs_root
    RISK_ROOT = OUTPUTS / "risk_matrices"
    suffix = f"_{args.seed_label}" if args.seed_label else ""
    OD_OUT = OUTPUTS / "od_paths" / f"seed_robustness_splitB_fixed150{suffix}"
    PYVRP_OUT = OUTPUTS / "pyvrp_cvrp"
    PAPER_SEED_OUT = args.paper_root / f"09_seed_robustness{suffix}"
    seeds = parse_seed_csv(args.seeds)
    if not (args.run_od or args.run_pyvrp or args.run_concentration):
        args.run_od = args.run_pyvrp = args.run_concentration = True

    if args.run_od:
        run_od(seeds)
    if args.run_pyvrp:
        run_pyvrp(seeds, args.max_runtime, args.pyvrp_seeds)
    if args.run_concentration:
        run_concentration(seeds, args.max_runtime, args.pyvrp_seeds)


if __name__ == "__main__":
    main()
