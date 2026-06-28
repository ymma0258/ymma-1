# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 6.282950 | 0.000% | 0.177174 | 1.869566 | 0.168377 | 0.875220 | 89.237% |
| 0.5 | 0 | 147093.7 | 9.773% | 3.146264 | 49.924% | 0.090319 | 1.145701 | 0.296597 | 0.825530 | 81.443% |
| 1 | 0 | 155535.2 | 16.073% | 2.202071 | 64.952% | 0.057789 | 0.828697 | 0.300631 | 0.770454 | 73.534% |
| 1.5 | 0 | 161572.9 | 20.579% | 1.708629 | 72.805% | 0.038371 | 0.559261 | 0.262239 | 0.723061 | 66.762% |
| 2 | 0 | 166945.6 | 24.589% | 1.801428 | 71.328% | 0.041499 | 0.580317 | 0.251754 | 0.738269 | 68.619% |
| 3 | 0 | 177110.2 | 32.174% | 1.521538 | 75.783% | 0.031913 | 0.461991 | 0.229802 | 0.694673 | 61.869% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
