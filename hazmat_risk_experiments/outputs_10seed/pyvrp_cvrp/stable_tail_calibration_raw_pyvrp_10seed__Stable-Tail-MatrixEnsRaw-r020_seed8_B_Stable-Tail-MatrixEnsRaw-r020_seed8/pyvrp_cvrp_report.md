# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 6.105233 | 0.000% | 0.188815 | 1.841503 | 0.180829 | 0.859430 | 87.790% |
| 0.25 | 0 | 156298.7 | 6.231% | 5.074782 | 16.878% | 0.121643 | 1.737087 | 0.226639 | 0.855417 | 86.919% |
| 0.5 | 0 | 165178.2 | 12.266% | 3.800374 | 37.752% | 0.092165 | 1.264999 | 0.241889 | 0.832867 | 83.206% |
| 1 | 0 | 175731.1 | 19.439% | 2.440237 | 60.030% | 0.057886 | 0.848906 | 0.218406 | 0.782188 | 75.479% |
| 2 | 0 | 190370.6 | 29.389% | 1.989800 | 67.408% | 0.043438 | 0.572271 | 0.193719 | 0.753759 | 70.890% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
