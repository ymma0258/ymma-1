## Table 2. Split A node-risk evaluation results

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |
|---|---:|---:|---:|---:|---:|---:|
| MLP | 0.3434 | 1.7610 | 0.3372 | 0.3843 | 0.3105 | 0.6157 |
| GCN | 0.3535 | 1.2677 | 0.2795 | 0.2392 | 0.3920 | 0.7608 |
| Weighted-GCN | 0.3560 | 1.6477 | 0.3205 | 0.3647 | 0.3517 | 0.6353 |
| Edge-GAT | 0.3420 | 1.3211 | 0.2753 | 0.2471 | 0.3745 | 0.7529 |
| TEG-low | 0.3446 | 1.6438 | 0.3393 | 0.3471 | 0.3571 | 0.6529 |
| Stable-Tail GNN | 0.2997 | 1.1885 | 0.3234 | 0.2882 | 0.3946 | 0.7118 |

## Table 3. Split B node-risk evaluation results

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |
|---|---:|---:|---:|---:|---:|---:|
| MLP | 0.2843 | 1.7219 | 0.3211 | 0.3385 | 0.3556 | 0.6615 |
| GCN | 0.2978 | 1.3308 | 0.2431 | 0.2115 | 0.3560 | 0.7885 |
| Weighted-GCN | 0.2811 | 1.6176 | 0.2911 | 0.2923 | 0.3470 | 0.7077 |
| Edge-GAT | 0.2891 | 1.3384 | 0.2580 | 0.2077 | 0.3313 | 0.7923 |
| TEG-low | 0.2683 | 1.6078 | 0.3019 | 0.2692 | 0.3502 | 0.7308 |
| Stable-Tail GNN | 0.2776 | 1.2089 | 0.2704 | 0.2423 | 0.3716 | 0.7577 |

Notes:

- `High FN` is the high-risk false-negative rate for labels 6-8.
- Values are computed from `formal_graph_models_A_B_s0_9_e50_10seed_summary.csv + teg_loss_teg_low_tail_s0_9_e50_10seed_summary.csv + gcn_stabilized_teg_s0_9_e50_10seed_summary.csv`, `eval_split=data_2021_test`, and rounded to four decimals.
