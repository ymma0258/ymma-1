# Paper model comparison: final 10-seed results

All downstream cross-model risk values below use the same common reference risk matrix.

## Node-risk evaluation (Split B)

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |
|---|---:|---:|---:|---:|---:|---:|
| GCN | 0.2881 | 1.3739 | 0.2562 | 0.2154 | 0.3495 | 0.7846 |
| GAT | 0.2546 | 1.3744 | 0.2032 | 0.1769 | 0.3059 | 0.8231 |
| GraphSAGE | 0.2960 | 1.2773 | 0.2992 | 0.2808 | 0.3763 | 0.7192 |
| TEG-only | 0.2878 | 1.6617 | 0.2993 | 0.3000 | 0.3455 | 0.7000 |
| Stable-Tail GNN | 0.2896 | 1.2666 | 0.2904 | 0.2462 | 0.3659 | 0.7538 |
| Gradformer-adapted | 0.2612 | 1.4125 | 0.2556 | 0.2346 | 0.3242 | 0.7654 |
| SGFormer-adapted | 0.3217 | 1.2509 | 0.3717 | 0.3692 | 0.3557 | 0.6308 |
| GraphSAGE-TEG-Concat | 0.2335 | 1.2633 | 0.3205 | 0.3538 | 0.3503 | 0.6462 |
| SGFormer-TEG-Concat | 0.2668 | 1.2575 | 0.3515 | 0.3615 | 0.3744 | 0.6385 |
| GraphSAGE-TEG-Gate | 0.2420 | 1.2325 | 0.2665 | 0.2808 | 0.3675 | 0.7192 |
| SGFormer-TEG-Gate | 0.3002 | 1.2776 | 0.3532 | 0.3692 | 0.3701 | 0.6308 |

## Structure and loss ablation

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |
|---|---:|---:|---:|---:|---:|---:|
| GCN-only branch | 0.2881 | 1.3739 | 0.2562 | 0.2154 | 0.3495 | 0.7846 |
| TEG-only | 0.2878 | 1.6617 | 0.2993 | 0.3000 | 0.3455 | 0.7000 |
| Stable-Tail w/o Tail Loss | 0.2323 | 1.1871 | 0.1964 | 0.1538 | 0.3319 | 0.8462 |
| Stable-Tail GNN | 0.2896 | 1.2666 | 0.2904 | 0.2462 | 0.3659 | 0.7538 |

## Fixed-budget common-risk comparison

| Set | Budget | Model | Cost inc. | Common risk | CVaR90 |
|---|---:|---|---:|---:|---:|
| A | 20% | GCN | 16.92% | 3.4870 | 0.0909 |
| A | 20% | GAT | 17.43% | 3.5534 | 0.0913 |
| A | 20% | GraphSAGE | 16.90% | 3.3628 | 0.0859 |
| A | 20% | GraphSAGE-TEG-Concat | 16.57% | 3.5715 | 0.0911 |
| A | 20% | GraphSAGE-TEG-Gate | 17.59% | 3.4100 | 0.0864 |
| A | 20% | SGFormer-adapted | 16.40% | 3.5731 | 0.0905 |
| A | 20% | SGFormer-TEG-Concat | 15.89% | 3.4239 | 0.0859 |
| A | 20% | SGFormer-TEG-Gate | 16.04% | 3.5075 | 0.0902 |
| A | 20% | Gradformer-adapted | 16.13% | 4.0016 | 0.1056 |
| A | 20% | TEG-only | 17.45% | 3.5139 | 0.0906 |
| A | 20% | Stable-Tail w/o Tail Loss | 17.77% | 3.4988 | 0.0898 |
| A | 20% | Stable-Tail GNN | 17.68% | 3.2726 | 0.0814 |
| A | 25% | GCN | 18.56% | 3.1994 | 0.0811 |
| A | 25% | GAT | 19.08% | 3.3622 | 0.0846 |
| A | 25% | GraphSAGE | 20.29% | 3.1107 | 0.0747 |
| A | 25% | GraphSAGE-TEG-Concat | 19.80% | 3.1276 | 0.0737 |
| A | 25% | GraphSAGE-TEG-Gate | 19.99% | 3.1118 | 0.0747 |
| A | 25% | SGFormer-adapted | 19.48% | 3.2624 | 0.0760 |
| A | 25% | SGFormer-TEG-Concat | 21.52% | 3.0928 | 0.0706 |
| A | 25% | SGFormer-TEG-Gate | 20.84% | 3.0563 | 0.0708 |
| A | 25% | Gradformer-adapted | 20.32% | 3.5867 | 0.0916 |
| A | 25% | TEG-only | 19.06% | 3.2473 | 0.0813 |
| A | 25% | Stable-Tail w/o Tail Loss | 18.63% | 3.3518 | 0.0847 |
| A | 25% | Stable-Tail GNN | 17.68% | 3.2726 | 0.0814 |
| A | 30% | GCN | 24.63% | 2.8853 | 0.0638 |
| A | 30% | GAT | 23.34% | 3.1047 | 0.0726 |
| A | 30% | GraphSAGE | 24.20% | 2.9200 | 0.0630 |
| A | 30% | GraphSAGE-TEG-Concat | 24.50% | 2.8368 | 0.0596 |
| A | 30% | GraphSAGE-TEG-Gate | 24.87% | 2.7835 | 0.0583 |
| A | 30% | SGFormer-adapted | 24.25% | 2.9583 | 0.0630 |
| A | 30% | SGFormer-TEG-Concat | 23.43% | 3.0097 | 0.0656 |
| A | 30% | SGFormer-TEG-Gate | 24.77% | 2.8972 | 0.0623 |
| A | 30% | Gradformer-adapted | 22.26% | 3.3954 | 0.0826 |
| A | 30% | TEG-only | 22.22% | 3.1014 | 0.0748 |
| A | 30% | Stable-Tail w/o Tail Loss | 26.18% | 2.9454 | 0.0656 |
| A | 30% | Stable-Tail GNN | 26.68% | 2.8188 | 0.0578 |
| B | 20% | GCN | 13.68% | 5.9449 | 0.1426 |
| B | 20% | GAT | 14.42% | 6.0629 | 0.1460 |
| B | 20% | GraphSAGE | 16.49% | 5.1561 | 0.1247 |
| B | 20% | GraphSAGE-TEG-Concat | 15.34% | 5.5392 | 0.1323 |
| B | 20% | GraphSAGE-TEG-Gate | 14.74% | 5.4566 | 0.1316 |
| B | 20% | SGFormer-adapted | 16.41% | 5.0190 | 0.1191 |
| B | 20% | SGFormer-TEG-Concat | 15.96% | 5.2127 | 0.1251 |
| B | 20% | SGFormer-TEG-Gate | 16.37% | 4.9264 | 0.1184 |
| B | 20% | Gradformer-adapted | 14.59% | 5.7554 | 0.1411 |
| B | 20% | TEG-only | 13.77% | 5.7275 | 0.1378 |
| B | 20% | Stable-Tail w/o Tail Loss | 15.18% | 5.6034 | 0.1370 |
| B | 20% | Stable-Tail GNN | 16.42% | 5.1154 | 0.1227 |
| B | 25% | GCN | 20.84% | 4.5061 | 0.1091 |
| B | 25% | GAT | 20.86% | 5.0451 | 0.1210 |
| B | 25% | GraphSAGE | 20.20% | 4.4291 | 0.1054 |
| B | 25% | GraphSAGE-TEG-Concat | 21.19% | 4.2742 | 0.1005 |
| B | 25% | GraphSAGE-TEG-Gate | 20.51% | 4.2778 | 0.1017 |
| B | 25% | SGFormer-adapted | 20.61% | 4.4884 | 0.1063 |
| B | 25% | SGFormer-TEG-Concat | 21.01% | 4.2318 | 0.0999 |
| B | 25% | SGFormer-TEG-Gate | 19.57% | 4.2389 | 0.1006 |
| B | 25% | Gradformer-adapted | 21.70% | 4.6234 | 0.1112 |
| B | 25% | TEG-only | 21.39% | 4.3433 | 0.1034 |
| B | 25% | Stable-Tail w/o Tail Loss | 20.01% | 4.4986 | 0.1101 |
| B | 25% | Stable-Tail GNN | 20.57% | 4.2554 | 0.1001 |
| B | 30% | GCN | 22.94% | 4.1844 | 0.1008 |
| B | 30% | GAT | 23.00% | 4.7664 | 0.1150 |
| B | 30% | GraphSAGE | 23.07% | 4.1207 | 0.0974 |
| B | 30% | GraphSAGE-TEG-Concat | 23.95% | 4.0173 | 0.0938 |
| B | 30% | GraphSAGE-TEG-Gate | 23.27% | 3.9406 | 0.0927 |
| B | 30% | SGFormer-adapted | 22.58% | 4.2039 | 0.0990 |
| B | 30% | SGFormer-TEG-Concat | 23.98% | 4.0396 | 0.0945 |
| B | 30% | SGFormer-TEG-Gate | 25.64% | 3.8244 | 0.0903 |
| B | 30% | Gradformer-adapted | 23.87% | 4.3251 | 0.1029 |
| B | 30% | TEG-only | 22.44% | 4.2875 | 0.1020 |
| B | 30% | Stable-Tail w/o Tail Loss | 22.06% | 4.2300 | 0.1025 |
| B | 30% | Stable-Tail GNN | 22.45% | 4.0884 | 0.0956 |

## Extended downstream metrics at B=20%

| Set | Model | LoadRisk | Top10 burden share | Edge burden Gini | Max vehicle risk |
|---|---|---:|---:|---:|---:|
| A | GCN | 1.7691 | 76.58% | 0.7630 | 1.1335 |
| A | GAT | 1.8330 | 77.19% | 0.7685 | 1.1365 |
| A | GraphSAGE | 1.7364 | 75.93% | 0.7579 | 1.1390 |
| A | GraphSAGE-TEG-Concat | 1.8138 | 77.18% | 0.7683 | 1.1646 |
| A | GraphSAGE-TEG-Gate | 1.6926 | 76.38% | 0.7611 | 1.1468 |
| A | SGFormer-adapted | 1.7872 | 77.21% | 0.7681 | 1.1470 |
| A | SGFormer-TEG-Concat | 1.7226 | 76.27% | 0.7603 | 1.1172 |
| A | SGFormer-TEG-Gate | 1.7388 | 76.77% | 0.7644 | 1.1774 |
| A | Gradformer-adapted | 2.0088 | 79.48% | 0.7850 | 1.2404 |
| A | TEG-only | 1.7922 | 76.64% | 0.7627 | 1.1195 |
| A | Stable-Tail w/o Tail Loss | 1.8000 | 76.73% | 0.7635 | 1.0944 |
| A | Stable-Tail GNN | 1.6563 | 75.49% | 0.7538 | 1.0631 |
| B | GCN | 2.9436 | 84.86% | 0.8274 | 1.9330 |
| B | GAT | 3.0823 | 85.03% | 0.8289 | 1.8998 |
| B | GraphSAGE | 2.6529 | 82.23% | 0.8079 | 1.6790 |
| B | GraphSAGE-TEG-Concat | 2.8567 | 83.67% | 0.8190 | 1.7651 |
| B | GraphSAGE-TEG-Gate | 2.7455 | 83.35% | 0.8151 | 1.8106 |
| B | SGFormer-adapted | 2.5481 | 82.03% | 0.8067 | 1.7054 |
| B | SGFormer-TEG-Concat | 2.5658 | 82.33% | 0.8081 | 1.7189 |
| B | SGFormer-TEG-Gate | 2.4733 | 81.38% | 0.8016 | 1.6319 |
| B | Gradformer-adapted | 2.9320 | 84.30% | 0.8224 | 1.7821 |
| B | TEG-only | 2.9761 | 84.06% | 0.8198 | 1.8684 |
| B | Stable-Tail w/o Tail Loss | 2.8935 | 83.80% | 0.8201 | 1.7974 |
| B | Stable-Tail GNN | 2.6069 | 82.13% | 0.8061 | 1.7296 |

## OD path validation (CVaR-risk)

| Model | Hop inc. | Total risk reduction | CVaR90 reduction |
|---|---:|---:|---:|
| GAT | 9.58% | 84.02% | 89.80% |
| GCN | 10.02% | 84.17% | 90.04% |
| GraphSAGE | 10.39% | 84.31% | 89.84% |
| Stable-Tail GNN | 10.23% | 84.77% | 90.08% |
| Stable-Tail w/o Tail Loss | 9.56% | 85.48% | 90.07% |
| TEG-only | 11.03% | 80.61% | 89.42% |
| Gradformer-adapted | 9.46% | 84.29% | 90.63% |
| SGFormer-adapted | 9.75% | 84.00% | 90.34% |
| GraphSAGE-TEG-Concat | 9.51% | 85.03% | 89.85% |
| SGFormer-TEG-Concat | 10.14% | 84.43% | 90.18% |
| GraphSAGE-TEG-Gate | 9.75% | 85.02% | 89.95% |
| SGFormer-TEG-Gate | 10.41% | 83.69% | 90.05% |

## Cost-risk AUBRC over 0-40% budget

Lower is better; each curve is the lower envelope of observed beta candidates.

| Set | Model | Common risk AUBRC | CVaR90 AUBRC | LoadRisk AUBRC | Max-vehicle risk AUBRC |
|---|---|---:|---:|---:|---:|
| A | GCN | 4.5073 | 0.1214 | 2.3526 | 1.4199 |
| A | GAT | 4.6053 | 0.1245 | 2.3925 | 1.4424 |
| A | GraphSAGE | 4.4522 | 0.1190 | 2.2928 | 1.4234 |
| A | GraphSAGE-TEG-Concat | 4.4844 | 0.1202 | 2.3129 | 1.4207 |
| A | GraphSAGE-TEG-Gate | 4.4014 | 0.1159 | 2.2718 | 1.4137 |
| A | SGFormer-adapted | 4.5118 | 0.1197 | 2.2796 | 1.4321 |
| A | SGFormer-TEG-Concat | 4.4254 | 0.1176 | 2.2614 | 1.3852 |
| A | SGFormer-TEG-Gate | 4.4265 | 0.1171 | 2.2861 | 1.4003 |
| A | Gradformer-adapted | 4.7222 | 0.1278 | 2.4336 | 1.4516 |
| A | TEG-only | 4.5380 | 0.1233 | 2.3381 | 1.4501 |
| A | Stable-Tail w/o Tail Loss | 4.5389 | 0.1228 | 2.3565 | 1.4248 |
| A | Stable-Tail GNN | 4.4074 | 0.1171 | 2.2956 | 1.4063 |
| B | GCN | 5.7474 | 0.1483 | 2.8274 | 1.9097 |
| B | GAT | 6.0402 | 0.1561 | 2.9981 | 1.9441 |
| B | GraphSAGE | 5.6574 | 0.1459 | 2.8539 | 1.8577 |
| B | GraphSAGE-TEG-Concat | 5.6941 | 0.1465 | 2.8461 | 1.8722 |
| B | GraphSAGE-TEG-Gate | 5.5919 | 0.1447 | 2.7463 | 1.8517 |
| B | SGFormer-adapted | 5.5689 | 0.1417 | 2.7851 | 1.8654 |
| B | SGFormer-TEG-Concat | 5.5915 | 0.1447 | 2.7628 | 1.8565 |
| B | SGFormer-TEG-Gate | 5.5204 | 0.1425 | 2.7284 | 1.8619 |
| B | Gradformer-adapted | 5.8821 | 0.1538 | 2.9131 | 1.8945 |
| B | TEG-only | 5.6500 | 0.1449 | 2.8228 | 1.8580 |
| B | Stable-Tail w/o Tail Loss | 5.6407 | 0.1452 | 2.8498 | 1.8747 |
| B | Stable-Tail GNN | 5.5517 | 0.1426 | 2.7745 | 1.8449 |

## Budget sweep: 10%-40%

A win is the lowest common risk for the same model seed, customer set, and budget.

| Set | Model | Wins | Comparisons | Win rate | Average Risk@B |
|---|---|---:|---:|---:|---:|
| A | GCN | 1 | 70 | 1.43% | 3.6560 |
| B | GCN | 6 | 70 | 8.57% | 5.0463 |
| A | GAT | 0 | 70 | 0.00% | 3.7709 |
| B | GAT | 1 | 70 | 1.43% | 5.4249 |
| A | GraphSAGE | 3 | 70 | 4.29% | 3.5965 |
| B | GraphSAGE | 2 | 70 | 2.86% | 4.9489 |
| A | GraphSAGE-TEG-Concat | 16 | 70 | 22.86% | 3.5589 |
| B | GraphSAGE-TEG-Concat | 10 | 70 | 14.29% | 4.9441 |
| A | GraphSAGE-TEG-Gate | 13 | 70 | 18.57% | 3.4603 |
| B | GraphSAGE-TEG-Gate | 8 | 70 | 11.43% | 4.8588 |
| A | SGFormer-adapted | 6 | 70 | 8.57% | 3.6235 |
| B | SGFormer-adapted | 12 | 70 | 17.14% | 4.9176 |
| A | SGFormer-TEG-Concat | 6 | 70 | 8.57% | 3.5663 |
| B | SGFormer-TEG-Concat | 5 | 70 | 7.14% | 4.8382 |
| A | SGFormer-TEG-Gate | 9 | 70 | 12.86% | 3.5766 |
| B | SGFormer-TEG-Gate | 8 | 70 | 11.43% | 4.7648 |
| A | Gradformer-adapted | 5 | 70 | 7.14% | 3.8566 |
| B | Gradformer-adapted | 6 | 70 | 8.57% | 5.1340 |
| A | TEG-only | 4 | 70 | 5.71% | 3.6704 |
| B | TEG-only | 4 | 70 | 5.71% | 4.9478 |
| A | Stable-Tail w/o Tail Loss | 2 | 70 | 2.86% | 3.6901 |
| B | Stable-Tail w/o Tail Loss | 2 | 70 | 2.86% | 4.9789 |
| A | Stable-Tail GNN | 5 | 70 | 7.14% | 3.5686 |
| B | Stable-Tail GNN | 6 | 70 | 8.57% | 4.7901 |

## AUBRC paired significance

Positive difference means Stable-Tail GNN has lower AUBRC.

| Set | Baseline | Baseline - Stable | Relative reduction | 95% CI | Holm p |
|---|---|---:|---:|---:|---:|
| A | GCN | 0.1000 | 2.22% | [0.0200, 0.1714] | 0.2598 |
| A | GAT | 0.1979 | 4.30% | [0.1306, 0.2543] | 0.02148 |
| A | GraphSAGE | 0.0448 | 1.01% | [-0.0113, 0.1020] | 0.9297 |
| A | GraphSAGE-TEG-Concat | 0.0770 | 1.72% | [-0.0094, 0.1427] | 0.5273 |
| A | GraphSAGE-TEG-Gate | -0.0060 | -0.14% | [-0.0688, 0.0591] | 1 |
| A | SGFormer-adapted | 0.1045 | 2.32% | [0.0138, 0.1883] | 0.3867 |
| A | SGFormer-TEG-Concat | 0.0180 | 0.41% | [-0.0411, 0.0860] | 1 |
| A | SGFormer-TEG-Gate | 0.0192 | 0.43% | [-0.0552, 0.0967] | 1 |
| A | Gradformer-adapted | 0.3149 | 6.67% | [0.2256, 0.4071] | 0.02148 |
| A | TEG-only | 0.1307 | 2.88% | [0.0690, 0.1879] | 0.1094 |
| A | Stable-Tail w/o Tail Loss | 0.1315 | 2.90% | [0.0989, 0.1635] | 0.02148 |
| B | GCN | 0.1957 | 3.41% | [0.0849, 0.3173] | 0.08789 |
| B | GAT | 0.4885 | 8.09% | [0.3461, 0.6027] | 0.03906 |
| B | GraphSAGE | 0.1057 | 1.87% | [-0.0331, 0.2537] | 1 |
| B | GraphSAGE-TEG-Concat | 0.1425 | 2.50% | [0.0237, 0.2523] | 0.3906 |
| B | GraphSAGE-TEG-Gate | 0.0402 | 0.72% | [-0.0650, 0.1481] | 1 |
| B | SGFormer-adapted | 0.0172 | 0.31% | [-0.0767, 0.1124] | 1 |
| B | SGFormer-TEG-Concat | 0.0398 | 0.71% | [-0.0821, 0.1828] | 1 |
| B | SGFormer-TEG-Gate | -0.0313 | -0.57% | [-0.1225, 0.0709] | 1 |
| B | Gradformer-adapted | 0.3304 | 5.62% | [0.1785, 0.5042] | 0.02148 |
| B | TEG-only | 0.0983 | 1.74% | [0.0060, 0.1880] | 0.7383 |
| B | Stable-Tail w/o Tail Loss | 0.0890 | 1.58% | [-0.0162, 0.1847] | 0.7852 |

## Paired significance at Risk@20

Positive difference means Stable-Tail GNN has lower common risk.

| Set | Baseline | Baseline - Stable | Relative reduction | 95% CI | Holm p |
|---|---|---:|---:|---:|---:|
| A | GCN | 0.2144 | 6.15% | [-0.0790, 0.5994] | 1 |
| A | GAT | 0.2808 | 7.90% | [0.0751, 0.5578] | 0.1953 |
| A | GraphSAGE | 0.0903 | 2.68% | [-0.0986, 0.3656] | 1 |
| A | GraphSAGE-TEG-Concat | 0.2989 | 8.37% | [-0.0110, 0.6574] | 1 |
| A | GraphSAGE-TEG-Gate | 0.1374 | 4.03% | [-0.0912, 0.4642] | 1 |
| A | SGFormer-adapted | 0.3005 | 8.41% | [0.0350, 0.5958] | 1 |
| A | SGFormer-TEG-Concat | 0.1513 | 4.42% | [-0.1073, 0.4470] | 1 |
| A | SGFormer-TEG-Gate | 0.2349 | 6.70% | [-0.0550, 0.6009] | 1 |
| A | Gradformer-adapted | 0.7290 | 18.22% | [0.4122, 1.0473] | 0.04297 |
| A | TEG-only | 0.2413 | 6.87% | [-0.0497, 0.6125] | 1 |
| A | Stable-Tail w/o Tail Loss | 0.2262 | 6.47% | [0.0467, 0.4980] | 0.4395 |
| B | GCN | 0.8295 | 13.95% | [0.3539, 1.2908] | 0.1367 |
| B | GAT | 0.9475 | 15.63% | [0.4900, 1.4228] | 0.06445 |
| B | GraphSAGE | 0.0407 | 0.79% | [-0.5518, 0.6340] | 1 |
| B | GraphSAGE-TEG-Concat | 0.4238 | 7.65% | [0.0210, 0.8799] | 0.916 |
| B | GraphSAGE-TEG-Gate | 0.3412 | 6.25% | [-0.1981, 0.8794] | 1 |
| B | SGFormer-adapted | -0.0964 | -1.92% | [-0.4605, 0.2807] | 1 |
| B | SGFormer-TEG-Concat | 0.0973 | 1.87% | [-0.6328, 0.8293] | 1 |
| B | SGFormer-TEG-Gate | -0.1890 | -3.84% | [-0.6773, 0.2315] | 1 |
| B | Gradformer-adapted | 0.6400 | 11.12% | [0.1512, 1.0773] | 0.334 |
| B | TEG-only | 0.6121 | 10.69% | [0.1761, 1.0619] | 0.334 |
| B | Stable-Tail w/o Tail Loss | 0.4880 | 8.71% | [0.0317, 0.9954] | 0.9609 |

## Interpretation guardrails

- Node classification and downstream route safety are related but distinct objectives.
- Cross-model route claims must use the common-risk tables, not each model's self-evaluation scale.
- The budget selector chooses the lowest-common-risk observed beta candidate feasible under each cost budget.
- Statistical tests pair identical model-seed indices; bootstrap intervals use 10,000 resamples by default.

## Gate-targeted paired significance

Positive `reference - target` means the target model is lower/better. Holm correction is applied within each Set × metric block over the six targeted Gate comparisons.

| Set | Metric | Target | Reference | Reference - target | Relative | 95% CI | Holm p |
|---|---|---|---|---:|---:|---:|---:|
| A | common_risk_aubrc | SGFormer-TEG-Gate | SGFormer-TEG-Concat | -0.0011 | -0.03% | [-0.0770, 0.0819] | 1 |
| A | common_risk_aubrc | SGFormer-TEG-Gate | SGFormer-adapted | 0.0853 | 1.89% | [-0.0071, 0.1809] | 0.6406 |
| A | common_risk_aubrc | SGFormer-TEG-Gate | Stable-Tail GNN | -0.0192 | -0.44% | [-0.0965, 0.0549] | 1 |
| A | common_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0830 | 1.85% | [-0.0094, 0.1714] | 0.5273 |
| A | common_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE | 0.0508 | 1.14% | [-0.0033, 0.1173] | 0.3867 |
| A | common_risk_aubrc | GraphSAGE-TEG-Gate | Stable-Tail GNN | 0.0060 | 0.14% | [-0.0599, 0.0699] | 1 |
| A | cvar90_aubrc | SGFormer-TEG-Gate | SGFormer-TEG-Concat | 0.0005 | 0.43% | [-0.0027, 0.0038] | 1 |
| A | cvar90_aubrc | SGFormer-TEG-Gate | SGFormer-adapted | 0.0026 | 2.17% | [-0.0001, 0.0056] | 1 |
| A | cvar90_aubrc | SGFormer-TEG-Gate | Stable-Tail GNN | -0.0000 | -0.01% | [-0.0034, 0.0033] | 1 |
| A | cvar90_aubrc | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0043 | 3.61% | [0.0002, 0.0086] | 0.5273 |
| A | cvar90_aubrc | GraphSAGE-TEG-Gate | GraphSAGE | 0.0031 | 2.59% | [0.0004, 0.0066] | 0.5039 |
| A | cvar90_aubrc | GraphSAGE-TEG-Gate | Stable-Tail GNN | 0.0012 | 1.03% | [-0.0019, 0.0044] | 1 |
| A | load_risk_aubrc | SGFormer-TEG-Gate | SGFormer-TEG-Concat | -0.0247 | -1.09% | [-0.0713, 0.0249] | 1 |
| A | load_risk_aubrc | SGFormer-TEG-Gate | SGFormer-adapted | -0.0065 | -0.29% | [-0.0841, 0.0745] | 1 |
| A | load_risk_aubrc | SGFormer-TEG-Gate | Stable-Tail GNN | 0.0095 | 0.42% | [-0.0396, 0.0634] | 1 |
| A | load_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0411 | 1.78% | [-0.0084, 0.0881] | 0.6328 |
| A | load_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE | 0.0210 | 0.91% | [-0.0314, 0.0726] | 1 |
| A | load_risk_aubrc | GraphSAGE-TEG-Gate | Stable-Tail GNN | 0.0238 | 1.04% | [-0.0210, 0.0676] | 1 |
| A | average_common_risk_at_b | SGFormer-TEG-Gate | SGFormer-TEG-Concat | -0.0103 | -0.29% | [-0.1018, 0.0802] | 1 |
| A | average_common_risk_at_b | SGFormer-TEG-Gate | SGFormer-adapted | 0.0468 | 1.29% | [-0.1150, 0.2034] | 1 |
| A | average_common_risk_at_b | SGFormer-TEG-Gate | Stable-Tail GNN | -0.0081 | -0.23% | [-0.1292, 0.1252] | 1 |
| A | average_common_risk_at_b | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0987 | 2.77% | [0.0297, 0.1729] | 0.2441 |
| A | average_common_risk_at_b | GraphSAGE-TEG-Gate | GraphSAGE | 0.1362 | 3.79% | [0.0617, 0.2087] | 0.1172 |
| A | average_common_risk_at_b | GraphSAGE-TEG-Gate | Stable-Tail GNN | 0.1083 | 3.04% | [0.0214, 0.2021] | 0.2578 |
| B | common_risk_aubrc | SGFormer-TEG-Gate | SGFormer-TEG-Concat | 0.0711 | 1.27% | [-0.0733, 0.2346] | 1 |
| B | common_risk_aubrc | SGFormer-TEG-Gate | SGFormer-adapted | 0.0485 | 0.87% | [-0.0612, 0.1649] | 1 |
| B | common_risk_aubrc | SGFormer-TEG-Gate | Stable-Tail GNN | 0.0313 | 0.56% | [-0.0796, 0.1218] | 1 |
| B | common_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.1023 | 1.80% | [-0.0061, 0.2212] | 0.9609 |
| B | common_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE | 0.0655 | 1.16% | [-0.0831, 0.2167] | 1 |
| B | common_risk_aubrc | GraphSAGE-TEG-Gate | Stable-Tail GNN | -0.0402 | -0.72% | [-0.1481, 0.0608] | 1 |
| B | cvar90_aubrc | SGFormer-TEG-Gate | SGFormer-TEG-Concat | 0.0022 | 1.52% | [-0.0027, 0.0075] | 1 |
| B | cvar90_aubrc | SGFormer-TEG-Gate | SGFormer-adapted | -0.0008 | -0.56% | [-0.0041, 0.0023] | 1 |
| B | cvar90_aubrc | SGFormer-TEG-Gate | Stable-Tail GNN | 0.0001 | 0.09% | [-0.0031, 0.0029] | 1 |
| B | cvar90_aubrc | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0019 | 1.27% | [-0.0019, 0.0060] | 1 |
| B | cvar90_aubrc | GraphSAGE-TEG-Gate | GraphSAGE | 0.0012 | 0.83% | [-0.0036, 0.0056] | 1 |
| B | cvar90_aubrc | GraphSAGE-TEG-Gate | Stable-Tail GNN | -0.0021 | -1.45% | [-0.0057, 0.0018] | 1 |
| B | load_risk_aubrc | SGFormer-TEG-Gate | SGFormer-TEG-Concat | 0.0344 | 1.24% | [-0.0517, 0.1239] | 0.9844 |
| B | load_risk_aubrc | SGFormer-TEG-Gate | SGFormer-adapted | 0.0567 | 2.04% | [-0.0043, 0.1181] | 0.4805 |
| B | load_risk_aubrc | SGFormer-TEG-Gate | Stable-Tail GNN | 0.0460 | 1.66% | [-0.0010, 0.0864] | 0.2578 |
| B | load_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0998 | 3.51% | [0.0380, 0.1620] | 0.1172 |
| B | load_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE | 0.1075 | 3.77% | [0.0191, 0.1918] | 0.1855 |
| B | load_risk_aubrc | GraphSAGE-TEG-Gate | Stable-Tail GNN | 0.0281 | 1.01% | [-0.0325, 0.0874] | 0.9844 |
| B | average_common_risk_at_b | SGFormer-TEG-Gate | SGFormer-TEG-Concat | 0.0734 | 1.52% | [-0.1390, 0.2855] | 1 |
| B | average_common_risk_at_b | SGFormer-TEG-Gate | SGFormer-adapted | 0.1529 | 3.11% | [-0.0227, 0.3232] | 1 |
| B | average_common_risk_at_b | SGFormer-TEG-Gate | Stable-Tail GNN | 0.0253 | 0.53% | [-0.1695, 0.1913] | 1 |
| B | average_common_risk_at_b | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0853 | 1.73% | [-0.0799, 0.2721] | 1 |
| B | average_common_risk_at_b | GraphSAGE-TEG-Gate | GraphSAGE | 0.0901 | 1.82% | [-0.1039, 0.2594] | 1 |
| B | average_common_risk_at_b | GraphSAGE-TEG-Gate | Stable-Tail GNN | -0.0687 | -1.43% | [-0.2184, 0.0736] | 1 |
