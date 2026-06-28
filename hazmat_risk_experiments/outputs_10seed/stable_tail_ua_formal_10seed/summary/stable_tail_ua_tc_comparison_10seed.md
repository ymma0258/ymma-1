# Stable-Tail UA-GNN-TC Comparison (10seed)

Common evaluator: Ensemble-4 10seed floor_0.01 risk matrix. Cost inc. is from the solved objective summary; risk metrics are common-evaluator metrics.

| Set | Method | beta | lambda | Cost inc. | Risk red. | Global Risk | CVaR90 | Max Vehicle Risk | Edge Gini | Top10 Share | Delta cost pp | Delta Risk | Delta CVaR90 | Delta Edge Gini | Delta Top10 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | Stable-Tail-TC-lite | 1.5 | 1.0 | 30.72% | 68.51% | 2.4550 | 0.0440 | 0.8820 | 0.6886 | 66.88% |  |  |  |  |  |
| B | Stable-Tail-TC-lite | 1.5 | 1.0 | 36.28% | 62.40% | 3.1579 | 0.0689 | 1.1104 | 0.7363 | 72.19% |  |  |  |  |  |
| A | Stable-Tail-UA-GNN-TC-lite | 1.5 | 1.0 | 38.07% | 71.13% | 2.2564 | 0.0384 | 0.8638 | 0.6661 | 64.00% | +7.35pp | -0.1986 | -0.0055 | -0.0225 | -2.88pp |
| B | Stable-Tail-UA-GNN-TC-lite | 1.5 | 1.0 | 48.67% | 64.52% | 2.9796 | 0.0626 | 1.1641 | 0.7237 | 70.42% | +12.39pp | -0.1783 | -0.0063 | -0.0127 | -1.78pp |
| A | Stable-Tail-TC | 2.0 | 1.0 | 34.83% | 70.07% | 2.3526 | 0.0406 | 0.8703 | 0.6765 | 65.37% |  |  |  |  |  |
| B | Stable-Tail-TC | 2.0 | 1.0 | 41.61% | 62.57% | 3.1423 | 0.0670 | 1.1144 | 0.7358 | 72.05% |  |  |  |  |  |
| A | Stable-Tail-UA-GNN-TC | 2.0 | 1.0 | 43.66% | 71.06% | 2.2617 | 0.0386 | 0.8764 | 0.6661 | 63.98% | +8.84pp | -0.0908 | -0.0020 | -0.0105 | -1.39pp |
| B | Stable-Tail-UA-GNN-TC | 2.0 | 1.0 | 56.19% | 64.46% | 2.9847 | 0.0620 | 1.1348 | 0.7244 | 70.44% | +14.58pp | -0.1576 | -0.0050 | -0.0114 | -1.61pp |

## Decision Notes

- Set A, beta=1.5: UA lower Global Risk=True, lower CVaR90=True, fairness not worse=True, cost delta <= 5pp=False.
- Set A, beta=2: UA lower Global Risk=True, lower CVaR90=True, fairness not worse=True, cost delta <= 5pp=False.
- Set B, beta=1.5: UA lower Global Risk=True, lower CVaR90=True, fairness not worse=True, cost delta <= 5pp=False.
- Set B, beta=2: UA lower Global Risk=True, lower CVaR90=True, fairness not worse=True, cost delta <= 5pp=False.
