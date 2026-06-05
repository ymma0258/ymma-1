# Small Formal Model Comparison Report

Source: `hazmat_risk_experiments\outputs\models\gcn_stabilized_teg_seed0_e50_summary.csv`

This is a short 20-epoch, seed-0 stability run. It verifies the experimental pipeline and gives an initial trend, but it is not a final multi-seed result.

## Test Metrics By Split

### Split A

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | Precision@6-8 | PR-AUC high | High FN rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| gcn | 0.3240 | 1.2171 | 0.2358 | 0.2157 | 0.5238 | 0.3818 | 0.7843 |
| gcn_teg_concat | 0.2733 | 1.1712 | 0.2755 | 0.2549 | 0.5200 | 0.3455 | 0.7451 |
| gcn_teg_residual_fixed | 0.3653 | 1.1904 | 0.3441 | 0.2941 | 0.6250 | 0.3829 | 0.7059 |
| gcn_teg_residual_learnable | 0.3702 | 1.1836 | 0.3399 | 0.2941 | 0.6250 | 0.3830 | 0.7059 |
| teg_gnn | 0.3702 | 1.6527 | 0.3498 | 0.4118 | 0.3818 | 0.3092 | 0.5882 |

Initial bests:
- Macro-F1: `teg_gnn` (0.3702).
- MAE: `gcn_teg_concat` (1.1712).
- QWK: `teg_gnn` (0.3498).
- Recall@6-8: `teg_gnn` (0.4118).

### Split B

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | Precision@6-8 | PR-AUC high | High FN rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| gcn | 0.3168 | 1.2274 | 0.1870 | 0.1538 | 0.4000 | 0.4067 | 0.8462 |
| gcn_teg_concat | 0.3212 | 1.1071 | 0.3031 | 0.2692 | 0.5385 | 0.4129 | 0.7308 |
| gcn_teg_residual_fixed | 0.3350 | 1.1830 | 0.3121 | 0.2692 | 0.4667 | 0.4116 | 0.7308 |
| gcn_teg_residual_learnable | 0.3083 | 1.1798 | 0.3135 | 0.2692 | 0.4667 | 0.4132 | 0.7308 |
| teg_gnn | 0.2917 | 1.4930 | 0.3488 | 0.3077 | 0.4211 | 0.4004 | 0.6923 |

Initial bests:
- Macro-F1: `gcn_teg_residual_fixed` (0.3350).
- MAE: `gcn_teg_concat` (1.1071).
- QWK: `teg_gnn` (0.3488).
- Recall@6-8: `teg_gnn` (0.3077).

## Notes

- This report uses only one seed, so all standard deviations are zero in the source summary.
- The next formal step should run multiple seeds and more epochs before drawing paper-level conclusions.
- The current result is useful for checking whether the training code, splits, and metrics behave sensibly.
