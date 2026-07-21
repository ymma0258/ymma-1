# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 8.884174 | 0.000% | 0.287935 | 2.634278 | 0.174664 | 0.872230 | 89.250% |
| 0.25 | 0 | 143204.7 | 6.764% | 6.453212 | 27.363% | 0.187475 | 2.137135 | 0.233282 | 0.862922 | 87.477% |
| 0.5 | 0 | 149388.7 | 11.375% | 4.826069 | 45.678% | 0.140544 | 1.909583 | 0.299711 | 0.839996 | 83.855% |
| 1 | 0 | 158532.8 | 18.192% | 3.277621 | 63.107% | 0.088971 | 1.286794 | 0.296112 | 0.801489 | 77.572% |
| 2 | 0 | 171623.0 | 27.951% | 2.567974 | 71.095% | 0.057085 | 0.889713 | 0.261293 | 0.763338 | 71.598% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
