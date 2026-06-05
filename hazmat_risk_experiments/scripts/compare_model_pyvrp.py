"""Compare model risk matrices in PyVRP with fixed CVRP instances."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
PYVRP_SCRIPT = SCRIPT_DIR / "validate_pyvrp_cvrp.py"
DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\pyvrp_cvrp")
DEFAULT_META_A = DEFAULT_OUTPUT / "pyvrp50_setA_floor001_teg_e50_s0_4" / "pyvrp_cvrp_meta.json"
DEFAULT_META_B = DEFAULT_OUTPUT / "pyvrp50_setB_floor001_teg_e50_s0_4" / "pyvrp_cvrp_meta.json"


def parse_label_dir(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("risk dirs must use label=path")
    label, path = value.split("=", 1)
    return label.strip(), Path(path.strip())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("risk_dirs", nargs="+", type=parse_label_dir)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--meta-a", type=Path, default=DEFAULT_META_A)
    parser.add_argument("--meta-b", type=Path, default=DEFAULT_META_B)
    parser.add_argument("--betas", default="0,1.0")
    parser.add_argument("--lambda-concentration", default="0")
    parser.add_argument("--concentration-threshold", choices=["mean", "p75", "p90"], default="p75")
    parser.add_argument("--seeds", default="0,1,2,3,4")
    parser.add_argument("--max-runtime", type=float, default=10.0)
    parser.add_argument("--batch-name", default="model_pyvrp_comparison")
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


def write_report(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# Fixed-Instance PyVRP Multi-Model Comparison",
        "",
        "| Customer set | Risk source | lambda | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 share |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        if float(row["beta"]) != 1.0:
            continue
        lines.append(
            "| {set_name} | {src} | {lam:g} | {cost:.3%} | {risk:.6f} | {red:.3%} | {cvar:.6f} | {maxveh:.6f} | {vgini:.6f} | {egini:.6f} | {top:.3%} |".format(
                set_name=row["customer_set"],
                lam=float(row.get("lambda_concentration", 0.0)),
                src=row["risk_source"],
                cost=float(row["cost_increase_pct"]),
                risk=float(row["global_risk_mean"]),
                red=float(row["risk_reduction_pct"]),
                cvar=float(row["global_cvar90_mean"]),
                maxveh=float(row["max_vehicle_risk_mean"]),
                vgini=float(row["vehicle_risk_gini_mean"]),
                egini=float(row["edge_burden_gini_used_mean"]),
                top=float(row["top10_burden_share_mean"]),
            )
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def run_one(
    label: str,
    risk_dir: Path,
    customer_set: str,
    meta_path: Path,
    args: argparse.Namespace,
) -> tuple[list[dict[str, object]], dict[str, object] | None]:
    run_name = f"{args.batch_name}_{customer_set}_{label}".replace(" ", "_")
    cmd = [
        sys.executable,
        "-B",
        str(PYVRP_SCRIPT),
        "--risk-dir",
        str(risk_dir),
        "--year",
        "data_2021",
        "--num-customers",
        "50",
        "--num-vehicles",
        "5",
        "--capacity",
        "10",
        "--customer-set",
        customer_set,
        "--betas",
        args.betas,
        "--lambda-concentration",
        args.lambda_concentration,
        "--concentration-threshold",
        args.concentration_threshold,
        "--seeds",
        args.seeds,
        "--max-runtime",
        str(args.max_runtime),
        "--fixed-instance-meta",
        str(meta_path),
        "--batch-name",
        run_name,
    ]
    completed = subprocess.run(
        cmd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        return [], {
            "risk_source": label,
            "customer_set": customer_set,
            "returncode": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        }

    summary_path = args.output_dir / run_name / "pyvrp_cvrp_summary.csv"
    rows: list[dict[str, object]] = []
    for row in read_csv(summary_path):
        row["risk_source"] = label
        row["risk_dir"] = str(risk_dir)
        row["customer_set"] = customer_set
        row["run_name"] = run_name
        rows.append(row)
    return rows, None


def main() -> None:
    args = parse_args()
    out_dir = args.output_dir / args.batch_name
    out_dir.mkdir(parents=True, exist_ok=True)

    all_rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    for label, risk_dir in args.risk_dirs:
        for customer_set, meta_path in [("A", args.meta_a), ("B", args.meta_b)]:
            print(f"[pyvrp] source={label} set={customer_set}")
            rows, failure = run_one(label, risk_dir, customer_set, meta_path, args)
            all_rows.extend(rows)
            if failure:
                failures.append(failure)

    write_csv(out_dir / "model_pyvrp_summary.csv", all_rows)
    (out_dir / "model_pyvrp_failures.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_report(out_dir / "model_pyvrp_summary.md", all_rows)
    print(f"Wrote fixed-instance PyVRP model comparison to {out_dir}")
    print(f"Rows: {len(all_rows)}; failures: {len(failures)}")


if __name__ == "__main__":
    main()
