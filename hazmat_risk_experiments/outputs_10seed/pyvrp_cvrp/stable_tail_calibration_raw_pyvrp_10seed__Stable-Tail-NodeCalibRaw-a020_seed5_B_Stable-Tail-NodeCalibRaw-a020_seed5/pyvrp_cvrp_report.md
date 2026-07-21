# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.3 | 0.000% | 7.963883 | 0.000% | 0.244130 | 2.718456 | 0.240778 | 0.874707 | 89.398% |
| 0.25 | 0 | 156888.4 | 6.535% | 6.901477 | 13.340% | 0.173900 | 2.329414 | 0.260412 | 0.871233 | 88.529% |
| 0.5 | 0 | 165393.7 | 12.311% | 5.059453 | 36.470% | 0.123283 | 1.836684 | 0.279745 | 0.848350 | 84.666% |
| 1 | 0 | 175864.1 | 19.421% | 3.515362 | 55.859% | 0.089286 | 1.305612 | 0.298381 | 0.816280 | 79.318% |
| 2 | 0 | 191768.9 | 30.221% | 2.861710 | 64.066% | 0.069466 | 0.986845 | 0.299364 | 0.794894 | 75.600% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
