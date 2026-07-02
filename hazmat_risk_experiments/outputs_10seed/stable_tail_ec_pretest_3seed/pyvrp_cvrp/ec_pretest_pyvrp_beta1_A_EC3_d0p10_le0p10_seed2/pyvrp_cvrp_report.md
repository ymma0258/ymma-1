# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.430294 | 0.000% | 0.264358 | 2.306202 | 0.142949 | 0.870265 | 89.790% |
| 1 | 0 | 160413.0 | 19.713% | 3.505118 | 58.422% | 0.088429 | 1.212635 | 0.264970 | 0.824335 | 80.511% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
