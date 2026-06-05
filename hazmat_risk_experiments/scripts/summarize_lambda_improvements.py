"""Summarize lambda=1 improvements over lambda=0 for PyVRP results."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


DEFAULT_SELF = Path(
    r"D:\PyVRP-main\hazmat_risk_experiments\outputs\pyvrp_cvrp"
    r"\concentration_pyvrp50_gcn_teglow_beta1_fixedAB\model_pyvrp_summary.csv"
)
DEFAULT_COMMON = Path(
    r"D:\PyVRP-main\hazmat_risk_experiments\outputs\pyvrp_cvrp"
    r"\common_eval_concentration_pyvrp50_gcn_teglow_ensemble4\common_route_summary.csv"
)
DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\pyvrp_cvrp")
EPS = 1e-12


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-summary", type=Path, default=DEFAULT_SELF)
    parser.add_argument("--common-summary", type=Path, default=DEFAULT_COMMON)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--batch-name", default="lambda1_improvement_tables")
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def row_key(row: dict[str, str]) -> tuple[str, str]:
    source = row.get("risk_source") or row.get("route_source")
    return str(row["customer_set"]), str(source)


def pct_reduction(base: float, method: float) -> float:
    return (base - method) / (base + EPS) if base > EPS else 0.0


def cost_delta_points(base: dict[str, str], method: dict[str, str]) -> float:
    return float(method["cost_increase_pct"]) - float(base["cost_increase_pct"])


def summarize_self(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    by_key_lambda = {
        (row_key(row), float(row["lambda_concentration"])): row
        for row in rows
        if abs(float(row["beta"]) - 1.0) <= 1e-9
    }
    output: list[dict[str, object]] = []
    for (key, lam), base in sorted(by_key_lambda.items()):
        if abs(lam) > 1e-9:
            continue
        method = by_key_lambda.get((key, 1.0))
        if method is None:
            continue
        customer_set, source = key
        output.append(
            {
                "customer_set": customer_set,
                "risk_source": source,
                "delta_cost_points": cost_delta_points(base, method),
                "delta_risk": pct_reduction(
                    float(base["global_risk_mean"]),
                    float(method["global_risk_mean"]),
                ),
                "delta_cvar90": pct_reduction(
                    float(base["global_cvar90_mean"]),
                    float(method["global_cvar90_mean"]),
                ),
                "delta_edge_gini": pct_reduction(
                    float(base["edge_burden_gini_used_mean"]),
                    float(method["edge_burden_gini_used_mean"]),
                ),
                "delta_top10": pct_reduction(
                    float(base["top10_burden_share_mean"]),
                    float(method["top10_burden_share_mean"]),
                ),
                "risk_lambda0": float(base["global_risk_mean"]),
                "risk_lambda1": float(method["global_risk_mean"]),
                "edge_gini_lambda0": float(base["edge_burden_gini_used_mean"]),
                "edge_gini_lambda1": float(method["edge_burden_gini_used_mean"]),
                "top10_lambda0": float(base["top10_burden_share_mean"]),
                "top10_lambda1": float(method["top10_burden_share_mean"]),
            }
        )
    return output


def summarize_common(
    common_rows: list[dict[str, str]],
    self_rows: list[dict[str, str]],
) -> list[dict[str, object]]:
    by_self = {
        (row["customer_set"], row["risk_source"], float(row["lambda_concentration"])): row
        for row in self_rows
        if abs(float(row["beta"]) - 1.0) <= 1e-9
    }
    by_common = {
        (row["customer_set"], row["risk_source"], float(row["lambda_concentration"])): row
        for row in common_rows
        if abs(float(row["beta"]) - 1.0) <= 1e-9
    }
    output: list[dict[str, object]] = []
    for (customer_set, source, lam), base in sorted(by_common.items()):
        if abs(lam) > 1e-9:
            continue
        method = by_common.get((customer_set, source, 1.0))
        self_base = by_self.get((customer_set, source.removesuffix(f"-{customer_set}"), 0.0))
        self_method = by_self.get((customer_set, source.removesuffix(f"-{customer_set}"), 1.0))
        if method is None or self_base is None or self_method is None:
            continue
        output.append(
            {
                "customer_set": customer_set,
                "route_source": source,
                "delta_cost_points": cost_delta_points(self_base, self_method),
                "delta_risk": pct_reduction(
                    float(base["common_global_risk_mean"]),
                    float(method["common_global_risk_mean"]),
                ),
                "delta_cvar90": pct_reduction(
                    float(base["common_global_cvar90_mean"]),
                    float(method["common_global_cvar90_mean"]),
                ),
                "delta_edge_gini": pct_reduction(
                    float(base["common_edge_burden_gini_used_mean"]),
                    float(method["common_edge_burden_gini_used_mean"]),
                ),
                "delta_top10": pct_reduction(
                    float(base["common_top10_burden_share_mean"]),
                    float(method["common_top10_burden_share_mean"]),
                ),
                "risk_lambda0": float(base["common_global_risk_mean"]),
                "risk_lambda1": float(method["common_global_risk_mean"]),
                "edge_gini_lambda0": float(base["common_edge_burden_gini_used_mean"]),
                "edge_gini_lambda1": float(method["common_edge_burden_gini_used_mean"]),
                "top10_lambda0": float(base["common_top10_burden_share_mean"]),
                "top10_lambda1": float(method["common_top10_burden_share_mean"]),
            }
        )
    return output


def write_report(path: Path, title: str, rows: list[dict[str, object]], source_field: str) -> None:
    lines = [
        f"# {title}",
        "",
        "| Set | Source | Delta Cost points | Delta Risk | Delta CVaR90 | Delta Gini | Delta Top10 |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {set_name} | {src} | {cost:.3%} | {risk:.3%} | {cvar:.3%} | {gini:.3%} | {top:.3%} |".format(
                set_name=row["customer_set"],
                src=row[source_field],
                cost=row["delta_cost_points"],
                risk=row["delta_risk"],
                cvar=row["delta_cvar90"],
                gini=row["delta_edge_gini"],
                top=row["delta_top10"],
            )
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    out_dir = args.output_dir / args.batch_name
    out_dir.mkdir(parents=True, exist_ok=True)

    self_rows = read_csv(args.self_summary)
    common_rows = read_csv(args.common_summary)
    self_summary = summarize_self(self_rows)
    common_summary = summarize_common(common_rows, self_rows)

    write_csv(out_dir / "lambda1_self_improvement.csv", self_summary)
    write_csv(out_dir / "lambda1_common_improvement.csv", common_summary)
    write_report(
        out_dir / "lambda1_self_improvement.md",
        "Table A: Self-Evaluated Lambda=1 Improvements over Lambda=0",
        self_summary,
        "risk_source",
    )
    write_report(
        out_dir / "lambda1_common_improvement.md",
        "Table B: Common-Evaluated Lambda=1 Improvements over Lambda=0",
        common_summary,
        "route_source",
    )
    print(f"Wrote lambda improvement tables to {out_dir}")


if __name__ == "__main__":
    main()
