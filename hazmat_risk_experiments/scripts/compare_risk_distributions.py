"""Compare edge-risk distributions across risk matrices."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np


DEFAULT_OUTPUT = Path(
    r"D:\PyVRP-main\hazmat_risk_experiments\outputs\risk_matrices"
)


def parse_label_dir(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("risk dirs must use label=path")
    label, path = value.split("=", 1)
    return label.strip(), Path(path.strip())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("risk_dirs", nargs="+", type=parse_label_dir)
    parser.add_argument("--year", default="data_2021", choices=["data_2020", "data_2021"])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--batch-name", default="risk_distribution_model_compare")
    return parser.parse_args()


def distribution_row(label: str, risk_dir: Path, year: str) -> dict[str, object]:
    data = np.load(risk_dir / f"{year}_edge_risk.npz")
    risks = np.asarray(data["R_ij"], dtype=float)
    return {
        "risk_matrix": label,
        "edge_count": int(risks.size),
        "mean": float(risks.mean()),
        "p50": float(np.quantile(risks, 0.50)),
        "p75": float(np.quantile(risks, 0.75)),
        "p90": float(np.quantile(risks, 0.90)),
        "p95": float(np.quantile(risks, 0.95)),
        "p99": float(np.quantile(risks, 0.99)),
        "max": float(risks.max()),
        "std": float(risks.std(ddof=0)),
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_report(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# Risk Matrix Distribution Comparison",
        "",
        "| Risk matrix | Mean | P50 | P75 | P90 | P95 | P99 | Max | Std |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {name} | {mean:.6f} | {p50:.6f} | {p75:.6f} | {p90:.6f} | {p95:.6f} | {p99:.6f} | {maxv:.6f} | {std:.6f} |".format(
                name=row["risk_matrix"],
                mean=row["mean"],
                p50=row["p50"],
                p75=row["p75"],
                p90=row["p90"],
                p95=row["p95"],
                p99=row["p99"],
                maxv=row["max"],
                std=row["std"],
            )
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    out_dir = args.output_dir / args.batch_name
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = [
        distribution_row(label, risk_dir, args.year)
        for label, risk_dir in args.risk_dirs
    ]
    write_csv(out_dir / "risk_distribution_summary.csv", rows)
    write_report(out_dir / "risk_distribution_summary.md", rows)
    print(f"Wrote risk distribution comparison to {out_dir}")


if __name__ == "__main__":
    main()
