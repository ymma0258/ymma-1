"""Compare multiple model risk matrices on a fixed OD set."""

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


ROOT = SCRIPT_DIR.parent
DEFAULT_OUTPUT = ROOT / "outputs_10seed" / "od_paths"
DEFAULT_PAIRS = DEFAULT_OUTPUT / "fixed_od_pairs_150.csv"


def parse_label_dir(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("risk dir entries must be label=path")
    label, path = value.split("=", 1)
    return label.strip(), Path(path.strip())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("risk_dirs", nargs="+", type=parse_label_dir)
    parser.add_argument("--pairs", type=Path, default=DEFAULT_PAIRS)
    parser.add_argument("--year", default="data_2021", choices=["data_2020", "data_2021"])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--batch-name", default="model_od_comparison")
    parser.add_argument("--k-paths", type=int, default=50)
    parser.add_argument("--cvar-alpha", type=float, default=0.90)
    parser.add_argument("--re-threshold", choices=["mean", "p75", "p90"], default="p75")
    return parser.parse_args()


def read_pairs(path: Path) -> list[dict[str, int | str]]:
    if not path.exists():
        raise FileNotFoundError(
            f"OD pair file not found: {path}. For 10seed runs, create it via "
            "run_10seed_pipeline.py or pass --pairs explicitly."
        )
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    pairs: list[dict[str, int | str]] = []
    for row in rows:
        pairs.append(
            {
                "group": row["group"],
                "src": int(row["src"]),
                "dst": int(row["dst"]),
            }
        )
    return pairs


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


def threshold_value(graph, threshold: str) -> float:
    risks = validate_od_paths.np.asarray(
        [data["risk"] for _, _, data in graph.edges(data=True)], dtype=float
    )
    if threshold == "mean":
        return float(validate_od_paths.np.mean(risks))
    if threshold == "p75":
        return float(validate_od_paths.np.percentile(risks, 75))
    if threshold == "p90":
        return float(validate_od_paths.np.percentile(risks, 90))
    raise ValueError(f"Unknown threshold: {threshold}")


def run_source(
    label: str,
    risk_dir: Path,
    year: str,
    pairs: list[dict[str, int | str]],
    k_paths: int,
    cvar_alpha: float,
    re_threshold: str,
    path_cache: dict[tuple[str, int, int], dict[str, list[int] | list[list[int]]]] | None = None,
) -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, object]]:
    graph, scores_norm, _ = validate_od_paths.load_graph(risk_dir, year)
    graph = validate_od_paths.largest_component_subgraph(graph)
    validate_od_paths.add_floor_risk(graph, 0.0)
    re_threshold_value = threshold_value(graph, re_threshold)
    risk_diag = validate_od_paths.risk_distribution_summary(graph, scores_norm)

    rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    for idx, pair in enumerate(pairs, start=1):
        src = int(pair["src"])
        dst = int(pair["dst"])
        try:
            key = (str(pair["group"]), src, dst)
            if path_cache is not None and key in path_cache:
                hop_path = path_cache[key]["hop"]
                candidates = path_cache[key]["candidates"]
                assert isinstance(hop_path, list)
                assert isinstance(candidates, list)
            else:
                hop_path = [
                    int(node)
                    for node in validate_od_paths.nx.shortest_path(
                        graph, src, dst, weight="hop"
                    )
                ]
                candidates = validate_od_paths.shortest_simple_candidates(
                    graph, src, dst, k_paths
                )
            cvar_path = validate_od_paths.choose_cvar_path(
                graph, candidates, re_threshold_value, cvar_alpha
            )
            baseline = validate_od_paths.path_metrics(graph, hop_path, re_threshold_value)
            for method, path in {
                "Hop-shortest": hop_path,
                "CVaR-risk": cvar_path,
            }.items():
                metrics = validate_od_paths.path_metrics(graph, path, re_threshold_value)
                row = validate_od_paths.metric_row(pair, method, path, metrics, baseline)
                row["risk_source"] = label
                row["risk_dir"] = str(risk_dir)
                rows.append(row)
        except Exception as exc:  # noqa: BLE001 - comparison records per-OD failures.
            failures.append(
                {
                    "risk_source": label,
                    "pair_index": idx,
                    **pair,
                    "error": repr(exc),
                }
            )

    meta = {
        "risk_source": label,
        "risk_dir": str(risk_dir),
        "largest_component_nodes": graph.number_of_nodes(),
        "largest_component_edges": graph.number_of_edges(),
        "re_threshold": re_threshold,
        "re_threshold_value": re_threshold_value,
        "risk_diagnostics": risk_diag,
    }
    return rows, failures, meta


def build_path_cache(
    risk_dir: Path,
    year: str,
    pairs: list[dict[str, int | str]],
    k_paths: int,
) -> dict[tuple[str, int, int], dict[str, list[int] | list[list[int]]]]:
    graph, _, _ = validate_od_paths.load_graph(risk_dir, year)
    graph = validate_od_paths.largest_component_subgraph(graph)
    cache: dict[tuple[str, int, int], dict[str, list[int] | list[list[int]]]] = {}
    for pair in pairs:
        src = int(pair["src"])
        dst = int(pair["dst"])
        key = (str(pair["group"]), src, dst)
        cache[key] = {
            "hop": [
                int(node)
                for node in validate_od_paths.nx.shortest_path(graph, src, dst, weight="hop")
            ],
            "candidates": validate_od_paths.shortest_simple_candidates(
                graph, src, dst, k_paths
            ),
        }
    return cache


def summarize_source(rows: list[dict[str, object]], label: str) -> list[dict[str, object]]:
    summary = validate_od_paths.summarize(rows)
    for row in summary:
        row["risk_source"] = label
    return summary


def write_report(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# Fixed-OD Multi-Model Path Comparison",
        "",
        "| Risk source | Method | Hop inc. | Total risk red. | CVaR90 red. | MaxRisk red. | RE red. | Wilcoxon p(total) | Wilcoxon p(CVaR90) |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        if row["method"] != "CVaR-risk":
            continue
        lines.append(
            "| {src} | {method} | {hop:.3%} | {risk:.3%} | {cvar:.3%} | {maxrisk:.3%} | {re:.3%} | {ptotal:.3g} | {pcvar:.3g} |".format(
                src=row["risk_source"],
                method=row["method"],
                hop=float(row["hop_increase_pct_mean"]),
                risk=float(row["total_risk_aggregate_reduction"]),
                cvar=float(row["cvar90_aggregate_reduction"]),
                maxrisk=float(row["max_risk_aggregate_reduction"]),
                re=float(row["re_aggregate_reduction"]),
                ptotal=float(row["total_risk_wilcoxon_p"]),
                pcvar=float(row["cvar90_wilcoxon_p"]),
            )
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    out_dir = args.output_dir / args.batch_name
    out_dir.mkdir(parents=True, exist_ok=True)

    pairs = read_pairs(args.pairs)
    path_cache = (
        build_path_cache(args.risk_dirs[0][1], args.year, pairs, args.k_paths)
        if args.risk_dirs
        else None
    )
    detail_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    metas: list[dict[str, object]] = []

    for label, risk_dir in args.risk_dirs:
        rows, source_failures, meta = run_source(
            label,
            risk_dir,
            args.year,
            pairs,
            args.k_paths,
            args.cvar_alpha,
            args.re_threshold,
            path_cache,
        )
        detail_rows.extend(rows)
        failures.extend(source_failures)
        metas.append(meta)
        summary_rows.extend(summarize_source(rows, label))

    write_csv(out_dir / "model_od_detail.csv", detail_rows)
    write_csv(out_dir / "model_od_summary.csv", summary_rows)
    (out_dir / "model_od_failures.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out_dir / "model_od_meta.json").write_text(
        json.dumps(
            {
                "pairs": str(args.pairs),
                "num_pairs": len(pairs),
                "year": args.year,
                "k_paths": args.k_paths,
                "cvar_alpha": args.cvar_alpha,
                "re_threshold": args.re_threshold,
                "sources": metas,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_report(out_dir / "model_od_summary.md", summary_rows)
    print(f"Wrote fixed-OD model comparison to {out_dir}")
    print(f"Sources: {len(args.risk_dirs)}; failures: {len(failures)}")


if __name__ == "__main__":
    main()
