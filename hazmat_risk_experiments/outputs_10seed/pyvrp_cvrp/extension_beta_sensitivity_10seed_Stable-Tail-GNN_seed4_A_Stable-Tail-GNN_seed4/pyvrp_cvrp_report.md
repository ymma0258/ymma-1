# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.803669 | 0.000% | 0.278188 | 2.639760 | 0.155480 | 0.875826 | 90.106% |
| 0.5 | 0 | 150377.9 | 12.224% | 4.832241 | 45.111% | 0.129812 | 1.310033 | 0.191368 | 0.847465 | 84.668% |
| 1 | 0 | 160054.1 | 19.446% | 3.409976 | 61.266% | 0.075068 | 1.160148 | 0.294724 | 0.811652 | 78.952% |
| 1.5 | 0 | 167896.8 | 25.298% | 2.896488 | 67.099% | 0.057036 | 1.082334 | 0.332038 | 0.787722 | 75.567% |
| 2 | 0 | 175033.4 | 30.624% | 2.717872 | 69.128% | 0.053936 | 1.087239 | 0.331742 | 0.773170 | 73.438% |
| 3 | 0 | 187188.6 | 39.696% | 2.476348 | 71.871% | 0.048498 | 1.106366 | 0.352327 | 0.755424 | 70.806% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
