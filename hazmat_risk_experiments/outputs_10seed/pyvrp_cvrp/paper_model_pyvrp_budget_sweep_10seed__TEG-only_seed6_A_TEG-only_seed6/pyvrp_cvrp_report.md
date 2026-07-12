# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.3 | 0.000% | 8.389732 | 0.000% | 0.267451 | 2.873190 | 0.214854 | 0.843142 | 86.190% |
| 0.25 | 0 | 143526.4 | 6.951% | 5.846467 | 30.314% | 0.153839 | 1.790122 | 0.210978 | 0.818272 | 83.126% |
| 0.5 | 0 | 150973.9 | 12.501% | 4.168721 | 50.312% | 0.110690 | 1.568129 | 0.273059 | 0.769381 | 76.591% |
| 1 | 0 | 159859.1 | 19.122% | 3.002746 | 64.209% | 0.071063 | 1.015882 | 0.266349 | 0.702175 | 68.268% |
| 2 | 0 | 175059.7 | 30.449% | 2.489117 | 70.331% | 0.049263 | 0.732012 | 0.179903 | 0.647035 | 61.643% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
