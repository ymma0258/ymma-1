# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.570012 | 0.000% | 0.264362 | 3.075490 | 0.283603 | 0.865479 | 89.090% |
| 1 | 0 | 181304.1 | 23.562% | 4.760146 | 44.456% | 0.122751 | 1.666483 | 0.286114 | 0.832115 | 83.084% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
