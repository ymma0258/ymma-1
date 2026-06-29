# Stable-Tail UA-GNN 3seed Pretest Summary

All outputs are isolated under `outputs_10seed/stable_tail_ua_pretest_3seed/`; existing formal 10seed results were not overwritten.

## Node Risk Evaluation

| Split | Model | runs | Macro-F1 | MAE | QWK | Recall@6-8 | PR-AUC | High FN | NLL | Brier | ECE | Err-Unc Corr | Error Unc | Correct Unc | High FN Unc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | Stable-Tail UA-GNN | 3 | 0.2512 | 1.2122 | 0.3009 | 0.2876 | 0.3791 | 0.7124 | 1.1366 | 0.5033 | 0.0758 | 0.0174 | 2.1455 | 2.1116 | 2.1474 |
| B | Stable-Tail UA-GNN | 3 | 0.2501 | 1.2175 | 0.2999 | 0.2821 | 0.3944 | 0.7179 | 1.1288 | 0.4830 | 0.0811 | 0.0419 | 2.2247 | 2.1741 | 2.2684 |

## OD fixed150 CVaR-risk

| Model | tau | runs | Hop Increase mean | Hop Increase std | Total Risk Red mean | Total Risk Red std | CVaR90 Red mean | CVaR90 Red std | MaxRisk Red mean | MaxRisk Red std | RE Red mean | RE Red std |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Stable-Tail UA-GNN | 0.0 | 3 | 9.54% | 0.67% | 85.04% | 0.79% | 89.95% | 0.49% | 90.65% | 0.50% | 91.82% | 0.31% |
| Stable-Tail UA-GNN | 0.25 | 3 | 8.77% | 0.15% | 83.93% | 0.42% | 90.35% | 0.26% | 90.48% | 0.22% | 92.28% | 0.21% |
| Stable-Tail UA-GNN | 0.5 | 3 | 7.69% | 0.87% | 82.69% | 0.50% | 90.87% | 0.22% | 90.76% | 0.19% | 92.60% | 0.41% |

## PyVRP beta=1 Common Evaluator

| Set | Model | tau | runs | Risk Reduction mean | Risk Reduction std | Global Risk mean | Global Risk std | CVaR90 mean | CVaR90 std | Max Vehicle Risk mean | Max Vehicle Risk std | Edge Gini mean | Edge Gini std | Top10 Share mean | Top10 Share std |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | Stable-Tail UA-GNN | 0.0 | 3 | 58.33% | 1.10% | 3.2101 | 0.0848 | 0.0762 | 0.0064 | 1.0000 | 0.1206 | 0.7537 | 0.0041 | 75.37% | 0.66% |
| A | Stable-Tail UA-GNN | 0.25 | 3 | 60.39% | 2.69% | 3.0512 | 0.2072 | 0.0701 | 0.0131 | 1.0759 | 0.0919 | 0.7453 | 0.0135 | 74.07% | 1.74% |
| A | Stable-Tail UA-GNN | 0.5 | 3 | 59.42% | 1.01% | 3.1260 | 0.0781 | 0.0713 | 0.0104 | 1.0623 | 0.1044 | 0.7483 | 0.0070 | 74.47% | 0.87% |
| B | Stable-Tail UA-GNN | 0.0 | 3 | 49.94% | 1.65% | 4.0416 | 0.1334 | 0.0953 | 0.0057 | 1.4038 | 0.1057 | 0.7819 | 0.0037 | 78.65% | 0.54% |
| B | Stable-Tail UA-GNN | 0.25 | 3 | 52.56% | 3.97% | 3.8306 | 0.3205 | 0.0922 | 0.0104 | 1.3190 | 0.1280 | 0.7719 | 0.0146 | 77.35% | 2.08% |
| B | Stable-Tail UA-GNN | 0.5 | 3 | 52.53% | 7.74% | 3.8324 | 0.6252 | 0.0925 | 0.0184 | 1.3258 | 0.2514 | 0.7724 | 0.0306 | 77.16% | 3.96% |