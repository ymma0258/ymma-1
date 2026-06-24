"""Summarize fixed CVRP customer-set composition for paper tables."""

from __future__ import annotations

import csv
import json
import argparse
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
RISK_DIR = OUTPUTS / "risk_matrices" / "gcn_teg_concat_splitB_seed0_epochs50_floor_0p01"
RISK_DIR_PATTERN = "gcn_teg_concat_splitB_seed{seed}_epochs50_floor_0p01"
MODEL_SEEDS = range(5)
META = {
    "A": OUTPUTS / "pyvrp_cvrp" / "pyvrp50_setA_floor001_teg_e50_s0_4" / "pyvrp_cvrp_meta.json",
    "B": OUTPUTS / "pyvrp_cvrp" / "pyvrp50_setB_floor001_teg_e50_s0_4" / "pyvrp_cvrp_meta.json",
}
SOURCE_OUT_DIR = OUTPUTS / "pyvrp_cvrp" / "customer_set_composition"
PAPER_OUT_DIR = OUTPUTS / "final_figures_stable_tail_gnn" / "paper_results" / "10_customer_sets"


def read_csv_rows(path: Path) -> list[dict[str, str]]:
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--outputs-root",
        type=Path,
        default=OUTPUTS,
        help="Experiment outputs root containing risk_matrices/ and pyvrp_cvrp/.",
    )
    parser.add_argument(
        "--paper-root",
        type=Path,
        default=OUTPUTS / "final_figures_stable_tail_gnn" / "paper_results",
        help="Paper-results root where the customer-set tables are mirrored.",
    )
    parser.add_argument(
        "--source-out-dir",
        type=Path,
        default=None,
        help="Optional source output directory. Defaults to outputs-root/pyvrp_cvrp/customer_set_composition.",
    )
    parser.add_argument(
        "--paper-section",
        default="10_customer_sets",
        help="Paper-results section name for customer-set outputs.",
    )
    parser.add_argument(
        "--risk-dir-pattern",
        default=RISK_DIR_PATTERN,
        help="Risk matrix directory pattern relative to outputs-root/risk_matrices, with {seed}.",
    )
    parser.add_argument(
        "--meta-a",
        type=Path,
        default=META["A"],
        help="Fixed Set A instance metadata.",
    )
    parser.add_argument(
        "--meta-b",
        type=Path,
        default=META["B"],
        help="Fixed Set B instance metadata.",
    )
    parser.add_argument(
        "--suffix",
        default="",
        help="Optional suffix for composition/detail outputs, e.g. '-1'.",
    )
    parser.add_argument(
        "--seeds",
        default="0,1,2,3,4",
        help="Comma-separated Stable-Tail model seeds for suffixed aggregate outputs.",
    )
    return parser.parse_args()


def parse_seed_csv(value: str) -> list[int]:
    return [int(item.strip()) for item in value.split(",") if item.strip()]


def write_outputs(
    out_dir: Path,
    summary_rows: list[dict[str, object]],
    detail_rows: list[dict[str, object]],
    suffix: str = "",
) -> None:
    write_csv(out_dir / f"customer_set_composition{suffix}.csv", summary_rows)
    write_csv(out_dir / f"customer_set_customer_detail{suffix}.csv", detail_rows)

    lines = [
        "# Customer-set composition",
        "",
        "| Set | High-risk customers | High-exposure customers | Mean risk | Risk P90 | Mean exposure | Q1-Q5 distribution |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in summary_rows:
        lines.append(
            "| {set} | {risk_ratio} | {exp_ratio} | {mean_risk} | {risk_p90} | {mean_exp} | {dist} |".format(
                set=row["set"],
                risk_ratio=row["high_risk_customer_ratio_pct"],
                exp_ratio=row["high_exposure_customer_ratio_pct"],
                mean_risk=fmt(float(row["mean_customer_risk_S_norm"])),
                risk_p90=fmt(float(row["risk_p90_S_norm"])),
                mean_exp=fmt(float(row["mean_customer_exposure_norm"])),
                dist=row["Q1_Q5_distribution"],
            )
        )
    lines.extend(
        [
            "",
            "Definitions:",
            "",
            "- High-risk customer: customer node whose Stable-Tail `S_i_norm` is in the global top 20% of 2021 nodes.",
            "- High-exposure customer: customer node whose normalized incident edge exposure is in the global top 20% of 2021 nodes.",
            "- Q1-Q5 distribution: customer-node risk quintiles computed from the global 2021 Stable-Tail `S_i_norm` distribution.",
            "- Risk source: Stable-Tail GNN, split B seed 0, `floor_0.01` edge-risk matrix.",
            "",
        ]
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"customer_set_composition{suffix}.md").write_text("\n".join(lines), encoding="utf-8")


def metric_mean_std(values: list[float]) -> tuple[float, float]:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return 0.0, 0.0
    return float(arr.mean()), float(arr.std(ddof=1)) if arr.size > 1 else 0.0


def fmt_mean_std(value: float, std: float) -> str:
    return f"{value:.6f} +/- {std:.6f}"


def pct_mean_std(value: float, std: float) -> str:
    return f"{value:.1%} +/- {std:.1%}"


def write_aggregate_outputs(
    out_dir: Path,
    summary_rows: list[dict[str, object]],
    detail_rows: list[dict[str, object]],
    suffix: str,
) -> None:
    by_set: dict[str, list[dict[str, object]]] = {}
    for row in summary_rows:
        by_set.setdefault(str(row["set"]), []).append(row)

    aggregate_rows: list[dict[str, object]] = []
    for set_name in sorted(by_set):
        rows = by_set[set_name]
        seed_values = sorted(int(row["seed"]) for row in rows)
        high_risk_mean, high_risk_std = metric_mean_std(
            [float(row["high_risk_customer_ratio"]) for row in rows]
        )
        high_exposure_mean, high_exposure_std = metric_mean_std(
            [float(row["high_exposure_customer_ratio"]) for row in rows]
        )
        mean_risk_mean, mean_risk_std = metric_mean_std(
            [float(row["mean_customer_risk_S_norm"]) for row in rows]
        )
        risk_p90_mean, risk_p90_std = metric_mean_std(
            [float(row["risk_p90_S_norm"]) for row in rows]
        )
        risk_p95_mean, risk_p95_std = metric_mean_std(
            [float(row["risk_p95_S_norm"]) for row in rows]
        )
        mean_exposure_mean, mean_exposure_std = metric_mean_std(
            [float(row["mean_customer_exposure_norm"]) for row in rows]
        )
        q_means: dict[int, tuple[float, float]] = {}
        for idx in range(1, 6):
            q_means[idx] = metric_mean_std([float(row[f"Q{idx}_count"]) for row in rows])

        aggregate_rows.append(
            {
                "set": set_name,
                "seeds": ",".join(str(seed) for seed in seed_values),
                "seed_count": len(seed_values),
                "customer_count": rows[0]["num_customers"],
                "high_risk_customer_ratio_mean": high_risk_mean,
                "high_risk_customer_ratio_std": high_risk_std,
                "high_risk_customer_ratio_display": pct_mean_std(high_risk_mean, high_risk_std),
                "high_exposure_customer_ratio_mean": high_exposure_mean,
                "high_exposure_customer_ratio_std": high_exposure_std,
                "high_exposure_customer_ratio_display": pct_mean_std(
                    high_exposure_mean, high_exposure_std
                ),
                "mean_customer_risk_S_norm_mean": mean_risk_mean,
                "mean_customer_risk_S_norm_std": mean_risk_std,
                "mean_customer_risk_S_norm_display": fmt_mean_std(
                    mean_risk_mean, mean_risk_std
                ),
                "risk_p90_S_norm_mean": risk_p90_mean,
                "risk_p90_S_norm_std": risk_p90_std,
                "risk_p90_S_norm_display": fmt_mean_std(risk_p90_mean, risk_p90_std),
                "risk_p95_S_norm_mean": risk_p95_mean,
                "risk_p95_S_norm_std": risk_p95_std,
                "risk_p95_S_norm_display": fmt_mean_std(risk_p95_mean, risk_p95_std),
                "mean_customer_exposure_norm_mean": mean_exposure_mean,
                "mean_customer_exposure_norm_std": mean_exposure_std,
                "mean_customer_exposure_norm_display": fmt_mean_std(
                    mean_exposure_mean, mean_exposure_std
                ),
                "Q1_count_display": fmt_mean_std(*q_means[1]),
                "Q2_count_display": fmt_mean_std(*q_means[2]),
                "Q3_count_display": fmt_mean_std(*q_means[3]),
                "Q4_count_display": fmt_mean_std(*q_means[4]),
                "Q5_count_display": fmt_mean_std(*q_means[5]),
                "Q1_Q5_distribution": " / ".join(
                    f"Q{idx}:{q_means[idx][0]:.1f} +/- {q_means[idx][1]:.1f}"
                    for idx in range(1, 6)
                ),
            }
        )

    write_csv(out_dir / f"customer_set_composition{suffix}.csv", aggregate_rows)
    write_csv(out_dir / f"customer_set_customer_detail{suffix}.csv", detail_rows)

    lines = [
        "# Customer-set composition",
        "",
        "| Set | Seeds | High-risk customers | High-exposure customers | Mean risk | Risk P90 | Mean exposure | Q1-Q5 distribution |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in aggregate_rows:
        lines.append(
            "| {set} | {seed_count} | {risk_ratio} | {exp_ratio} | {mean_risk} | {risk_p90} | {mean_exp} | {dist} |".format(
                set=row["set"],
                seed_count=row["seed_count"],
                risk_ratio=row["high_risk_customer_ratio_display"],
                exp_ratio=row["high_exposure_customer_ratio_display"],
                mean_risk=row["mean_customer_risk_S_norm_display"],
                risk_p90=row["risk_p90_S_norm_display"],
                mean_exp=row["mean_customer_exposure_norm_display"],
                dist=row["Q1_Q5_distribution"],
            )
        )
    lines.extend(
        [
            "",
            "Definitions:",
            "",
            "- Values are mean +/- std over the listed Stable-Tail GNN Split-B model seeds.",
            "- Customers are fixed Set A/B CVRP customers; only the risk matrix seed changes.",
            "- High-risk customer: customer node whose Stable-Tail `S_i_norm` is in the global top 20% of 2021 nodes for the corresponding seed.",
            "- High-exposure customer: customer node whose normalized incident edge exposure is in the global top 20% of 2021 nodes.",
            "- Q1-Q5 distribution: mean +/- std of customer counts in global 2021 risk quintiles across seeds.",
            "",
        ]
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"customer_set_composition{suffix}.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def write_diagnostics_outputs(
    out_dir: Path,
    diagnostic_rows: list[dict[str, object]],
    suffix: str = "",
) -> None:
    write_csv(out_dir / f"customer_set_diagnostics{suffix}.csv", diagnostic_rows)

    lines = [
        "# Customer-set diagnostics by model seed",
        "",
        "| Set | Seed | Customers | High-risk ratio | High-exposure ratio | Mean risk | Risk P90 | Risk P95 | Mean exposure | Q1 | Q2 | Q3 | Q4 | Q5 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in diagnostic_rows:
        lines.append(
            "| {set} | {seed} | {count} | {hr:.1%} | {he:.1%} | {mean_risk:.6f} | {p90:.6f} | {p95:.6f} | {mean_exp:.6f} | {q1} | {q2} | {q3} | {q4} | {q5} |".format(
                set=row["set"],
                seed=int(row["seed"]),
                count=int(row["customer_count"]),
                hr=float(row["high_risk_ratio"]),
                he=float(row["high_exposure_ratio"]),
                mean_risk=float(row["mean_risk"]),
                p90=float(row["risk_p90"]),
                p95=float(row["risk_p95"]),
                mean_exp=float(row["mean_exposure"]),
                q1=int(row["Q1_count"]),
                q2=int(row["Q2_count"]),
                q3=int(row["Q3_count"]),
                q4=int(row["Q4_count"]),
                q5=int(row["Q5_count"]),
            )
        )
    lines.extend(
        [
            "",
            "Definitions:",
            "",
            "- Each row uses the fixed Set A/B customers and one Stable-Tail GNN Split-B model seed risk matrix.",
            "- High-risk ratio uses the global top-20% threshold of `S_i_norm` for the corresponding seed.",
            "- High-exposure ratio uses the global top-20% threshold of normalized incident exposure for the corresponding seed risk matrix.",
            "- Q1-Q5 counts are risk quintiles computed from the global 2021 `S_i_norm` distribution for the corresponding seed.",
            "",
        ]
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"customer_set_diagnostics{suffix}.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def pct(value: float) -> str:
    return f"{value:.1%}"


def fmt(value: float) -> str:
    return f"{value:.6f}"


def risk_quintile(value: float, thresholds: np.ndarray) -> int:
    return int(np.searchsorted(thresholds, value, side="right") + 1)


def load_risk_context(risk_dir: Path) -> tuple[dict[int, float], dict[int, int], dict[int, float], float, float, np.ndarray]:
    node_rows = read_csv_rows(risk_dir / "data_2021_node_risk.csv")
    edge_rows = read_csv_rows(risk_dir / "data_2021_edge_risk.csv")
    node_risk = {int(row["node_id"]): float(row["S_i_norm"]) for row in node_rows}
    node_label = {int(row["node_id"]): int(row["label"]) for row in node_rows}

    exposure_raw = {node: 0.0 for node in node_risk}
    for row in edge_rows:
        src = int(row["src"])
        dst = int(row["dst"])
        weight = float(row["w_norm"])
        exposure_raw[src] = exposure_raw.get(src, 0.0) + weight
        exposure_raw[dst] = exposure_raw.get(dst, 0.0) + weight

    exposure_values = np.asarray([exposure_raw[node] for node in sorted(node_risk)], dtype=float)
    exposure_min = float(exposure_values.min())
    exposure_max = float(exposure_values.max())
    exposure_norm = {
        node: (exposure_raw[node] - exposure_min) / (exposure_max - exposure_min + 1e-12)
        for node in node_risk
    }

    risk_values = np.asarray(list(node_risk.values()), dtype=float)
    exposure_norm_values = np.asarray(list(exposure_norm.values()), dtype=float)
    high_risk_threshold = float(np.quantile(risk_values, 0.80))
    high_exposure_threshold = float(np.quantile(exposure_norm_values, 0.80))
    quintile_thresholds = np.quantile(risk_values, [0.20, 0.40, 0.60, 0.80])
    return (
        node_risk,
        node_label,
        exposure_norm,
        high_risk_threshold,
        high_exposure_threshold,
        quintile_thresholds,
    )


def customer_set_rows(
    risk_dir: Path,
    seed: int,
    include_detail: bool,
    meta_paths: dict[str, Path],
) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    (
        node_risk,
        node_label,
        exposure_norm,
        high_risk_threshold,
        high_exposure_threshold,
        quintile_thresholds,
    ) = load_risk_context(risk_dir)

    summary_rows: list[dict[str, object]] = []
    detail_rows: list[dict[str, object]] = []
    diagnostic_rows: list[dict[str, object]] = []
    for set_name, meta_path in meta_paths.items():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        customers = [int(node) for node in meta["customers"]]
        risks = np.asarray([node_risk[node] for node in customers], dtype=float)
        exposures = np.asarray([exposure_norm[node] for node in customers], dtype=float)
        high_risk_flags = risks >= high_risk_threshold
        high_exposure_flags = exposures >= high_exposure_threshold
        quintiles = [risk_quintile(node_risk[node], quintile_thresholds) for node in customers]
        quintile_counts = {idx: quintiles.count(idx) for idx in range(1, 6)}
        quintile_pct = {idx: quintile_counts[idx] / len(customers) for idx in range(1, 6)}

        diagnostic_rows.append(
            {
                "set": set_name,
                "seed": seed,
                "customer_count": len(customers),
                "high_risk_ratio": float(high_risk_flags.mean()),
                "high_exposure_ratio": float(high_exposure_flags.mean()),
                "mean_risk": float(risks.mean()),
                "risk_p90": float(np.quantile(risks, 0.90)),
                "risk_p95": float(np.quantile(risks, 0.95)),
                "mean_exposure": float(exposures.mean()),
                "Q1_count": quintile_counts[1],
                "Q2_count": quintile_counts[2],
                "Q3_count": quintile_counts[3],
                "Q4_count": quintile_counts[4],
                "Q5_count": quintile_counts[5],
                "risk_source": str(risk_dir),
                "instance_meta": str(meta_path),
            }
        )

        summary_rows.append(
            {
                "set": set_name,
                "seed": seed,
                "num_customers": len(customers),
                "high_risk_customer_ratio": float(high_risk_flags.mean()),
                "high_risk_customer_ratio_pct": pct(float(high_risk_flags.mean())),
                "high_exposure_customer_ratio": float(high_exposure_flags.mean()),
                "high_exposure_customer_ratio_pct": pct(float(high_exposure_flags.mean())),
                "mean_customer_risk_S_norm": float(risks.mean()),
                "risk_p90_S_norm": float(np.quantile(risks, 0.90)),
                "risk_p95_S_norm": float(np.quantile(risks, 0.95)),
                "mean_customer_exposure_norm": float(exposures.mean()),
                "Q1_count": quintile_counts[1],
                "Q2_count": quintile_counts[2],
                "Q3_count": quintile_counts[3],
                "Q4_count": quintile_counts[4],
                "Q5_count": quintile_counts[5],
                "Q1_Q5_distribution": " / ".join(
                    f"Q{idx}:{quintile_counts[idx]} ({pct(quintile_pct[idx])})"
                    for idx in range(1, 6)
                ),
                "high_risk_threshold_top20_global": high_risk_threshold,
                "high_exposure_threshold_top20_global": high_exposure_threshold,
                "risk_quintile_thresholds_global": json.dumps(
                    [float(val) for val in quintile_thresholds], ensure_ascii=False
                ),
                "risk_source": str(risk_dir),
                "instance_meta": str(meta_path),
            }
        )

        if include_detail:
            for node, q in zip(customers, quintiles):
                detail_rows.append(
                    {
                        "set": set_name,
                        "seed": seed,
                        "node_id": node,
                        "label": node_label.get(node, 0),
                        "S_i_norm": node_risk[node],
                        "exposure_norm": exposure_norm[node],
                        "high_risk_top20": int(node_risk[node] >= high_risk_threshold),
                        "high_exposure_top20": int(exposure_norm[node] >= high_exposure_threshold),
                        "risk_quintile_Q1_Q5": q,
                    }
                )

    return summary_rows, detail_rows, diagnostic_rows


def main() -> None:
    args = parse_args()
    requested_seeds = parse_seed_csv(args.seeds)
    source_out_dir = args.source_out_dir or args.outputs_root / "pyvrp_cvrp" / "customer_set_composition"
    paper_out_dir = args.paper_root / args.paper_section
    meta_paths = {"A": args.meta_a, "B": args.meta_b}

    first_seed = requested_seeds[0]
    first_risk_dir = args.outputs_root / "risk_matrices" / args.risk_dir_pattern.format(seed=first_seed)
    summary_rows, detail_rows, diagnostic_rows = customer_set_rows(
        first_risk_dir, first_seed, True, meta_paths
    )
    all_summaries = list(summary_rows)
    all_details = list(detail_rows)
    all_diagnostics = list(diagnostic_rows)

    for seed in requested_seeds:
        if seed == first_seed:
            continue
        risk_dir = args.outputs_root / "risk_matrices" / args.risk_dir_pattern.format(seed=seed)
        seed_summaries, seed_details, rows = customer_set_rows(risk_dir, seed, True, meta_paths)
        all_summaries.extend(seed_summaries)
        all_details.extend(seed_details)
        all_diagnostics.extend(rows)

    if args.suffix:
        write_aggregate_outputs(source_out_dir, all_summaries, all_details, args.suffix)
        write_aggregate_outputs(paper_out_dir, all_summaries, all_details, args.suffix)
        # The suffixed 10seed paper table still needs per-seed diagnostics:
        # composition/detail are aggregate views, while diagnostics preserve
        # the seed-level values used to defend Set A/B construction.
        write_diagnostics_outputs(source_out_dir, all_diagnostics, args.suffix)
        write_diagnostics_outputs(paper_out_dir, all_diagnostics, args.suffix)
    else:
        write_outputs(source_out_dir, summary_rows, detail_rows, args.suffix)
        write_outputs(paper_out_dir, summary_rows, detail_rows, args.suffix)
        write_diagnostics_outputs(source_out_dir, all_diagnostics)
        write_diagnostics_outputs(paper_out_dir, all_diagnostics)
    print(f"Wrote customer-set composition table to {source_out_dir}")
    print(f"Mirrored customer-set composition table to {paper_out_dir}")


if __name__ == "__main__":
    main()
