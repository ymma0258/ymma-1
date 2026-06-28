# Stable-Tail RC-GNN Post-hoc Summary

## Risk Matrix Distribution

| Delta | Mean | P50 | P75 | P90 | P95 | P99 | TailGap | Max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.03 | 0.0162 | 0.0016 | 0.0036 | 0.0083 | 0.0631 | 0.4163 | 0.3532 | 0.8727 |
| 0.05 | 0.0163 | 0.0016 | 0.0037 | 0.0083 | 0.0635 | 0.4181 | 0.3545 | 0.8753 |
| 0.08 | 0.0164 | 0.0017 | 0.0037 | 0.0084 | 0.0642 | 0.4205 | 0.3563 | 0.8792 |

Targets: Mean 0.018-0.023, P95 0.085-0.120, P99 0.430-0.500, TailGap >= 0.340.

## OD Fixed150 CVaR-Risk

| Delta | Hop Increase | Total Risk Red. | CVaR90 Red. | MaxRisk Red. | RE Red. |
|---:|---:|---:|---:|---:|---:|
| 0.03 | 10.24% +/- 0.72% | 84.99% +/- 0.41% | 90.04% +/- 0.26% | 90.78% +/- 0.27% | 91.73% +/- 0.51% |
| 0.05 | 10.24% +/- 0.72% | 84.98% +/- 0.41% | 90.04% +/- 0.26% | 90.77% +/- 0.27% | 91.73% +/- 0.51% |
| 0.08 | 10.24% +/- 0.72% | 84.96% +/- 0.42% | 90.04% +/- 0.26% | 90.76% +/- 0.27% | 91.75% +/- 0.51% |

## PyVRP beta=1 Common Evaluator

| Delta | Set | Cost inc. | Risk Red. | Global Risk | CVaR90 | Max Vehicle Risk | Edge Gini | Top10 Share |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 0.03 | A | 17.21% +/- 1.50% | 61.00% +/- 2.37% | 3.2594 +/- 0.1803 | 0.0810 +/- 0.0067 | 1.0757 +/- 0.0882 | 0.7538 +/- 0.0083 | 75.45% +/- 1.16% |
| 0.03 | B | 20.00% +/- 1.65% | 51.19% +/- 1.76% | 4.0918 +/- 0.1477 | 0.0952 +/- 0.0048 | 1.3974 +/- 0.0737 | 0.7793 +/- 0.0061 | 78.47% +/- 0.77% |
| 0.05 | A | 17.20% +/- 1.50% | 58.38% +/- 3.12% | 3.2764 +/- 0.2040 | 0.0833 +/- 0.0076 | 1.1002 +/- 0.0946 | 0.7560 +/- 0.0103 | 75.71% +/- 1.31% |
| 0.05 | B | 19.86% +/- 1.71% | 52.49% +/- 2.38% | 3.9896 +/- 0.1995 | 0.0929 +/- 0.0057 | 1.3532 +/- 0.1085 | 0.7761 +/- 0.0082 | 78.00% +/- 1.13% |
| 0.08 | A | 17.20% +/- 1.52% | 58.29% +/- 1.83% | 3.2516 +/- 0.1428 | 0.0812 +/- 0.0043 | 1.0699 +/- 0.1053 | 0.7538 +/- 0.0078 | 75.51% +/- 1.07% |
| 0.08 | B | 19.96% +/- 1.71% | 52.11% +/- 2.43% | 4.0219 +/- 0.2042 | 0.0944 +/- 0.0051 | 1.3995 +/- 0.1005 | 0.7788 +/- 0.0080 | 78.29% +/- 1.10% |

## Screening Decision

- delta=0.03: Set A Global Risk < 3.1467 = False; Set B Global Risk < 4.0353 = False; fairness not worse than Stable-Tail GNN = False.
- delta=0.05: Set A Global Risk < 3.1467 = False; Set B Global Risk < 4.0353 = True; fairness not worse than Stable-Tail GNN = False.
- delta=0.08: Set A Global Risk < 3.1467 = False; Set B Global Risk < 4.0353 = True; fairness not worse than Stable-Tail GNN = False.

Conclusion: delta=0.03/0.05/0.08 are too mild to move the risk matrix into the target P95 band or improve OD/PyVRP meaningfully. Do not proceed to TC for these deltas.
