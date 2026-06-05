"""Run OD path validation across risk-matrix modes and CVaR/RE settings."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import validate_od_paths  # noqa: E402

DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\od_paths")
DEFAULT_RISK_ROOT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\risk_matrices")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--risk-root", type=Path, default=DEFAULT_RISK_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--year", default="data_2021", choices=["data_2020", "data_2021"])
    parser.add_argument("--pairs-per-group", type=int, default=30)
    parser.add_argument("--k-paths", type=int, default=50)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--batch-prefix", default="od_modes_2021")
    parser.add_argument("--risk-modes", nargs="+", default=["raw", "floor_0p001", "floor_0p01", "floor_0p05"])
    parser.add_argument("--alphas", nargs="+", type=float, default=[0.80, 0.90])
    parser.add_argument("--lambdas", nargs="+", type=float, default=[0.0, 1.0, 5.0])
    parser.add_argument("--thresholds", nargs="+", default=["mean", "p75"], choices=["mean", "p75", "p90"])
    return parser.parse_args()


def risk_dirs(root: Path) -> dict[str, Path]:
    return {
        "raw": root / "teg_gnn_splitB_seed0_epochs20_raw",
        "floor_0p001": root / "teg_gnn_splitB_seed0_epochs20_floor_0p001",
        "floor_0p01": root / "teg_gnn_splitB_seed0_epochs20_floor_0p01",
        "floor_0p05": root / "teg_gnn_splitB_seed0_epochs20_floor_0p05",
    }


def format_float(value: float) -> str:
    return f"{value:g}".replace(".", "p")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
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


def write_report(path: Path, rows: list[dict[str, object]]) -> None:
    methods = ["Hop-shortest", "Mean-risk-raw", "Mean-risk-floor", "CVaR-risk", "CVaR+Concentration"]
    lines = [
        "# OD Path Risk-Mode Batch Summary",
        "",
        "| Risk mode | alpha | lambda | threshold | method | Hop inc. | Total risk agg. red. | CVaR90 agg. red. | RE agg. red. | overlap w/ CVaR | changed |",
        "|---|---:|---:|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        if row["method"] not in methods:
            continue
        lines.append(
            "| {risk_mode} | {alpha} | {lam} | {thr} | {method} | {hop:.3%} | {risk:.3%} | {cvar:.3%} | {re:.3%} | {overlap:.3%} | {changed:.3%} |".format(
                risk_mode=row["risk_mode"],
                alpha=float(row["cvar_alpha"]),
                lam=float(row["lambda_re"]),
                thr=row["re_threshold"],
                method=row["method"],
                hop=float(row["hop_increase_pct_mean"]),
                risk=float(row["total_risk_aggregate_reduction"]),
                cvar=float(row["cvar90_aggregate_reduction"]),
                re=float(row["re_aggregate_reduction"]),
                overlap=float(row["path_overlap_with_cvar"]),
                changed=float(row["selected_path_changed_rate"]),
            )
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def re_threshold_value(graph, threshold: str) -> float:
    risks = validate_od_paths.np.asarray(
        [data["risk"] for _, _, data in graph.edges(data=True)], dtype=float
    )
    if threshold == "mean":
        return float(validate_od_paths.np.mean(risks))
    if threshold == "p75":
        return float(validate_od_paths.np.percentile(risks, 75))
    if threshold == "p90":
        return float(validate_od_paths.np.percentile(risks, 90))
    raise ValueError(f"Unknown RE threshold: {threshold}")


def build_cached_paths(
    graph,
    scores_norm,
    pairs_per_group: int,
    k_paths: int,
    seed: int,
) -> tuple[list[dict[str, int | str]], dict[tuple[str, int, int], dict[str, object]]]:
    pairs = validate_od_paths.sample_pairs(graph, scores_norm, pairs_per_group, seed)
    cache: dict[tuple[str, int, int], dict[str, object]] = {}
    for pair in pairs:
        key = (str(pair["group"]), int(pair["src"]), int(pair["dst"]))
        src = int(pair["src"])
        dst = int(pair["dst"])
        cache[key] = {
            "hop": [int(node) for node in validate_od_paths.nx.shortest_path(graph, src, dst, weight="hop")],
            "mean_raw": [
                int(node)
                for node in validate_od_paths.nx.shortest_path(graph, src, dst, weight="risk")
            ],
            "mean_floor": [
                int(node)
                for node in validate_od_paths.nx.shortest_path(graph, src, dst, weight="risk_floor")
            ],
            "candidates": validate_od_paths.shortest_simple_candidates(
                graph, src, dst, k_paths
            ),
        }
    return pairs, cache


def run_combo(
    graph,
    pairs: list[dict[str, int | str]],
    cache: dict[tuple[str, int, int], dict[str, object]],
    threshold: str,
    alpha: float,
    lambda_re: float,
) -> tuple[list[dict[str, object]], list[dict[str, object]], float]:
    threshold_value = re_threshold_value(graph, threshold)
    rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    for idx, pair in enumerate(pairs, start=1):
        key = (str(pair["group"]), int(pair["src"]), int(pair["dst"]))
        try:
            cached = cache[key]
            candidates = cached["candidates"]
            assert isinstance(candidates, list)
            paths = {
                "Hop-shortest": cached["hop"],
                "Mean-risk-raw": cached["mean_raw"],
                "Mean-risk-floor": cached["mean_floor"],
                "CVaR-risk": validate_od_paths.choose_cvar_path(
                    graph, candidates, threshold_value, alpha
                ),
                "CVaR+Concentration": validate_od_paths.choose_cvar_re_path(
                    graph, candidates, threshold_value, lambda_re, alpha
                ),
            }
            baseline = validate_od_paths.path_metrics(
                graph, paths["Hop-shortest"], threshold_value
            )
            for method, path in paths.items():
                metrics = validate_od_paths.path_metrics(graph, path, threshold_value)
                rows.append(validate_od_paths.metric_row(pair, method, path, metrics, baseline))
        except Exception as exc:  # noqa: BLE001 - batch validation records OD failures.
            failures.append({"pair_index": idx, **pair, "error": repr(exc)})
    return rows, failures, threshold_value


def main() -> None:
    args = parse_args()
    batch_root = args.output_dir / args.batch_prefix
    batch_root.mkdir(parents=True, exist_ok=True)

    alphas = args.alphas
    lambdas = args.lambdas
    thresholds = args.thresholds
    all_rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []

    for risk_mode, risk_dir in risk_dirs(args.risk_root).items():
        if risk_mode not in args.risk_modes:
            continue
        if not risk_dir.exists():
            failures.append({"risk_mode": risk_mode, "error": f"Missing risk dir: {risk_dir}"})
            continue
        graph, scores_norm, _ = validate_od_paths.load_graph(risk_dir, args.year)
        graph = validate_od_paths.largest_component_subgraph(graph)
        risk_floor = 1e-4 if risk_mode == "raw" else 0.0
        validate_od_paths.add_floor_risk(graph, risk_floor)
        pairs, cache = build_cached_paths(
            graph, scores_norm, args.pairs_per_group, args.k_paths, args.seed
        )
        risk_diag = validate_od_paths.risk_distribution_summary(graph, scores_norm)

        for alpha in alphas:
            for lambda_re in lambdas:
                for threshold in thresholds:
                    run_name = (
                        f"{args.batch_prefix}_{risk_mode}_a{format_float(alpha)}"
                        f"_l{format_float(lambda_re)}_{threshold}"
                    )
                    out_dir = args.output_dir / run_name
                    out_dir.mkdir(parents=True, exist_ok=True)
                    detail_rows, combo_failures, threshold_value = run_combo(
                        graph, pairs, cache, threshold, alpha, lambda_re
                    )
                    summary_rows = validate_od_paths.summarize(detail_rows)
                    meta = {
                        "year": args.year,
                        "risk_dir": str(risk_dir),
                        "num_pairs": len(pairs),
                        "num_successful_pairs": len(
                            {(row["group"], row["src"], row["dst"]) for row in detail_rows}
                        ),
                        "num_failures": len(combo_failures),
                        "pairs_per_group": args.pairs_per_group,
                        "k_paths": args.k_paths,
                        "lambda_re": lambda_re,
                        "cvar_alpha": alpha,
                        "re_threshold": threshold,
                        "re_threshold_value": threshold_value,
                        "risk_floor": risk_floor,
                        "seed": args.seed,
                        "largest_component_nodes": graph.number_of_nodes(),
                        "largest_component_edges": graph.number_of_edges(),
                        "risk_diagnostics": risk_diag,
                    }

                    validate_od_paths.write_csv(out_dir / "od_pairs.csv", pairs)
                    validate_od_paths.write_csv(out_dir / "od_path_detail.csv", detail_rows)
                    validate_od_paths.write_csv(out_dir / "od_path_summary.csv", summary_rows)
                    (out_dir / "od_path_failures.json").write_text(
                        json.dumps(combo_failures, ensure_ascii=False, indent=2),
                        encoding="utf-8",
                    )
                    (out_dir / "od_path_meta.json").write_text(
                        json.dumps(meta, ensure_ascii=False, indent=2),
                        encoding="utf-8",
                    )
                    (out_dir / "risk_diagnostics.json").write_text(
                        json.dumps(risk_diag, ensure_ascii=False, indent=2),
                        encoding="utf-8",
                    )
                    validate_od_paths.write_report(
                        out_dir / "od_path_report.md", summary_rows, meta
                    )
                    failures.extend(
                        {
                            "risk_mode": risk_mode,
                            "cvar_alpha": alpha,
                            "lambda_re": lambda_re,
                            "re_threshold": threshold,
                            **failure,
                        }
                        for failure in combo_failures
                    )
                    for row in summary_rows:
                        row.update(
                            {
                                "risk_mode": risk_mode,
                                "cvar_alpha": alpha,
                                "lambda_re": lambda_re,
                                "re_threshold": threshold,
                                "run_name": run_name,
                                "risk_dir": str(risk_dir),
                            }
                        )
                        all_rows.append(row)

    write_csv(batch_root / "od_modes_summary.csv", all_rows)
    (batch_root / "od_modes_failures.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_report(batch_root / "od_modes_summary.md", all_rows)
    print(f"Wrote OD mode batch summary to {batch_root}")
    print(f"Runs summarized: {len({row['run_name'] for row in all_rows})}; failures: {len(failures)}")


if __name__ == "__main__":
    main()
