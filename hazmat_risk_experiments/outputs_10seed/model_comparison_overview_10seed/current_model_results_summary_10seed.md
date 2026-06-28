# Current Model Results Summary (10seed)

This file summarizes the current 10seed results across node risk evaluation, risk-matrix behavior, OD path validation, PyVRP common-evaluator validation, and tail/concentration-aware CVRP extensions.

## 1. Node Risk Evaluation

### Split A

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |
|---|---:|---:|---:|---:|---:|---:|
| MLP | 0.3434 | 1.7610 | 0.3372 | 0.3843 | 0.3105 | 0.6157 |
| GCN | 0.3535 | 1.2677 | 0.2795 | 0.2392 | 0.3920 | 0.7608 |
| Weighted-GCN | 0.3560 | 1.6477 | 0.3205 | 0.3647 | 0.3517 | 0.6353 |
| Edge-GAT | 0.3420 | 1.3211 | 0.2753 | 0.2471 | 0.3745 | 0.7529 |
| TEG-low | 0.3446 | 1.6438 | 0.3393 | 0.3471 | 0.3571 | 0.6529 |
| Stable-Tail GNN | 0.2997 | 1.1885 | 0.3234 | 0.2882 | 0.3946 | 0.7118 |
| Stable-Tail UA-GNN | 0.2427 | 1.2322 | 0.2866 | 0.2686 | 0.3742 | 0.7314 |

### Split B

| Model | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN |
|---|---:|---:|---:|---:|---:|---:|
| MLP | 0.2843 | 1.7219 | 0.3211 | 0.3385 | 0.3556 | 0.6615 |
| GCN | 0.2978 | 1.3308 | 0.2431 | 0.2115 | 0.3560 | 0.7885 |
| Weighted-GCN | 0.2811 | 1.6176 | 0.2911 | 0.2923 | 0.3470 | 0.7077 |
| Edge-GAT | 0.2891 | 1.3384 | 0.2580 | 0.2077 | 0.3313 | 0.7923 |
| TEG-low | 0.2683 | 1.6078 | 0.3019 | 0.2692 | 0.3502 | 0.7308 |
| Stable-Tail GNN | 0.2776 | 1.2089 | 0.2704 | 0.2423 | 0.3716 | 0.7577 |
| Stable-Tail UA-GNN | 0.2422 | 1.2625 | 0.2675 | 0.2538 | 0.3750 | 0.7462 |

## 2. UA-GNN Uncertainty Metrics

| Split | Model | NLL | Brier | ECE | Err-Unc Corr | Error Unc | Correct Unc | High FN Unc |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | Stable-Tail UA-GNN | 1.1291 | 0.5092 | 0.0778 | 0.0846 | 2.1628 | 2.0743 | 2.1466 |
| B | Stable-Tail UA-GNN | 1.1380 | 0.5024 | 0.0965 | 0.0989 | 2.2325 | 2.1358 | 2.2176 |

Interpretation: UA-GNN gives positive error-uncertainty correlation and assigns higher uncertainty to wrong predictions than correct predictions. Its node classification metrics are not uniformly better than Stable-Tail GNN, so its strongest role is uncertainty-aware downstream routing.

## 3. Risk Matrix Distribution

| Risk Matrix | Mean | P50 | P75 | P90 | P95 | P99 | TailGap | Max | Std |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Stable-Tail GNN | 0.0160 | 0.0016 | 0.0036 | 0.0082 | 0.0626 | 0.4137 | 0.3511 | 0.8689 | 0.0737 |
| Stable-Tail UA-GNN tau=0 | 0.0175 | 0.0018 | 0.0038 | 0.0076 | 0.0848 | 0.4163 | 0.3315 | 0.8519 | 0.0745 |
| Stable-Tail UA-GNN tau=0.25 | 0.0274 | 0.0034 | 0.0058 | 0.0098 | 0.1686 | 0.5417 | 0.3731 | 1.0000 | 0.1045 |

Interpretation: tau=0.25 increases middle/high risk sensitivity and keeps a strong tail gap. It is more conservative than Stable-Tail GNN.

## 4. OD Fixed150 CVaR-Risk Downstream Validation

| Model | Seeds | Hop Increase | Total Risk Red. | CVaR90 Red. | MaxRisk Red. | RE Red. |
|---|---:|---:|---:|---:|---:|---:|
| GCN | 10 | 10.13 +/- 0.70% | 84.49 +/- 0.39% | 90.11 +/- 0.25% | 90.63 +/- 0.31% | 92.02 +/- 0.23% |
| TEG-low | 10 | 10.80 +/- 0.94% | 81.20 +/- 0.71% | 89.52 +/- 0.26% | 90.60 +/- 0.35% | 92.21 +/- 0.26% |
| Stable-Tail GNN | 10 | 10.23 +/- 0.72% | 85.01 +/- 0.41% | 90.05 +/- 0.27% | 90.78 +/- 0.27% | 91.72 +/- 0.50% |
| Stable-Tail UA-GNN tau=0 | 10 | 9.52 +/- 0.48% | 84.67 +/- 0.67% | 89.87 +/- 0.35% | 90.52 +/- 0.37% | 91.66 +/- 0.49% |
| Stable-Tail UA-GNN tau=0.25 | 10 | 8.81 +/- 0.24% | 83.67 +/- 0.52% | 90.32 +/- 0.25% | 90.42 +/- 0.31% | 92.18 +/- 0.35% |
| Weighted-GCN | 10 | 10.77 +/- 0.70% | 80.86 +/- 1.07% | 89.49 +/- 0.44% | 90.35 +/- 0.46% | 92.14 +/- 0.33% |
| Edge-GAT | 10 | 9.98 +/- 0.55% | 84.28 +/- 0.44% | 89.85 +/- 0.37% | 90.44 +/- 0.34% | 91.85 +/- 0.44% |
| Ensemble-4 | 10 | 10.47 +/- 0.70% | 82.87 +/- 0.58% | 89.76 +/- 0.28% | 90.47 +/- 0.29% | 91.82 +/- 0.38% |
| Fusion-rho025 | 10 | 10.31 +/- 0.84% | 83.78 +/- 0.39% | 89.97 +/- 0.25% | 90.56 +/- 0.29% | 91.93 +/- 0.22% |

Interpretation: Stable-Tail GNN gives the best total-risk reduction in OD validation. UA-GNN tau=0.25 gives the best CVaR90 and RE reduction while requiring the lowest hop increase among the Stable-Tail variants.

## 5. PyVRP beta=1 Common Evaluator

### Set A

| Model | Seeds | Global Risk | CVaR90 | Max Vehicle Risk | Edge Gini | Top10 Share |
|---|---:|---:|---:|---:|---:|---:|
| GCN | 10 | 3.1467 +/- 0.0693 | 0.0793 +/- 0.0061 | 1.0587 +/- 0.1116 | 0.7486 +/- 0.0041 | 74.75 +/- 0.57% |
| TEG-low | 10 | 3.1799 +/- 0.1427 | 0.0771 +/- 0.0055 | 0.9614 +/- 0.0453 | 0.7500 +/- 0.0087 | 74.93 +/- 1.18% |
| Stable-Tail GNN | 10 | 3.2668 +/- 0.1417 | 0.0828 +/- 0.0054 | 1.0346 +/- 0.0790 | 0.7546 +/- 0.0069 | 75.60 +/- 0.96% |
| Stable-Tail UA-GNN tau=0.25 | 10 | 3.0480 +/- 0.0353 | 0.0726 +/- 0.0033 | 1.0672 +/- 0.0961 | 0.7445 +/- 0.0028 | 74.07 +/- 0.34% |
| Weighted-GCN | 10 | 3.2307 +/- 0.0787 | 0.0792 +/- 0.0034 | 1.0036 +/- 0.1317 | 0.7537 +/- 0.0055 | 75.48 +/- 0.72% |
| Edge-GAT | 10 | 3.1673 +/- 0.0833 | 0.0789 +/- 0.0068 | 1.0759 +/- 0.1000 | 0.7503 +/- 0.0056 | 74.91 +/- 0.68% |
| Ensemble-4 | 10 | 3.1785 +/- 0.0662 | 0.0778 +/- 0.0055 | 1.0171 +/- 0.0765 | 0.7501 +/- 0.0034 | 74.94 +/- 0.46% |
| Fusion-rho025 | 10 | 3.1892 +/- 0.0808 | 0.0814 +/- 0.0060 | 1.0556 +/- 0.0753 | 0.7514 +/- 0.0037 | 75.10 +/- 0.56% |

### Set B

| Model | Seeds | Global Risk | CVaR90 | Max Vehicle Risk | Edge Gini | Top10 Share |
|---|---:|---:|---:|---:|---:|---:|
| GCN | 10 | 4.0781 +/- 0.1923 | 0.0980 +/- 0.0073 | 1.3761 +/- 0.0489 | 0.7825 +/- 0.0082 | 78.62 +/- 1.04% |
| TEG-low | 10 | 4.0793 +/- 0.2017 | 0.0968 +/- 0.0057 | 1.3986 +/- 0.1125 | 0.7794 +/- 0.0089 | 78.48 +/- 1.16% |
| Stable-Tail GNN | 10 | 4.0353 +/- 0.2035 | 0.0946 +/- 0.0046 | 1.3827 +/- 0.0774 | 0.7777 +/- 0.0075 | 78.22 +/- 1.01% |
| Stable-Tail UA-GNN tau=0.25 | 10 | 3.8551 +/- 0.1635 | 0.0927 +/- 0.0055 | 1.3423 +/- 0.0972 | 0.7732 +/- 0.0067 | 77.46 +/- 0.95% |
| Weighted-GCN | 10 | 4.2547 +/- 0.2258 | 0.1006 +/- 0.0065 | 1.4097 +/- 0.0906 | 0.7848 +/- 0.0083 | 79.29 +/- 1.13% |
| Edge-GAT | 10 | 4.3678 +/- 0.3777 | 0.1052 +/- 0.0102 | 1.3975 +/- 0.0943 | 0.7916 +/- 0.0141 | 79.83 +/- 1.67% |
| Ensemble-4 | 10 | 4.1240 +/- 0.1242 | 0.0991 +/- 0.0050 | 1.3737 +/- 0.0733 | 0.7827 +/- 0.0053 | 78.85 +/- 0.70% |
| Fusion-rho025 | 10 | 4.0672 +/- 0.1754 | 0.0976 +/- 0.0062 | 1.3815 +/- 0.0827 | 0.7820 +/- 0.0080 | 78.63 +/- 1.03% |

Interpretation: Under beta=1 common evaluation, Stable-Tail UA-GNN tau=0.25 is the best overall PyVRP risk-matrix model for both Set A and Set B.

## 6. Tail + Concentration CVRP Extensions

| Set | Method | beta | lambda | Cost inc. | Risk Red. | Global Risk | CVaR90 | Max Vehicle Risk | Edge Gini | Top10 Share |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | Stable-Tail-TC-lite | 1.5 | 1.0 | 30.72% | 68.51% | 2.4550 | 0.0440 | 0.8820 | 0.6886 | 66.88% |
| A | Stable-Tail-UA-GNN-TC-lite | 1.5 | 1.0 | 38.07% | 71.13% | 2.2564 | 0.0384 | 0.8638 | 0.6661 | 64.00% |
| B | Stable-Tail-TC-lite | 1.5 | 1.0 | 36.28% | 62.40% | 3.1579 | 0.0689 | 1.1104 | 0.7363 | 72.19% |
| B | Stable-Tail-UA-GNN-TC-lite | 1.5 | 1.0 | 48.67% | 64.52% | 2.9796 | 0.0626 | 1.1641 | 0.7237 | 70.42% |
| A | Stable-Tail-TC | 2.0 | 1.0 | 34.83% | 70.07% | 2.3526 | 0.0406 | 0.8703 | 0.6765 | 65.37% |
| A | Stable-Tail-UA-GNN-TC | 2.0 | 1.0 | 43.66% | 71.06% | 2.2617 | 0.0386 | 0.8764 | 0.6661 | 63.98% |
| B | Stable-Tail-TC | 2.0 | 1.0 | 41.61% | 62.57% | 3.1423 | 0.0670 | 1.1144 | 0.7358 | 72.05% |
| B | Stable-Tail-UA-GNN-TC | 2.0 | 1.0 | 56.19% | 64.46% | 2.9847 | 0.0620 | 1.1348 | 0.7244 | 70.44% |

Interpretation: UA-GNN-TC improves risk, CVaR90, Edge Gini, and Top10 Share, but increases cost by more than the 3-5 percentage-point tolerance. It is best framed as a safety-prioritized robust extension, not as the default final TC method.

## 7. Recommended Positioning

1. Node risk evaluation:
   - Stable-Tail GNN has the best MAE among the graph-tail models and strong PR-AUC.
   - TEG-low and Weighted-GCN improve high-risk recall but with larger MAE.
   - Stable-Tail UA-GNN adds uncertainty information rather than pure classification superiority.

2. OD validation:
   - Stable-Tail GNN is strongest for total-risk reduction.
   - Stable-Tail UA-GNN tau=0.25 is strongest for CVaR90/RE reduction with lower hop increase.

3. PyVRP beta=1 common evaluator:
   - Stable-Tail UA-GNN tau=0.25 is the best current model for Global Risk, CVaR90, Edge Gini, and Top10 Share in both Set A and Set B.

4. Final method choice:
   - Main final method: Stable-Tail-TC.
   - Robust safety-prioritized extension: Stable-Tail UA-GNN-TC.
   - If the paper emphasizes safety over cost, UA-GNN-TC can be presented as the conservative variant.
