# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.507386 | 0.000% | 0.202382 | 3.231190 | 0.249148 | 0.882380 | 90.366% |
| 1 | 0 | 172302.4 | 17.427% | 3.084840 | 67.553% | 0.061255 | 1.038825 | 0.261322 | 0.794112 | 74.995% |
| 2 | 0 | 183318.7 | 24.935% | 2.537215 | 73.313% | 0.048417 | 0.896206 | 0.249540 | 0.758355 | 69.593% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
