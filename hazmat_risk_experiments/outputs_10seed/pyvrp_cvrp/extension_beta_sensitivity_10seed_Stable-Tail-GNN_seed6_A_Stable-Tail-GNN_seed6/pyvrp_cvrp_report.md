# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.736093 | 0.000% | 0.233101 | 2.305522 | 0.160077 | 0.879734 | 89.716% |
| 0.5 | 0 | 149614.5 | 11.655% | 4.047717 | 47.678% | 0.112820 | 1.427905 | 0.263684 | 0.842823 | 83.340% |
| 1 | 0 | 158998.3 | 18.658% | 2.898866 | 62.528% | 0.077334 | 0.951183 | 0.275062 | 0.808054 | 77.941% |
| 1.5 | 0 | 166220.0 | 24.047% | 2.398580 | 68.995% | 0.047824 | 0.909927 | 0.285293 | 0.777687 | 73.325% |
| 2 | 0 | 172971.8 | 29.086% | 2.289503 | 70.405% | 0.045007 | 0.895112 | 0.311456 | 0.768777 | 72.128% |
| 3 | 0 | 185633.4 | 38.535% | 2.050441 | 73.495% | 0.041606 | 0.940295 | 0.328095 | 0.752540 | 69.392% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
