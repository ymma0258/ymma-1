# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.755311 | 0.000% | 0.254725 | 2.939045 | 0.232741 | 0.856257 | 88.655% |
| 1 | 0 | 180484.0 | 23.003% | 4.301133 | 50.874% | 0.094297 | 1.609196 | 0.331858 | 0.803490 | 80.164% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
