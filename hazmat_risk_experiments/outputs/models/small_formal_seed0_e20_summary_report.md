# Small Formal Model Comparison Report

Source: `hazmat_risk_experiments\outputs\models\small_formal_seed0_e20_summary.csv`

This is a short 20-epoch, seed-0 stability run. It verifies the experimental pipeline and gives an initial trend, but it is not a final multi-seed result.

## Test Metrics By Split

### Split A

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | Precision@6-8 | PR-AUC high | High FN rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| edge_gat | 0.2759 | 1.4947 | 0.2457 | 0.1961 | 0.5000 | 0.3018 | 0.8039 |
| gcn | 0.2975 | 1.5601 | 0.2404 | 0.2157 | 0.4400 | 0.3220 | 0.7843 |
| mlp | 0.2909 | 2.3772 | 0.3035 | 0.4314 | 0.3607 | 0.3070 | 0.5686 |
| teg_gnn | 0.2606 | 2.1763 | 0.3337 | 0.3922 | 0.3636 | 0.2871 | 0.6078 |
| weighted_gcn | 0.2560 | 2.2257 | 0.3434 | 0.4510 | 0.3770 | 0.3407 | 0.5490 |

Initial bests:
- Macro-F1: `gcn` (0.2975).
- MAE: `edge_gat` (1.4947).
- QWK: `weighted_gcn` (0.3434).
- Recall@6-8: `weighted_gcn` (0.4510).

### Split B

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | Precision@6-8 | PR-AUC high | High FN rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| edge_gat | 0.2496 | 1.5075 | 0.2491 | 0.1923 | 0.4167 | 0.3219 | 0.8077 |
| gcn | 0.2887 | 1.5711 | 0.3069 | 0.2692 | 0.5833 | 0.4197 | 0.7308 |
| mlp | 0.2586 | 2.2954 | 0.3135 | 0.3846 | 0.4000 | 0.3957 | 0.6154 |
| teg_gnn | 0.2516 | 2.0624 | 0.4452 | 0.4615 | 0.4138 | 0.4212 | 0.5385 |
| weighted_gcn | 0.2470 | 2.1379 | 0.3316 | 0.3462 | 0.4737 | 0.4564 | 0.6538 |

Initial bests:
- Macro-F1: `gcn` (0.2887).
- MAE: `edge_gat` (1.5075).
- QWK: `teg_gnn` (0.4452).
- Recall@6-8: `teg_gnn` (0.4615).

### Split C

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | Precision@6-8 | PR-AUC high | High FN rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| edge_gat | 0.2307 | 1.6949 | 0.1806 | 0.1154 | 0.3750 | 0.1981 | 0.8846 |
| gcn | 0.2386 | 1.7201 | 0.2057 | 0.1923 | 0.5556 | 0.2684 | 0.8077 |
| mlp | 0.1933 | 2.5651 | 0.0598 | 0.1923 | 0.2083 | 0.1546 | 0.8077 |
| teg_gnn | 0.2065 | 2.2701 | 0.1867 | 0.3077 | 0.2581 | 0.1891 | 0.6923 |
| weighted_gcn | 0.2115 | 2.3372 | 0.2261 | 0.3077 | 0.3478 | 0.2389 | 0.6923 |

Initial bests:
- Macro-F1: `gcn` (0.2386).
- MAE: `edge_gat` (1.6949).
- QWK: `weighted_gcn` (0.2261).
- Recall@6-8: `teg_gnn` (0.3077).

## Notes

- This report uses only one seed, so all standard deviations are zero in the source summary.
- The next formal step should run multiple seeds and more epochs before drawing paper-level conclusions.
- The current result is useful for checking whether the training code, splits, and metrics behave sensibly.
