# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.354824 | 0.000% | 0.232899 | 2.745072 | 0.226724 | 0.846367 | 87.402% |
| 1 | 0 | 158644.4 | 18.394% | 3.151374 | 62.281% | 0.071000 | 1.107252 | 0.267489 | 0.714024 | 70.141% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
