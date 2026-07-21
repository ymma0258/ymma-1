# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.2 | 0.000% | 6.940477 | 0.000% | 0.206782 | 2.464919 | 0.262199 | 0.869613 | 88.896% |
| 0.25 | 0 | 155575.7 | 5.788% | 5.804752 | 16.364% | 0.141299 | 2.188440 | 0.276725 | 0.864399 | 87.831% |
| 0.5 | 0 | 163625.2 | 11.261% | 4.612220 | 33.546% | 0.115343 | 1.838273 | 0.304923 | 0.850707 | 85.311% |
| 1 | 0 | 175181.1 | 19.119% | 3.571517 | 48.541% | 0.088897 | 1.409073 | 0.287675 | 0.836625 | 82.355% |
| 2 | 0 | 191937.3 | 30.513% | 2.827334 | 59.263% | 0.071383 | 1.085220 | 0.279478 | 0.809480 | 77.875% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
