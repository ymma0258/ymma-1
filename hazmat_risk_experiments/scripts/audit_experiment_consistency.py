"""Audit consistency assumptions for the 10seed paper experiment package.

The checks here do not rerun models or PyVRP.  They read existing 10seed
outputs and create small review tables that make the experimental口径 explicit:

* exported edge risk versus OD/PyVRP graph loaders;
* cost-only beta=0 baseline route/cost consistency;
* self-evaluation versus common-evaluator risk values;
* fixed 150 OD pair uniqueness and failure counts;
* fixed Set A/B CVRP instance identity.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, stdev


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import validate_od_paths  # noqa: E402
import validate_pyvrp_cvrp  # noqa: E402


ROOT = SCRIPT_DIR.parent
DEFAULT_OUTPUTS = ROOT / "outputs_10seed"
DEFAULT_FINAL = ROOT / "outputs" / "final_figures_stable_tail_gnn_10seed"
EPS = 1e-12


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outputs-root", type=Path, default=DEFAULT_OUTPUTS)
    parser.add_argument("--final-root", type=Path, default=DEFAULT_FINAL)
    parser.add_argument("--sample-risk-dir", type=Path)
    parser.add_argument("--common-risk-dir", type=Path)
    parser.add_argument("--num-edge-samples", type=int, default=20)
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


def sha1_text(value: object) -> str:
    return hashlib.sha1(json.dumps(value, sort_keys=True).encode("utf-8")).hexdigest()[:12]


def canonical_route_hash(routes_text: str) -> str:
    """Hash routes independent of vehicle ordering.

    PyVRP may return the same beta=0 solution with vehicles listed in a
    different order. Sorting the route tuples makes the baseline comparison
    reflect solution identity rather than display order.
    """
    routes = json.loads(routes_text)
    canonical = sorted(tuple(int(node) for node in route) for route in routes)
    return sha1_text(canonical)


def risk_dir(outputs_root: Path, name: str) -> Path:
    return outputs_root / "risk_matrices" / name


def sample_risk_dir(outputs_root: Path) -> Path:
    return risk_dir(outputs_root, "gcn_teg_concat_splitB_seed0_epochs50_10seed_floor_0p01")


def common_risk_dir(outputs_root: Path) -> Path:
    return risk_dir(outputs_root, "common_ensemble4_10seed_floor_0p01")


def graph_risk(graph, src: int, dst: int) -> float | None:
    return float(graph[src][dst]["risk"]) if graph.has_edge(src, dst) else None


def edge_risk_consistency(args: argparse.Namespace, out_dir: Path) -> list[dict[str, object]]:
    sample_dir = args.sample_risk_dir or sample_risk_dir(args.outputs_root)
    common_dir = args.common_risk_dir or common_risk_dir(args.outputs_root)
    edge_rows = read_csv(sample_dir / "data_2021_edge_risk.csv")
    od_graph, _, _ = validate_od_paths.load_graph(sample_dir, "data_2021")
    pyvrp_graph, _, _ = validate_pyvrp_cvrp.load_graph(sample_dir, "data_2021")
    common_graph, _, _ = validate_pyvrp_cvrp.load_graph(common_dir, "data_2021")

    rows: list[dict[str, object]] = []
    for row in edge_rows[: args.num_edge_samples]:
        src = int(row["src"])
        dst = int(row["dst"])
        matrix_risk = float(row["R_ij"])
        od_risk = graph_risk(od_graph, src, dst)
        pyvrp_risk = graph_risk(pyvrp_graph, src, dst)
        common_risk = graph_risk(common_graph, src, dst)
        rows.append(
            {
                "edge_id": row["edge_id"],
                "src": src,
                "dst": dst,
                "risk_matrix_Rij": matrix_risk,
                "OD_graph_Rij": od_risk,
                "PyVRP_graph_Rij": pyvrp_risk,
                "common_eval_Rij": common_risk,
                "matrix_OD_abs_diff": abs(matrix_risk - od_risk) if od_risk is not None else "",
                "matrix_PyVRP_abs_diff": abs(matrix_risk - pyvrp_risk)
                if pyvrp_risk is not None
                else "",
                "sample_risk_dir": str(sample_dir),
                "common_risk_dir": str(common_dir),
            }
        )
    write_csv(out_dir / "edge_risk_consistency_sample_10seed.csv", rows)
    return rows


def pyvrp_run_dirs(outputs_root: Path, batch: str) -> list[Path]:
    root = outputs_root / "pyvrp_cvrp"
    return sorted(path for path in root.glob(f"{batch}__*_*_*") if path.is_dir())


def beta0_baseline_check(args: argparse.Namespace, out_dir: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for run_dir in pyvrp_run_dirs(args.outputs_root, "model_pyvrp50_beta1_10seed"):
        detail_path = run_dir / "pyvrp_cvrp_detail.csv"
        meta_path = run_dir / "pyvrp_cvrp_meta.json"
        if not detail_path.exists() or not meta_path.exists():
            continue
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        risk_source = run_dir.name.split("__", 1)[-1]
        for row in read_csv(detail_path):
            if abs(float(row["beta"])) > 1e-12:
                continue
            rows.append(
                {
                    "customer_set": meta["customer_set"],
                    "route_source": risk_source,
                    "solver_seed": int(row["seed"]),
                    "beta0_total_cost": float(row["pyvrp_cost"]),
                    "beta0_route_hash": canonical_route_hash(row["routes"]),
                    "run_dir": str(run_dir),
                }
            )
    write_csv(out_dir / "beta0_baseline_consistency_10seed.csv", rows)

    summary: list[dict[str, object]] = []
    grouped: dict[tuple[str, int], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["customer_set"]), int(row["solver_seed"]))].append(row)
    for (customer_set, solver_seed), group in sorted(grouped.items()):
        costs = {float(row["beta0_total_cost"]) for row in group}
        hashes = {str(row["beta0_route_hash"]) for row in group}
        summary.append(
            {
                "customer_set": customer_set,
                "solver_seed": solver_seed,
                "route_sources": len(group),
                "unique_beta0_costs": len(costs),
                "unique_beta0_route_hashes": len(hashes),
                "cost_min": min(costs) if costs else "",
                "cost_max": max(costs) if costs else "",
                "shared_cost_baseline": len(costs) == 1,
                "shared_route_baseline": len(hashes) == 1,
            }
        )
    write_csv(out_dir / "beta0_baseline_consistency_summary_10seed.csv", summary)
    return summary


def self_vs_common_eval(args: argparse.Namespace, out_dir: Path) -> list[dict[str, object]]:
    self_rows = read_csv(
        args.outputs_root / "pyvrp_cvrp" / "model_pyvrp50_beta1_10seed" / "model_pyvrp_summary.csv"
    )
    common_rows = read_csv(
        args.outputs_root
        / "pyvrp_cvrp"
        / "common_eval_pyvrp50_10seed"
        / "common_route_summary.csv"
    )
    common_by_key = {
        (row["risk_source"], row["customer_set"], row["beta"], row["lambda_concentration"]): row
        for row in common_rows
    }
    rows: list[dict[str, object]] = []
    for row in self_rows:
        if abs(float(row["beta"]) - 1.0) > 1e-12 or abs(float(row["lambda_concentration"])) > 1e-12:
            continue
        common_key = (
            f"{row['customer_set']}_{row['risk_source']}",
            row["customer_set"],
            row["beta"],
            row["lambda_concentration"],
        )
        common = common_by_key.get(common_key)
        if common is None:
            continue
        rows.append(
            {
                "customer_set": row["customer_set"],
                "route_source": row["risk_source"],
                "self_global_risk": float(row["global_risk_mean"]),
                "common_global_risk": float(common["common_global_risk_mean"]),
                "self_cvar90": float(row["global_cvar90_mean"]),
                "common_cvar90": float(common["common_global_cvar90_mean"]),
                "self_max_vehicle_risk": float(row["max_vehicle_risk_mean"]),
                "common_max_vehicle_risk": float(common["common_max_vehicle_risk_mean"]),
                "self_edge_gini": float(row["edge_burden_gini_used_mean"]),
                "common_edge_gini": float(common["common_edge_burden_gini_used_mean"]),
                "self_top10_share": float(row["top10_burden_share_mean"]),
                "common_top10_share": float(common["common_top10_burden_share_mean"]),
            }
        )
    write_csv(out_dir / "self_vs_common_evaluator_10seed.csv", rows)
    return rows


def od_fixed_pair_check(args: argparse.Namespace, out_dir: Path) -> list[dict[str, object]]:
    pairs = read_csv(args.outputs_root / "od_paths" / "fixed_od_pairs_150.csv")
    failures = json.loads(
        (args.outputs_root / "od_paths" / "model_od_comparison_10seed" / "model_od_failures.json")
        .read_text(encoding="utf-8")
    )
    unique_pairs = {(row["group"], row["src"], row["dst"]) for row in pairs}
    counts = Counter(row["group"] for row in pairs)
    row = {
        "od_count": len(pairs),
        "unique_count": len(unique_pairs),
        "failed_count": len(failures),
        "high_high_count": counts.get("high_high", 0),
        "high_normal_count": counts.get("high_normal", 0),
        "normal_high_count": counts.get("normal_high", 0),
        "pairs_file": str(args.outputs_root / "od_paths" / "fixed_od_pairs_150.csv"),
    }
    rows = [row]
    write_csv(out_dir / "od_fixed_pair_check_10seed.csv", rows)
    return rows


def set_instance_check(args: argparse.Namespace, out_dir: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for set_name in ["A", "B"]:
        meta_path = (
            args.outputs_root
            / "pyvrp_cvrp"
            / "fixed_instances_10seed"
            / f"set{set_name}"
            / "pyvrp_cvrp_meta.json"
        )
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        customer_hash = sha1_text([int(node) for node in meta["customers"]])
        for seed in meta["seeds"]:
            rows.append(
                {
                    "set": set_name,
                    "seed": seed,
                    "customer_hash": customer_hash,
                    "depot": meta["depot"],
                    "customer_count": len(meta["customers"]),
                    "demand_sum": len(meta["customers"]),
                    "capacity": meta["capacity"],
                    "num_vehicles": meta["num_vehicles"],
                    "construction_risk_dir": meta.get("risk_dir", ""),
                    "fixed_instance_meta_source": meta.get("fixed_instance_meta", ""),
                }
            )
    write_csv(out_dir / "set_instance_consistency_10seed.csv", rows)
    return rows


def mean_std(values: list[float]) -> tuple[float, float]:
    if not values:
        return 0.0, 0.0
    return mean(values), stdev(values) if len(values) > 1 else 0.0


def write_markdown_report(
    out_dir: Path,
    edge_rows: list[dict[str, object]],
    beta0_rows: list[dict[str, object]],
    common_rows: list[dict[str, object]],
    od_rows: list[dict[str, object]],
    set_rows: list[dict[str, object]],
) -> None:
    edge_ok = all(
        float(row["matrix_OD_abs_diff"]) <= 1e-12
        and float(row["matrix_PyVRP_abs_diff"]) <= 1e-12
        for row in edge_rows
    )
    shared_cost = all(bool(row["shared_cost_baseline"]) for row in beta0_rows)
    shared_route = all(bool(row["shared_route_baseline"]) for row in beta0_rows)
    global_diffs = [
        float(row["common_global_risk"]) - float(row["self_global_risk"])
        for row in common_rows
    ]
    diff_mean, diff_std = mean_std(global_diffs)
    od = od_rows[0]
    set_hashes = {
        set_name: sorted(
            {str(row["customer_hash"]) for row in set_rows if row["set"] == set_name}
        )
        for set_name in ["A", "B"]
    }

    lines = [
        "# 10seed Consistency Checks",
        "",
        "## Answers",
        "",
        f"- Edge-risk loader consistency: {'PASS' if edge_ok else 'CHECK'} for the sampled {len(edge_rows)} edges; exported `R_ij`, OD graph risk, and PyVRP graph risk match.",
        "- Self-evaluation vs common evaluator: self-evaluation is valid for within-model beta/lambda comparisons; cross-model route safety should use the common evaluator.",
        f"- beta=0 cost baseline: shared cost baseline = `{shared_cost}`, shared route baseline = `{shared_route}`. If route hashes differ, compare cross-model cost increases cautiously.",
        f"- OD fixed pairs: {od['od_count']} rows, {od['unique_count']} unique, failures = {od['failed_count']}.",
        f"- Set A/B fixed instances: Set A hash `{set_hashes['A'][0]}`, Set B hash `{set_hashes['B'][0]}`; all solver seeds reuse the same depot/customers inside each set.",
        f"- Common minus self global-risk mean difference across matched beta=1 rows: `{diff_mean:.6f} +/- {diff_std:.6f}`.",
        "",
        "## Generated Tables",
        "",
        "- `edge_risk_consistency_sample_10seed.csv`",
        "- `beta0_baseline_consistency_10seed.csv`",
        "- `beta0_baseline_consistency_summary_10seed.csv`",
        "- `self_vs_common_evaluator_10seed.csv`",
        "- `od_fixed_pair_check_10seed.csv`",
        "- `set_instance_consistency_10seed.csv`",
        "",
        "## Paper Wording Notes",
        "",
        "- Use common-evaluator results for cross-model PyVRP claims.",
        "- Treat OD results mainly as downstream path-validation evidence, not the sole model ranking criterion.",
        "- Describe concentration-aware cost as a risk-burden concentration penalty plus posterior fairness evaluation, not as a strict fairness-constrained optimizer.",
        "- State that PyVRP optimization uses normalized cost components, while posterior risk metrics use continuous edge risks loaded from the risk matrix.",
    ]
    (out_dir / "consistency_check_report_10seed.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def main() -> None:
    args = parse_args()
    out_dir = args.final_root / "paper_results" / "11_consistency_checks"
    out_dir.mkdir(parents=True, exist_ok=True)

    edge_rows = edge_risk_consistency(args, out_dir)
    beta0_rows = beta0_baseline_check(args, out_dir)
    common_rows = self_vs_common_eval(args, out_dir)
    od_rows = od_fixed_pair_check(args, out_dir)
    set_rows = set_instance_check(args, out_dir)
    write_markdown_report(out_dir, edge_rows, beta0_rows, common_rows, od_rows, set_rows)
    print(f"Wrote consistency checks to {out_dir}")


if __name__ == "__main__":
    main()
