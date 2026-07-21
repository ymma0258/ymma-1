# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.1 | 0.000% | 9.171716 | 0.000% | 0.301075 | 2.609964 | 0.175177 | 0.872938 | 89.456% |
| 0.25 | 0 | 143417.9 | 6.711% | 6.205226 | 32.344% | 0.178798 | 1.984579 | 0.222731 | 0.862328 | 87.253% |
| 0.5 | 0 | 149291.0 | 11.081% | 4.607441 | 49.765% | 0.133065 | 1.876073 | 0.310798 | 0.837286 | 83.384% |
| 1 | 0 | 158831.4 | 18.180% | 3.235024 | 64.728% | 0.087641 | 1.366636 | 0.312374 | 0.793756 | 76.565% |
| 2 | 0 | 172043.5 | 28.010% | 2.558977 | 72.099% | 0.059635 | 0.854982 | 0.248682 | 0.761046 | 71.403% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
