"""Run and aggregate batches of risk-model experiments.

The defaults are intentionally small and safe. Increase ``--epochs`` and pass
more seeds/models when running formal experiments.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path
from types import SimpleNamespace


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import train_risk_model  # noqa: E402


DEFAULT_OUTPUT = Path(r"D:\PyVRP-main\hazmat_risk_experiments\outputs\models")


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_int_csv(value: str) -> list[int]:
    return [int(item) for item in parse_csv(value)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", type=Path, default=train_risk_model.DEFAULT_ZIP)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--models",
        default="mlp,gcn,weighted_gcn,edge_gat,teg_gnn",
        help="Comma-separated model list.",
    )
    parser.add_argument("--splits", default="A,B,C", help="Comma-separated split list.")
    parser.add_argument("--seeds", default="0", help="Comma-separated integer seeds.")
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--hidden-dim", type=int, default=64)
    parser.add_argument("--dropout", type=float, default=0.2)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--topk-frac", type=float, default=0.2)
    parser.add_argument("--alpha-ord", type=float, default=0.5)
    parser.add_argument("--alpha-hr", type=float, default=1.0)
    parser.add_argument("--alpha-topk", type=float, default=0.3)
    parser.add_argument("--lambda-nll", type=float, default=0.0)
    parser.add_argument("--lambda-var", type=float, default=0.0)
    parser.add_argument("--gamma-unc", type=float, default=0.5)
    parser.add_argument("--logvar-min", type=float, default=-5.0)
    parser.add_argument("--logvar-max", type=float, default=2.0)
    parser.add_argument("--stage1-epochs", type=int, default=0)
    parser.add_argument("--split-b-val-fraction", type=float, default=0.2)
    parser.add_argument(
        "--checkpoint-selection", choices=["best", "last"], default="best"
    )
    parser.add_argument("--checkpoint-score-pr-weight", type=float, default=0.8)
    parser.add_argument("--checkpoint-min-recall", type=float, default=0.0)
    parser.add_argument("--checkpoint-max-high-fn", type=float, default=1.0)
    parser.add_argument("--checkpoint-dir", type=Path, default=None)
    parser.add_argument("--gate-normalized", action="store_true")
    parser.add_argument("--feature-standardization", action="store_true")
    parser.add_argument(
        "--edge-normalization",
        choices=["per_year", "shared_2020", "shared_train"],
        default="per_year",
    )
    parser.add_argument("--experiment-tag", default="")
    parser.add_argument(
        "--batch-name",
        default="batch",
        help="Prefix for aggregate CSV/JSON files.",
    )
    return parser.parse_args()


def train_args(base: argparse.Namespace, model: str, split: str, seed: int) -> argparse.Namespace:
    return SimpleNamespace(
        zip=base.zip,
        output_dir=base.output_dir,
        model=model,
        split=split,
        epochs=base.epochs,
        hidden_dim=base.hidden_dim,
        dropout=base.dropout,
        lr=base.lr,
        weight_decay=base.weight_decay,
        seed=seed,
        topk_frac=base.topk_frac,
        alpha_ord=base.alpha_ord,
        alpha_hr=base.alpha_hr,
        alpha_topk=base.alpha_topk,
        lambda_nll=base.lambda_nll,
        lambda_var=base.lambda_var,
        gamma_unc=base.gamma_unc,
        logvar_min=base.logvar_min,
        logvar_max=base.logvar_max,
        stage1_epochs=base.stage1_epochs,
        split_b_val_fraction=base.split_b_val_fraction,
        checkpoint_selection=base.checkpoint_selection,
        checkpoint_score_pr_weight=base.checkpoint_score_pr_weight,
        checkpoint_min_recall=base.checkpoint_min_recall,
        checkpoint_max_high_fn=base.checkpoint_max_high_fn,
        checkpoint_dir=base.checkpoint_dir,
        gate_normalized=base.gate_normalized,
        feature_standardization=base.feature_standardization,
        edge_normalization=base.edge_normalization,
        experiment_tag=base.experiment_tag,
    )


def metric_rows(result: dict[str, object]) -> list[dict[str, object]]:
    metrics = result["metrics"]
    assert isinstance(metrics, dict)

    rows: list[dict[str, object]] = []
    for eval_split, values in metrics.items():
        assert isinstance(values, dict)
        row: dict[str, object] = {
            "model": result["model"],
            "split": result["split"],
            "seed": result["seed"],
            "epochs": result["epochs"],
            "best_epoch": result.get("best_epoch", result["epochs"]),
            "experiment_tag": result.get("experiment_tag", ""),
            "alpha_ord": result.get("alpha_ord", ""),
            "alpha_hr": result.get("alpha_hr", ""),
            "alpha_topk": result.get("alpha_topk", ""),
            "lambda_nll": result.get("lambda_nll", ""),
            "lambda_var": result.get("lambda_var", ""),
            "gamma_unc": result.get("gamma_unc", ""),
            "topk_frac": result.get("topk_frac", ""),
            "stage1_epochs": result.get("stage1_epochs", ""),
            "checkpoint_selection": result.get("checkpoint_selection", ""),
            "gate_normalized": result.get("gate_normalized", False),
            "feature_standardization": result.get("feature_standardization", False),
            "edge_normalization": result.get("edge_normalization", ""),
            "eval_split": eval_split,
        }
        row.update(values)
        rows.append(row)
    return rows


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


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    metric_names = [
        "macro_f1",
        "weighted_f1",
        "mae",
        "qwk",
        "recall_6_8",
        "precision_6_8",
        "pr_auc_high",
        "high_fn_rate",
        "brier",
        "ece",
        "ordinal_nll",
        "uncertainty_mean",
        "correct_uncertainty",
        "error_uncertainty",
        "error_uncertainty_corr",
        "high_fn_uncertainty",
    ]
    grouped: dict[tuple[object, object, object], list[dict[str, object]]] = {}
    for row in rows:
        key = (row.get("experiment_tag", ""), row["model"], row["split"], row["eval_split"])
        grouped.setdefault(key, []).append(row)

    summary: list[dict[str, object]] = []
    for (tag, model, split, eval_split), group_rows in sorted(grouped.items()):
        out: dict[str, object] = {
            "experiment_tag": tag,
            "model": model,
            "split": split,
            "eval_split": eval_split,
            "runs": len(group_rows),
        }
        for metric in metric_names:
            vals = [float(row[metric]) for row in group_rows if row.get(metric) not in ("", None)]
            if not vals:
                continue
            mean = sum(vals) / len(vals)
            var = sum((value - mean) ** 2 for value in vals) / max(1, len(vals) - 1)
            out[f"{metric}_mean"] = mean
            out[f"{metric}_std"] = var**0.5
        summary.append(out)
    return summary


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    models = parse_csv(args.models)
    splits = parse_csv(args.splits)
    seeds = parse_int_csv(args.seeds)

    all_rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    started = time.time()

    for model in models:
        for split in splits:
            for seed in seeds:
                cfg = train_args(args, model, split, seed)
                label = f"model={model} split={split} seed={seed} epochs={args.epochs}"
                print(f"[run] {label}")
                try:
                    result = train_risk_model.train(cfg)
                    train_risk_model.write_outputs(cfg, result)
                    all_rows.extend(metric_rows(result))
                except Exception as exc:  # noqa: BLE001 - batch runner records failures.
                    print(f"[failed] {label}: {exc}")
                    failures.append(
                        {
                            "model": model,
                            "split": split,
                            "seed": seed,
                "epochs": args.epochs,
                "experiment_tag": args.experiment_tag,
                "alpha_ord": args.alpha_ord,
                "alpha_hr": args.alpha_hr,
                "alpha_topk": args.alpha_topk,
                "lambda_nll": args.lambda_nll,
                "lambda_var": args.lambda_var,
                "gamma_unc": args.gamma_unc,
                "topk_frac": args.topk_frac,
                "stage1_epochs": args.stage1_epochs,
                "error": repr(exc),
                        }
                    )

    detail_path = args.output_dir / f"{args.batch_name}_detail.csv"
    summary_path = args.output_dir / f"{args.batch_name}_summary.csv"
    failures_path = args.output_dir / f"{args.batch_name}_failures.json"
    meta_path = args.output_dir / f"{args.batch_name}_meta.json"

    write_csv(detail_path, all_rows)
    write_csv(summary_path, summarize(all_rows))
    failures_path.write_text(json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8")
    meta_path.write_text(
        json.dumps(
            {
                "models": models,
                "splits": splits,
                "seeds": seeds,
                "epochs": args.epochs,
                "experiment_tag": args.experiment_tag,
                "alpha_ord": args.alpha_ord,
                "alpha_hr": args.alpha_hr,
                "alpha_topk": args.alpha_topk,
                "lambda_nll": args.lambda_nll,
                "lambda_var": args.lambda_var,
                "gamma_unc": args.gamma_unc,
                "topk_frac": args.topk_frac,
                "stage1_epochs": args.stage1_epochs,
                "split_b_val_fraction": args.split_b_val_fraction,
                "checkpoint_selection": args.checkpoint_selection,
                "gate_normalized": args.gate_normalized,
                "feature_standardization": args.feature_standardization,
                "edge_normalization": args.edge_normalization,
                "elapsed_seconds": time.time() - started,
                "num_metric_rows": len(all_rows),
                "num_failures": len(failures),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Wrote {detail_path}")
    print(f"Wrote {summary_path}")
    print(f"Wrote {failures_path}")
    print(f"Wrote {meta_path}")


if __name__ == "__main__":
    main()
