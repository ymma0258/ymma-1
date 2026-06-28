# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 15.108525 | 0.000% | 0.427328 | 4.630639 | 0.186149 | 0.850595 | 89.004% |
| 1.5 | 1 | 225251.9 | 53.514% | 5.978736 | 60.428% | 0.133134 | 2.449156 | 0.409759 | 0.777614 | 77.064% |
| 2 | 1 | 238362.1 | 62.448% | 5.989343 | 60.358% | 0.136234 | 2.435415 | 0.392231 | 0.776072 | 76.911% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
