"""Batch-export Stable-Tail post-processing calibrations for model seeds."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
DEFAULT_OUTPUTS = ROOT / "outputs_10seed"
CALIBRATION_SCHEMA_VERSION = 4


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outputs-root", type=Path, default=DEFAULT_OUTPUTS)
    parser.add_argument("--seeds", default="0,1,2,3,4,5,6,7,8,9")
    parser.add_argument(
        "--base-pattern",
        default="stable_tail_gnn_splitB_seed{seed}_epochs50_paper_comparison_10seed_floor_0p01",
    )
    parser.add_argument(
        "--methods",
        default="edge_tail_correction,tail_only_correction,node_calibration,risk_matrix_ensemble",
    )
    parser.add_argument("--alphas", default="0.05,0.10,0.20,0.30")
    parser.add_argument("--rhos", default="0.05,0.10,0.20,0.30,0.40")
    parser.add_argument("--tail-quantile", type=float, default=0.90)
    parser.add_argument("--tail-sharpness", type=float, default=20.0)
    parser.add_argument("--hard-tail", action="store_true")
    parser.add_argument("--p-high-modes", default="raw")
    parser.add_argument("--p-high-gate-threshold", type=float, default=0.5)
    parser.add_argument("--year", choices=["data_2020", "data_2021", "all"], default="data_2021")
    parser.add_argument("--clip", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def code(value: float) -> str:
    return f"{round(value * 100):03d}"


def qcode(value: float) -> str:
    return f"{round(value * 100):03d}"


def mode_tag(mode: str, threshold: float) -> str:
    if mode == "raw":
        return "raw"
    if mode == "gate":
        return f"gate{round(threshold * 100):02d}"
    raise ValueError(f"Unknown P_high mode: {mode}")


def configurations(args: argparse.Namespace) -> list[tuple[str, str, float, float, str, str]]:
    methods = parse_csv(args.methods)
    alphas = [float(value) for value in parse_csv(args.alphas)]
    rhos = [float(value) for value in parse_csv(args.rhos)]
    modes = parse_csv(args.p_high_modes)
    result: list[tuple[str, str, float, float, str, str]] = []
    for mode in modes:
        tag = mode_tag(mode, args.p_high_gate_threshold)
        display_tag = "Raw" if mode == "raw" else f"Gate{round(args.p_high_gate_threshold * 100):02d}"
        for method in methods:
            if method == "risk_matrix_ensemble":
                for rho in rhos:
                    result.append(
                        (mode, method, 0.1, rho, f"Stable-Tail-MatrixEns{display_tag}-r{code(rho)}", f"stable_tail_matrix_ens_{tag}_r{code(rho)}")
                    )
            else:
                prefixes = {
                    "edge_tail_correction": (f"Stable-Tail-EdgeTail{display_tag}", "stable_tail_edge_tail"),
                    "tail_only_correction": (f"Stable-Tail-TailOnly{display_tag}", "stable_tail_tail_only"),
                    "node_calibration": (f"Stable-Tail-NodeCalib{display_tag}", "stable_tail_node_calib"),
                }
                if method not in prefixes:
                    raise ValueError(f"Unknown calibration method: {method}")
                label_prefix, dir_prefix = prefixes[method]
                for alpha in alphas:
                    label = f"{label_prefix}-a{code(alpha)}"
                    stem = f"{dir_prefix}_{tag}_a{code(alpha)}"
                    result.append((mode, method, alpha, 0.2, label, stem))
    return result


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def source_fingerprints(base: Path, year: str) -> dict[str, str]:
    years = ["data_2020", "data_2021"] if year == "all" else [year]
    result: dict[str, str] = {}
    for item_year in years:
        for suffix in ("node_risk.npz", "edge_risk.npz"):
            path = base / f"{item_year}_{suffix}"
            if not path.exists():
                raise FileNotFoundError(f"Stable-Tail source file missing: {path}")
            result[path.name] = file_sha256(path)
    return result


def complete(
    path: Path,
    base: Path,
    method: str,
    alpha: float,
    rho: float,
    mode: str,
    args: argparse.Namespace,
) -> bool:
    meta_path = path / "calibration_meta.json"
    alias_meta_path = path / "meta.json"
    years = ["data_2020", "data_2021"] if args.year == "all" else [args.year]
    required = [
        path / f"{item_year}_{suffix}"
        for item_year in years
        for suffix in ("node_risk.npz", "edge_risk.npz", "edge_risk.csv")
    ]
    if not meta_path.exists() or not all(item.exists() for item in required):
        return False
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    expected = {
        "schema_version": CALIBRATION_SCHEMA_VERSION,
        "method": method,
        "year": args.year,
        "hard_tail": args.hard_tail,
        "clip": args.clip,
        "p_high_mode": mode,
    }
    ok = all(meta.get(key) == value for key, value in expected.items())
    for key, value in {
        "alpha": alpha,
        "rho": rho,
        "tail_quantile": args.tail_quantile,
        "tail_sharpness": args.tail_sharpness,
        "p_high_gate_threshold": args.p_high_gate_threshold,
    }.items():
        ok = ok and abs(float(meta.get(key, -1)) - value) < 1e-12
    ok = ok and Path(str(meta.get("base_risk_dir", ""))).resolve() == base.resolve()
    ok = ok and meta.get("source_fingerprints") == source_fingerprints(base, args.year)
    if ok and not alias_meta_path.exists():
        alias_meta_path.write_text(
            meta_path.read_text(encoding="utf-8"), encoding="utf-8"
        )
    return ok


def main() -> None:
    args = parse_args()
    modes = parse_csv(args.p_high_modes)
    if not modes or any(mode not in {"raw", "gate"} for mode in modes):
        raise ValueError("p-high-modes must contain only raw and/or gate")
    if not 0 <= args.p_high_gate_threshold <= 1:
        raise ValueError("p-high-gate-threshold must be in [0,1]")
    risk_root = args.outputs_root / "risk_matrices"
    risk_root.mkdir(parents=True, exist_ok=True)
    seeds = [int(value) for value in parse_csv(args.seeds)]
    rows: list[dict[str, object]] = []
    rows_by_mode: dict[str, list[dict[str, object]]] = {mode: [] for mode in modes}
    for mode, method, alpha, rho, label, stem in configurations(args):
        for seed in seeds:
            base = risk_root / args.base_pattern.format(seed=seed)
            if not base.exists():
                raise FileNotFoundError(f"Stable-Tail base risk matrix missing: {base}")
            name = f"{stem}_splitB_seed{seed}_floor_0p01"
            dest = risk_root / name
            if not args.force and complete(dest, base, method, alpha, rho, mode, args):
                print(f"[skip] complete calibration {name}")
            else:
                cmd = [
                    sys.executable,
                    "-B",
                    str(SCRIPT_DIR / "export_stable_tail_calibrated_risk_matrix.py"),
                    "--base-risk-dir",
                    str(base),
                    "--output-dir",
                    str(risk_root),
                    "--name",
                    name,
                    "--method",
                    method,
                    "--alpha",
                    str(alpha),
                    "--rho",
                    str(rho),
                    "--tail-quantile",
                    str(args.tail_quantile),
                    "--tail-sharpness",
                    str(args.tail_sharpness),
                    "--p-high-mode",
                    mode,
                    "--p-high-gate-threshold",
                    str(args.p_high_gate_threshold),
                    "--year",
                    args.year,
                ]
                if args.hard_tail:
                    cmd.append("--hard-tail")
                if not args.clip:
                    cmd.append("--no-clip")
                subprocess.run(cmd, check=True)
            row = {
                    "label": label,
                    "seed": seed,
                    "risk_source": f"{label}_seed{seed}",
                    "risk_dir": str(dest),
                    "method": method,
                    "alpha": alpha,
                    "rho": rho,
                    "tail_quantile": args.tail_quantile,
                    "tail_sharpness": args.tail_sharpness,
                    "hard_tail": args.hard_tail,
                    "p_high_mode": mode,
                    "p_high_gate_threshold": args.p_high_gate_threshold,
                    "year": args.year,
                    "clip": args.clip,
                }
            rows.append(row)
            rows_by_mode[mode].append(row)
    for mode, mode_rows in rows_by_mode.items():
        tag = mode_tag(mode, args.p_high_gate_threshold)
        manifest = risk_root / f"stable_tail_calibration_{tag}_sources_10seed.csv"
        with manifest.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(mode_rows[0]))
            writer.writeheader()
            writer.writerows(mode_rows)
        (risk_root / f"stable_tail_calibration_{tag}_sources_10seed.json").write_text(
            json.dumps(mode_rows, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"Wrote {len(mode_rows)} {tag} calibration sources to {manifest}")


if __name__ == "__main__":
    main()
