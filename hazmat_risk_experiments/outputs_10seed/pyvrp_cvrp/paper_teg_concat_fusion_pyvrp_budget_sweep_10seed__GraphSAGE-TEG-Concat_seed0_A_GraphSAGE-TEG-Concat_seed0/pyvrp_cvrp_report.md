# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.1 | 0.000% | 8.701670 | 0.000% | 0.276754 | 2.589683 | 0.186597 | 0.879207 | 89.840% |
| 0.25 | 0 | 143227.7 | 6.729% | 5.964934 | 31.451% | 0.169749 | 1.928882 | 0.211122 | 0.866915 | 87.374% |
| 0.5 | 0 | 149376.2 | 11.310% | 4.486369 | 48.442% | 0.127129 | 1.819357 | 0.305718 | 0.841453 | 83.658% |
| 1 | 0 | 158673.6 | 18.238% | 2.833751 | 67.434% | 0.071208 | 1.178601 | 0.327477 | 0.788746 | 75.085% |
| 2 | 0 | 169666.6 | 26.430% | 1.861269 | 78.610% | 0.033809 | 0.602842 | 0.225668 | 0.704271 | 63.134% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
