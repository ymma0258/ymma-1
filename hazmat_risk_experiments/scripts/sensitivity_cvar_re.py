"""Sensitivity analysis for CVaR + concentration OD path selection."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import networkx as nx
import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import validate_od_paths as od  # noqa: E402


DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\od_paths")


def parse_csv_int(value: str) -> list[int]:
    return [int(item.strip()) for item in value.split(",") if item.strip()]


def parse_csv_float(value: str) -> list[float]:
    return [float(item.strip()) for item in value.split(",") if item.strip()]


def parse_csv_str(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--risk-dir", type=Path, default=od.DEFAULT_RISK_DIR)
    parser.add_argument("--year", default="data_2021", choices=["data_2020", "data_2021"])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--pairs-per-group", type=int, default=10)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--k-values", default="20,50,100")
    parser.add_argument("--lambda-values", default="0,1,5,10")
    parser.add_argument("--thresholds", default="mean,p75,p90")
    parser.add_argument("--alphas", default="0.8,0.9")
    parser.add_argument("--batch-name", default="cvar_re_sensitivity")
    return parser.parse_args()


def re_with_threshold(risks: np.ndarray, threshold: float) -> float:
    if risks.size == 0:
        return 0.0
    return float(np.maximum(risks - threshold, 0.0).mean())


def cvar_alpha(risks: np.ndarray, alpha: float) -> float:
    return od.cvar(risks, alpha)


def choose_path(
    graph: nx.Graph,
    candidates: list[list[int]],
    threshold: float,
    alpha: float,
    lambda_re: float,
) -> list[int]:
    def objective(path: list[int]) -> tuple[float, float, int]:
        risks = od.path_edge_risks(graph, path)
        cvar_value = cvar_alpha(risks, alpha)
        re_value = re_with_threshold(risks, threshold)
        return (cvar_value + lambda_re * re_value, cvar_value, len(path))

    return min(candidates, key=objective)


def path_equal(left: list[int], right: list[int]) -> bool:
    return len(left) == len(right) and all(a == b for a, b in zip(left, right))


def run_combo(
    graph: nx.Graph,
    pairs: list[dict[str, int | str]],
    candidate_cache: dict[tuple[int, int], list[list[int]]],
    k_paths: int,
    lambda_re: float,
    threshold_name: str,
    threshold: float,
    alpha: float,
) -> dict[str, object]:
    changed = []
    overlaps = []
    re_values = []
    re_base = []
    cvar90_values = []
    cvar90_base = []
    max_values = []

    for pair in pairs:
        src = int(pair["src"])
        dst = int(pair["dst"])
        candidates = candidate_cache[(src, dst)][:k_paths]
        cvar_path = choose_path(graph, candidates, threshold, alpha, 0.0)
        cvar_re_path = choose_path(graph, candidates, threshold, alpha, lambda_re)
        cvar_risks = od.path_edge_risks(graph, cvar_path)
        cvar_re_risks = od.path_edge_risks(graph, cvar_re_path)

        same = path_equal(cvar_path, cvar_re_path)
        changed.append(0 if same else 1)
        overlaps.append(len(set(cvar_path).intersection(cvar_re_path)) / max(1, len(set(cvar_path).union(cvar_re_path))))
        re_base.append(re_with_threshold(cvar_risks, threshold))
        re_values.append(re_with_threshold(cvar_re_risks, threshold))
        cvar90_base.append(cvar_alpha(cvar_risks, 0.90))
        cvar90_values.append(cvar_alpha(cvar_re_risks, 0.90))
        max_values.append(float(cvar_re_risks.max()) if cvar_re_risks.size else 0.0)

    re_base_arr = np.asarray(re_base)
    re_arr = np.asarray(re_values)
    cvar_base_arr = np.asarray(cvar90_base)
    cvar_arr = np.asarray(cvar90_values)
    return {
        "k_paths": k_paths,
        "lambda_re": lambda_re,
        "threshold": threshold_name,
        "alpha": alpha,
        "path_overlap_with_cvar": float(np.mean(overlaps)),
        "selected_path_changed_rate": float(np.mean(changed)),
        "re_mean": float(re_arr.mean()),
        "re_reduction": float((re_base_arr.mean() - re_arr.mean()) / (re_base_arr.mean() + od.EPS)),
        "cvar90": float(cvar_arr.mean()),
        "cvar90_reduction": float((cvar_base_arr.mean() - cvar_arr.mean()) / (cvar_base_arr.mean() + od.EPS)),
        "maxrisk_mean": float(np.mean(max_values)),
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_report(path: Path, rows: list[dict[str, object]], meta: dict[str, object]) -> None:
    lines = [
        "# CVaR + Concentration Sensitivity Report",
        "",
        f"- OD pairs: `{meta['num_pairs']}`",
        f"- k values: `{meta['k_values']}`",
        f"- lambda values: `{meta['lambda_values']}`",
        f"- thresholds: `{meta['thresholds']}`",
        f"- alphas: `{meta['alphas']}`",
        "",
        "| k | lambda | threshold | alpha | changed rate | overlap | RE mean | RE reduction | CVaR90 | CVaR90 reduction |",
        "|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {k} | {lam:g} | {thr} | {alpha:.2f} | {changed:.3%} | {overlap:.4f} | {re:.6f} | {rered:.3%} | {cvar:.6f} | {cvarred:.3%} |".format(
                k=row["k_paths"],
                lam=row["lambda_re"],
                thr=row["threshold"],
                alpha=row["alpha"],
                changed=row["selected_path_changed_rate"],
                overlap=row["path_overlap_with_cvar"],
                re=row["re_mean"],
                rered=row["re_reduction"],
                cvar=row["cvar90"],
                cvarred=row["cvar90_reduction"],
            )
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    out_dir = args.output_dir / args.batch_name
    out_dir.mkdir(parents=True, exist_ok=True)

    graph, scores_norm, _ = od.load_graph(args.risk_dir, args.year)
    graph = od.largest_component_subgraph(graph)
    pairs = od.sample_pairs(graph, scores_norm, args.pairs_per_group, args.seed)
    max_k = max(parse_csv_int(args.k_values))
    candidate_cache = {
        (int(pair["src"]), int(pair["dst"])): od.shortest_simple_candidates(
            graph, int(pair["src"]), int(pair["dst"]), max_k
        )
        for pair in pairs
    }
    risks = np.asarray([data["risk"] for _, _, data in graph.edges(data=True)], dtype=float)
    thresholds = {
        "mean": float(risks.mean()),
        "p75": float(np.percentile(risks, 75)),
        "p90": float(np.percentile(risks, 90)),
    }

    rows = []
    for k in parse_csv_int(args.k_values):
        for lam in parse_csv_float(args.lambda_values):
            for threshold_name in parse_csv_str(args.thresholds):
                for alpha in parse_csv_float(args.alphas):
                    rows.append(
                        run_combo(
                            graph,
                            pairs,
                            candidate_cache,
                            k,
                            lam,
                            threshold_name,
                            thresholds[threshold_name],
                            alpha,
                        )
                    )

    meta = {
        "year": args.year,
        "risk_dir": str(args.risk_dir),
        "num_pairs": len(pairs),
        "max_cached_k": max_k,
        "pairs_per_group": args.pairs_per_group,
        "seed": args.seed,
        "k_values": parse_csv_int(args.k_values),
        "lambda_values": parse_csv_float(args.lambda_values),
        "thresholds": parse_csv_str(args.thresholds),
        "threshold_values": thresholds,
        "alphas": parse_csv_float(args.alphas),
    }
    write_csv(out_dir / "sensitivity_summary.csv", rows)
    (out_dir / "sensitivity_meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_report(out_dir / "sensitivity_report.md", rows, meta)
    print(f"Wrote CVaR+RE sensitivity to {out_dir}")


if __name__ == "__main__":
    main()
