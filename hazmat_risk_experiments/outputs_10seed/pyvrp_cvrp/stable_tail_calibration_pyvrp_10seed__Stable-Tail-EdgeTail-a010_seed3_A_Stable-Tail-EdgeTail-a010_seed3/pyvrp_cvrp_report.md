# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134531.0 | 0.000% | 7.320148 | 0.000% | 0.232099 | 2.226030 | 0.179947 | 0.873102 | 88.817% |
| 0.25 | 0 | 141743.1 | 5.361% | 4.815913 | 34.210% | 0.135983 | 1.467269 | 0.194491 | 0.854090 | 86.439% |
| 0.5 | 0 | 147088.4 | 9.334% | 3.696805 | 49.498% | 0.106644 | 1.220785 | 0.222205 | 0.837425 | 83.492% |
| 1 | 0 | 154758.6 | 15.036% | 2.466459 | 66.306% | 0.064615 | 0.783220 | 0.236701 | 0.775031 | 75.150% |
| 2 | 0 | 166495.7 | 23.760% | 2.160451 | 70.486% | 0.051959 | 0.698791 | 0.228487 | 0.754685 | 71.797% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
