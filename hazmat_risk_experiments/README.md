# Hazardous Materials Risk Experiments

This folder contains the hazardous-material transportation risk experiments built
around PyVRP.  The PyVRP source tree is kept in `../PyVRP-main`; this experiment
package uses PyVRP only as a downstream CVRP solver.

## Current Paper Workflow

The formal paper workflow is the isolated 10seed pipeline:

```powershell
.\PyVRP-main\.venv\Scripts\python.exe -B .\hazmat_risk_experiments\scripts\run_10seed_pipeline.py
```

Main settings:

- Model seeds: `0,1,2,3,4,5,6,7,8,9`.
- PyVRP solver seeds: `0,1,2,3,4,5,6,7,8,9`.
- Formal downstream split: `Split B`.
- Edge-risk mode: `floor_0.01`, with `w_floor = 0.01 + 0.99w`.
- Main risk matrix: `R_ij = w_floor * max(S_i_norm, S_j_norm)`.
- Final model name in the paper: `Stable-Tail GNN`, implemented as
  `stable_tail_gnn`.
- Common-reference route evaluation uses
  `paper_common_reference_10seed_floor_0p01`: an equal-weight aggregate of
  every seed of the five paper main models (GCN, GAT, GraphSAGE, TEG-only,
  and Stable-Tail GNN). Both the paper and Gate load evaluations use this
  same reference matrix.

Formal 10seed outputs are stored separately from legacy 5seed/exploration files:

```text
hazmat_risk_experiments/outputs_10seed/
hazmat_risk_experiments/outputs/final_figures_stable_tail_gnn_10seed/
```

The old 5seed result folders were intentionally removed.  Do not use legacy
paper-result paths as formal outputs.

## Directory Map

```text
hazmat_risk_experiments/
  final_experiment_plan.md
  scripts/
  outputs/
    audit/
    final_figures_stable_tail_gnn_10seed/
  outputs_10seed/
    models/
    risk_matrices/
    od_paths/
    pyvrp_cvrp/
```

Important result packages:

- `outputs_10seed/models/`: node-risk model training results.
- `outputs_10seed/risk_matrices/`: exported node and edge risk matrices.
- `outputs_10seed/od_paths/`: OD path validation results.
- `outputs_10seed/pyvrp_cvrp/`: PyVRP CVRP downstream results.
- `outputs/final_figures_stable_tail_gnn_10seed/paper_results/`: paper-ready
  tables, figures, manifest, and seed-robustness summaries.

## Script Groups

### Data Audit

- `audit_hazmat_data.py`: audits graph size, labels, edge attributes, and
  connected components.

### Node-Risk Models

- `train_risk_model.py`: trains one model, selects a validation checkpoint,
  and stores its fitted feature/edge preprocessing state.
- `run_model_experiments.py`: runs model batches and summarizes metrics.
- `summarize_model_results.py`: helper for older model-result summaries.
- `summarize_node_risk_eval_tables.py`: creates paper-ready node-risk tables,
  including High FN rate. Its main table intentionally combines formal
  baseline sources with the Stable-Tail source, while the separate ablation
  table uses the stabilized-TEG source only.

### Risk Matrix Export

- `export_risk_matrix.py`: loads a saved checkpoint and exports node risk,
  edge risk, and 5x8 matrix tables. It retrains only when the explicit
  diagnostic flag `--train-before-export` is supplied.
- `run_risk_matrix_exports.py`: batch wrapper for risk matrix export.
- `export_ensemble_risk_matrix.py`: combines model risk matrices.
- `export_label_oracle_risk_matrix.py`: creates the label-supported reference.
- `export_calibrated_risk_matrix.py`: exploratory calibrated edge-risk export.
- `export_tail_enhanced_risk_matrix.py`: formal tail-enhanced scoring with
  `S_tail = clip(S_norm + eta * P_high, 0, 1)` and
  `R_ij,tail = w_ij,floor * max(S_i,tail, S_j,tail)`.
- `diagnose_risk_matrix.py`: checks zero-risk and distribution diagnostics.

Checkpoint-backed export example:

```powershell
.\PyVRP-main\.venv\Scripts\python.exe -B .\hazmat_risk_experiments\scripts\train_risk_model.py --zip D:\城市危险化学品运输车辆轨迹数据.zip --output-dir .\hazmat_risk_experiments\outputs_10seed\models --model gcn_teg_concat --split B --seed 0 --epochs 50
.\PyVRP-main\.venv\Scripts\python.exe -B .\hazmat_risk_experiments\scripts\export_risk_matrix.py --zip D:\城市危险化学品运输车辆轨迹数据.zip --checkpoint .\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gcn_teg_concat_splitB_seed0_epochs50.pt --output-dir .\hazmat_risk_experiments\outputs_10seed\risk_matrices --risk-mode exposure_floor --exposure-delta 0.01
```

New Split B runs reserve 20% of the 2021 adaptation pool for validation and
select the epoch maximizing `-MAE + 0.8 * PR-AUC`. The historical no-validation
behaviour is available only with `--split-b-val-fraction 0` and
`--checkpoint-selection last`.

### OD Path Validation

- `validate_od_paths.py`: runs OD path validation for one risk matrix.
- `compare_model_od_paths.py`: compares multiple risk matrices on fixed OD
  pairs. The formal 10seed pair file is
  `outputs_10seed/od_paths/fixed_od_pairs_150.csv`.
- `sensitivity_cvar_re.py`: CVaR and concentration sensitivity analysis.
- `run_od_validation_modes.py`: exploratory risk-mode validation wrapper.

### PyVRP Downstream Validation

- `validate_pyvrp_cvrp.py`: constructs a CVRP instance, solves it with PyVRP,
  and evaluates posterior risk/fairness.
- `compare_model_pyvrp.py`: compares multiple risk matrices on fixed CVRP
  instances.
- `common_evaluate_pyvrp_routes.py`: re-evaluates routes under a common
  reference risk matrix.
- `summarize_lambda_improvements.py`: summarizes concentration-aware
  improvements.
- `summarize_customer_sets.py`: reports Set A/B customer-set diagnostics.
- `audit_experiment_consistency.py`: creates 10seed consistency-check tables
  for edge-risk loading, fixed OD pairs, fixed CVRP instances, beta=0 baseline
  stability, and self-vs-common evaluator comparisons.

### Paper Figures and Packaging

- `create_10seed_summary_figures.py`: creates the current 10seed summary
  figures.
- `organize_10seed_paper_results.py`: builds the self-contained 10seed
  `paper_results` package.
- `create_final_paper_figures.py`, `create_additional_risk_distribution_figures.py`,
  `create_path_case_figures.py`, `create_vrp_route_figures.py`, and
  `organize_paper_results.py` are legacy 5seed/exploratory figure-packaging
  scripts. They are kept for traceability but should not be used for the current
  formal 10seed result package unless their output roots are explicitly changed.

## Recommended Checks

Syntax check for experiment scripts:

```powershell
@'
import ast, pathlib
for root in ["hazmat_risk_experiments/scripts"]:
    for path in pathlib.Path(root).rglob("*.py"):
        ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
print("syntax ok")
'@ | .\PyVRP-main\.venv\Scripts\python.exe -B -
```

Dry-run the full 10seed pipeline:

```powershell
.\PyVRP-main\.venv\Scripts\python.exe -B .\hazmat_risk_experiments\scripts\run_10seed_pipeline.py --dry-run --stages paper_models,strong_models,fusion_models,gate_models,paper_risk,strong_risk,fusion_risk,gate_risk,paper_tables,paper_od,strong_od,fusion_od,gate_od,paper_pyvrp,strong_pyvrp,fusion_pyvrp,gate_pyvrp,gate_load_eval,customer_sets,consistency_checks
```

Use `node_tables` in the stage list when regenerating paper-ready node-risk
tables without rerunning model training:

```powershell
.\PyVRP-main\.venv\Scripts\python.exe -B .\hazmat_risk_experiments\scripts\run_10seed_pipeline.py --stages node_tables
```

Rebuild the consistency-check tables:

```powershell
.\PyVRP-main\.venv\Scripts\python.exe -B .\hazmat_risk_experiments\scripts\run_10seed_pipeline.py --stages consistency_checks
```

Rebuild the paper-results package:

```powershell
.\PyVRP-main\.venv\Scripts\python.exe -B .\hazmat_risk_experiments\scripts\organize_10seed_paper_results.py
```

## Notes

- `y=0` means unlabeled, not low risk.
- PyVRP is used only for downstream CVRP validation. It is not used as a
  risk-fairness optimizer.
- Risk fairness in the paper should focus on edge burden metrics, especially
  `Edge Burden Gini-used` and `Top10% Burden Share`.
- Some older scripts still have legacy `outputs/` defaults. The formal 10seed
  pipeline passes explicit paths and is the safest entry point.
- Cross-model PyVRP safety claims should use common-evaluator results. The
  self-evaluation tables are appropriate for within-model beta/lambda
  comparisons because they use the same risk matrix scale.
- `concentration-aware` should be described as a risk-burden concentration
  penalty with posterior fairness evaluation, not as a strict fairness
  constrained PyVRP optimizer.
