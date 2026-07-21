# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.1 | 0.000% | 8.513457 | 0.000% | 0.260090 | 2.406763 | 0.157531 | 0.868849 | 89.018% |
| 0.25 | 0 | 143253.1 | 6.747% | 4.996309 | 41.313% | 0.149883 | 1.675958 | 0.264433 | 0.844493 | 84.970% |
| 0.5 | 0 | 149246.0 | 11.213% | 4.036683 | 52.585% | 0.118208 | 1.493072 | 0.291548 | 0.818814 | 81.684% |
| 1 | 0 | 158728.8 | 18.279% | 2.957028 | 65.266% | 0.079329 | 0.990219 | 0.281532 | 0.778173 | 75.870% |
| 2 | 0 | 173093.8 | 28.984% | 2.304414 | 72.932% | 0.053472 | 0.883187 | 0.309066 | 0.731526 | 69.290% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
