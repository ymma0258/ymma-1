# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.957604 | 0.000% | 0.251216 | 2.294489 | 0.144218 | 0.869637 | 89.394% |
| 0.5 | 0 | 149726.6 | 11.738% | 4.854055 | 39.001% | 0.139963 | 1.622160 | 0.232575 | 0.850024 | 85.678% |
| 1 | 0 | 159127.0 | 18.754% | 3.263350 | 58.991% | 0.079953 | 1.155032 | 0.308450 | 0.807153 | 79.294% |
| 1.5 | 0 | 166776.2 | 24.462% | 2.992007 | 62.401% | 0.066070 | 1.030205 | 0.291553 | 0.794892 | 77.417% |
| 2 | 0 | 174145.2 | 29.961% | 2.930972 | 63.168% | 0.067372 | 0.980743 | 0.277638 | 0.789303 | 76.668% |
| 3 | 0 | 186778.8 | 39.390% | 2.428452 | 69.483% | 0.047746 | 0.957947 | 0.317389 | 0.756388 | 71.775% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
