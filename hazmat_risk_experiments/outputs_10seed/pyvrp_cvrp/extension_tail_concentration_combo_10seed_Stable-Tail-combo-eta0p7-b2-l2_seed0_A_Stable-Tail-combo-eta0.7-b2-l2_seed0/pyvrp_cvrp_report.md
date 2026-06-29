# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.397525 | 0.000% | 0.232973 | 2.390638 | 0.223678 | 0.880360 | 90.067% |
| 2 | 2 | 178093.9 | 32.908% | 1.423726 | 80.754% | 0.022711 | 0.389131 | 0.150495 | 0.661562 | 56.943% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
