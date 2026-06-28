# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 12.288222 | 0.000% | 0.291319 | 3.330279 | 0.122514 | 0.839855 | 87.677% |
| 1 | 0 | 161573.3 | 20.580% | 5.629481 | 54.188% | 0.095224 | 1.903451 | 0.217345 | 0.773646 | 77.850% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
