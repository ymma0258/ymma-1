"""Evaluate saved PyVRP routes with a common reference risk matrix."""

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


DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\pyvrp_cvrp")


def parse_label_dir(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("run dirs must use label=path")
    label, path = value.split("=", 1)
    return label.strip(), Path(path.strip())


def parse_float_list(value: str) -> list[float]:
    return [float(item.strip()) for item in value.split(",") if item.strip()]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dirs", nargs="*", type=parse_label_dir)
    parser.add_argument(
        "--run-list",
        type=Path,
        default=None,
        help="Optional CSV with label and run_dir columns. Appended to positional run dirs.",
    )
    parser.add_argument("--common-risk-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--batch-name", default="common_route_evaluation")
    parser.add_argument("--beta", type=float, default=1.0)
    parser.add_argument(
        "--betas",
        default=None,
        help="Optional comma-separated beta filter. Overrides --beta when provided.",
    )
    parser.add_argument(
        "--lambda-concentration",
        type=float,
        default=None,
        help="Optional lambda_concentration filter. If omitted, all lambdas are evaluated.",
    )
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


def load_run_sources(args: argparse.Namespace) -> list[tuple[str, Path]]:
    sources: list[tuple[str, Path]] = list(args.run_dirs)
    if args.run_list is not None:
        for row in read_csv(args.run_list):
            sources.append((row["label"], Path(row["run_dir"])))
    if not sources:
        raise ValueError("Provide at least one run dir or --run-list CSV.")
    return sources


def route_risks(graph, inst, seq: list[int]) -> np.ndarray:
    risks = []
    for left, right in zip(seq[:-1], seq[1:]):
        path = inst.hop_paths[(left, right)]
        for src, dst in zip(path[:-1], path[1:]):
            risks.append(float(graph[src][dst]["risk"]))
    return np.asarray(risks, dtype=float)


def edge_burdens(graph, inst, sequences: list[list[int]]) -> np.ndarray:
    burdens: dict[tuple[int, int], float] = {}
    for seq in sequences:
        for left, right in zip(seq[:-1], seq[1:]):
            path = inst.hop_paths[(left, right)]
            for src, dst in zip(path[:-1], path[1:]):
                key = (min(src, dst), max(src, dst))
                burdens[key] = burdens.get(key, 0.0) + float(graph[src][dst]["risk"])
    return np.asarray(list(burdens.values()), dtype=float)


def metrics_for_sequences(graph, inst, sequences: list[list[int]]) -> dict[str, float]:
    route_totals = []
    route_cvars = []
    all_risks = []
    for seq in sequences:
        risks = route_risks(graph, inst, seq)
        route_totals.append(float(risks.sum()))
        route_cvars.append(pyvrp_eval.cvar(risks, 0.90))
        all_risks.extend(risks.tolist())

    route_arr = np.asarray(route_totals, dtype=float)
    all_arr = np.asarray(all_risks, dtype=float)
    burdens = edge_burdens(graph, inst, sequences)
    top_count = max(1, int(math.ceil(burdens.size * 0.10))) if burdens.size else 0
    top_share = (
        float(np.sort(burdens)[-top_count:].sum() / (burdens.sum() + pyvrp_eval.EPS))
        if top_count
        else 0.0
    )
    return {
        "common_global_risk": float(all_arr.sum()) if all_arr.size else 0.0,
        "common_global_cvar90": pyvrp_eval.cvar(all_arr, 0.90),
        "common_max_vehicle_risk": float(route_arr.max()) if route_arr.size else 0.0,
        "common_max_vehicle_cvar90": float(max(route_cvars)) if route_cvars else 0.0,
        "common_vehicle_risk_gini": pyvrp_eval.gini(route_arr),
        "common_edge_burden_gini_used": pyvrp_eval.gini(burdens),
        "common_top10_burden_share": top_share,
        "common_max_edge_burden": float(burdens.max()) if burdens.size else 0.0,
    }


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    metrics = [
        "common_global_risk",
        "common_global_cvar90",
        "common_max_vehicle_risk",
        "common_max_vehicle_cvar90",
        "common_vehicle_risk_gini",
        "common_edge_burden_gini_used",
        "common_top10_burden_share",
        "common_max_edge_burden",
    ]
    grouped: dict[tuple[str, str, float, float], list[dict[str, object]]] = {}
    for row in rows:
        grouped.setdefault(
            (
                str(row["risk_source"]),
                str(row["customer_set"]),
                float(row["beta"]),
                float(row.get("lambda_concentration", 0.0)),
            ),
            [],
        ).append(row)

    summary: list[dict[str, object]] = []
    for (source, customer_set, beta, lambda_concentration), group in sorted(grouped.items()):
        out: dict[str, object] = {
            "risk_source": source,
            "customer_set": customer_set,
            "beta": beta,
            "lambda_concentration": lambda_concentration,
            "runs": len(group),
        }
        for metric in metrics:
            values = np.asarray([float(row[metric]) for row in group], dtype=float)
            out[f"{metric}_mean"] = float(values.mean())
            out[f"{metric}_std"] = float(values.std(ddof=1)) if values.size > 1 else 0.0
        summary.append(out)
    return summary


def write_report(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# Common-Risk PyVRP Route Evaluation",
        "",
        "| Customer set | Route source | lambda | Global risk | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 share |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {set_name} | {src} | {lam:g} | {risk:.6f} | {cvar:.6f} | {maxveh:.6f} | {vgini:.6f} | {egini:.6f} | {top:.3%} |".format(
                set_name=row["customer_set"],
                src=row["risk_source"],
                lam=row["lambda_concentration"],
                risk=row["common_global_risk_mean"],
                cvar=row["common_global_cvar90_mean"],
                maxveh=row["common_max_vehicle_risk_mean"],
                vgini=row["common_vehicle_risk_gini_mean"],
                egini=row["common_edge_burden_gini_used_mean"],
                top=row["common_top10_burden_share_mean"],
            )
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    out_dir = args.output_dir / args.batch_name
    out_dir.mkdir(parents=True, exist_ok=True)

    allowed_betas = parse_float_list(args.betas) if args.betas else [args.beta]
    graph, scores_norm, _ = pyvrp_eval.load_graph(args.common_risk_dir, "data_2021")
    graph = pyvrp_eval.largest_component(graph)
    run_sources = load_run_sources(args)

    rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    for label, run_dir in run_sources:
        meta = json.loads((run_dir / "pyvrp_cvrp_meta.json").read_text(encoding="utf-8"))
        try:
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
                row_beta = float(row["beta"])
                if all(abs(row_beta - beta) > 1e-9 for beta in allowed_betas):
                    continue
                lambda_concentration = float(row.get("lambda_concentration", 0.0))
                if (
                    args.lambda_concentration is not None
                    and abs(lambda_concentration - args.lambda_concentration) > 1e-9
                ):
                    continue
                sequences = json.loads(row["routes"])
                metrics = metrics_for_sequences(graph, inst, sequences)
                rows.append(
                    {
                        "risk_source": label,
                        "customer_set": meta["customer_set"],
                        "beta": row_beta,
                        "lambda_concentration": lambda_concentration,
                        "seed": int(row["seed"]),
                        **metrics,
                    }
                )
        except Exception as exc:  # noqa: BLE001 - evaluator records source failures.
            failures.append({"risk_source": label, "run_dir": str(run_dir), "error": repr(exc)})

    summary = summarize(rows)
    write_csv(out_dir / "common_route_detail.csv", rows)
    write_csv(out_dir / "common_route_summary.csv", summary)
    (out_dir / "common_route_failures.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out_dir / "common_route_meta.json").write_text(
        json.dumps(
            {
                "common_risk_dir": str(args.common_risk_dir),
                "betas": allowed_betas,
                "lambda_concentration": args.lambda_concentration,
                "run_dirs": {label: str(path) for label, path in run_sources},
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_report(out_dir / "common_route_summary.md", summary)
    print(f"Wrote common route evaluation to {out_dir}")
    print(f"Rows: {len(rows)}; failures: {len(failures)}")


if __name__ == "__main__":
    main()
