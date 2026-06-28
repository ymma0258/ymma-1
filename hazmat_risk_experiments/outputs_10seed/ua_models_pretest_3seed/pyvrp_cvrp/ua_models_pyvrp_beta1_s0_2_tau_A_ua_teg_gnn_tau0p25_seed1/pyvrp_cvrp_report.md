# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 11.134891 | 0.000% | 0.280268 | 3.024491 | 0.129396 | 0.854768 | 88.935% |
| 1 | 0 | 159848.7 | 19.292% | 4.821344 | 56.701% | 0.092346 | 1.671544 | 0.243015 | 0.801364 | 79.682% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
