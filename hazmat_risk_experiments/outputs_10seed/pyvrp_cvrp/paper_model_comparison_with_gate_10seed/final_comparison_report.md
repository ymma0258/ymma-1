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

| Set | Budget | Model | Cost inc. | Common risk | CVaR90 | CVaR95 | Max edge risk |
|---|---:|---|---:|---:|---:|---:|---:|
| A | 20% | GCN | 16.92% | 3.3070 | 0.0767 | 0.1204 | 0.4522 |
| A | 20% | GAT | 17.43% | 3.3777 | 0.0793 | 0.1255 | 0.4245 |
| A | 20% | GraphSAGE | 16.90% | 3.1897 | 0.0721 | 0.1107 | 0.4113 |
| A | 20% | GraphSAGE-TEG-Concat | 16.57% | 3.3961 | 0.0800 | 0.1297 | 0.4755 |
| A | 20% | GraphSAGE-TEG-Gate | 17.59% | 3.2399 | 0.0749 | 0.1197 | 0.4154 |
| A | 20% | SGFormer-adapted | 16.40% | 3.4059 | 0.0806 | 0.1362 | 0.4511 |
| A | 20% | SGFormer-TEG-Concat | 15.89% | 3.2672 | 0.0733 | 0.1173 | 0.4275 |
| A | 20% | SGFormer-TEG-Gate | 16.04% | 3.3397 | 0.0789 | 0.1217 | 0.4553 |
| A | 20% | Gradformer-adapted | 16.13% | 3.8268 | 0.0947 | 0.1694 | 0.6218 |
| A | 20% | TEG-only | 17.45% | 3.3568 | 0.0798 | 0.1297 | 0.4562 |
| A | 20% | Stable-Tail w/o Tail Loss | 17.77% | 3.3225 | 0.0750 | 0.1202 | 0.4099 |
| A | 20% | Stable-Tail GNN | 17.68% | 3.1064 | 0.0690 | 0.1018 | 0.3630 |
| A | 25% | GCN | 18.56% | 3.0249 | 0.0672 | 0.0962 | 0.3643 |
| A | 25% | GAT | 19.08% | 3.1860 | 0.0728 | 0.1066 | 0.3769 |
| A | 25% | GraphSAGE | 20.29% | 2.9374 | 0.0650 | 0.0936 | 0.3572 |
| A | 25% | GraphSAGE-TEG-Concat | 19.80% | 2.9546 | 0.0648 | 0.0945 | 0.3531 |
| A | 25% | GraphSAGE-TEG-Gate | 19.99% | 2.9432 | 0.0650 | 0.0933 | 0.3471 |
| A | 25% | SGFormer-adapted | 19.48% | 3.0963 | 0.0691 | 0.1100 | 0.3632 |
| A | 25% | SGFormer-TEG-Concat | 21.52% | 2.9340 | 0.0626 | 0.0929 | 0.3443 |
| A | 25% | SGFormer-TEG-Gate | 20.84% | 2.8945 | 0.0636 | 0.0918 | 0.3488 |
| A | 25% | Gradformer-adapted | 20.32% | 3.4198 | 0.0777 | 0.1240 | 0.4879 |
| A | 25% | TEG-only | 19.06% | 3.0940 | 0.0681 | 0.1037 | 0.3725 |
| A | 25% | Stable-Tail w/o Tail Loss | 18.63% | 3.1785 | 0.0702 | 0.1098 | 0.3631 |
| A | 25% | Stable-Tail GNN | 17.68% | 3.1064 | 0.0690 | 0.1018 | 0.3630 |
| A | 30% | GCN | 24.63% | 2.7100 | 0.0589 | 0.0852 | 0.3405 |
| A | 30% | GAT | 23.34% | 2.9285 | 0.0665 | 0.0943 | 0.3685 |
| A | 30% | GraphSAGE | 24.20% | 2.7460 | 0.0594 | 0.0868 | 0.3417 |
| A | 30% | GraphSAGE-TEG-Concat | 24.50% | 2.6642 | 0.0577 | 0.0831 | 0.3173 |
| A | 30% | GraphSAGE-TEG-Gate | 24.87% | 2.6157 | 0.0559 | 0.0818 | 0.3053 |
| A | 30% | SGFormer-adapted | 24.25% | 2.7945 | 0.0599 | 0.0876 | 0.3263 |
| A | 30% | SGFormer-TEG-Concat | 23.43% | 2.8522 | 0.0596 | 0.0894 | 0.3318 |
| A | 30% | SGFormer-TEG-Gate | 24.77% | 2.7354 | 0.0586 | 0.0856 | 0.3189 |
| A | 30% | Gradformer-adapted | 22.26% | 3.2281 | 0.0725 | 0.1122 | 0.4437 |
| A | 30% | TEG-only | 22.22% | 2.9466 | 0.0656 | 0.0960 | 0.3640 |
| A | 30% | Stable-Tail w/o Tail Loss | 26.18% | 2.7686 | 0.0607 | 0.0893 | 0.3366 |
| A | 30% | Stable-Tail GNN | 26.68% | 2.6505 | 0.0563 | 0.0826 | 0.3202 |
| B | 20% | GCN | 13.68% | 5.8433 | 0.1499 | 0.2960 | 0.6917 |
| B | 20% | GAT | 14.42% | 5.9564 | 0.1513 | 0.3017 | 0.6886 |
| B | 20% | GraphSAGE | 16.49% | 5.0808 | 0.1312 | 0.2514 | 0.6113 |
| B | 20% | GraphSAGE-TEG-Concat | 15.34% | 5.4416 | 0.1411 | 0.2728 | 0.6979 |
| B | 20% | GraphSAGE-TEG-Gate | 14.74% | 5.3700 | 0.1373 | 0.2651 | 0.6314 |
| B | 20% | SGFormer-adapted | 16.41% | 4.9544 | 0.1262 | 0.2425 | 0.5605 |
| B | 20% | SGFormer-TEG-Concat | 15.96% | 5.1396 | 0.1287 | 0.2500 | 0.6016 |
| B | 20% | SGFormer-TEG-Gate | 16.37% | 4.8612 | 0.1230 | 0.2381 | 0.5488 |
| B | 20% | Gradformer-adapted | 14.59% | 5.6683 | 0.1460 | 0.2831 | 0.6609 |
| B | 20% | TEG-only | 13.77% | 5.6459 | 0.1412 | 0.2767 | 0.6195 |
| B | 20% | Stable-Tail w/o Tail Loss | 15.18% | 5.5001 | 0.1435 | 0.2792 | 0.7189 |
| B | 20% | Stable-Tail GNN | 16.42% | 5.0451 | 0.1280 | 0.2461 | 0.5557 |
| B | 25% | GCN | 20.84% | 4.4349 | 0.1110 | 0.2179 | 0.5444 |
| B | 25% | GAT | 20.86% | 4.9442 | 0.1290 | 0.2460 | 0.5905 |
| B | 25% | GraphSAGE | 20.20% | 4.3732 | 0.1110 | 0.2123 | 0.4910 |
| B | 25% | GraphSAGE-TEG-Concat | 21.19% | 4.2119 | 0.1029 | 0.2010 | 0.4722 |
| B | 25% | GraphSAGE-TEG-Gate | 20.51% | 4.2155 | 0.1051 | 0.2035 | 0.4803 |
| B | 25% | SGFormer-adapted | 20.61% | 4.4305 | 0.1110 | 0.2147 | 0.4637 |
| B | 25% | SGFormer-TEG-Concat | 21.01% | 4.1870 | 0.1034 | 0.2002 | 0.4263 |
| B | 25% | SGFormer-TEG-Gate | 19.57% | 4.1914 | 0.1043 | 0.2018 | 0.4145 |
| B | 25% | Gradformer-adapted | 21.70% | 4.5729 | 0.1167 | 0.2250 | 0.5476 |
| B | 25% | TEG-only | 21.39% | 4.2946 | 0.1081 | 0.2080 | 0.4797 |
| B | 25% | Stable-Tail w/o Tail Loss | 20.01% | 4.4222 | 0.1127 | 0.2162 | 0.5630 |
| B | 25% | Stable-Tail GNN | 20.57% | 4.2030 | 0.1055 | 0.2014 | 0.4423 |
| B | 30% | GCN | 22.94% | 4.1177 | 0.1018 | 0.1999 | 0.5050 |
| B | 30% | GAT | 23.00% | 4.6696 | 0.1205 | 0.2308 | 0.5670 |
| B | 30% | GraphSAGE | 23.07% | 4.0672 | 0.1000 | 0.1914 | 0.4488 |
| B | 30% | GraphSAGE-TEG-Concat | 23.95% | 3.9537 | 0.0936 | 0.1839 | 0.4399 |
| B | 30% | GraphSAGE-TEG-Gate | 23.27% | 3.8799 | 0.0929 | 0.1760 | 0.4289 |
| B | 30% | SGFormer-adapted | 22.58% | 4.1474 | 0.1008 | 0.1965 | 0.4291 |
| B | 30% | SGFormer-TEG-Concat | 23.98% | 3.9896 | 0.0959 | 0.1847 | 0.3864 |
| B | 30% | SGFormer-TEG-Gate | 25.64% | 3.7792 | 0.0898 | 0.1750 | 0.3490 |
| B | 30% | Gradformer-adapted | 23.87% | 4.2800 | 0.1067 | 0.2051 | 0.5142 |
| B | 30% | TEG-only | 22.44% | 4.2390 | 0.1055 | 0.2040 | 0.4743 |
| B | 30% | Stable-Tail w/o Tail Loss | 22.06% | 4.1592 | 0.1024 | 0.2008 | 0.5225 |
| B | 30% | Stable-Tail GNN | 22.45% | 4.0365 | 0.0990 | 0.1879 | 0.4171 |

## Extended downstream metrics at B=20%

| Set | Model | LoadRisk | Load CVaR90 | Load CVaR95 | Max vehicle risk | Max vehicle CVaR90 | Top10 burden share | Edge burden Gini |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | GCN | 1.6803 | 0.0488 | 0.0800 | 1.0785 | 0.1442 | 77.32% | 0.7740 |
| A | GAT | 1.7462 | 0.0511 | 0.0840 | 1.0907 | 0.1353 | 77.98% | 0.7796 |
| A | GraphSAGE | 1.6541 | 0.0478 | 0.0792 | 1.0771 | 0.1353 | 76.70% | 0.7693 |
| A | GraphSAGE-TEG-Concat | 1.7263 | 0.0502 | 0.0834 | 1.1194 | 0.1436 | 77.89% | 0.7789 |
| A | GraphSAGE-TEG-Gate | 1.6162 | 0.0464 | 0.0776 | 1.0820 | 0.1300 | 77.16% | 0.7725 |
| A | SGFormer-adapted | 1.7085 | 0.0493 | 0.0822 | 1.0922 | 0.1396 | 78.04% | 0.7798 |
| A | SGFormer-TEG-Concat | 1.6559 | 0.0475 | 0.0774 | 1.0566 | 0.1361 | 77.15% | 0.7725 |
| A | SGFormer-TEG-Gate | 1.6637 | 0.0483 | 0.0797 | 1.1202 | 0.1389 | 77.58% | 0.7760 |
| A | Gradformer-adapted | 1.9320 | 0.0578 | 0.0961 | 1.1955 | 0.1844 | 80.22% | 0.7951 |
| A | TEG-only | 1.7191 | 0.0502 | 0.0832 | 1.0708 | 0.1408 | 77.50% | 0.7744 |
| A | Stable-Tail w/o Tail Loss | 1.7120 | 0.0498 | 0.0799 | 1.0418 | 0.1325 | 77.47% | 0.7744 |
| A | Stable-Tail GNN | 1.5778 | 0.0448 | 0.0734 | 0.9976 | 0.1249 | 76.30% | 0.7654 |
| B | GCN | 2.8762 | 0.0850 | 0.1552 | 1.8991 | 0.2740 | 85.83% | 0.8387 |
| B | GAT | 3.0148 | 0.0901 | 0.1626 | 1.8772 | 0.2871 | 85.97% | 0.8400 |
| B | GraphSAGE | 2.6037 | 0.0753 | 0.1369 | 1.6659 | 0.2274 | 83.52% | 0.8229 |
| B | GraphSAGE-TEG-Concat | 2.8031 | 0.0823 | 0.1495 | 1.7285 | 0.2434 | 84.79% | 0.8321 |
| B | GraphSAGE-TEG-Gate | 2.6939 | 0.0787 | 0.1422 | 1.7843 | 0.2499 | 84.54% | 0.8288 |
| B | SGFormer-adapted | 2.5129 | 0.0718 | 0.1312 | 1.6744 | 0.2239 | 83.38% | 0.8221 |
| B | SGFormer-TEG-Concat | 2.5202 | 0.0719 | 0.1292 | 1.6924 | 0.2274 | 83.62% | 0.8231 |
| B | SGFormer-TEG-Gate | 2.4330 | 0.0690 | 0.1261 | 1.6046 | 0.2088 | 82.79% | 0.8179 |
| B | Gradformer-adapted | 2.8765 | 0.0855 | 0.1534 | 1.7712 | 0.2508 | 85.37% | 0.8350 |
| B | TEG-only | 2.9222 | 0.0867 | 0.1543 | 1.8630 | 0.2655 | 85.13% | 0.8321 |
| B | Stable-Tail w/o Tail Loss | 2.8360 | 0.0835 | 0.1527 | 1.7625 | 0.2482 | 84.88% | 0.8327 |
| B | Stable-Tail GNN | 2.5602 | 0.0737 | 0.1329 | 1.7158 | 0.2267 | 83.42% | 0.8211 |

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

| Set | Model | Common risk AUBRC | CVaR90 AUBRC | CVaR95 AUBRC | LoadRisk AUBRC | Load CVaR90 AUBRC | Max-vehicle risk AUBRC | Max-vehicle CVaR90 AUBRC |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | GCN | 4.3142 | 0.1163 | 0.2016 | 2.2578 | 0.0700 | 1.3689 | 0.2034 |
| A | GAT | 4.4105 | 0.1195 | 0.2071 | 2.2950 | 0.0716 | 1.3973 | 0.2102 |
| A | GraphSAGE | 4.2625 | 0.1137 | 0.1963 | 2.2029 | 0.0680 | 1.3669 | 0.1997 |
| A | GraphSAGE-TEG-Concat | 4.2930 | 0.1159 | 0.1993 | 2.2207 | 0.0686 | 1.3729 | 0.2015 |
| A | GraphSAGE-TEG-Gate | 4.2136 | 0.1113 | 0.1976 | 2.1813 | 0.0669 | 1.3590 | 0.1940 |
| A | SGFormer-adapted | 4.3280 | 0.1154 | 0.2003 | 2.1943 | 0.0674 | 1.3757 | 0.2039 |
| A | SGFormer-TEG-Concat | 4.2485 | 0.1118 | 0.1925 | 2.1808 | 0.0669 | 1.3256 | 0.1905 |
| A | SGFormer-TEG-Gate | 4.2444 | 0.1112 | 0.1956 | 2.1998 | 0.0675 | 1.3444 | 0.1947 |
| A | Gradformer-adapted | 4.5361 | 0.1214 | 0.2172 | 2.3442 | 0.0730 | 1.4070 | 0.2111 |
| A | TEG-only | 4.3596 | 0.1169 | 0.2044 | 2.2540 | 0.0699 | 1.4039 | 0.2099 |
| A | Stable-Tail w/o Tail Loss | 4.3468 | 0.1167 | 0.2036 | 2.2621 | 0.0701 | 1.3752 | 0.2004 |
| A | Stable-Tail GNN | 4.2221 | 0.1116 | 0.1939 | 2.2060 | 0.0679 | 1.3501 | 0.2005 |
| B | GCN | 5.6523 | 0.1441 | 0.2725 | 2.7720 | 0.0804 | 1.8761 | 0.2560 |
| B | GAT | 5.9285 | 0.1536 | 0.2901 | 2.9361 | 0.0863 | 1.9171 | 0.2737 |
| B | GraphSAGE | 5.5699 | 0.1422 | 0.2672 | 2.8022 | 0.0812 | 1.8298 | 0.2513 |
| B | GraphSAGE-TEG-Concat | 5.5980 | 0.1423 | 0.2679 | 2.7951 | 0.0809 | 1.8424 | 0.2516 |
| B | GraphSAGE-TEG-Gate | 5.5000 | 0.1399 | 0.2589 | 2.6963 | 0.0779 | 1.8168 | 0.2484 |
| B | SGFormer-adapted | 5.4883 | 0.1400 | 0.2644 | 2.7390 | 0.0791 | 1.8357 | 0.2454 |
| B | SGFormer-TEG-Concat | 5.5114 | 0.1395 | 0.2643 | 2.7150 | 0.0781 | 1.8276 | 0.2439 |
| B | SGFormer-TEG-Gate | 5.4408 | 0.1380 | 0.2620 | 2.6832 | 0.0773 | 1.8221 | 0.2460 |
| B | Gradformer-adapted | 5.7963 | 0.1492 | 0.2808 | 2.8631 | 0.0835 | 1.8759 | 0.2633 |
| B | TEG-only | 5.5677 | 0.1416 | 0.2646 | 2.7728 | 0.0803 | 1.8344 | 0.2514 |
| B | Stable-Tail w/o Tail Loss | 5.5440 | 0.1420 | 0.2666 | 2.7954 | 0.0811 | 1.8454 | 0.2529 |
| B | Stable-Tail GNN | 5.4668 | 0.1385 | 0.2610 | 2.7269 | 0.0787 | 1.8144 | 0.2447 |

## Budget sweep: 10%-40%

A win is the lowest common risk for the same model seed, customer set, and budget.

| Set | Model | Wins | Comparisons | Win rate | Average Risk@B |
|---|---|---:|---:|---:|---:|
| A | GCN | 1 | 70 | 1.43% | 3.4725 |
| B | GCN | 6 | 70 | 8.57% | 4.9623 |
| A | GAT | 1 | 70 | 1.43% | 3.5855 |
| B | GAT | 1 | 70 | 1.43% | 5.3205 |
| A | GraphSAGE | 3 | 70 | 4.29% | 3.4170 |
| B | GraphSAGE | 2 | 70 | 2.86% | 4.8746 |
| A | GraphSAGE-TEG-Concat | 16 | 70 | 22.86% | 3.3786 |
| B | GraphSAGE-TEG-Concat | 10 | 70 | 14.29% | 4.8588 |
| A | GraphSAGE-TEG-Gate | 13 | 70 | 18.57% | 3.2837 |
| B | GraphSAGE-TEG-Gate | 8 | 70 | 11.43% | 4.7790 |
| A | SGFormer-adapted | 6 | 70 | 8.57% | 3.4519 |
| B | SGFormer-adapted | 12 | 70 | 17.14% | 4.8504 |
| A | SGFormer-TEG-Concat | 6 | 70 | 8.57% | 3.4014 |
| B | SGFormer-TEG-Concat | 5 | 70 | 7.14% | 4.7729 |
| A | SGFormer-TEG-Gate | 8 | 70 | 11.43% | 3.4061 |
| B | SGFormer-TEG-Gate | 8 | 70 | 11.43% | 4.7005 |
| A | Gradformer-adapted | 5 | 70 | 7.14% | 3.6819 |
| B | Gradformer-adapted | 6 | 70 | 8.57% | 5.0643 |
| A | TEG-only | 4 | 70 | 5.71% | 3.5056 |
| B | TEG-only | 4 | 70 | 5.71% | 4.8798 |
| A | Stable-Tail w/o Tail Loss | 2 | 70 | 2.86% | 3.5068 |
| B | Stable-Tail w/o Tail Loss | 2 | 70 | 2.86% | 4.8925 |
| A | Stable-Tail GNN | 5 | 70 | 7.14% | 3.3939 |
| B | Stable-Tail GNN | 6 | 70 | 8.57% | 4.7204 |

## AUBRC paired significance

Positive difference means Stable-Tail GNN has lower AUBRC.

| Set | Baseline | Baseline - Stable | Relative reduction | 95% CI | Holm p |
|---|---|---:|---:|---:|---:|
| A | GCN | 0.0921 | 2.13% | [0.0146, 0.1620] | 0.3418 |
| A | GAT | 0.1883 | 4.27% | [0.1214, 0.2436] | 0.02148 |
| A | GraphSAGE | 0.0404 | 0.95% | [-0.0140, 0.0959] | 1 |
| A | GraphSAGE-TEG-Concat | 0.0709 | 1.65% | [-0.0170, 0.1369] | 0.5273 |
| A | GraphSAGE-TEG-Gate | -0.0085 | -0.20% | [-0.0714, 0.0578] | 1 |
| A | SGFormer-adapted | 0.1059 | 2.45% | [0.0192, 0.1857] | 0.3867 |
| A | SGFormer-TEG-Concat | 0.0264 | 0.62% | [-0.0321, 0.0948] | 1 |
| A | SGFormer-TEG-Gate | 0.0222 | 0.52% | [-0.0510, 0.0978] | 1 |
| A | Gradformer-adapted | 0.3140 | 6.92% | [0.2238, 0.4075] | 0.02148 |
| A | TEG-only | 0.1375 | 3.15% | [0.0768, 0.1944] | 0.03125 |
| A | Stable-Tail w/o Tail Loss | 0.1247 | 2.87% | [0.0937, 0.1558] | 0.02148 |
| B | GCN | 0.1855 | 3.28% | [0.0797, 0.3016] | 0.08789 |
| B | GAT | 0.4617 | 7.79% | [0.3266, 0.5698] | 0.03906 |
| B | GraphSAGE | 0.1031 | 1.85% | [-0.0300, 0.2454] | 1 |
| B | GraphSAGE-TEG-Concat | 0.1312 | 2.34% | [0.0151, 0.2381] | 0.5156 |
| B | GraphSAGE-TEG-Gate | 0.0332 | 0.60% | [-0.0671, 0.1364] | 1 |
| B | SGFormer-adapted | 0.0215 | 0.39% | [-0.0716, 0.1166] | 1 |
| B | SGFormer-TEG-Concat | 0.0446 | 0.81% | [-0.0749, 0.1831] | 1 |
| B | SGFormer-TEG-Gate | -0.0260 | -0.48% | [-0.1149, 0.0740] | 1 |
| B | Gradformer-adapted | 0.3294 | 5.68% | [0.1832, 0.4956] | 0.02148 |
| B | TEG-only | 0.1009 | 1.81% | [0.0119, 0.1893] | 0.5879 |
| B | Stable-Tail w/o Tail Loss | 0.0772 | 1.39% | [-0.0251, 0.1686] | 0.7852 |

## Paired significance at Risk@20

Positive difference means Stable-Tail GNN has lower common risk.

| Set | Baseline | Baseline - Stable | Relative reduction | 95% CI | Holm p |
|---|---|---:|---:|---:|---:|
| A | GCN | 0.2006 | 6.07% | [-0.0865, 0.5758] | 1 |
| A | GAT | 0.2713 | 8.03% | [0.0663, 0.5452] | 0.2461 |
| A | GraphSAGE | 0.0833 | 2.61% | [-0.1036, 0.3529] | 1 |
| A | GraphSAGE-TEG-Concat | 0.2897 | 8.53% | [-0.0205, 0.6475] | 1 |
| A | GraphSAGE-TEG-Gate | 0.1335 | 4.12% | [-0.0958, 0.4588] | 1 |
| A | SGFormer-adapted | 0.2995 | 8.79% | [0.0369, 0.5898] | 1 |
| A | SGFormer-TEG-Concat | 0.1608 | 4.92% | [-0.0940, 0.4512] | 1 |
| A | SGFormer-TEG-Gate | 0.2333 | 6.99% | [-0.0518, 0.5912] | 1 |
| A | Gradformer-adapted | 0.7203 | 18.82% | [0.4078, 1.0343] | 0.04297 |
| A | TEG-only | 0.2504 | 7.46% | [-0.0374, 0.6148] | 1 |
| A | Stable-Tail w/o Tail Loss | 0.2160 | 6.50% | [0.0425, 0.4757] | 0.1953 |
| B | GCN | 0.7982 | 13.66% | [0.3349, 1.2465] | 0.1367 |
| B | GAT | 0.9112 | 15.30% | [0.4670, 1.3699] | 0.1074 |
| B | GraphSAGE | 0.0356 | 0.70% | [-0.5386, 0.6115] | 1 |
| B | GraphSAGE-TEG-Concat | 0.3965 | 7.29% | [0.0019, 0.8452] | 1 |
| B | GraphSAGE-TEG-Gate | 0.3249 | 6.05% | [-0.1972, 0.8465] | 1 |
| B | SGFormer-adapted | -0.0907 | -1.83% | [-0.4440, 0.2761] | 1 |
| B | SGFormer-TEG-Concat | 0.0944 | 1.84% | [-0.6142, 0.8039] | 1 |
| B | SGFormer-TEG-Gate | -0.1839 | -3.78% | [-0.6623, 0.2281] | 1 |
| B | Gradformer-adapted | 0.6231 | 10.99% | [0.1508, 1.0474] | 0.334 |
| B | TEG-only | 0.6008 | 10.64% | [0.1800, 1.0338] | 0.334 |
| B | Stable-Tail w/o Tail Loss | 0.4549 | 8.27% | [0.0141, 0.9444] | 1 |

## Interpretation guardrails

- Node classification and downstream route safety are related but distinct objectives.
- Cross-model route claims must use the common-risk tables, not each model's self-evaluation scale.
- The budget selector chooses the lowest-common-risk observed beta candidate feasible under each cost budget.
- Statistical tests pair identical model-seed indices; bootstrap intervals use 10,000 resamples by default.

## Gate-targeted paired significance

Positive `reference - target` means the target model is lower/better. Holm correction is applied within each Set × metric block over the six targeted Gate comparisons.

| Set | Metric | Target | Reference | Reference - target | Relative | 95% CI | Holm p |
|---|---|---|---|---:|---:|---:|---:|
| A | common_risk_aubrc | SGFormer-TEG-Gate | SGFormer-TEG-Concat | 0.0041 | 0.10% | [-0.0708, 0.0863] | 1 |
| A | common_risk_aubrc | SGFormer-TEG-Gate | SGFormer-adapted | 0.0836 | 1.93% | [-0.0044, 0.1736] | 0.7852 |
| A | common_risk_aubrc | SGFormer-TEG-Gate | Stable-Tail GNN | -0.0222 | -0.53% | [-0.0971, 0.0504] | 1 |
| A | common_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0794 | 1.85% | [-0.0141, 0.1679] | 0.7852 |
| A | common_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE | 0.0489 | 1.15% | [-0.0019, 0.1096] | 0.7852 |
| A | common_risk_aubrc | GraphSAGE-TEG-Gate | Stable-Tail GNN | 0.0085 | 0.20% | [-0.0590, 0.0725] | 1 |
| A | cvar90_aubrc | SGFormer-TEG-Gate | SGFormer-TEG-Concat | 0.0006 | 0.51% | [-0.0021, 0.0035] | 1 |
| A | cvar90_aubrc | SGFormer-TEG-Gate | SGFormer-adapted | 0.0042 | 3.67% | [0.0011, 0.0074] | 0.293 |
| A | cvar90_aubrc | SGFormer-TEG-Gate | Stable-Tail GNN | 0.0004 | 0.34% | [-0.0026, 0.0034] | 1 |
| A | cvar90_aubrc | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0047 | 4.02% | [0.0010, 0.0081] | 0.293 |
| A | cvar90_aubrc | GraphSAGE-TEG-Gate | GraphSAGE | 0.0024 | 2.10% | [0.0002, 0.0050] | 0.293 |
| A | cvar90_aubrc | GraphSAGE-TEG-Gate | Stable-Tail GNN | 0.0003 | 0.26% | [-0.0022, 0.0028] | 1 |
| A | load_risk_aubrc | SGFormer-TEG-Gate | SGFormer-TEG-Concat | -0.0190 | -0.87% | [-0.0643, 0.0290] | 1 |
| A | load_risk_aubrc | SGFormer-TEG-Gate | SGFormer-adapted | -0.0054 | -0.25% | [-0.0790, 0.0701] | 1 |
| A | load_risk_aubrc | SGFormer-TEG-Gate | Stable-Tail GNN | 0.0062 | 0.28% | [-0.0409, 0.0575] | 1 |
| A | load_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0394 | 1.77% | [-0.0076, 0.0840] | 0.9609 |
| A | load_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE | 0.0216 | 0.98% | [-0.0287, 0.0693] | 1 |
| A | load_risk_aubrc | GraphSAGE-TEG-Gate | Stable-Tail GNN | 0.0247 | 1.12% | [-0.0195, 0.0658] | 1 |
| A | average_common_risk_at_b | SGFormer-TEG-Gate | SGFormer-TEG-Concat | -0.0048 | -0.14% | [-0.0956, 0.0866] | 1 |
| A | average_common_risk_at_b | SGFormer-TEG-Gate | SGFormer-adapted | 0.0458 | 1.33% | [-0.1105, 0.1973] | 1 |
| A | average_common_risk_at_b | SGFormer-TEG-Gate | Stable-Tail GNN | -0.0123 | -0.36% | [-0.1298, 0.1188] | 1 |
| A | average_common_risk_at_b | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0949 | 2.81% | [0.0255, 0.1684] | 0.2578 |
| A | average_common_risk_at_b | GraphSAGE-TEG-Gate | GraphSAGE | 0.1333 | 3.90% | [0.0617, 0.2021] | 0.1172 |
| A | average_common_risk_at_b | GraphSAGE-TEG-Gate | Stable-Tail GNN | 0.1102 | 3.25% | [0.0241, 0.2040] | 0.2441 |
| B | common_risk_aubrc | SGFormer-TEG-Gate | SGFormer-TEG-Concat | 0.0706 | 1.28% | [-0.0653, 0.2251] | 1 |
| B | common_risk_aubrc | SGFormer-TEG-Gate | SGFormer-adapted | 0.0475 | 0.87% | [-0.0594, 0.1593] | 1 |
| B | common_risk_aubrc | SGFormer-TEG-Gate | Stable-Tail GNN | 0.0260 | 0.48% | [-0.0816, 0.1150] | 1 |
| B | common_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0980 | 1.75% | [-0.0069, 0.2125] | 0.7852 |
| B | common_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE | 0.0699 | 1.25% | [-0.0731, 0.2155] | 0.9668 |
| B | common_risk_aubrc | GraphSAGE-TEG-Gate | Stable-Tail GNN | -0.0332 | -0.61% | [-0.1363, 0.0644] | 1 |
| B | cvar90_aubrc | SGFormer-TEG-Gate | SGFormer-TEG-Concat | 0.0015 | 1.05% | [-0.0034, 0.0072] | 1 |
| B | cvar90_aubrc | SGFormer-TEG-Gate | SGFormer-adapted | 0.0020 | 1.41% | [-0.0019, 0.0060] | 1 |
| B | cvar90_aubrc | SGFormer-TEG-Gate | Stable-Tail GNN | 0.0005 | 0.37% | [-0.0035, 0.0039] | 1 |
| B | cvar90_aubrc | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0024 | 1.66% | [-0.0015, 0.0064] | 1 |
| B | cvar90_aubrc | GraphSAGE-TEG-Gate | GraphSAGE | 0.0023 | 1.61% | [-0.0014, 0.0063] | 1 |
| B | cvar90_aubrc | GraphSAGE-TEG-Gate | Stable-Tail GNN | -0.0014 | -1.01% | [-0.0050, 0.0019] | 1 |
| B | load_risk_aubrc | SGFormer-TEG-Gate | SGFormer-TEG-Concat | 0.0318 | 1.17% | [-0.0512, 0.1187] | 0.9844 |
| B | load_risk_aubrc | SGFormer-TEG-Gate | SGFormer-adapted | 0.0558 | 2.04% | [-0.0034, 0.1154] | 0.3926 |
| B | load_risk_aubrc | SGFormer-TEG-Gate | Stable-Tail GNN | 0.0436 | 1.60% | [-0.0022, 0.0836] | 0.2578 |
| B | load_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0988 | 3.54% | [0.0364, 0.1601] | 0.08203 |
| B | load_risk_aubrc | GraphSAGE-TEG-Gate | GraphSAGE | 0.1059 | 3.78% | [0.0187, 0.1892] | 0.1855 |
| B | load_risk_aubrc | GraphSAGE-TEG-Gate | Stable-Tail GNN | 0.0306 | 1.12% | [-0.0290, 0.0883] | 0.9844 |
| B | average_common_risk_at_b | SGFormer-TEG-Gate | SGFormer-TEG-Concat | 0.0725 | 1.52% | [-0.1302, 0.2762] | 1 |
| B | average_common_risk_at_b | SGFormer-TEG-Gate | SGFormer-adapted | 0.1499 | 3.09% | [-0.0217, 0.3156] | 1 |
| B | average_common_risk_at_b | SGFormer-TEG-Gate | Stable-Tail GNN | 0.0199 | 0.42% | [-0.1711, 0.1823] | 1 |
| B | average_common_risk_at_b | GraphSAGE-TEG-Gate | GraphSAGE-TEG-Concat | 0.0799 | 1.64% | [-0.0782, 0.2566] | 1 |
| B | average_common_risk_at_b | GraphSAGE-TEG-Gate | GraphSAGE | 0.0956 | 1.96% | [-0.0900, 0.2569] | 1 |
| B | average_common_risk_at_b | GraphSAGE-TEG-Gate | Stable-Tail GNN | -0.0586 | -1.24% | [-0.2034, 0.0784] | 1 |
