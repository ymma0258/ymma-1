# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 9.736404 | 0.000% | 0.195896 | 2.964003 | 0.180254 | 0.879248 | 89.426% |
| 1 | 0 | 155748.8 | 16.233% | 3.241951 | 66.703% | 0.049250 | 1.263696 | 0.286293 | 0.785004 | 74.074% |
| 2 | 0 | 166165.0 | 24.006% | 2.504394 | 74.278% | 0.034850 | 0.761863 | 0.229225 | 0.743270 | 67.920% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
