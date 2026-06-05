# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 7.112312 | 0.000% | 0.220839 | 2.386151 | 0.237350 | 0.877486 | 89.797% |
| 1 | 0 | 156742.0 | 16.974% | 2.349958 | 66.959% | 0.050820 | 0.865722 | 0.257270 | 0.790399 | 75.196% |
| 1 | 1 | 164413.0 | 22.699% | 1.595215 | 77.571% | 0.026973 | 0.422155 | 0.168173 | 0.692607 | 61.421% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
