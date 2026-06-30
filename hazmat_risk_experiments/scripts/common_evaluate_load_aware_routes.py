"""Evaluate saved CVRP routes using common risk weighted by remaining load.

This is a posterior evaluator only. It does not change the PyVRP objective or
the saved routes. For each depot-to-customer leg, every expanded regional edge
risk is multiplied by the vehicle's remaining-load fraction before service at
the destination customer. The empty return leg therefore has zero load-aware
cargo risk.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import validate_pyvrp_cvrp as pyvrp_eval  # noqa: E402


def parse_label_dir(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("run dirs must use label=path")
    label, path = value.split("=", 1)
    return label.strip(), Path(path.strip())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dirs", nargs="+", type=parse_label_dir)
    parser.add_argument("--common-risk-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--batch-name", default="load_aware_common_evaluation")
    parser.add_argument("--betas", default="1.0")
    parser.add_argument("--lambda-concentration", type=float, default=None)
    return parser.parse_args()


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


def load_weighted_route_risks(graph, inst, sequence: list[int]) -> np.ndarray:
    """Expand one route and weight edge risk by pre-service remaining load."""

    demand = {idx: float(value) for idx, value in enumerate(inst.demands, start=1)}
    remaining = sum(demand.get(client, 0.0) for client in sequence)
    weighted: list[float] = []
    for left, right in zip(sequence[:-1], sequence[1:]):
        load_fraction = remaining / max(float(inst.capacity), pyvrp_eval.EPS)
        path = inst.hop_paths[(left, right)]
        for src, dst in zip(path[:-1], path[1:]):
            weighted.append(float(graph[src][dst]["risk"]) * load_fraction)
        remaining = max(0.0, remaining - demand.get(right, 0.0))
    return np.asarray(weighted, dtype=float)


def load_weighted_edge_burdens(graph, inst, sequences: list[list[int]]) -> np.ndarray:
    demand = {idx: float(value) for idx, value in enumerate(inst.demands, start=1)}
    burdens: dict[tuple[int, int], float] = {}
    for sequence in sequences:
        remaining = sum(demand.get(client, 0.0) for client in sequence)
        for left, right in zip(sequence[:-1], sequence[1:]):
            load_fraction = remaining / max(float(inst.capacity), pyvrp_eval.EPS)
            path = inst.hop_paths[(left, right)]
            for src, dst in zip(path[:-1], path[1:]):
                key = (min(src, dst), max(src, dst))
                burdens[key] = burdens.get(key, 0.0) + float(
                    graph[src][dst]["risk"]
                ) * load_fraction
            remaining = max(0.0, remaining - demand.get(right, 0.0))
    return np.asarray(list(burdens.values()), dtype=float)


def metrics(graph, inst, sequences: list[list[int]]) -> dict[str, float]:
    vehicle_arrays = [load_weighted_route_risks(graph, inst, seq) for seq in sequences]
    vehicle_risks = np.asarray([values.sum() for values in vehicle_arrays], dtype=float)
    all_risks = np.concatenate([values for values in vehicle_arrays if values.size])
    burdens = load_weighted_edge_burdens(graph, inst, sequences)
    top_count = max(1, int(math.ceil(burdens.size * 0.10))) if burdens.size else 0
    top_share = (
        float(np.sort(burdens)[-top_count:].sum() / (burdens.sum() + pyvrp_eval.EPS))
        if top_count
        else 0.0
    )
    return {
        "load_global_risk": float(all_risks.sum()),
        "load_cvar90": pyvrp_eval.cvar(all_risks, 0.90),
        "load_max_vehicle_risk": float(vehicle_risks.max()) if vehicle_risks.size else 0.0,
        "load_vehicle_gini": pyvrp_eval.gini(vehicle_risks),
        "load_edge_burden_gini_used": pyvrp_eval.gini(burdens),
        "load_top10_burden_share": top_share,
        "load_max_edge_burden": float(burdens.max()) if burdens.size else 0.0,
    }


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    metric_names = [
        "load_global_risk",
        "load_cvar90",
        "load_max_vehicle_risk",
        "load_vehicle_gini",
        "load_edge_burden_gini_used",
        "load_top10_burden_share",
        "load_max_edge_burden",
    ]
    grouped: dict[tuple[str, str, float, float], list[dict[str, object]]] = {}
    for row in rows:
        key = (
            str(row["risk_source"]),
            str(row["customer_set"]),
            float(row["beta"]),
            float(row["lambda_concentration"]),
        )
        grouped.setdefault(key, []).append(row)
    result: list[dict[str, object]] = []
    for (source, customer_set, beta, lam), group in sorted(grouped.items()):
        out: dict[str, object] = {
            "risk_source": source,
            "customer_set": customer_set,
            "beta": beta,
            "lambda_concentration": lam,
            "runs": len(group),
        }
        for name in metric_names:
            values = np.asarray([float(row[name]) for row in group], dtype=float)
            out[f"{name}_mean"] = float(values.mean())
            out[f"{name}_std"] = float(values.std(ddof=1)) if values.size > 1 else 0.0
        result.append(out)
    return result


def write_report(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# Load-Aware Common Evaluation",
        "",
        "Edge risk is weighted by the vehicle's remaining-load fraction before each customer service.",
        "",
        "| Set | Route source | beta | lambda | Load risk | Load CVaR90 | Max vehicle load risk | Edge burden Gini | Top10 share |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {set_name} | {source} | {beta:g} | {lam:g} | {risk:.6f} | {cvar:.6f} | {maxrisk:.6f} | {gini:.6f} | {top:.3%} |".format(
                set_name=row["customer_set"],
                source=row["risk_source"],
                beta=float(row["beta"]),
                lam=float(row["lambda_concentration"]),
                risk=float(row["load_global_risk_mean"]),
                cvar=float(row["load_cvar90_mean"]),
                maxrisk=float(row["load_max_vehicle_risk_mean"]),
                gini=float(row["load_edge_burden_gini_used_mean"]),
                top=float(row["load_top10_burden_share_mean"]),
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    out_dir = args.output_dir / args.batch_name
    out_dir.mkdir(parents=True, exist_ok=True)
    allowed_betas = {float(item) for item in args.betas.split(",") if item.strip()}
    graph, scores_norm, _ = pyvrp_eval.load_graph(args.common_risk_dir, "data_2021")
    graph = pyvrp_eval.largest_component(graph)
    rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    for label, run_dir in args.run_dirs:
        try:
            meta = json.loads((run_dir / "pyvrp_cvrp_meta.json").read_text(encoding="utf-8"))
            inst = pyvrp_eval.build_instance(
                graph,
                scores_norm,
                int(meta["num_customers"]),
                int(meta["num_vehicles"]),
                int(meta["capacity"]),
                str(meta["customer_set"]),
                0,
                int(meta["depot"]),
                [int(node) for node in meta["customers"]],
            )
            for row in read_csv(run_dir / "pyvrp_cvrp_detail.csv"):
                beta = float(row["beta"])
                lam = float(row.get("lambda_concentration", 0.0))
                if beta not in allowed_betas:
                    continue
                if args.lambda_concentration is not None and not math.isclose(
                    lam, args.lambda_concentration
                ):
                    continue
                sequences = json.loads(row["routes"])
                rows.append(
                    {
                        "risk_source": label,
                        "customer_set": meta["customer_set"],
                        "beta": beta,
                        "lambda_concentration": lam,
                        "seed": int(row["seed"]),
                        **metrics(graph, inst, sequences),
                    }
                )
        except Exception as exc:  # noqa: BLE001 - preserve per-source failures.
            failures.append({"risk_source": label, "run_dir": str(run_dir), "error": repr(exc)})
    summary = summarize(rows)
    write_csv(out_dir / "load_aware_detail.csv", rows)
    write_csv(out_dir / "load_aware_summary.csv", summary)
    (out_dir / "load_aware_failures.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out_dir / "load_aware_meta.json").write_text(
        json.dumps(
            {
                "common_risk_dir": str(args.common_risk_dir),
                "betas": sorted(allowed_betas),
                "lambda_concentration": args.lambda_concentration,
                "definition": "regional edge risk multiplied by pre-service remaining load / vehicle capacity",
                "run_dirs": {label: str(path) for label, path in args.run_dirs},
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_report(out_dir / "load_aware_summary.md", summary)
    print(f"Wrote load-aware common evaluation to {out_dir}")
    print(f"Rows: {len(rows)}; failures: {len(failures)}")


if __name__ == "__main__":
    main()
