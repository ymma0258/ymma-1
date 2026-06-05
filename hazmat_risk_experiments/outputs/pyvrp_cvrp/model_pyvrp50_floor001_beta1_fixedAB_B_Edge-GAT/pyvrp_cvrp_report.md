# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146531.2 | 0.000% | 8.223217 | 0.000% | 0.222894 | 2.856373 | 0.249336 | 0.866811 | 89.849% |
| 1 | 178159.0 | 21.584% | 3.537995 | 56.976% | 0.073080 | 1.384320 | 0.303497 | 0.811199 | 79.738% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
