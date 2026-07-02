# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.205942 | 0.000% | 0.290462 | 2.803422 | 0.180172 | 0.862282 | 89.650% |
| 1 | 0 | 181917.3 | 23.980% | 4.431443 | 51.863% | 0.115081 | 1.449994 | 0.238156 | 0.833347 | 83.302% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
