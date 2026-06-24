# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.280496 | 0.000% | 0.208685 | 2.332222 | 0.202410 | 0.859043 | 88.408% |
| 1 | 0 | 157168.7 | 17.292% | 2.702133 | 62.885% | 0.062687 | 0.917234 | 0.226062 | 0.755739 | 74.299% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
