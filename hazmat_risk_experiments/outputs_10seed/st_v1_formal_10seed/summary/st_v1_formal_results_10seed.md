# ST-v1 Formal 10seed Results

- Node MAE: 1.2085 +/- 0.0584
- Node PR-AUC: 0.3713 +/- 0.0548
- Recall@6-8: 0.2423 +/- 0.0943
- Risk P95/P99/TailGap: 0.0626 / 0.4137 / 0.3511
- OD total-risk/CVaR90/MaxRisk reduction: 85.01% / 90.05% / 90.78%

## PyVRP Self Evaluation

| Method | Set | Cost increase | Risk reduction | Global risk | CVaR90 | Edge Gini | Top10 share |
|---|---|---:|---:|---:|---:|---:|---:|
| beta1 | A | 17.17% | 63.50% | 2.7855 | 0.0663 | 0.7957 | 76.57% |
| beta1 | B | 19.87% | 59.69% | 3.3801 | 0.0794 | 0.8182 | 78.87% |
| TC-lite eta0.7 beta1.5 lambda1 | A | 30.74% | 74.04% | 1.9859 | 0.0375 | 0.7273 | 66.27% |
| TC-lite eta0.7 beta1.5 lambda1 | B | 36.29% | 68.71% | 2.6276 | 0.0546 | 0.7843 | 73.11% |

## Common Evaluation

| Method | Set | Global risk | CVaR90 | Max vehicle risk | Edge Gini | Top10 share |
|---|---|---:|---:|---:|---:|---:|
| beta1 | A | 3.2508 | 0.0822 | 1.0338 | 0.7539 | 75.50% |
| beta1 | B | 4.0300 | 0.0946 | 1.3826 | 0.7775 | 78.18% |
| TC-lite eta0.7 beta1.5 lambda1 | A | 2.4601 | 0.0435 | 0.8849 | 0.6892 | 66.95% |
| TC-lite eta0.7 beta1.5 lambda1 | B | 3.1586 | 0.0694 | 1.1224 | 0.7363 | 72.19% |

## Load-Aware Common Evaluation

| Method | Set | Load risk | Load CVaR90 | Max vehicle load risk | Load edge Gini | Load Top10 share |
|---|---|---:|---:|---:|---:|---:|
| beta1 | A | 1.6100 | 0.0451 | 0.5604 | 0.8030 | 76.68% |
| beta1 | B | 1.9739 | 0.0519 | 0.7304 | 0.8161 | 78.46% |
| TC-lite eta0.7 beta1.5 lambda1 | A | 1.2132 | 0.0288 | 0.4517 | 0.7477 | 69.03% |
| TC-lite eta0.7 beta1.5 lambda1 | B | 1.6149 | 0.0386 | 0.6044 | 0.7875 | 74.07% |
