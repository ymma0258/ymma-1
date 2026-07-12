# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 8.359689 | 0.000% | 0.256148 | 2.446118 | 0.180442 | 0.837297 | 86.105% |
| 0.25 | 0 | 143448.7 | 6.893% | 5.800343 | 30.615% | 0.144451 | 1.850867 | 0.216384 | 0.810282 | 82.892% |
| 0.5 | 0 | 149862.4 | 11.672% | 4.517382 | 45.962% | 0.111926 | 1.917853 | 0.323329 | 0.771291 | 78.225% |
| 1 | 0 | 159579.6 | 18.913% | 3.308614 | 60.422% | 0.078137 | 1.026055 | 0.203806 | 0.707909 | 70.266% |
| 2 | 0 | 175110.9 | 30.487% | 2.641252 | 68.405% | 0.047959 | 0.851113 | 0.188069 | 0.641502 | 62.073% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
