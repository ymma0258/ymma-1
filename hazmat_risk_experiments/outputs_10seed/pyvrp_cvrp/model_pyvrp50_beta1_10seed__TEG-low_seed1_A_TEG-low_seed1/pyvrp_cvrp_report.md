# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.554942 | 0.000% | 0.238247 | 2.277329 | 0.167129 | 0.837137 | 86.143% |
| 1 | 0 | 157340.2 | 17.420% | 2.922636 | 61.315% | 0.060573 | 0.934375 | 0.228478 | 0.692118 | 68.227% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
