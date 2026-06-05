## Table 2. Split A node-risk evaluation results

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |
|---|---:|---:|---:|---:|---:|---:|
| GCN | 0.3430 | 1.2369 | 0.2634 | 0.2275 | 0.3940 | 0.7725 |
| TEG-low | 0.3440 | 1.6377 | 0.3345 | 0.3529 | 0.3613 | 0.6471 |
| Stable-Tail GNN | 0.3067 | 1.1826 | 0.3255 | 0.2941 | 0.3882 | 0.7059 |
| Residual fixed | 0.3388 | 1.2443 | 0.2778 | 0.2392 | 0.3977 | 0.7608 |
| Residual learnable | 0.3412 | 1.2381 | 0.2779 | 0.2392 | 0.3991 | 0.7608 |

## Table 3. Split B node-risk evaluation results

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |
|---|---:|---:|---:|---:|---:|---:|
| GCN | 0.3015 | 1.2677 | 0.2377 | 0.1923 | 0.3705 | 0.8077 |
| TEG-low | 0.2676 | 1.5953 | 0.2743 | 0.2385 | 0.3530 | 0.7615 |
| Stable-Tail GNN | 0.2966 | 1.1783 | 0.2913 | 0.2462 | 0.3892 | 0.7538 |
| Residual fixed | 0.2890 | 1.2749 | 0.2497 | 0.2077 | 0.3653 | 0.7923 |
| Residual learnable | 0.2863 | 1.2692 | 0.2508 | 0.2077 | 0.3680 | 0.7923 |

Notes:

- `High FN` is the high-risk false-negative rate for labels 6-8.
- Values are computed from `gcn_stabilized_teg_s0_4_e50_summary.csv`, `eval_split=data_2021_test`, and rounded to four decimals.
