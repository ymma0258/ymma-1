"""Run the isolated 10seed Stable-Tail GNN experiment pipeline.

This orchestrator writes formal 10seed outputs to ``outputs_10seed`` and keeps
the existing 5seed outputs untouched.  It is intentionally command-oriented:
each stage delegates to the existing experiment scripts, but passes explicit
output roots and 10seed batch names.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import json
import shutil
import subprocess
import sys
from pathlib import Path
from statistics import mean, stdev


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
DEFAULT_OUTPUTS = ROOT / "outputs_10seed"
DEFAULT_FINAL = ROOT / "outputs" / "final_figures_stable_tail_gnn_10seed"
LEGACY_OUTPUTS = ROOT / "outputs"

PYTHON = sys.executable
SEEDS_10 = "0,1,2,3,4,5,6,7,8,9"
LOW_TAIL_ARGS = [
    "--alpha-ord",
    "0.3",
    "--alpha-hr",
    "0.5",
    "--alpha-topk",
    "0.1",
    "--topk-frac",
    "0.2",
    "--stage1-epochs",
    "0",
]
PAPER_COMPARISON_TAG = "paper_comparison_10seed"
PAPER_NO_TAIL_TAG = "paper_no_tail_loss_10seed"
PAPER_MODELS = "gcn,gat,graphsage,teg_only,stable_tail_gnn"
STRONG_BASELINE_TAG = "paper_strong_baselines_10seed"
STRONG_MODELS = "sgformer_adapted,gradformer_adapted"
FUSION_COMPARISON_TAG = "paper_teg_concat_fusions_10seed"
FUSION_MODELS = "graphsage_teg_concat,sgformer_teg_concat"
GATE_COMPARISON_TAG = "paper_teg_gate_fusions_10seed"
GATE_MODELS = "sgformer_teg_gate,graphsage_teg_gate"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outputs-root", type=Path, default=DEFAULT_OUTPUTS)
    parser.add_argument("--final-root", type=Path, default=DEFAULT_FINAL)
    parser.add_argument("--seeds", default=SEEDS_10)
    parser.add_argument("--pyvrp-seeds", default=SEEDS_10)
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--max-runtime", type=float, default=10.0)
    parser.add_argument(
        "--pyvrp-workers",
        type=int,
        default=4,
        help="Independent PyVRP risk-source chunks to run concurrently.",
    )
    parser.add_argument(
        "--stages",
        default=(
            "paper_models,strong_models,fusion_models,gate_models,"
            "paper_risk,strong_risk,fusion_risk,gate_risk,paper_tables,"
            "paper_od,strong_od,fusion_od,gate_od,paper_pyvrp,strong_pyvrp,"
            "fusion_pyvrp,gate_pyvrp,gate_load_eval,customer_sets,"
            "consistency_checks"
        ),
        help=(
            "Comma-separated stages: models,node_tables,risk,od,pyvrp,"
            "concentration,customer_sets,consistency_checks,"
            "paper_models,paper_tables,paper_risk,paper_od,paper_pyvrp,"
            "strong_models,strong_risk,strong_od,strong_pyvrp,paper_load_eval,"
            "fusion_models,fusion_risk,fusion_od,fusion_pyvrp,fusion_load_eval,"
            "gate_models,gate_risk,gate_od,gate_pyvrp,gate_load_eval. The paper_* stages "
            "run the new GCN/GAT/GraphSAGE/TEG-only/Stable-Tail comparison."
        ),
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_seed_csv(value: str) -> list[int]:
    return [int(item.strip()) for item in value.split(",") if item.strip()]


def run(cmd: list[str], dry_run: bool) -> None:
    print("[cmd] " + " ".join(str(part) for part in cmd))
    if not dry_run:
        subprocess.run(cmd, check=True)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
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


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def mean_std(values: list[float]) -> tuple[float, float]:
    if not values:
        return 0.0, 0.0
    return mean(values), stdev(values) if len(values) > 1 else 0.0


def fmt_mean_std(value: float, std: float, pct: bool = True) -> str:
    if pct:
        return f"{value:.3%} +/- {std:.3%}"
    return f"{value:.6f} +/- {std:.6f}"


def script(name: str) -> str:
    return str(SCRIPT_DIR / name)


def model_dir(outputs_root: Path) -> Path:
    return outputs_root / "models"


def risk_root(outputs_root: Path) -> Path:
    return outputs_root / "risk_matrices"


def pyvrp_root(outputs_root: Path) -> Path:
    return outputs_root / "pyvrp_cvrp"


def od_root(outputs_root: Path) -> Path:
    return outputs_root / "od_paths"


def fixed_od_pairs_path(args: argparse.Namespace) -> Path:
    return od_root(args.outputs_root) / "fixed_od_pairs_150.csv"


def ensure_fixed_od_pairs(args: argparse.Namespace) -> Path:
    """Keep the formal 150 OD pairs inside the 10seed output tree.

    Earlier exploratory scripts defaulted to the old 5seed ``outputs`` tree.
    The 10seed pipeline must be self-contained, so this helper copies an
    existing pair file when available or reconstructs the unique OD list from
    the current 10seed model comparison details.
    """
    dest = fixed_od_pairs_path(args)
    if args.dry_run or dest.exists():
        return dest

    dest.parent.mkdir(parents=True, exist_ok=True)
    comparison_dir = od_root(args.outputs_root) / "model_od_comparison_10seed"
    meta_path = comparison_dir / "model_od_meta.json"
    if meta_path.exists():
        pairs_path = Path(json.loads(meta_path.read_text(encoding="utf-8")).get("pairs", ""))
        if pairs_path.exists():
            shutil.copy2(pairs_path, dest)
            print(f"[od] copied fixed OD pairs from {pairs_path}")
            return dest

    detail_path = comparison_dir / "model_od_detail.csv"
    if detail_path.exists():
        rows = read_csv(detail_path)
        pairs: list[dict[str, object]] = []
        seen: set[tuple[str, str, str]] = set()
        for row in rows:
            key = (row["group"], row["src"], row["dst"])
            if key in seen:
                continue
            seen.add(key)
            pairs.append({"group": row["group"], "src": row["src"], "dst": row["dst"]})
        if pairs:
            write_csv(dest, pairs)
            print(f"[od] rebuilt {len(pairs)} fixed OD pairs from {detail_path}")
            return dest

    raise FileNotFoundError(
        "Cannot find or rebuild fixed OD pairs. Run one OD comparison once or "
        f"provide {dest} before running the OD stage."
    )


def fixed_instance_meta_paths(args: argparse.Namespace) -> dict[str, Path]:
    root = pyvrp_root(args.outputs_root) / "fixed_instances_10seed"
    return {
        "A": root / "setA" / "pyvrp_cvrp_meta.json",
        "B": root / "setB" / "pyvrp_cvrp_meta.json",
    }


def existing_meta_candidates(args: argparse.Namespace, customer_set: str) -> list[Path]:
    """Prefer already-created 10seed instance metadata before bootstrapping.

    The old 5seed workflow stored Set A/B metadata under ``outputs/``.  The
    10seed pipeline must not depend on those files because the paper package is
    now isolated under ``outputs_10seed``.
    """
    first_seed = parse_seed_csv(args.seeds)[0]
    root = pyvrp_root(args.outputs_root)
    preferred = [
        root
        / (
            "stable_tail_pyvrp50_beta_curve_10seed__"
            f"Stable-Tail-GNN_seed{first_seed}_{customer_set}_Stable-Tail-GNN_seed{first_seed}"
        )
        / "pyvrp_cvrp_meta.json",
        root
        / (
            "model_pyvrp50_beta1_10seed__"
            f"Stable-Tail-GNN_seed{first_seed}_{customer_set}_Stable-Tail-GNN_seed{first_seed}"
        )
        / "pyvrp_cvrp_meta.json",
    ]
    discovered = sorted(root.glob(f"*_{customer_set}_*/pyvrp_cvrp_meta.json"))
    seen: set[Path] = set()
    result: list[Path] = []
    for path in [*preferred, *discovered]:
        resolved = path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            result.append(path)
    return result


def ensure_fixed_instance_meta(args: argparse.Namespace) -> dict[str, Path]:
    """Create canonical 10seed Set A/B metadata if it is not present.

    PyVRP comparisons are only fair when all risk matrices use the same depot
    and customer nodes.  This helper keeps that fixed instance inside the
    10seed output tree, so reruns do not silently fall back to deleted or stale
    5seed metadata.
    """
    meta_paths = fixed_instance_meta_paths(args)
    if args.dry_run:
        return meta_paths

    first_seed = parse_seed_csv(args.seeds)[0]
    stable_risk = risk_dir(args.outputs_root, stable_tail_dir(first_seed))
    for customer_set, dest in meta_paths.items():
        if dest.exists():
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        copied = False
        for candidate in existing_meta_candidates(args, customer_set):
            if candidate.exists() and candidate.resolve() != dest.resolve():
                shutil.copy2(candidate, dest)
                print(f"[meta] copied fixed Set {customer_set} instance from {candidate}")
                copied = True
                break
        if copied:
            continue
        if not stable_risk.exists():
            raise FileNotFoundError(
                f"Cannot bootstrap fixed Set {customer_set} metadata because "
                f"Stable-Tail seed {first_seed} risk matrix is missing: {stable_risk}"
            )
        batch_name = f"fixed_instance_10seed_set{customer_set}"
        run(
            [
                PYTHON,
                "-B",
                script("validate_pyvrp_cvrp.py"),
                "--output-dir",
                str(pyvrp_root(args.outputs_root)),
                "--risk-dir",
                str(stable_risk),
                "--num-customers",
                "50",
                "--num-vehicles",
                "5",
                "--capacity",
                "10",
                "--customer-set",
                customer_set,
                "--betas",
                "0",
                "--lambda-concentration",
                "0",
                "--seeds",
                str(first_seed),
                "--sample-seed",
                "0",
                "--max-runtime",
                str(args.max_runtime),
                "--batch-name",
                batch_name,
            ],
            dry_run=False,
        )
        generated = pyvrp_root(args.outputs_root) / batch_name / "pyvrp_cvrp_meta.json"
        if not generated.exists():
            raise FileNotFoundError(f"Failed to bootstrap fixed metadata: {generated}")
        shutil.copy2(generated, dest)
    return meta_paths


def risk_dir(outputs_root: Path, name: str) -> Path:
    return risk_root(outputs_root) / name


def gcn_dir(seed: int) -> str:
    return f"gcn_splitB_seed{seed}_epochs50_10seed_floor_0p01"


def weighted_dir(seed: int) -> str:
    return f"weighted_gcn_splitB_seed{seed}_epochs50_10seed_floor_0p01"


def edge_gat_dir(seed: int) -> str:
    return f"edge_gat_splitB_seed{seed}_epochs50_10seed_floor_0p01"


def teg_low_dir(seed: int) -> str:
    return f"teg_gnn_splitB_seed{seed}_epochs50_teg_low_tail_10seed_floor_0p01"


def stable_tail_dir(seed: int) -> str:
    return f"gcn_teg_concat_splitB_seed{seed}_epochs50_10seed_floor_0p01"


def paper_model_dir(model: str, seed: int) -> str:
    return (
        f"{model}_splitB_seed{seed}_epochs50_"
        f"{PAPER_COMPARISON_TAG}_floor_0p01"
    )


def paper_no_tail_dir(seed: int) -> str:
    return (
        f"stable_tail_gnn_splitB_seed{seed}_epochs50_"
        f"{PAPER_NO_TAIL_TAG}_floor_0p01"
    )


def strong_model_dir(model: str, seed: int) -> str:
    return (
        f"{model}_splitB_seed{seed}_epochs50_"
        f"{STRONG_BASELINE_TAG}_floor_0p01"
    )


def fusion_model_dir(model: str, seed: int) -> str:
    return (
        f"{model}_splitB_seed{seed}_epochs50_"
        f"{FUSION_COMPARISON_TAG}_floor_0p01"
    )


def gate_model_dir(model: str, seed: int) -> str:
    return (
        f"{model}_splitB_seed{seed}_epochs50_"
        f"{GATE_COMPARISON_TAG}_floor_0p01"
    )


def fusion_dir(seed: int, rho: str) -> str:
    return f"fusion_gcn_teg_low_rho{rho}_splitB_seed{seed}_epochs50_10seed_floor_0p01"


def ensemble4_dir(seed: int) -> str:
    return f"ensemble_graph4_teg_low_tail_splitB_seed{seed}_epochs50_10seed_floor_0p01"


def label_ref_dir(seed: int) -> str:
    return f"label_reference_splitB_seed{seed}_10seed_floor_0p01"


def common_ensemble_dir() -> str:
    return "common_ensemble4_10seed_floor_0p01"


def paper_common_reference_dir() -> str:
    return "paper_common_reference_10seed_floor_0p01"


MODEL_RISK_DIRS = {
    "GCN": gcn_dir,
    "Weighted-GCN": weighted_dir,
    "Edge-GAT": edge_gat_dir,
    "TEG-low": teg_low_dir,
    "Stable-Tail-GNN": stable_tail_dir,
    "Fusion-rho025": lambda seed: fusion_dir(seed, "025"),
    "Ensemble-4": ensemble4_dir,
    "GCN (paper)": lambda seed: paper_model_dir("gcn", seed),
    "GAT": lambda seed: paper_model_dir("gat", seed),
    "GraphSAGE": lambda seed: paper_model_dir("graphsage", seed),
    "TEG-only": lambda seed: paper_model_dir("teg_only", seed),
    "Stable-Tail GNN (paper)": lambda seed: paper_model_dir(
        "stable_tail_gnn", seed
    ),
    "Stable-Tail w/o Tail Loss": paper_no_tail_dir,
    "SGFormer-adapted": lambda seed: strong_model_dir("sgformer_adapted", seed),
    "Gradformer-adapted": lambda seed: strong_model_dir(
        "gradformer_adapted", seed
    ),
    "GraphSAGE-TEG-Concat": lambda seed: fusion_model_dir(
        "graphsage_teg_concat", seed
    ),
    "SGFormer-TEG-Concat": lambda seed: fusion_model_dir(
        "sgformer_teg_concat", seed
    ),
    "SGFormer-TEG-Gate": lambda seed: gate_model_dir(
        "sgformer_teg_gate", seed
    ),
    "GraphSAGE-TEG-Gate": lambda seed: gate_model_dir(
        "graphsage_teg_gate", seed
    ),
}


def risk_sources(args: argparse.Namespace, model_names: list[str]) -> list[tuple[str, Path]]:
    sources: list[tuple[str, Path]] = []
    for model in model_names:
        dir_fn = MODEL_RISK_DIRS[model]
        for seed in parse_seed_csv(args.seeds):
            label = f"{model}_seed{seed}"
            sources.append((label, risk_dir(args.outputs_root, dir_fn(seed))))
    return sources


def source_args(sources: list[tuple[str, Path]]) -> list[str]:
    return [f"{label}={path}" for label, path in sources]


def write_run_list(path: Path, sources: list[tuple[str, Path]]) -> Path:
    write_csv(
        path,
        [{"label": label, "run_dir": str(run_dir)} for label, run_dir in sources],
    )
    return path


def safe_name(value: str) -> str:
    safe = value.replace(" ", "_")
    for char in "\\/:*?\"<>|":
        safe = safe.replace(char, "_")
    return safe


def run_dirs_for_batch(
    args: argparse.Namespace,
    batch_name: str,
    sources: list[tuple[str, Path]],
) -> list[tuple[str, Path]]:
    run_dirs: list[tuple[str, Path]] = []
    for label, _ in sources:
        for customer_set in ["A", "B"]:
            run_name = f"{batch_name}_{customer_set}_{label}".replace(" ", "_")
            run_dirs.append((f"{customer_set}_{label}", pyvrp_root(args.outputs_root) / run_name))
    return run_dirs


def run_dirs_for_chunked_batch(
    args: argparse.Namespace,
    batch_name: str,
    sources: list[tuple[str, Path]],
) -> list[tuple[str, Path]]:
    run_dirs: list[tuple[str, Path]] = []
    for label, _ in sources:
        part_batch = f"{batch_name}__{safe_name(label)}"
        for customer_set in ["A", "B"]:
            run_name = f"{part_batch}_{customer_set}_{label}".replace(" ", "_")
            run_dirs.append((f"{customer_set}_{label}", pyvrp_root(args.outputs_root) / run_name))
    return run_dirs


def stage_models(args: argparse.Namespace) -> None:
    out = model_dir(args.outputs_root)
    base = [
        PYTHON,
        "-B",
        script("run_model_experiments.py"),
        "--output-dir",
        str(out),
        "--splits",
        "A,B",
        "--seeds",
        args.seeds,
        "--epochs",
        str(args.epochs),
    ]
    batches = [
        ("mlp", "mlp_A_B_s0_9_e50_10seed", "10seed", []),
        (
            "gcn,weighted_gcn,edge_gat,teg_gnn",
            "formal_graph_models_A_B_s0_9_e50_10seed",
            "10seed",
            [],
        ),
        (
            "teg_gnn",
            "teg_loss_teg_low_tail_s0_9_e50_10seed",
            "teg_low_tail_10seed",
            LOW_TAIL_ARGS,
        ),
        (
            "gcn,teg_gnn,gcn_teg_concat,gcn_teg_residual_fixed,gcn_teg_residual_learnable",
            "gcn_stabilized_teg_s0_9_e50_10seed",
            "gcn_stabilized_lowtail_10seed",
            LOW_TAIL_ARGS,
        ),
    ]
    for models, batch_name, tag, extra in batches:
        run(
            base
            + [
                "--models",
                models,
                "--batch-name",
                batch_name,
                "--experiment-tag",
                tag,
            ]
            + extra,
            args.dry_run,
        )


def stage_paper_models(args: argparse.Namespace) -> None:
    """Train the paper-facing main comparison and loss ablation on Split B."""

    base = [
        PYTHON,
        "-B",
        script("run_model_experiments.py"),
        "--output-dir",
        str(model_dir(args.outputs_root)),
        "--splits",
        "B",
        "--seeds",
        args.seeds,
        "--epochs",
        str(args.epochs),
    ]
    run(
        base
        + [
            "--models",
            PAPER_MODELS,
            "--batch-name",
            "paper_main_comparison_splitB_10seed",
            "--experiment-tag",
            PAPER_COMPARISON_TAG,
        ],
        args.dry_run,
    )
    run(
        base
        + [
            "--models",
            "stable_tail_gnn",
            "--batch-name",
            "paper_stable_tail_no_tail_loss_splitB_10seed",
            "--experiment-tag",
            PAPER_NO_TAIL_TAG,
            "--alpha-hr",
            "0",
            "--alpha-topk",
            "0",
        ],
        args.dry_run,
    )


def stage_strong_models(args: argparse.Namespace) -> None:
    run(
        [
            PYTHON,
            "-B",
            script("run_model_experiments.py"),
            "--output-dir",
            str(model_dir(args.outputs_root)),
            "--splits",
            "B",
            "--seeds",
            args.seeds,
            "--epochs",
            str(args.epochs),
            "--models",
            STRONG_MODELS,
            "--batch-name",
            "paper_strong_baselines_splitB_10seed",
            "--experiment-tag",
            STRONG_BASELINE_TAG,
        ],
        args.dry_run,
    )


def stage_fusion_models(args: argparse.Namespace) -> None:
    run(
        [
            PYTHON,
            "-B",
            script("run_model_experiments.py"),
            "--output-dir",
            str(model_dir(args.outputs_root)),
            "--splits",
            "B",
            "--seeds",
            args.seeds,
            "--epochs",
            str(args.epochs),
            "--models",
            FUSION_MODELS,
            "--batch-name",
            "paper_teg_concat_fusions_splitB_10seed",
            "--experiment-tag",
            FUSION_COMPARISON_TAG,
        ],
        args.dry_run,
    )


def stage_gate_models(args: argparse.Namespace) -> None:
    run(
        [
            PYTHON,
            "-B",
            script("run_model_experiments.py"),
            "--output-dir",
            str(model_dir(args.outputs_root)),
            "--splits",
            "B",
            "--seeds",
            args.seeds,
            "--epochs",
            str(args.epochs),
            "--models",
            GATE_MODELS,
            "--batch-name",
            "paper_teg_gate_fusions_splitB_10seed",
            "--experiment-tag",
            GATE_COMPARISON_TAG,
        ],
        args.dry_run,
    )


def stage_node_tables(args: argparse.Namespace) -> None:
    out_dir = model_dir(args.outputs_root) / "node_risk_eval_tables_10seed"
    paper_dir = args.final_root / "paper_results" / "02_model_results"
    run(
        [
            PYTHON,
            "-B",
            script("summarize_node_risk_eval_tables.py"),
            "--mlp-source",
            str(model_dir(args.outputs_root) / "mlp_A_B_s0_9_e50_10seed_summary.csv"),
            "--formal-source",
            str(
                model_dir(args.outputs_root)
                / "formal_graph_models_A_B_s0_9_e50_10seed_summary.csv"
            ),
            "--teg-low-source",
            str(model_dir(args.outputs_root) / "teg_loss_teg_low_tail_s0_9_e50_10seed_summary.csv"),
            "--stable-source",
            str(
                model_dir(args.outputs_root)
                / "gcn_stabilized_teg_s0_9_e50_10seed_summary.csv"
            ),
            "--source-out-dir",
            str(out_dir),
            "--paper-out-dir",
            str(paper_dir),
            "--suffix",
            "_10seed",
            "--note-label",
            (
                "formal_graph_models_A_B_s0_9_e50_10seed_summary.csv + "
                "teg_loss_teg_low_tail_s0_9_e50_10seed_summary.csv + "
                "gcn_stabilized_teg_s0_9_e50_10seed_summary.csv"
            ),
        ],
        args.dry_run,
    )


def export_base(
    args: argparse.Namespace,
    models: str,
    tag: str,
    extra_loss_args: list[str] | None = None,
    checkpoint_tag: str | None = None,
) -> None:
    cmd = [
        PYTHON,
        "-B",
        script("run_risk_matrix_exports.py"),
        "--output-dir",
        str(risk_root(args.outputs_root)),
        "--models",
        models,
        "--split",
        "B",
        "--seeds",
        args.seeds,
        "--epochs",
        str(args.epochs),
        "--risk-mode",
        "exposure_floor",
        "--exposure-delta",
        "0.01",
        "--experiment-tag",
        tag,
        "--checkpoint-dir",
        str(model_dir(args.outputs_root) / "checkpoints"),
    ]
    if checkpoint_tag is not None:
        cmd.extend(["--checkpoint-tag", checkpoint_tag])
    if extra_loss_args:
        cmd.extend(extra_loss_args)
    run(cmd, args.dry_run)


def stage_risk(args: argparse.Namespace) -> None:
    export_base(args, "gcn,weighted_gcn,edge_gat", "10seed")
    export_base(args, "teg_gnn", "teg_low_tail_10seed", LOW_TAIL_ARGS)
    export_base(
        args,
        "gcn_teg_concat",
        "10seed",
        LOW_TAIL_ARGS,
        checkpoint_tag="gcn_stabilized_lowtail_10seed",
    )

    seeds = parse_seed_csv(args.seeds)
    for seed in seeds:
        gcn = risk_dir(args.outputs_root, gcn_dir(seed))
        weighted = risk_dir(args.outputs_root, weighted_dir(seed))
        edge = risk_dir(args.outputs_root, edge_gat_dir(seed))
        teg = risk_dir(args.outputs_root, teg_low_dir(seed))
        stable = risk_dir(args.outputs_root, stable_tail_dir(seed))

        for rho, weights in [("025", "0.75,0.25"), ("050", "0.5,0.5"), ("075", "0.25,0.75")]:
            run(
                [
                    PYTHON,
                    "-B",
                    script("export_ensemble_risk_matrix.py"),
                    str(gcn),
                    str(teg),
                    "--output-dir",
                    str(risk_root(args.outputs_root)),
                    "--name",
                    fusion_dir(seed, rho),
                    "--weights",
                    weights,
                ],
                args.dry_run,
            )
        run(
            [
                PYTHON,
                "-B",
                script("export_ensemble_risk_matrix.py"),
                str(gcn),
                str(weighted),
                str(edge),
                str(teg),
                "--output-dir",
                str(risk_root(args.outputs_root)),
                "--name",
                ensemble4_dir(seed),
            ],
            args.dry_run,
        )
        run(
            [
                PYTHON,
                "-B",
                script("export_label_oracle_risk_matrix.py"),
                "--base-risk-dir",
                str(stable),
                "--output-dir",
                str(risk_root(args.outputs_root)),
                "--name",
                label_ref_dir(seed),
            ],
            args.dry_run,
        )

    ensemble_dirs = [
        str(risk_dir(args.outputs_root, ensemble4_dir(seed)))
        for seed in seeds
    ]
    run(
        [
            PYTHON,
            "-B",
            script("export_ensemble_risk_matrix.py"),
            *ensemble_dirs,
            "--output-dir",
            str(risk_root(args.outputs_root)),
            "--name",
            common_ensemble_dir(),
        ],
        args.dry_run,
    )


def aggregate_od_model_summary(batch_dir: Path) -> None:
    src = batch_dir / "model_od_summary.csv"
    if not src.exists():
        return
    rows = read_csv(src)
    metrics = {
        "hop_increase": "hop_increase_pct_mean",
        "total_risk_reduction": "total_risk_aggregate_reduction",
        "cvar90_reduction": "cvar90_aggregate_reduction",
        "maxrisk_reduction": "max_risk_aggregate_reduction",
        "re_reduction": "re_aggregate_reduction",
    }
    grouped: dict[tuple[str, str], list[dict[str, str]]] = {}
    for row in rows:
        if "_seed" not in row["risk_source"]:
            continue
        model, seed = row["risk_source"].rsplit("_seed", 1)
        row["model"] = model
        row["model_seed"] = seed
        grouped.setdefault((model, row["method"]), []).append(row)

    out_rows: list[dict[str, object]] = []
    for (model, method), group in sorted(grouped.items()):
        out: dict[str, object] = {"model": model, "method": method, "model_seed_runs": len(group)}
        for out_name, src_name in metrics.items():
            vals = [float(row[src_name]) for row in group if row.get(src_name) not in ("", None)]
            avg, sd = mean_std(vals)
            out[f"{out_name}_mean"] = avg
            out[f"{out_name}_std"] = sd
            out[f"{out_name}_mean_std"] = fmt_mean_std(avg, sd)
        out_rows.append(out)
    write_csv(batch_dir / "od_seed_robustness_by_model_10seed.csv", out_rows)

    lines = [
        "# OD downstream seed robustness 10seed",
        "",
        "| Model | Method | Hop inc. | Total Risk red. | CVaR90 red. | MaxRisk red. | RE red. |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in out_rows:
        if row["method"] != "CVaR-risk":
            continue
        lines.append(
            "| {model} | {method} | {hop} | {risk} | {cvar} | {maxrisk} | {re} |".format(
                model=row["model"],
                method=row["method"],
                hop=row["hop_increase_mean_std"],
                risk=row["total_risk_reduction_mean_std"],
                cvar=row["cvar90_reduction_mean_std"],
                maxrisk=row["maxrisk_reduction_mean_std"],
                re=row["re_reduction_mean_std"],
            )
        )
    (batch_dir / "od_seed_robustness_by_model_10seed.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def stage_paper_tables(args: argparse.Namespace) -> None:
    out_dir = model_dir(args.outputs_root) / "paper_comparison_tables_10seed"
    paper_dir = args.final_root / "paper_results" / "02_model_results"
    run(
        [
            PYTHON,
            "-B",
            script("summarize_node_risk_eval_tables.py"),
            "--paper-source",
            str(
                model_dir(args.outputs_root)
                / "paper_main_comparison_splitB_10seed_summary.csv"
            ),
            "--no-tail-source",
            str(
                model_dir(args.outputs_root)
                / "paper_stable_tail_no_tail_loss_splitB_10seed_summary.csv"
            ),
            "--strong-source",
            str(model_dir(args.outputs_root) / "paper_strong_baselines_splitB_10seed_summary.csv"),
            "--fusion-source",
            str(model_dir(args.outputs_root) / "paper_teg_concat_fusions_splitB_10seed_summary.csv"),
            "--gate-source",
            str(model_dir(args.outputs_root) / "paper_teg_gate_fusions_splitB_10seed_summary.csv"),
            "--source-out-dir",
            str(out_dir),
            "--paper-out-dir",
            str(paper_dir),
            "--suffix",
            "_paper_10seed",
            "--note-label",
            "paper comparison Split B, 10 seeds, common full loss",
        ],
        args.dry_run,
    )


def stage_paper_risk(args: argparse.Namespace) -> None:
    """Export every paper comparison through the common floor-0.01 rule."""

    export_base(
        args,
        PAPER_MODELS,
        PAPER_COMPARISON_TAG,
        checkpoint_tag=PAPER_COMPARISON_TAG,
    )
    export_base(
        args,
        "stable_tail_gnn",
        PAPER_NO_TAIL_TAG,
        ["--alpha-hr", "0", "--alpha-topk", "0"],
        checkpoint_tag=PAPER_NO_TAIL_TAG,
    )
    reference_sources = [
        str(risk_dir(args.outputs_root, paper_model_dir(model, seed)))
        for model in PAPER_MODELS.split(",")
        for seed in parse_seed_csv(args.seeds)
    ]
    run(
        [
            PYTHON,
            "-B",
            script("export_ensemble_risk_matrix.py"),
            *reference_sources,
            "--output-dir",
            str(risk_root(args.outputs_root)),
            "--name",
            paper_common_reference_dir(),
        ],
        args.dry_run,
    )


def stage_strong_risk(args: argparse.Namespace) -> None:
    export_base(
        args,
        STRONG_MODELS,
        STRONG_BASELINE_TAG,
        checkpoint_tag=STRONG_BASELINE_TAG,
    )


def stage_fusion_risk(args: argparse.Namespace) -> None:
    export_base(
        args,
        FUSION_MODELS,
        FUSION_COMPARISON_TAG,
        checkpoint_tag=FUSION_COMPARISON_TAG,
    )


def stage_gate_risk(args: argparse.Namespace) -> None:
    export_base(
        args,
        GATE_MODELS,
        GATE_COMPARISON_TAG,
        checkpoint_tag=GATE_COMPARISON_TAG,
    )


def stage_od(args: argparse.Namespace) -> None:
    sources = risk_sources(
        args,
        [
            "GCN",
            "Weighted-GCN",
            "Edge-GAT",
            "TEG-low",
            "Stable-Tail-GNN",
            "Fusion-rho025",
            "Ensemble-4",
        ],
    )
    batch_name = "model_od_comparison_10seed"
    pairs_path = ensure_fixed_od_pairs(args)
    run(
        [
            PYTHON,
            "-B",
            script("compare_model_od_paths.py"),
            *source_args(sources),
            "--pairs",
            str(pairs_path),
            "--output-dir",
            str(od_root(args.outputs_root)),
            "--batch-name",
            batch_name,
            "--k-paths",
            "50",
            "--cvar-alpha",
            "0.9",
            "--re-threshold",
            "p75",
        ],
        args.dry_run,
    )
    if not args.dry_run:
        aggregate_od_model_summary(od_root(args.outputs_root) / batch_name)


def stage_paper_od(args: argparse.Namespace) -> None:
    sources = risk_sources(
        args,
        [
            "GCN (paper)",
            "GAT",
            "GraphSAGE",
            "TEG-only",
            "Stable-Tail w/o Tail Loss",
            "Stable-Tail GNN (paper)",
        ],
    )
    batch_name = "paper_model_od_comparison_10seed"
    run(
        [
            PYTHON,
            "-B",
            script("compare_model_od_paths.py"),
            *source_args(sources),
            "--pairs",
            str(ensure_fixed_od_pairs(args)),
            "--output-dir",
            str(od_root(args.outputs_root)),
            "--batch-name",
            batch_name,
            "--k-paths",
            "50",
            "--cvar-alpha",
            "0.9",
            "--re-threshold",
            "p75",
        ],
        args.dry_run,
    )
    if not args.dry_run:
        aggregate_od_model_summary(od_root(args.outputs_root) / batch_name)


def stage_strong_od(args: argparse.Namespace) -> None:
    sources = risk_sources(args, ["SGFormer-adapted", "Gradformer-adapted"])
    batch_name = "paper_strong_od_comparison_10seed"
    run(
        [
            PYTHON,
            "-B",
            script("compare_model_od_paths.py"),
            *source_args(sources),
            "--pairs",
            str(ensure_fixed_od_pairs(args)),
            "--output-dir",
            str(od_root(args.outputs_root)),
            "--batch-name",
            batch_name,
            "--k-paths",
            "50",
            "--cvar-alpha",
            "0.9",
            "--re-threshold",
            "p75",
        ],
        args.dry_run,
    )
    if not args.dry_run:
        aggregate_od_model_summary(od_root(args.outputs_root) / batch_name)


def stage_fusion_od(args: argparse.Namespace) -> None:
    sources = risk_sources(
        args, ["GraphSAGE-TEG-Concat", "SGFormer-TEG-Concat"]
    )
    batch_name = "paper_teg_concat_fusion_od_10seed"
    run(
        [
            PYTHON,
            "-B",
            script("compare_model_od_paths.py"),
            *source_args(sources),
            "--pairs",
            str(ensure_fixed_od_pairs(args)),
            "--output-dir",
            str(od_root(args.outputs_root)),
            "--batch-name",
            batch_name,
            "--k-paths",
            "50",
            "--cvar-alpha",
            "0.9",
            "--re-threshold",
            "p75",
        ],
        args.dry_run,
    )
    if not args.dry_run:
        aggregate_od_model_summary(od_root(args.outputs_root) / batch_name)


def stage_gate_od(args: argparse.Namespace) -> None:
    sources = risk_sources(
        args, ["SGFormer-TEG-Gate", "GraphSAGE-TEG-Gate"]
    )
    batch_name = "paper_teg_gate_fusion_od_10seed"
    run(
        [
            PYTHON,
            "-B",
            script("compare_model_od_paths.py"),
            *source_args(sources),
            "--pairs",
            str(ensure_fixed_od_pairs(args)),
            "--output-dir",
            str(od_root(args.outputs_root)),
            "--batch-name",
            batch_name,
            "--k-paths",
            "50",
            "--cvar-alpha",
            "0.9",
            "--re-threshold",
            "p75",
        ],
        args.dry_run,
    )
    if not args.dry_run:
        aggregate_od_model_summary(od_root(args.outputs_root) / batch_name)


def aggregate_pyvrp_summary(batch_dir: Path, output_name: str) -> None:
    src = batch_dir / "model_pyvrp_summary.csv"
    if not src.exists():
        return
    rows = read_csv(src)
    metrics = {
        "cost_increase": "cost_increase_pct",
        "global_risk": "global_risk_mean",
        "risk_reduction": "risk_reduction_pct",
        "cvar90": "global_cvar90_mean",
        "max_vehicle_risk": "max_vehicle_risk_mean",
        "edge_burden_gini": "edge_burden_gini_used_mean",
        "top10_share": "top10_burden_share_mean",
    }
    grouped: dict[tuple[str, str, str, str], list[dict[str, str]]] = {}
    for row in rows:
        if "_seed" not in row["risk_source"]:
            continue
        model, seed = row["risk_source"].rsplit("_seed", 1)
        row["model"] = model
        row["model_seed"] = seed
        key = (row["customer_set"], model, row["beta"], row.get("lambda_concentration", "0"))
        grouped.setdefault(key, []).append(row)

    out_rows: list[dict[str, object]] = []
    for (customer_set, model, beta, lam), group in sorted(grouped.items()):
        out: dict[str, object] = {
            "customer_set": customer_set,
            "model": model,
            "beta": beta,
            "lambda_concentration": lam,
            "model_seed_runs": len(group),
        }
        for out_name, src_name in metrics.items():
            vals = [float(row[src_name]) for row in group if row.get(src_name) not in ("", None)]
            avg, sd = mean_std(vals)
            pct = out_name in {"cost_increase", "risk_reduction", "top10_share"}
            out[f"{out_name}_mean"] = avg
            out[f"{out_name}_std"] = sd
            out[f"{out_name}_mean_std"] = fmt_mean_std(avg, sd, pct=pct)
        out_rows.append(out)
    write_csv(batch_dir / output_name, out_rows)


def merge_pyvrp_chunks(args: argparse.Namespace, batch_name: str, chunk_names: list[str]) -> Path:
    master = pyvrp_root(args.outputs_root) / batch_name
    master.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    for chunk_name in chunk_names:
        chunk_dir = pyvrp_root(args.outputs_root) / chunk_name
        summary_path = chunk_dir / "model_pyvrp_summary.csv"
        if summary_path.exists():
            rows.extend(read_csv(summary_path))
        failure_path = chunk_dir / "model_pyvrp_failures.json"
        if failure_path.exists():
            failures.extend(json.loads(failure_path.read_text(encoding="utf-8")))
    write_csv(master / "model_pyvrp_summary.csv", rows)
    (master / "model_pyvrp_failures.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return master


def run_pyvrp_chunked(
    args: argparse.Namespace,
    sources: list[tuple[str, Path]],
    batch_name: str,
    betas: str,
    lambda_concentration: str,
) -> list[str]:
    meta_paths = ensure_fixed_instance_meta(args)
    chunk_names: list[str] = []
    commands: list[list[str]] = []
    expected_rows = 2 * len(parse_csv(betas))
    for label, path in sources:
        chunk_name = f"{batch_name}__{safe_name(label)}"
        chunk_names.append(chunk_name)
        chunk_dir = pyvrp_root(args.outputs_root) / chunk_name
        if not args.dry_run:
            summary_path = chunk_dir / "model_pyvrp_summary.csv"
            failure_path = chunk_dir / "model_pyvrp_failures.json"
            failures = (
                json.loads(failure_path.read_text(encoding="utf-8"))
                if failure_path.exists()
                else ["missing failure manifest"]
            )
            rows = read_csv(summary_path) if summary_path.exists() else []
            if len(rows) == expected_rows and not failures:
                print(f"[skip] existing complete PyVRP chunk {chunk_name}")
                continue
        commands.append(
            [
                PYTHON,
                "-B",
                script("compare_model_pyvrp.py"),
                f"{label}={path}",
                "--output-dir",
                str(pyvrp_root(args.outputs_root)),
                "--batch-name",
                chunk_name,
                "--customer-sets",
                "A,B",
                "--meta-a",
                str(meta_paths["A"]),
                "--meta-b",
                str(meta_paths["B"]),
                "--betas",
                betas,
                "--lambda-concentration",
                lambda_concentration,
                "--seeds",
                args.pyvrp_seeds,
                "--max-runtime",
                str(args.max_runtime),
            ]
        )
    workers = max(1, min(getattr(args, "pyvrp_workers", 1), len(commands)))
    if workers == 1 or args.dry_run:
        for cmd in commands:
            run(cmd, args.dry_run)
    else:
        print(f"[pyvrp] running {len(commands)} chunks with {workers} workers")
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
            futures = [pool.submit(run, cmd, False) for cmd in commands]
            for future in concurrent.futures.as_completed(futures):
                future.result()
    return chunk_names


def aggregate_concentration_improvements(batch_dir: Path) -> None:
    src = batch_dir / "model_pyvrp_summary.csv"
    if not src.exists():
        return
    rows = read_csv(src)
    grouped: dict[tuple[str, str, str], dict[float, dict[str, str]]] = {}
    for row in rows:
        if abs(float(row["beta"]) - 1.0) > 1e-12 or "_seed" not in row["risk_source"]:
            continue
        model, seed = row["risk_source"].rsplit("_seed", 1)
        grouped.setdefault((model, seed, row["customer_set"]), {})[
            float(row.get("lambda_concentration", 0.0))
        ] = row

    detail: list[dict[str, object]] = []
    for (model, seed, customer_set), by_lambda in sorted(grouped.items()):
        if 0.0 not in by_lambda or 1.0 not in by_lambda:
            continue
        base = by_lambda[0.0]
        conc = by_lambda[1.0]
        out: dict[str, object] = {"model": model, "model_seed": seed, "customer_set": customer_set}
        for out_name, metric in [
            ("risk_improvement", "global_risk_mean"),
            ("cvar90_improvement", "global_cvar90_mean"),
            ("max_vehicle_risk_improvement", "max_vehicle_risk_mean"),
            ("edge_gini_improvement", "edge_burden_gini_used_mean"),
            ("top10_share_improvement", "top10_burden_share_mean"),
        ]:
            base_val = float(base[metric])
            conc_val = float(conc[metric])
            out[out_name] = (base_val - conc_val) / (base_val + 1e-12)
        out["extra_cost_percentage_points"] = float(conc["cost_increase_pct"]) - float(
            base["cost_increase_pct"]
        )
        detail.append(out)
    write_csv(batch_dir / "stable_tail_lambda1_improvement_by_seed_10seed.csv", detail)

    metrics = [
        "risk_improvement",
        "cvar90_improvement",
        "max_vehicle_risk_improvement",
        "edge_gini_improvement",
        "top10_share_improvement",
        "extra_cost_percentage_points",
    ]
    grouped_set: dict[tuple[str, str], list[dict[str, object]]] = {}
    for row in detail:
        grouped_set.setdefault((str(row["customer_set"]), str(row["model"])), []).append(row)
    summary: list[dict[str, object]] = []
    for (customer_set, model), group in sorted(grouped_set.items()):
        out: dict[str, object] = {
            "customer_set": customer_set,
            "model": model,
            "model_seed_runs": len(group),
        }
        for metric in metrics:
            vals = [float(row[metric]) for row in group]
            avg, sd = mean_std(vals)
            out[f"{metric}_mean"] = avg
            out[f"{metric}_std"] = sd
            out[f"{metric}_mean_std"] = fmt_mean_std(avg, sd)
        summary.append(out)
    write_csv(batch_dir / "stable_tail_lambda1_improvement_by_set_10seed.csv", summary)


def stage_pyvrp(args: argparse.Namespace) -> None:
    stable_sources = risk_sources(args, ["Stable-Tail-GNN"])
    beta_batch = "stable_tail_pyvrp50_beta_curve_10seed"
    beta_chunks = run_pyvrp_chunked(
        args,
        stable_sources,
        beta_batch,
        "0,0.25,0.5,1.0,2.0",
        "0",
    )
    if not args.dry_run:
        beta_dir = merge_pyvrp_chunks(args, beta_batch, beta_chunks)
        aggregate_pyvrp_summary(beta_dir, "beta_sensitivity_10seed.csv")

    sources = risk_sources(
        args,
        [
            "GCN",
            "Weighted-GCN",
            "Edge-GAT",
            "TEG-low",
            "Stable-Tail-GNN",
            "Fusion-rho025",
            "Ensemble-4",
        ],
    )
    model_batch = "model_pyvrp50_beta1_10seed"
    model_chunks = run_pyvrp_chunked(args, sources, model_batch, "0,1.0", "0")
    if not args.dry_run:
        model_batch_dir = merge_pyvrp_chunks(args, model_batch, model_chunks)
        aggregate_pyvrp_summary(model_batch_dir, "model_pyvrp_comparison_10seed.csv")
        run(
            [
                PYTHON,
                "-B",
                script("common_evaluate_pyvrp_routes.py"),
                *source_args(run_dirs_for_chunked_batch(args, model_batch, sources)),
                "--common-risk-dir",
                str(risk_dir(args.outputs_root, common_ensemble_dir())),
                "--output-dir",
                str(pyvrp_root(args.outputs_root)),
                "--batch-name",
                "common_eval_pyvrp50_10seed",
                "--beta",
                "1.0",
                "--lambda-concentration",
                "0",
            ],
            args.dry_run,
        )


def stage_paper_pyvrp(args: argparse.Namespace) -> None:
    sources = risk_sources(
        args,
        [
            "GCN (paper)",
            "GAT",
            "GraphSAGE",
            "TEG-only",
            "Stable-Tail w/o Tail Loss",
            "Stable-Tail GNN (paper)",
        ],
    )
    batch = "paper_model_pyvrp_budget_sweep_10seed"
    chunks = run_pyvrp_chunked(
        args,
        sources,
        batch,
        "0,0.25,0.5,1.0,2.0",
        "0",
    )
    if not args.dry_run:
        batch_dir = merge_pyvrp_chunks(args, batch, chunks)
        aggregate_pyvrp_summary(batch_dir, "paper_model_pyvrp_summary_10seed.csv")
        run(
            [
                PYTHON,
                "-B",
                script("common_evaluate_pyvrp_routes.py"),
                *source_args(run_dirs_for_chunked_batch(args, batch, sources)),
                "--common-risk-dir",
                str(risk_dir(args.outputs_root, common_ensemble_dir())),
                "--output-dir",
                str(pyvrp_root(args.outputs_root)),
                "--batch-name",
                "paper_common_eval_pyvrp_10seed",
                "--betas",
                "0,0.25,0.5,1.0,2.0",
                "--lambda-concentration",
                "0",
            ],
            args.dry_run,
        )


def stage_strong_pyvrp(args: argparse.Namespace) -> None:
    sources = risk_sources(args, ["SGFormer-adapted", "Gradformer-adapted"])
    batch = "paper_strong_pyvrp_budget_sweep_10seed"
    chunks = run_pyvrp_chunked(
        args,
        sources,
        batch,
        "0,0.25,0.5,1.0,2.0",
        "0",
    )
    if not args.dry_run:
        batch_dir = merge_pyvrp_chunks(args, batch, chunks)
        aggregate_pyvrp_summary(
            batch_dir, "paper_strong_pyvrp_summary_10seed.csv"
        )


def stage_fusion_pyvrp(args: argparse.Namespace) -> None:
    sources = risk_sources(
        args, ["GraphSAGE-TEG-Concat", "SGFormer-TEG-Concat"]
    )
    batch = "paper_teg_concat_fusion_pyvrp_budget_sweep_10seed"
    chunks = run_pyvrp_chunked(
        args,
        sources,
        batch,
        "0,0.25,0.5,1.0,2.0",
        "0",
    )
    if not args.dry_run:
        batch_dir = merge_pyvrp_chunks(args, batch, chunks)
        aggregate_pyvrp_summary(
            batch_dir, "paper_teg_concat_fusion_pyvrp_summary_10seed.csv"
        )


def stage_gate_pyvrp(args: argparse.Namespace) -> None:
    sources = risk_sources(
        args, ["SGFormer-TEG-Gate", "GraphSAGE-TEG-Gate"]
    )
    batch = "paper_teg_gate_fusion_pyvrp_budget_sweep_10seed"
    chunks = run_pyvrp_chunked(
        args,
        sources,
        batch,
        "0,0.25,0.5,1.0,2.0",
        "0",
    )
    if not args.dry_run:
        batch_dir = merge_pyvrp_chunks(args, batch, chunks)
        aggregate_pyvrp_summary(
            batch_dir, "paper_teg_gate_fusion_pyvrp_summary_10seed.csv"
        )


def stage_paper_load_eval(args: argparse.Namespace) -> None:
    base_sources = risk_sources(
        args,
        [
            "GCN (paper)",
            "GAT",
            "GraphSAGE",
            "TEG-only",
            "Stable-Tail w/o Tail Loss",
            "Stable-Tail GNN (paper)",
        ],
    )
    strong_sources = risk_sources(
        args, ["SGFormer-adapted", "Gradformer-adapted"]
    )
    run_dirs = [
        *run_dirs_for_chunked_batch(
            args, "paper_model_pyvrp_budget_sweep_10seed", base_sources
        ),
        *run_dirs_for_chunked_batch(
            args, "paper_strong_pyvrp_budget_sweep_10seed", strong_sources
        ),
    ]
    common_dir = risk_dir(args.outputs_root, paper_common_reference_dir())
    run_list = write_run_list(
        pyvrp_root(args.outputs_root) / "paper_all_models_run_list_10seed.csv",
        run_dirs,
    )
    common_args = [
        "--run-list",
        str(run_list),
        "--common-risk-dir",
        str(common_dir),
        "--output-dir",
        str(pyvrp_root(args.outputs_root)),
        "--betas",
        "0,0.25,0.5,1.0,2.0",
        "--lambda-concentration",
        "0",
    ]
    run(
        [
            PYTHON,
            "-B",
            script("common_evaluate_pyvrp_routes.py"),
            *common_args,
            "--batch-name",
            "paper_all_models_common_eval_10seed",
        ],
        args.dry_run,
    )
    run(
        [
            PYTHON,
            "-B",
            script("common_evaluate_load_aware_routes.py"),
            *common_args,
            "--batch-name",
            "paper_all_models_load_eval_10seed",
        ],
        args.dry_run,
    )


def stage_fusion_load_eval(args: argparse.Namespace) -> None:
    base_sources = risk_sources(
        args,
        [
            "GCN (paper)",
            "GAT",
            "GraphSAGE",
            "TEG-only",
            "Stable-Tail w/o Tail Loss",
            "Stable-Tail GNN (paper)",
        ],
    )
    strong_sources = risk_sources(
        args, ["SGFormer-adapted", "Gradformer-adapted"]
    )
    fusion_sources = risk_sources(
        args, ["GraphSAGE-TEG-Concat", "SGFormer-TEG-Concat"]
    )
    run_dirs = [
        *run_dirs_for_chunked_batch(
            args, "paper_model_pyvrp_budget_sweep_10seed", base_sources
        ),
        *run_dirs_for_chunked_batch(
            args, "paper_strong_pyvrp_budget_sweep_10seed", strong_sources
        ),
        *run_dirs_for_chunked_batch(
            args, "paper_teg_concat_fusion_pyvrp_budget_sweep_10seed", fusion_sources
        ),
    ]
    run_list = write_run_list(
        pyvrp_root(args.outputs_root) / "paper_all_models_with_fusion_run_list_10seed.csv",
        run_dirs,
    )
    common_args = [
        "--run-list",
        str(run_list),
        "--common-risk-dir",
        str(risk_dir(args.outputs_root, paper_common_reference_dir())),
        "--output-dir",
        str(pyvrp_root(args.outputs_root)),
        "--betas",
        "0,0.25,0.5,1.0,2.0",
        "--lambda-concentration",
        "0",
    ]
    run(
        [
            PYTHON,
            "-B",
            script("common_evaluate_pyvrp_routes.py"),
            *common_args,
            "--batch-name",
            "paper_all_models_with_fusion_common_eval_10seed",
        ],
        args.dry_run,
    )
    run(
        [
            PYTHON,
            "-B",
            script("common_evaluate_load_aware_routes.py"),
            *common_args,
            "--batch-name",
            "paper_all_models_with_fusion_load_eval_10seed",
        ],
        args.dry_run,
    )


def stage_gate_load_eval(args: argparse.Namespace) -> None:
    base_sources = risk_sources(
        args,
        [
            "GCN (paper)",
            "GAT",
            "GraphSAGE",
            "TEG-only",
            "Stable-Tail w/o Tail Loss",
            "Stable-Tail GNN (paper)",
        ],
    )
    strong_sources = risk_sources(
        args, ["SGFormer-adapted", "Gradformer-adapted"]
    )
    fusion_sources = risk_sources(
        args, ["GraphSAGE-TEG-Concat", "SGFormer-TEG-Concat"]
    )
    gate_sources = risk_sources(
        args, ["SGFormer-TEG-Gate", "GraphSAGE-TEG-Gate"]
    )
    run_dirs = [
        *run_dirs_for_chunked_batch(
            args, "paper_model_pyvrp_budget_sweep_10seed", base_sources
        ),
        *run_dirs_for_chunked_batch(
            args, "paper_strong_pyvrp_budget_sweep_10seed", strong_sources
        ),
        *run_dirs_for_chunked_batch(
            args, "paper_teg_concat_fusion_pyvrp_budget_sweep_10seed", fusion_sources
        ),
        *run_dirs_for_chunked_batch(
            args, "paper_teg_gate_fusion_pyvrp_budget_sweep_10seed", gate_sources
        ),
    ]
    run_list = write_run_list(
        pyvrp_root(args.outputs_root) / "paper_all_models_with_gate_run_list_10seed.csv",
        run_dirs,
    )
    common_args = [
        "--run-list",
        str(run_list),
        "--common-risk-dir",
        str(risk_dir(args.outputs_root, common_ensemble_dir())),
        "--output-dir",
        str(pyvrp_root(args.outputs_root)),
        "--betas",
        "0,0.25,0.5,1.0,2.0",
        "--lambda-concentration",
        "0",
    ]
    run(
        [
            PYTHON,
            "-B",
            script("common_evaluate_pyvrp_routes.py"),
            *common_args,
            "--batch-name",
            "paper_all_models_with_gate_common_eval_10seed",
        ],
        args.dry_run,
    )
    run(
        [
            PYTHON,
            "-B",
            script("common_evaluate_load_aware_routes.py"),
            *common_args,
            "--batch-name",
            "paper_all_models_with_gate_load_eval_10seed",
        ],
        args.dry_run,
    )
def stage_concentration(args: argparse.Namespace) -> None:
    stable_sources = risk_sources(args, ["Stable-Tail-GNN"])
    batch = "stable_tail_concentration_beta1_lambda0_1_10seed"
    chunks = run_pyvrp_chunked(args, stable_sources, batch, "0,1.0", "0,1")
    if not args.dry_run:
        batch_dir = merge_pyvrp_chunks(args, batch, chunks)
        aggregate_pyvrp_summary(batch_dir, "concentration_pyvrp_summary_10seed.csv")
        aggregate_concentration_improvements(batch_dir)
        run(
            [
                PYTHON,
                "-B",
                script("common_evaluate_pyvrp_routes.py"),
                *source_args(run_dirs_for_chunked_batch(args, batch, stable_sources)),
                "--common-risk-dir",
                str(risk_dir(args.outputs_root, common_ensemble_dir())),
                "--output-dir",
                str(pyvrp_root(args.outputs_root)),
                "--batch-name",
                "common_eval_concentration_10seed",
                "--beta",
                "1.0",
            ],
            args.dry_run,
        )

def stage_customer_sets(args: argparse.Namespace) -> None:
    meta_paths = ensure_fixed_instance_meta(args)
    run(
        [
            PYTHON,
            "-B",
            script("summarize_customer_sets.py"),
            "--outputs-root",
            str(args.outputs_root),
            "--paper-root",
            str(args.final_root / "paper_results"),
            "--paper-section",
            "10_customer_sets_10seed",
            "--risk-dir-pattern",
            "stable_tail_gnn_splitB_seed{seed}_epochs50_paper_comparison_10seed_floor_0p01",
            "--meta-a",
            str(meta_paths["A"]),
            "--meta-b",
            str(meta_paths["B"]),
            "--seeds",
            args.seeds,
            "--suffix",
            "_10seed",
        ],
        args.dry_run,
    )


def stage_consistency_checks(args: argparse.Namespace) -> None:
    run(
        [
            PYTHON,
            "-B",
            script("audit_experiment_consistency.py"),
            "--outputs-root",
            str(args.outputs_root),
            "--final-root",
            str(args.final_root),
        ],
        args.dry_run,
    )


def write_manifest(args: argparse.Namespace) -> None:
    if args.dry_run:
        return
    manifest_dir = args.final_root / "paper_results" / "00_manifest"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "seed_label": "10seed",
        "model_seeds": parse_seed_csv(args.seeds),
        "pyvrp_seeds": parse_seed_csv(args.pyvrp_seeds),
        "outputs_root": str(args.outputs_root),
        "final_root": str(args.final_root),
        "risk_mode": "floor_0.01",
        "common_reference_risk_matrix": paper_common_reference_dir(),
        "common_reference_description": (
            "Equal-weight ensemble of all 10 seeds of the five paper main models "
            "(GCN, GAT, GraphSAGE, TEG-only, and Stable-Tail GNN)."
        ),
        "epochs": args.epochs,
        "max_runtime": args.max_runtime,
    }
    (manifest_dir / "run_10seed_pipeline_meta.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> None:
    args = parse_args()
    args.outputs_root.mkdir(parents=True, exist_ok=True)
    args.final_root.mkdir(parents=True, exist_ok=True)

    stages = set(parse_csv(args.stages))
    if "models" in stages:
        stage_models(args)
    if "paper_models" in stages:
        stage_paper_models(args)
    if "strong_models" in stages:
        stage_strong_models(args)
    if "fusion_models" in stages:
        stage_fusion_models(args)
    if "gate_models" in stages:
        stage_gate_models(args)
    if "node_tables" in stages:
        stage_node_tables(args)
    if "paper_tables" in stages:
        stage_paper_tables(args)
    if "risk" in stages:
        stage_risk(args)
    if "paper_risk" in stages:
        stage_paper_risk(args)
    if "strong_risk" in stages:
        stage_strong_risk(args)
    if "fusion_risk" in stages:
        stage_fusion_risk(args)
    if "gate_risk" in stages:
        stage_gate_risk(args)
    if "od" in stages:
        stage_od(args)
    if "paper_od" in stages:
        stage_paper_od(args)
    if "strong_od" in stages:
        stage_strong_od(args)
    if "fusion_od" in stages:
        stage_fusion_od(args)
    if "gate_od" in stages:
        stage_gate_od(args)
    if "pyvrp" in stages:
        stage_pyvrp(args)
    if "paper_pyvrp" in stages:
        stage_paper_pyvrp(args)
    if "strong_pyvrp" in stages:
        stage_strong_pyvrp(args)
    if "fusion_pyvrp" in stages:
        stage_fusion_pyvrp(args)
    if "gate_pyvrp" in stages:
        stage_gate_pyvrp(args)
    if "paper_load_eval" in stages:
        stage_paper_load_eval(args)
    if "fusion_load_eval" in stages:
        stage_fusion_load_eval(args)
    if "gate_load_eval" in stages:
        stage_gate_load_eval(args)
    if "concentration" in stages:
        stage_concentration(args)
    if "customer_sets" in stages:
        stage_customer_sets(args)
    if "consistency_checks" in stages:
        stage_consistency_checks(args)
    write_manifest(args)


if __name__ == "__main__":
    main()
