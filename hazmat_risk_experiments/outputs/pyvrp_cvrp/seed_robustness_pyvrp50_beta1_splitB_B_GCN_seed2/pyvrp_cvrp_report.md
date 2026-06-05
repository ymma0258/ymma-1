# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 9.451363 | 0.000% | 0.287898 | 3.375419 | 0.273113 | 0.866882 | 90.159% |
| 1 | 0 | 180885.4 | 23.445% | 5.037652 | 46.699% | 0.140612 | 1.952960 | 0.317411 | 0.840157 | 83.978% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
