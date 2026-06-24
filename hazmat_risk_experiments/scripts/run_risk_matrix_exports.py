"""Batch-export risk matrices for multiple trained configurations."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
EXPORT_SCRIPT = SCRIPT_DIR / "export_risk_matrix.py"


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_int_csv(value: str) -> list[int]:
    return [int(item.strip()) for item in value.split(",") if item.strip()]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\risk_matrices"),
        help="Directory where exported risk matrices are written.",
    )
    parser.add_argument("--models", default="gcn,weighted_gcn,edge_gat,teg_gnn")
    parser.add_argument("--split", default="B", choices=["A", "B", "C"])
    parser.add_argument("--seeds", default="0")
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--hidden-dim", type=int, default=64)
    parser.add_argument("--experiment-tag", default="")
    parser.add_argument("--topk-frac", type=float, default=0.2)
    parser.add_argument("--alpha-ord", type=float, default=0.5)
    parser.add_argument("--alpha-hr", type=float, default=1.0)
    parser.add_argument("--alpha-topk", type=float, default=0.3)
    parser.add_argument("--stage1-epochs", type=int, default=0)
    parser.add_argument("--risk-mode", default="exposure_floor", choices=["raw", "exposure_floor", "positive_only"])
    parser.add_argument("--exposure-delta", type=float, default=0.01)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    failures: list[tuple[str, int, int]] = []
    for model in parse_csv(args.models):
        for seed in parse_int_csv(args.seeds):
            cmd = [
                sys.executable,
                "-B",
                str(EXPORT_SCRIPT),
                "--output-dir",
                str(args.output_dir),
                "--model",
                model,
                "--split",
                args.split,
                "--epochs",
                str(args.epochs),
                "--hidden-dim",
                str(args.hidden_dim),
                "--topk-frac",
                str(args.topk_frac),
                "--alpha-ord",
                str(args.alpha_ord),
                "--alpha-hr",
                str(args.alpha_hr),
                "--alpha-topk",
                str(args.alpha_topk),
                "--stage1-epochs",
                str(args.stage1_epochs),
                "--seed",
                str(seed),
                "--risk-mode",
                args.risk_mode,
                "--exposure-delta",
                str(args.exposure_delta),
            ]
            if args.experiment_tag:
                cmd.extend(["--experiment-tag", args.experiment_tag])
            print(f"[export] model={model} split={args.split} seed={seed} epochs={args.epochs}")
            completed = subprocess.run(cmd, text=True, check=False)
            if completed.returncode != 0:
                failures.append((model, seed, completed.returncode))
    if failures:
        raise SystemExit(f"Export failures: {failures}")


if __name__ == "__main__":
    main()
