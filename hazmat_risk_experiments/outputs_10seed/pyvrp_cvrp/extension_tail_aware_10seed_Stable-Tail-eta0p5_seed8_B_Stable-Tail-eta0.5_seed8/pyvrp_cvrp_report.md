# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.576581 | 0.000% | 0.189225 | 3.006130 | 0.187905 | 0.880303 | 89.179% |
| 1 | 0 | 177058.3 | 20.669% | 4.028412 | 57.935% | 0.061043 | 1.782416 | 0.358603 | 0.818949 | 78.333% |
| 2 | 0 | 194118.4 | 32.296% | 3.320840 | 65.323% | 0.048980 | 1.343836 | 0.315548 | 0.799956 | 74.914% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
