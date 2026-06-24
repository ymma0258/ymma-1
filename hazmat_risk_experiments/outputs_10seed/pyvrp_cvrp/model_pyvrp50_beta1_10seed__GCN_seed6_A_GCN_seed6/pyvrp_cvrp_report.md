# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.957604 | 0.000% | 0.251216 | 2.294489 | 0.144218 | 0.869637 | 89.394% |
| 1 | 0 | 159127.0 | 18.754% | 3.263350 | 58.991% | 0.079953 | 1.155032 | 0.308450 | 0.807153 | 79.294% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
