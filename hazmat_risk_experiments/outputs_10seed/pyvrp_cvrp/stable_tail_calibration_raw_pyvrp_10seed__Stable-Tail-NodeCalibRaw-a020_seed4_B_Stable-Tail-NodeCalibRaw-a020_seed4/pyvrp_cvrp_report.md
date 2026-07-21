# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.1 | 0.000% | 8.585782 | 0.000% | 0.254474 | 2.920361 | 0.232578 | 0.873765 | 89.312% |
| 0.25 | 0 | 156695.4 | 6.404% | 7.379798 | 14.046% | 0.216552 | 2.351384 | 0.190614 | 0.871567 | 88.437% |
| 0.5 | 0 | 164983.2 | 12.032% | 5.659933 | 34.078% | 0.150244 | 1.896370 | 0.251233 | 0.854488 | 85.430% |
| 1 | 0 | 175412.0 | 19.114% | 4.036273 | 52.989% | 0.102146 | 1.615878 | 0.311842 | 0.822281 | 80.362% |
| 2 | 0 | 191915.1 | 30.320% | 3.114215 | 63.728% | 0.067037 | 1.214994 | 0.318586 | 0.796784 | 76.063% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
