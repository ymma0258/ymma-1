# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.2 | 0.000% | 8.486117 | 0.000% | 0.267963 | 2.609617 | 0.199474 | 0.870624 | 89.921% |
| 0.25 | 0 | 158353.4 | 7.725% | 7.204693 | 15.100% | 0.197297 | 2.166595 | 0.181013 | 0.869529 | 89.390% |
| 0.5 | 0 | 168077.4 | 14.341% | 5.115503 | 39.719% | 0.136474 | 1.624520 | 0.241121 | 0.848217 | 85.565% |
| 1 | 0 | 179462.1 | 22.085% | 3.497244 | 58.789% | 0.082394 | 1.281556 | 0.292674 | 0.817421 | 80.160% |
| 2 | 0 | 196884.0 | 33.937% | 2.885592 | 65.996% | 0.054978 | 0.903596 | 0.248046 | 0.792734 | 76.185% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
