## Table 2. Split A Stable-Tail ablation results

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |
|---|---:|---:|---:|---:|---:|---:|
| GCN low-tail setting | 0.3477 | 1.2407 | 0.2677 | 0.2255 | 0.3912 | 0.7745 |
| TEG-low | 0.3446 | 1.6438 | 0.3393 | 0.3471 | 0.3571 | 0.6529 |
| Stable-Tail GNN | 0.2997 | 1.1885 | 0.3234 | 0.2882 | 0.3946 | 0.7118 |
| Residual fixed | 0.3495 | 1.2487 | 0.2947 | 0.2569 | 0.4013 | 0.7431 |
| Residual learnable | 0.3505 | 1.2402 | 0.2966 | 0.2588 | 0.4027 | 0.7412 |

## Table 3. Split B Stable-Tail ablation results

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |
|---|---:|---:|---:|---:|---:|---:|
| GCN low-tail setting | 0.2942 | 1.2946 | 0.2435 | 0.2077 | 0.3623 | 0.7923 |
| TEG-low | 0.2683 | 1.6078 | 0.3019 | 0.2692 | 0.3502 | 0.7308 |
| Stable-Tail GNN | 0.2776 | 1.2089 | 0.2704 | 0.2423 | 0.3716 | 0.7577 |
| Residual fixed | 0.2855 | 1.2822 | 0.2524 | 0.2115 | 0.3550 | 0.7885 |
| Residual learnable | 0.2916 | 1.2769 | 0.2565 | 0.2154 | 0.3580 | 0.7846 |

Notes:

- `High FN` is the high-risk false-negative rate for labels 6-8.
- Values are computed from `formal_graph_models_A_B_s0_9_e50_10seed_summary.csv + teg_loss_teg_low_tail_s0_9_e50_10seed_summary.csv + gcn_stabilized_teg_s0_9_e50_10seed_summary.csv`, `eval_split=data_2021_test`, and rounded to four decimals.
