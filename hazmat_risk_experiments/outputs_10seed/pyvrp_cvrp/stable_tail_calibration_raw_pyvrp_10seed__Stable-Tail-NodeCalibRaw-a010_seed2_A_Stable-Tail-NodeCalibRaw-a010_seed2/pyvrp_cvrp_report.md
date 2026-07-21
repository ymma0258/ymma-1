# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.7 | 0.000% | 8.528672 | 0.000% | 0.277352 | 2.498244 | 0.178562 | 0.875341 | 89.706% |
| 0.25 | 0 | 142576.9 | 6.296% | 6.068790 | 28.843% | 0.174896 | 2.115291 | 0.263789 | 0.867725 | 87.998% |
| 0.5 | 0 | 148786.9 | 10.926% | 4.801430 | 43.702% | 0.138229 | 1.886595 | 0.290544 | 0.850497 | 85.154% |
| 1 | 0 | 157904.4 | 17.723% | 3.314778 | 61.134% | 0.083172 | 1.235738 | 0.311951 | 0.813580 | 79.511% |
| 2 | 0 | 172327.4 | 28.476% | 2.936225 | 65.572% | 0.069965 | 1.201073 | 0.314950 | 0.794688 | 76.351% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
