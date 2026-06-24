# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.126751 | 0.000% | 0.254293 | 2.607424 | 0.205133 | 0.860498 | 89.003% |
| 1 | 0 | 180448.8 | 22.979% | 3.912706 | 51.854% | 0.085831 | 1.273464 | 0.246989 | 0.808817 | 80.517% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
