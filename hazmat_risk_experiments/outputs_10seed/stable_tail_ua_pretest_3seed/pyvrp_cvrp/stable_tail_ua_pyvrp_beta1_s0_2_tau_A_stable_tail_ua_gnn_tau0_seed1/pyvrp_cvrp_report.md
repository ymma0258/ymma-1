# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 8.328534 | 0.000% | 0.264774 | 2.382243 | 0.128081 | 0.867895 | 89.261% |
| 1 | 0 | 157291.0 | 17.384% | 3.313684 | 60.213% | 0.091465 | 0.850304 | 0.156862 | 0.805476 | 78.183% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
