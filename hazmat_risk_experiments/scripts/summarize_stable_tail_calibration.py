"""Summarize Stable-Tail post-processing calibration downstream results."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs_10seed"
FINAL = ROOT / "outputs" / "final_figures_stable_tail_gnn_10seed"
BUDGETS = (0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40)
BASELINES = (
    "Stable-Tail GNN",
    "Stable-Tail-Gate",
    "GraphSAGE-TEG-Gate",
    "GCN",
    "GraphSAGE",
    "TEG-only",
    "Stable-Tail w/o Tail Loss",
)
METRICS = (
    "avg_risk_at_b",
    "common_aubrc",
    "cvar90_aubrc",
    "cvar95_aubrc",
    "load_cvar90_aubrc",
    "max_vehicle_cvar90_aubrc",
)
CORE = METRICS[:4]


def parse_args() -> argparse.Namespace:
    pyvrp = OUTPUTS / "pyvrp_cvrp"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-summary",
        type=Path,
        default=pyvrp / "stable_tail_calibration_pyvrp_10seed" / "model_pyvrp_summary.csv",
    )
    parser.add_argument(
        "--common-summary",
        type=Path,
        default=pyvrp / "stable_tail_calibration_common_eval_10seed" / "common_route_summary.csv",
    )
    parser.add_argument(
        "--load-summary",
        type=Path,
        default=pyvrp / "stable_tail_calibration_load_eval_10seed" / "load_aware_summary.csv",
    )
    parser.add_argument(
        "--baseline-summary",
        type=Path,
        default=pyvrp / "paper_budget_sweep_10seed" / "budget_sweep_summary.csv",
    )
    parser.add_argument(
        "--baseline-ab",
        type=Path,
        default=pyvrp / "paper_budget_sweep_10seed" / "budget_sweep_ab_average.csv",
    )
    parser.add_argument(
        "--source-manifest",
        type=Path,
        default=OUTPUTS / "risk_matrices" / "stable_tail_calibration_sources_10seed.csv",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=pyvrp / "stable_tail_calibration_budget_sweep_10seed",
    )
    parser.add_argument("--final-root", type=Path, default=FINAL)
    parser.add_argument("--p-high-mode", choices=("raw", "gate"), default="raw")
    parser.add_argument("--counterpart-dir", type=Path)
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Required calibration result missing: {path}")
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


def source_parts(value: str, common: bool = False) -> tuple[str, int]:
    if common and value.startswith(("A_", "B_")):
        value = value[2:]
    if "_seed" not in value:
        raise ValueError(f"Cannot parse calibration source: {value}")
    model, seed = value.rsplit("_seed", 1)
    return model, int(seed)


def trapezoid(values: list[float]) -> float:
    return sum(
        (BUDGETS[idx + 1] - BUDGETS[idx]) * (values[idx] + values[idx + 1]) / 2
        for idx in range(len(BUDGETS) - 1)
    )


def mean_std(values: list[float]) -> tuple[float, float]:
    return mean(values), stdev(values) if len(values) > 1 else 0.0


def dense_ranks(rows: list[dict[str, object]], metric: str) -> dict[str, float]:
    ordered = sorted((float(row[metric]), str(row["model"])) for row in rows)
    result: dict[str, float] = {}
    pos = 0
    while pos < len(ordered):
        end = pos + 1
        while end < len(ordered) and abs(ordered[end][0] - ordered[pos][0]) <= 1e-12:
            end += 1
        rank = ((pos + 1) + end) / 2
        for _, model in ordered[pos:end]:
            result[model] = rank
        pos = end
    return result


def mean_rank_scores(
    rows: list[dict[str, object]], metrics: tuple[str, ...]
) -> dict[str, float]:
    ranks = [dense_ranks(rows, metric) for metric in metrics]
    return {
        str(row["model"]): mean(rank[str(row["model"])] for rank in ranks)
        for row in rows
    }


def calibration_metadata(path: Path) -> dict[str, dict[str, str]]:
    rows = read_csv(path)
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        result[row["label"]] = row
    return result


def validate_input_freshness(args: argparse.Namespace) -> None:
    manifest = read_csv(args.source_manifest)
    risk_files = [
        Path(row["risk_dir"]) / "data_2021_edge_risk.npz" for row in manifest
    ]
    missing = [path for path in risk_files if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Calibration risk matrix missing: {missing[0]}")
    newest_risk = max(path.stat().st_mtime_ns for path in risk_files)
    stale = [
        path
        for path in (args.self_summary, args.common_summary, args.load_summary)
        if not path.exists() or path.stat().st_mtime_ns < newest_risk
    ]
    if stale:
        joined = ", ".join(str(path) for path in stale)
        raise RuntimeError(
            "Calibration downstream summaries are older than the risk matrices: "
            f"{joined}. Rerun stable_tail_calibration_pyvrp before summarizing."
        )


def build_detail(args: argparse.Namespace) -> list[dict[str, object]]:
    costs: dict[tuple[str, int, str, float], tuple[float, str]] = {}
    for row in read_csv(args.self_summary):
        model, seed = source_parts(row["risk_source"])
        costs[(model, seed, row["customer_set"], float(row["beta"]))] = (
            float(row["cost_increase_pct"]),
            str(args.self_summary),
        )
    loads: dict[tuple[str, int, str, float], dict[str, str]] = {}
    for row in read_csv(args.load_summary):
        model, seed = source_parts(row["risk_source"], common=True)
        loads[(model, seed, row["customer_set"], float(row["beta"]))] = row
    candidates: dict[tuple[str, int, str], list[dict[str, object]]] = defaultdict(list)
    for row in read_csv(args.common_summary):
        model, seed = source_parts(row["risk_source"], common=True)
        key = (model, seed, row["customer_set"], float(row["beta"]))
        if key not in costs or key not in loads:
            raise KeyError(f"Missing self/load calibration result for {key}")
        cost, source = costs[key]
        load = loads[key]
        candidates[(model, seed, row["customer_set"])].append(
            {
                "beta": float(row["beta"]),
                "cost_increase": cost,
                "risk": float(row["common_global_risk_mean"]),
                "cvar90": float(row["common_global_cvar90_mean"]),
                "cvar95": float(row["common_global_cvar95_mean"]),
                "load_cvar90": float(load["load_cvar90_mean"]),
                "max_vehicle_cvar90": float(row["common_max_vehicle_cvar90_mean"]),
                "source_file": f"{source};{args.common_summary};{args.load_summary}",
            }
        )
    detail: list[dict[str, object]] = []
    for (model, seed, customer_set), rows in sorted(candidates.items()):
        for budget in BUDGETS:
            feasible = [row for row in rows if float(row["cost_increase"]) <= budget + 1e-12]
            if not feasible:
                raise ValueError(f"No feasible calibration route for {(model, seed, customer_set, budget)}")
            best = min(feasible, key=lambda row: float(row["risk"]))
            detail.append(
                {
                    "model": model,
                    "seed": seed,
                    "customer_set": customer_set,
                    "budget": budget,
                    "risk_at_b": best["risk"],
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


def summarize(detail: list[dict[str, object]], metadata: dict[str, dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    grouped: dict[tuple[str, int, str], list[dict[str, object]]] = defaultdict(list)
    for row in detail:
        grouped[(str(row["model"]), int(row["seed"]), str(row["customer_set"]))].append(row)
    seed_rows: list[dict[str, object]] = []
    auc_map = {
        "common_aubrc": "risk_at_b",
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
            "avg_risk_at_b": mean(float(row["risk_at_b"]) for row in rows),
        }
        for output, source in auc_map.items():
            out[output] = trapezoid([float(row[source]) for row in rows])
        seed_rows.append(out)
    by_set: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in seed_rows:
        by_set[(str(row["model"]), str(row["customer_set"]))].append(row)
    summary: list[dict[str, object]] = []
    for (model, customer_set), rows in sorted(by_set.items()):
        meta = metadata[model]
        out: dict[str, object] = {
            "model": model,
            "customer_set": customer_set,
            "method": meta["method"],
            "alpha": meta["alpha"],
            "rho": meta["rho"],
            "p_high_mode": meta.get("p_high_mode", "gate"),
            "p_high_gate_threshold": meta.get(
                "p_high_gate_threshold", meta.get("high_risk_threshold", "0.5")
            ),
        }
        for metric in METRICS:
            avg, sd = mean_std([float(row[metric]) for row in rows])
            out[f"{metric}_mean"] = avg
            out[f"{metric}_std"] = sd
        summary.append(out)
    summary_by_set: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in summary:
        summary_by_set[str(row["customer_set"])].append(row)
    for rows in summary_by_set.values():
        scores = mean_rank_scores(rows, tuple(f"{metric}_mean" for metric in CORE))
        for row in rows:
            row["core_score"] = scores[str(row["model"])]
    grouped_ab: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in summary:
        grouped_ab[str(row["model"])].append(row)
    ab: list[dict[str, object]] = []
    for model, rows in sorted(grouped_ab.items()):
        out = {
            "model": model,
            "method": rows[0]["method"],
            "alpha": rows[0]["alpha"],
            "rho": rows[0]["rho"],
            "p_high_mode": rows[0]["p_high_mode"],
            "p_high_gate_threshold": rows[0]["p_high_gate_threshold"],
        }
        for metric in METRICS:
            out[f"{metric}_ab_mean"] = mean(float(row[f"{metric}_mean"]) for row in rows)
        ab.append(out)
    scores = mean_rank_scores(ab, tuple(f"{metric}_ab_mean" for metric in CORE))
    for row in ab:
        row["core_score"] = scores[str(row["model"])]
    ab.sort(key=lambda row: float(row["core_score"]))
    return seed_rows, summary, ab


def baseline_rows(args: argparse.Namespace) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    summary = [row for row in read_csv(args.baseline_summary) if row["model"] in BASELINES]
    ab = [row for row in read_csv(args.baseline_ab) if row["model"] in BASELINES]
    return summary, ab


def best_by_metric(ab: list[dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for metric in METRICS:
        key = f"{metric}_ab_mean"
        best = min(ab, key=lambda row: float(row[key]))
        rows.append({"metric": metric, "model": best["model"], "value": best[key], "method": best["method"], "alpha": best["alpha"], "rho": best["rho"]})
    return rows


def calibration_summary_md(calibration_ab: list[dict[str, object]]) -> str:
    lines = [
        "# Stable-Tail post-processing calibration",
        "",
        "All metrics are lower-is-better; AUBRC uses trapezoidal integration over B=10%--40%.",
        "",
        "| Rank | Calibration | Avg Risk@B | Common AUBRC | CVaR90 | CVaR95 | LoadCVaR90 | MaxVehCVaR90 | Core score |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for idx, row in enumerate(calibration_ab, start=1):
        lines.append(
            f"| {idx} | {row['model']} | {float(row['avg_risk_at_b_ab_mean']):.4f} | {float(row['common_aubrc_ab_mean']):.4f} | "
            f"{float(row['cvar90_aubrc_ab_mean']):.5f} | {float(row['cvar95_aubrc_ab_mean']):.5f} | "
            f"{float(row['load_cvar90_aubrc_ab_mean']):.5f} | {float(row['max_vehicle_cvar90_aubrc_ab_mean']):.5f} | {float(row['core_score']):.3f} |"
        )
    return "\n".join(lines) + "\n"


def improved_metrics(
    candidate: dict[str, object], baseline: dict[str, object], suffix: str
) -> list[str]:
    return [
        metric
        for metric in METRICS
        if float(candidate[f"{metric}{suffix}"]) < float(baseline[f"{metric}{suffix}"])
    ]


def comparison_text(
    candidate: dict[str, object], baseline: dict[str, object], suffix: str
) -> str:
    improved = improved_metrics(candidate, baseline, suffix)
    if len(improved) == len(METRICS):
        return "improves all six metrics"
    if not improved:
        return "improves none of the six metrics"
    return "improves " + ", ".join(improved)


def write_paper(args: argparse.Namespace, calibration_summary: list[dict[str, object]], calibration_ab: list[dict[str, object]], combined_summary: list[dict[str, object]], combined_ab: list[dict[str, object]]) -> None:
    mode_tag = "raw" if args.p_high_mode == "raw" else "gate05"
    paper = args.final_root / "paper_results" / f"04_stable_tail_calibration_{mode_tag}"
    paper.mkdir(parents=True, exist_ok=True)
    write_csv(paper / "calibration_setA.csv", [row for row in combined_summary if row["customer_set"] == "A"])
    write_csv(paper / "calibration_setB.csv", [row for row in combined_summary if row["customer_set"] == "B"])
    write_csv(paper / "calibration_ab_average.csv", combined_ab)
    best = calibration_ab[0]
    stable = next(row for row in combined_ab if row["model"] == "Stable-Tail GNN")
    graph_gate = next(row for row in combined_ab if row["model"] == "GraphSAGE-TEG-Gate")
    (paper / "calibration_summary.md").write_text(calibration_summary_md(calibration_ab), encoding="utf-8")
    best_cvar95 = min(calibration_ab, key=lambda row: float(row["cvar95_aubrc_ab_mean"]))
    tradeoffs = [
        row
        for row in calibration_ab
        if float(row["cvar95_aubrc_ab_mean"]) < float(stable["cvar95_aubrc_ab_mean"])
        and float(row["avg_risk_at_b_ab_mean"]) > float(stable["avg_risk_at_b_ab_mean"])
    ]
    interpretation = [
        "# Calibration interpretation",
        "",
        f"- Best core-ranked calibration: **{best['model']}** (method={best['method']}, alpha={best['alpha']}, rho={best['rho']}).",
        f"- Against Stable-Tail GNN on the A/B average, the winner {comparison_text(best, stable, '_ab_mean')}.",
        f"- Against GraphSAGE-TEG-Gate on the A/B average, the winner {comparison_text(best, graph_gate, '_ab_mean')}.",
        f"- Best CVaR95 calibration: **{best_cvar95['model']}**.",
        "- Tail-risk trade-off models against Stable-Tail GNN: "
        + (", ".join(f"**{row['model']}**" for row in tradeoffs) if tradeoffs else "none")
        + ".",
    ]
    for customer_set in ("A", "B"):
        rows = [row for row in calibration_summary if row["customer_set"] == customer_set]
        best_score = min(float(row["core_score"]) for row in rows)
        winners = [row for row in rows if abs(float(row["core_score"]) - best_score) <= 1e-12]
        winner = min(winners, key=lambda row: str(row["model"]))
        stable_set = next(
            row
            for row in combined_summary
            if row["model"] == "Stable-Tail GNN" and row["customer_set"] == customer_set
        )
        graph_set = next(
            row
            for row in combined_summary
            if row["model"] == "GraphSAGE-TEG-Gate" and row["customer_set"] == customer_set
        )
        names = ", ".join(f"**{row['model']}**" for row in winners)
        interpretation.append(
            f"- Set {customer_set} best mean-rank calibration(s): {names}; "
            f"against Stable-Tail GNN, {winner['model']} {comparison_text(winner, stable_set, '_mean')}; "
            f"against GraphSAGE-TEG-Gate, it {comparison_text(winner, graph_set, '_mean')}."
        )
    (paper / "calibration_interpretation.md").write_text("\n".join(interpretation) + "\n", encoding="utf-8")


def calibration_label(row: dict[str, object], mode: str) -> str:
    display = "Raw" if mode == "raw" else "Gate05"
    method = str(row["method"])
    if method == "risk_matrix_ensemble":
        return f"Stable-Tail-MatrixEns{display}-r{round(float(row['rho']) * 100):03d}"
    prefixes = {
        "edge_tail_correction": "EdgeTail",
        "tail_only_correction": "TailOnly",
        "node_calibration": "NodeCalib",
    }
    return f"Stable-Tail-{prefixes[method]}{display}-a{round(float(row['alpha']) * 100):03d}"


def relabel_mode(rows: list[dict[str, object]], mode: str) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for source in rows:
        row = dict(source)
        row["model"] = calibration_label(row, mode)
        row["p_high_mode"] = mode
        row["p_high_gate_threshold"] = 0.5
        result.append(row)
    return result


def counterpart_paths(args: argparse.Namespace) -> tuple[Path, Path] | None:
    pyvrp = args.output_dir.parent
    if args.counterpart_dir is not None:
        candidates = [args.counterpart_dir]
    elif args.p_high_mode == "raw":
        candidates = [
            pyvrp / "stable_tail_calibration_gate05_budget_sweep_10seed",
            pyvrp / "stable_tail_calibration_budget_sweep_10seed",
        ]
    else:
        candidates = [pyvrp / "stable_tail_calibration_raw_budget_sweep_10seed"]
    for directory in candidates:
        summary_path = directory / "calibration_summary.csv"
        ab_path = directory / "calibration_ab_average.csv"
        if summary_path.exists() and ab_path.exists():
            return summary_path, ab_path
    return None


def raw_gate_comparison(
    raw_ab: list[dict[str, object]], gate_ab: list[dict[str, object]]
) -> list[dict[str, object]]:
    def key(row: dict[str, object]) -> tuple[str, float, float]:
        return str(row["method"]), float(row["alpha"]), float(row["rho"])

    gate_map = {key(row): row for row in gate_ab}
    rows: list[dict[str, object]] = []
    for raw in raw_ab:
        gate = gate_map.get(key(raw))
        if gate is None:
            continue
        out: dict[str, object] = {
            "method": raw["method"],
            "alpha": raw["alpha"],
            "rho": raw["rho"],
            "raw_model": raw["model"],
            "gate05_model": gate["model"],
        }
        for metric in METRICS:
            field = f"{metric}_ab_mean"
            raw_value = float(raw[field])
            gate_value = float(gate[field])
            out[f"raw_{metric}"] = raw_value
            out[f"gate05_{metric}"] = gate_value
            out[f"raw_minus_gate05_{metric}"] = raw_value - gate_value
        rows.append(out)
    return rows

def main() -> None:
    args = parse_args()
    validate_input_freshness(args)
    metadata = calibration_metadata(args.source_manifest)
    detail = build_detail(args)
    seed_rows, calibration_summary, calibration_ab = summarize(detail, metadata)
    base_summary, base_ab = baseline_rows(args)
    combined_summary: list[dict[str, object]] = [*base_summary, *calibration_summary]
    combined_ab: list[dict[str, object]] = [*base_ab, *calibration_ab]
    write_csv(args.output_dir / "budget_sweep_detail.csv", detail)
    write_csv(args.output_dir / "budget_sweep_seed_metrics.csv", seed_rows)
    write_csv(args.output_dir / "calibration_summary.csv", calibration_summary)
    (args.output_dir / "calibration_summary.md").write_text(
        calibration_summary_md(calibration_ab), encoding="utf-8"
    )
    write_csv(args.output_dir / "calibration_ab_average.csv", calibration_ab)
    write_csv(args.output_dir / "combined_summary.csv", combined_summary)
    write_csv(args.output_dir / "combined_ab_average.csv", combined_ab)
    write_csv(args.output_dir / "best_calibration_by_metric.csv", best_by_metric(calibration_ab))
    write_csv(args.output_dir / "best_calibration_core_rank.csv", calibration_ab)
    own_tag = "raw" if args.p_high_mode == "raw" else "gate05"
    write_csv(args.output_dir / f"{own_tag}_calibration_summary.csv", calibration_summary)
    write_csv(args.output_dir / f"{own_tag}_calibration_ab_average.csv", calibration_ab)
    write_csv(
        args.output_dir / f"best_{own_tag}_calibration_by_metric.csv",
        best_by_metric(calibration_ab),
    )
    counterpart = counterpart_paths(args)
    if counterpart is not None:
        other_mode = "gate" if args.p_high_mode == "raw" else "raw"
        other_tag = "gate05" if other_mode == "gate" else "raw"
        other_summary = relabel_mode(read_csv(counterpart[0]), other_mode)
        other_ab = relabel_mode(read_csv(counterpart[1]), other_mode)
        write_csv(args.output_dir / f"{other_tag}_calibration_summary.csv", other_summary)
        write_csv(args.output_dir / f"{other_tag}_calibration_ab_average.csv", other_ab)
        write_csv(
            args.output_dir / f"best_{other_tag}_calibration_by_metric.csv",
            best_by_metric(other_ab),
        )
        raw_ab, gate_ab = (
            (calibration_ab, other_ab)
            if args.p_high_mode == "raw"
            else (other_ab, calibration_ab)
        )
        write_csv(
            args.output_dir / "raw_vs_gate05_comparison.csv",
            raw_gate_comparison(raw_ab, gate_ab),
        )
    write_paper(args, calibration_summary, calibration_ab, combined_summary, combined_ab)
    print(f"Wrote calibration sweep: detail={len(detail)}, summary={len(calibration_summary)}, ab={len(calibration_ab)}")


if __name__ == "__main__":
    main()
