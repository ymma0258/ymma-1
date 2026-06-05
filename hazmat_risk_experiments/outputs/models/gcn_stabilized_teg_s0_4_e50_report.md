# Small Formal Model Comparison Report

Source: `hazmat_risk_experiments\outputs\models\gcn_stabilized_teg_s0_4_e50_summary.csv`

This is a short 20-epoch, seed-0 stability run. It verifies the experimental pipeline and gives an initial trend, but it is not a final multi-seed result.

## Test Metrics By Split

### Split A

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | Precision@6-8 | PR-AUC high | High FN rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| gcn | 0.3430 | 1.2369 | 0.2634 | 0.2275 | 0.5923 | 0.3940 | 0.7725 |
| gcn_teg_concat | 0.3067 | 1.1826 | 0.3255 | 0.2941 | 0.5484 | 0.3882 | 0.7059 |
| gcn_teg_residual_fixed | 0.3388 | 1.2443 | 0.2778 | 0.2392 | 0.5669 | 0.3977 | 0.7608 |
| gcn_teg_residual_learnable | 0.3412 | 1.2381 | 0.2779 | 0.2392 | 0.5667 | 0.3991 | 0.7608 |
| teg_gnn | 0.3440 | 1.6377 | 0.3345 | 0.3529 | 0.4231 | 0.3613 | 0.6471 |

Initial bests:
- Macro-F1: `teg_gnn` (0.3440).
- MAE: `gcn_teg_concat` (1.1826).
- QWK: `teg_gnn` (0.3345).
- Recall@6-8: `teg_gnn` (0.3529).

### Split B

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | Precision@6-8 | PR-AUC high | High FN rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| gcn | 0.3015 | 1.2677 | 0.2377 | 0.1923 | 0.4892 | 0.3705 | 0.8077 |
| gcn_teg_concat | 0.2966 | 1.1783 | 0.2913 | 0.2462 | 0.4275 | 0.3892 | 0.7538 |
| gcn_teg_residual_fixed | 0.2890 | 1.2749 | 0.2497 | 0.2077 | 0.4048 | 0.3653 | 0.7923 |
| gcn_teg_residual_learnable | 0.2863 | 1.2692 | 0.2508 | 0.2077 | 0.4048 | 0.3680 | 0.7923 |
| teg_gnn | 0.2676 | 1.5953 | 0.2743 | 0.2385 | 0.3507 | 0.3530 | 0.7615 |

Initial bests:
- Macro-F1: `gcn` (0.3015).
- MAE: `gcn_teg_concat` (1.1783).
- QWK: `gcn_teg_concat` (0.2913).
- Recall@6-8: `gcn_teg_concat` (0.2462).

## Notes

- This report uses only one seed, so all standard deviations are zero in the source summary.
- The next formal step should run multiple seeds and more epochs before drawing paper-level conclusions.
- The current result is useful for checking whether the training code, splits, and metrics behave sensibly.
