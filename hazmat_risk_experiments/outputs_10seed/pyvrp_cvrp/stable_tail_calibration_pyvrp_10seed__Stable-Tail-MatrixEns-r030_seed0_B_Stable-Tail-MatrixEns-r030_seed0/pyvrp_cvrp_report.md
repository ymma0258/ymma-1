# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 5.262058 | 0.000% | 0.144249 | 1.765235 | 0.249190 | 0.878351 | 89.508% |
| 0.25 | 0 | 156416.5 | 6.408% | 4.490736 | 14.658% | 0.110129 | 1.474755 | 0.241406 | 0.873140 | 88.425% |
| 0.5 | 0 | 164825.5 | 12.128% | 3.277398 | 37.716% | 0.083556 | 1.162718 | 0.233860 | 0.851475 | 84.756% |
| 1 | 0 | 175046.7 | 19.082% | 2.158529 | 58.979% | 0.055144 | 0.840205 | 0.307271 | 0.811234 | 78.245% |
| 2 | 0 | 190093.8 | 29.318% | 1.696684 | 67.756% | 0.034743 | 0.612156 | 0.268496 | 0.778595 | 72.610% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
