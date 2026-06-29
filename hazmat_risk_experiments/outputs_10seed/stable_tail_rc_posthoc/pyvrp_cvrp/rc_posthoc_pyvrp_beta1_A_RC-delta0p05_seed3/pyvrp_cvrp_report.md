# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.789092 | 0.000% | 0.198246 | 2.214994 | 0.216065 | 0.875461 | 89.225% |
| 1 | 0 | 154774.1 | 15.505% | 2.454019 | 63.854% | 0.058437 | 0.780024 | 0.228475 | 0.775245 | 75.045% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
