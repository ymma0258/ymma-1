# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.397525 | 0.000% | 0.232973 | 2.390638 | 0.223678 | 0.880360 | 90.067% |
| 3 | 1 | 182133.0 | 35.923% | 1.417078 | 80.844% | 0.023349 | 0.380569 | 0.143595 | 0.663886 | 57.143% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
