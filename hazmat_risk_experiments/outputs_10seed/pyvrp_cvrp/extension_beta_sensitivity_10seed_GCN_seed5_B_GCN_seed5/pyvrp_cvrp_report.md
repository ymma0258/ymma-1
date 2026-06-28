# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.365869 | 0.000% | 0.203249 | 2.526459 | 0.234141 | 0.862975 | 88.437% |
| 0.5 | 0 | 166067.5 | 13.178% | 5.155538 | 30.008% | 0.129087 | 1.564749 | 0.161042 | 0.844447 | 85.421% |
| 1 | 0 | 177845.5 | 21.205% | 3.174338 | 56.905% | 0.080723 | 1.080873 | 0.300202 | 0.801873 | 78.061% |
| 1.5 | 0 | 186627.0 | 27.190% | 2.779880 | 62.260% | 0.067637 | 0.851372 | 0.233932 | 0.784176 | 75.297% |
| 2 | 0 | 194426.8 | 32.506% | 2.683706 | 63.566% | 0.064237 | 0.855532 | 0.263842 | 0.778100 | 74.275% |
| 3 | 0 | 210378.3 | 43.377% | 2.676330 | 63.666% | 0.062667 | 0.860302 | 0.263188 | 0.777888 | 74.188% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
