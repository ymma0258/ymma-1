# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 8.775298 | 0.000% | 0.272924 | 2.844633 | 0.213610 | 0.867809 | 89.638% |
| 0.25 | 0 | 158445.8 | 7.593% | 7.899531 | 9.980% | 0.226970 | 2.698437 | 0.220645 | 0.870160 | 89.743% |
| 0.5 | 0 | 169024.6 | 14.777% | 5.386398 | 38.619% | 0.142584 | 1.740933 | 0.235721 | 0.846695 | 85.546% |
| 1 | 0 | 179933.9 | 22.185% | 3.441721 | 60.779% | 0.074863 | 1.185057 | 0.262981 | 0.808120 | 78.916% |
| 2 | 0 | 197966.5 | 34.430% | 3.038679 | 65.372% | 0.059416 | 0.968953 | 0.254965 | 0.793085 | 76.216% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
