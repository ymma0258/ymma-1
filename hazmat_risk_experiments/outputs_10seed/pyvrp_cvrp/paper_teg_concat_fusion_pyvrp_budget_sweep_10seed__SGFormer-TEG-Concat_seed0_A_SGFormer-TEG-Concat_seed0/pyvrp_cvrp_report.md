# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.6 | 0.000% | 8.799918 | 0.000% | 0.273876 | 2.645657 | 0.181482 | 0.870662 | 89.162% |
| 0.25 | 0 | 144050.0 | 7.235% | 5.673685 | 35.526% | 0.173237 | 1.847123 | 0.244736 | 0.853338 | 86.315% |
| 0.5 | 0 | 150566.9 | 12.086% | 4.301814 | 51.115% | 0.099980 | 1.962580 | 0.355001 | 0.822348 | 82.277% |
| 1 | 0 | 160747.3 | 19.665% | 2.837980 | 67.750% | 0.064984 | 1.038514 | 0.275826 | 0.759208 | 73.385% |
| 2 | 0 | 174725.9 | 30.071% | 2.228919 | 74.671% | 0.042769 | 0.759424 | 0.255979 | 0.705318 | 65.918% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
