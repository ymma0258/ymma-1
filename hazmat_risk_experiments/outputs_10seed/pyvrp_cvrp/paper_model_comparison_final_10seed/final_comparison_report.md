# Paper model comparison: final 10-seed results

All downstream cross-model risk values below use the same common reference risk matrix.

## Node-risk evaluation (Split B)

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |
|---|---:|---:|---:|---:|---:|---:|
| GCN | 0.2881 | 1.3739 | 0.2562 | 0.2154 | 0.3495 | 0.7846 |
| GAT | 0.2546 | 1.3744 | 0.2032 | 0.1769 | 0.3059 | 0.8231 |
| GraphSAGE | 0.2960 | 1.2773 | 0.2992 | 0.2808 | 0.3763 | 0.7192 |
| SGFormer-adapted | 0.3217 | 1.2509 | 0.3717 | 0.3692 | 0.3557 | 0.6308 |
| Gradformer-adapted | 0.2612 | 1.4125 | 0.2556 | 0.2346 | 0.3242 | 0.7654 |
| Stable-Tail GNN | 0.2896 | 1.2666 | 0.2904 | 0.2462 | 0.3659 | 0.7538 |
| Gradformer-adapted | 0.2612 | 1.4125 | 0.2556 | 0.2346 | 0.3242 | 0.7654 |
| SGFormer-adapted | 0.3217 | 1.2509 | 0.3717 | 0.3692 | 0.3557 | 0.6308 |

## Structure and loss ablation

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |
|---|---:|---:|---:|---:|---:|---:|
| GCN-only branch | 0.2881 | 1.3739 | 0.2562 | 0.2154 | 0.3495 | 0.7846 |
| TEG-only | 0.2878 | 1.6617 | 0.2993 | 0.3000 | 0.3455 | 0.7000 |
| Stable-Tail w/o Tail Loss | 0.2323 | 1.1871 | 0.1964 | 0.1538 | 0.3319 | 0.8462 |
| Stable-Tail GNN | 0.2896 | 1.2666 | 0.2904 | 0.2462 | 0.3659 | 0.7538 |

## Fixed-budget common-risk comparison

| Set | Budget | Model | Cost inc. | Common risk | CVaR90 | CVaR95 | Max edge risk |
|---|---:|---|---:|---:|---:|---:|---:|
| A | 20% | GCN | 16.92% | 3.4870 | 0.0909 | 0.1702 | 0.4666 |
| A | 20% | GAT | 17.43% | 3.5534 | 0.0913 | 0.1749 | 0.4369 |
| A | 20% | GraphSAGE | 16.90% | 3.3628 | 0.0859 | 0.1635 | 0.4251 |
| A | 20% | SGFormer-adapted | 16.40% | 3.5731 | 0.0905 | 0.1737 | 0.4625 |
| A | 20% | Gradformer-adapted | 16.13% | 4.0016 | 0.1056 | 0.2097 | 0.6299 |
| A | 20% | TEG-only | 17.45% | 3.5139 | 0.0906 | 0.1719 | 0.4679 |
| A | 20% | Stable-Tail w/o Tail Loss | 17.77% | 3.4988 | 0.0898 | 0.1712 | 0.4243 |
| A | 20% | Stable-Tail GNN | 17.68% | 3.2726 | 0.0814 | 0.1527 | 0.3772 |
| A | 25% | GCN | 18.56% | 3.1994 | 0.0811 | 0.1511 | 0.3787 |
| A | 25% | GAT | 19.08% | 3.3622 | 0.0846 | 0.1608 | 0.3911 |
| A | 25% | GraphSAGE | 20.29% | 3.1107 | 0.0747 | 0.1434 | 0.3717 |
| A | 25% | SGFormer-adapted | 19.48% | 3.2624 | 0.0760 | 0.1510 | 0.3763 |
| A | 25% | Gradformer-adapted | 20.32% | 3.5867 | 0.0916 | 0.1789 | 0.4888 |
| A | 25% | TEG-only | 19.06% | 3.2473 | 0.0813 | 0.1537 | 0.3841 |
| A | 25% | Stable-Tail w/o Tail Loss | 18.63% | 3.3518 | 0.0847 | 0.1607 | 0.3773 |
| A | 25% | Stable-Tail GNN | 17.68% | 3.2726 | 0.0814 | 0.1527 | 0.3772 |
| A | 30% | GCN | 24.63% | 2.8853 | 0.0638 | 0.1296 | 0.3552 |
| A | 30% | GAT | 23.34% | 3.1047 | 0.0726 | 0.1446 | 0.3829 |
| A | 30% | GraphSAGE | 24.20% | 2.9200 | 0.0630 | 0.1273 | 0.3567 |
| A | 30% | SGFormer-adapted | 24.25% | 2.9583 | 0.0630 | 0.1274 | 0.3407 |
| A | 30% | Gradformer-adapted | 22.26% | 3.3954 | 0.0826 | 0.1646 | 0.4459 |
| A | 30% | TEG-only | 22.22% | 3.1014 | 0.0748 | 0.1405 | 0.3769 |
| A | 30% | Stable-Tail w/o Tail Loss | 26.18% | 2.9454 | 0.0656 | 0.1275 | 0.3513 |
| A | 30% | Stable-Tail GNN | 26.68% | 2.8188 | 0.0578 | 0.1172 | 0.3354 |
| B | 20% | GCN | 13.68% | 5.9449 | 0.1426 | 0.3013 | 0.7036 |
| B | 20% | GAT | 14.42% | 6.0629 | 0.1460 | 0.3078 | 0.7005 |
| B | 20% | GraphSAGE | 16.49% | 5.1561 | 0.1247 | 0.2536 | 0.6184 |
| B | 20% | SGFormer-adapted | 16.41% | 5.0190 | 0.1191 | 0.2440 | 0.5597 |
| B | 20% | Gradformer-adapted | 14.59% | 5.7554 | 0.1411 | 0.2873 | 0.6646 |
| B | 20% | TEG-only | 13.77% | 5.7275 | 0.1378 | 0.2807 | 0.6226 |
| B | 20% | Stable-Tail w/o Tail Loss | 15.18% | 5.6034 | 0.1370 | 0.2837 | 0.7347 |
| B | 20% | Stable-Tail GNN | 16.42% | 5.1154 | 0.1227 | 0.2481 | 0.5576 |
| B | 25% | GCN | 20.84% | 4.5061 | 0.1091 | 0.2192 | 0.5420 |
| B | 25% | GAT | 20.86% | 5.0451 | 0.1210 | 0.2496 | 0.5885 |
| B | 25% | GraphSAGE | 20.20% | 4.4291 | 0.1054 | 0.2121 | 0.4850 |
| B | 25% | SGFormer-adapted | 20.61% | 4.4884 | 0.1063 | 0.2154 | 0.4649 |
| B | 25% | Gradformer-adapted | 21.70% | 4.6234 | 0.1112 | 0.2251 | 0.5347 |
| B | 25% | TEG-only | 21.39% | 4.3433 | 0.1034 | 0.2072 | 0.4725 |
| B | 25% | Stable-Tail w/o Tail Loss | 20.01% | 4.4986 | 0.1101 | 0.2181 | 0.5591 |
| B | 25% | Stable-Tail GNN | 20.57% | 4.2554 | 0.1001 | 0.2015 | 0.4392 |
| B | 30% | GCN | 22.94% | 4.1844 | 0.1008 | 0.2004 | 0.4976 |
| B | 30% | GAT | 23.00% | 4.7664 | 0.1150 | 0.2342 | 0.5628 |
| B | 30% | GraphSAGE | 23.07% | 4.1207 | 0.0974 | 0.1943 | 0.4393 |
| B | 30% | SGFormer-adapted | 22.58% | 4.2039 | 0.0990 | 0.1985 | 0.4274 |
| B | 30% | Gradformer-adapted | 23.87% | 4.3251 | 0.1029 | 0.2061 | 0.4971 |
| B | 30% | TEG-only | 22.44% | 4.2875 | 0.1020 | 0.2038 | 0.4671 |
| B | 30% | Stable-Tail w/o Tail Loss | 22.06% | 4.2300 | 0.1025 | 0.2024 | 0.5154 |
| B | 30% | Stable-Tail GNN | 22.45% | 4.0884 | 0.0956 | 0.1915 | 0.4144 |

## Extended downstream metrics at B=20%

| Set | Model | LoadRisk | Load CVaR90 | Load CVaR95 | Max vehicle risk | Max vehicle CVaR90 | Top10 burden share | Edge burden Gini |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | GCN | 1.7691 | 0.0509 | 0.0841 | 1.1335 | 0.1518 | 76.58% | 0.7630 |
| A | GAT | 1.8330 | 0.0533 | 0.0881 | 1.1365 | 0.1432 | 77.19% | 0.7685 |
| A | GraphSAGE | 1.7364 | 0.0496 | 0.0828 | 1.1390 | 0.1448 | 75.93% | 0.7579 |
| A | SGFormer-adapted | 1.7872 | 0.0511 | 0.0849 | 1.1470 | 0.1462 | 77.21% | 0.7681 |
| A | Gradformer-adapted | 2.0088 | 0.0596 | 0.0990 | 1.2404 | 0.1883 | 79.48% | 0.7850 |
| A | TEG-only | 1.7922 | 0.0515 | 0.0846 | 1.1195 | 0.1470 | 76.64% | 0.7627 |
| A | Stable-Tail w/o Tail Loss | 1.8000 | 0.0518 | 0.0844 | 1.0944 | 0.1409 | 76.73% | 0.7635 |
| A | Stable-Tail GNN | 1.6563 | 0.0466 | 0.0765 | 1.0631 | 0.1338 | 75.49% | 0.7538 |
| B | GCN | 2.9436 | 0.0861 | 0.1579 | 1.9330 | 0.2770 | 84.86% | 0.8274 |
| B | GAT | 3.0823 | 0.0914 | 0.1656 | 1.8998 | 0.2887 | 85.03% | 0.8289 |
| B | GraphSAGE | 2.6529 | 0.0760 | 0.1375 | 1.6790 | 0.2288 | 82.23% | 0.8079 |
| B | SGFormer-adapted | 2.5481 | 0.0717 | 0.1315 | 1.7054 | 0.2261 | 82.03% | 0.8067 |
| B | Gradformer-adapted | 2.9320 | 0.0863 | 0.1550 | 1.7821 | 0.2533 | 84.30% | 0.8224 |
| B | TEG-only | 2.9761 | 0.0872 | 0.1565 | 1.8684 | 0.2670 | 84.06% | 0.8198 |
| B | Stable-Tail w/o Tail Loss | 2.8935 | 0.0843 | 0.1539 | 1.7974 | 0.2513 | 83.80% | 0.8201 |
| B | Stable-Tail GNN | 2.6069 | 0.0739 | 0.1340 | 1.7296 | 0.2263 | 82.13% | 0.8061 |

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

## Cost-risk AUBRC over 0-40% budget

Lower is better; each curve is the lower envelope of observed beta candidates.

| Set | Model | Common risk AUBRC | CVaR90 AUBRC | CVaR95 AUBRC | LoadRisk AUBRC | Load CVaR90 AUBRC | Max-vehicle risk AUBRC | Max-vehicle CVaR90 AUBRC |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | GCN | 4.5073 | 0.1214 | 0.2311 | 2.3526 | 0.0724 | 1.4199 | 0.2141 |
| A | GAT | 4.6053 | 0.1245 | 0.2375 | 2.3925 | 0.0742 | 1.4424 | 0.2203 |
| A | GraphSAGE | 4.4522 | 0.1190 | 0.2263 | 2.2928 | 0.0701 | 1.4234 | 0.2099 |
| A | SGFormer-adapted | 4.5118 | 0.1197 | 0.2273 | 2.2796 | 0.0695 | 1.4321 | 0.2131 |
| A | Gradformer-adapted | 4.7222 | 0.1278 | 0.2442 | 2.4336 | 0.0752 | 1.4516 | 0.2204 |
| A | TEG-only | 4.5380 | 0.1233 | 0.2311 | 2.3381 | 0.0718 | 1.4501 | 0.2193 |
| A | Stable-Tail w/o Tail Loss | 4.5389 | 0.1228 | 0.2310 | 2.3565 | 0.0724 | 1.4248 | 0.2110 |
| A | Stable-Tail GNN | 4.4074 | 0.1171 | 0.2224 | 2.2956 | 0.0702 | 1.4063 | 0.2103 |
| B | GCN | 5.7474 | 0.1483 | 0.2804 | 2.8274 | 0.0814 | 1.9097 | 0.2608 |
| B | GAT | 6.0402 | 0.1561 | 0.2978 | 2.9981 | 0.0873 | 1.9441 | 0.2772 |
| B | GraphSAGE | 5.6574 | 0.1459 | 0.2739 | 2.8539 | 0.0819 | 1.8577 | 0.2555 |
| B | SGFormer-adapted | 5.5689 | 0.1417 | 0.2687 | 2.7851 | 0.0795 | 1.8654 | 0.2497 |
| B | Gradformer-adapted | 5.8821 | 0.1538 | 0.2861 | 2.9131 | 0.0843 | 1.8945 | 0.2657 |
| B | TEG-only | 5.6500 | 0.1449 | 0.2715 | 2.8228 | 0.0809 | 1.8580 | 0.2551 |
| B | Stable-Tail w/o Tail Loss | 5.6407 | 0.1452 | 0.2752 | 2.8498 | 0.0818 | 1.8747 | 0.2565 |
| B | Stable-Tail GNN | 5.5517 | 0.1426 | 0.2675 | 2.7745 | 0.0791 | 1.8449 | 0.2485 |

## Budget sweep: 10%-40%

A win is the lowest common risk for the same model seed, customer set, and budget.

| Set | Model | Wins | Comparisons | Win rate | Average Risk@B |
|---|---|---:|---:|---:|---:|
| A | GCN | 7 | 70 | 10.00% | 3.6560 |
| B | GCN | 10 | 70 | 14.29% | 5.0463 |
| A | GAT | 3 | 70 | 4.29% | 3.7709 |
| B | GAT | 2 | 70 | 2.86% | 5.4249 |
| A | GraphSAGE | 15 | 70 | 21.43% | 3.5965 |
| B | GraphSAGE | 10 | 70 | 14.29% | 4.9489 |
| A | SGFormer-adapted | 13 | 70 | 18.57% | 3.6235 |
| B | SGFormer-adapted | 16 | 70 | 22.86% | 4.9176 |
| A | Gradformer-adapted | 13 | 70 | 18.57% | 3.8566 |
| B | Gradformer-adapted | 11 | 70 | 15.71% | 5.1340 |
| A | TEG-only | 4 | 70 | 5.71% | 3.6704 |
| B | TEG-only | 5 | 70 | 7.14% | 4.9478 |
| A | Stable-Tail w/o Tail Loss | 5 | 70 | 7.14% | 3.6901 |
| B | Stable-Tail w/o Tail Loss | 5 | 70 | 7.14% | 4.9789 |
| A | Stable-Tail GNN | 10 | 70 | 14.29% | 3.5686 |
| B | Stable-Tail GNN | 11 | 70 | 15.71% | 4.7901 |

## AUBRC paired significance

Positive difference means Stable-Tail GNN has lower AUBRC.

| Set | Baseline | Baseline - Stable | Relative reduction | 95% CI | Holm p |
|---|---|---:|---:|---:|---:|
| A | GCN | 0.1000 | 2.22% | [0.0200, 0.1714] | 0.1113 |
| A | GAT | 0.1979 | 4.30% | [0.1306, 0.2543] | 0.01367 |
| A | GraphSAGE | 0.0448 | 1.01% | [-0.0113, 0.1020] | 0.2324 |
| A | SGFormer-adapted | 0.1045 | 2.32% | [0.0138, 0.1883] | 0.1289 |
| A | Gradformer-adapted | 0.3149 | 6.67% | [0.2256, 0.4071] | 0.01367 |
| A | TEG-only | 0.1307 | 2.88% | [0.0690, 0.1879] | 0.05469 |
| A | Stable-Tail w/o Tail Loss | 0.1315 | 2.90% | [0.0989, 0.1635] | 0.01367 |
| B | GCN | 0.1957 | 3.41% | [0.0849, 0.3173] | 0.04883 |
| B | GAT | 0.4885 | 8.09% | [0.3461, 0.6027] | 0.02344 |
| B | GraphSAGE | 0.1057 | 1.87% | [-0.0331, 0.2537] | 0.5508 |
| B | SGFormer-adapted | 0.0172 | 0.31% | [-0.0767, 0.1124] | 0.7695 |
| B | Gradformer-adapted | 0.3304 | 5.62% | [0.1785, 0.5042] | 0.01367 |
| B | TEG-only | 0.0983 | 1.74% | [0.0060, 0.1880] | 0.4219 |
| B | Stable-Tail w/o Tail Loss | 0.0890 | 1.58% | [-0.0162, 0.1847] | 0.4219 |

## Paired significance at Risk@20

Positive difference means Stable-Tail GNN has lower common risk.

| Set | Baseline | Baseline - Stable | Relative reduction | 95% CI | Holm p |
|---|---|---:|---:|---:|---:|
| A | GCN | 0.2144 | 6.15% | [-0.0790, 0.5994] | 1 |
| A | GAT | 0.2808 | 7.90% | [0.0751, 0.5578] | 0.1172 |
| A | GraphSAGE | 0.0903 | 2.68% | [-0.0986, 0.3656] | 1 |
| A | SGFormer-adapted | 0.3005 | 8.41% | [0.0350, 0.5958] | 0.6406 |
| A | Gradformer-adapted | 0.7290 | 18.22% | [0.4122, 1.0473] | 0.02734 |
| A | TEG-only | 0.2413 | 6.87% | [-0.0497, 0.6125] | 1 |
| A | Stable-Tail w/o Tail Loss | 0.2262 | 6.47% | [0.0467, 0.4980] | 0.2441 |
| B | GCN | 0.8295 | 13.95% | [0.3539, 1.2908] | 0.08203 |
| B | GAT | 0.9475 | 15.63% | [0.4900, 1.4228] | 0.04102 |
| B | GraphSAGE | 0.0407 | 0.79% | [-0.5518, 0.6340] | 1 |
| B | SGFormer-adapted | -0.0964 | -1.92% | [-0.4605, 0.2807] | 1 |
| B | Gradformer-adapted | 0.6400 | 11.12% | [0.1512, 1.0773] | 0.1855 |
| B | TEG-only | 0.6121 | 10.69% | [0.1761, 1.0619] | 0.1855 |
| B | Stable-Tail w/o Tail Loss | 0.4880 | 8.71% | [0.0317, 0.9954] | 0.4805 |

## Interpretation guardrails

- Node classification and downstream route safety are related but distinct objectives.
- Cross-model route claims must use the common-risk tables, not each model's self-evaluation scale.
- The budget selector chooses the lowest-common-risk observed beta candidate feasible under each cost budget.
- Statistical tests pair identical model-seed indices; bootstrap intervals use 10,000 resamples by default.
