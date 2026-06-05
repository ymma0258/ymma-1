# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 9.036024 | 0.000% | 0.280547 | 3.010459 | 0.227724 | 0.878002 | 89.916% |
| 1 | 0 | 177054.4 | 20.831% | 4.083574 | 54.808% | 0.100482 | 1.530836 | 0.324186 | 0.824376 | 80.408% |
| 1 | 1 | 190532.2 | 30.028% | 3.132813 | 65.330% | 0.066704 | 1.345625 | 0.350328 | 0.793930 | 75.456% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
