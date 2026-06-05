# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.4 | 0.000% | 7.111819 | 0.000% | 0.204514 | 2.388795 | 0.222908 | 0.854089 | 88.084% |
| 1 | 157690.6 | 17.682% | 2.619884 | 63.162% | 0.056648 | 0.914526 | 0.237236 | 0.737247 | 72.482% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
