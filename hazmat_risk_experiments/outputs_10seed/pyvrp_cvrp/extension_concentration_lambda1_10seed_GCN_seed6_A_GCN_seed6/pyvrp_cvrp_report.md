# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.143273 | 0.000% | 0.261415 | 2.456271 | 0.157879 | 0.871322 | 89.607% |
| 1 | 0 | 159127.0 | 18.754% | 3.263350 | 59.926% | 0.079953 | 1.155032 | 0.308450 | 0.807153 | 79.294% |
| 1 | 1 | 171595.8 | 28.059% | 2.873081 | 64.718% | 0.064912 | 1.020258 | 0.294650 | 0.787001 | 76.253% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
