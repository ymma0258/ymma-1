# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 8.387987 | 0.000% | 0.262491 | 2.331867 | 0.152375 | 0.866922 | 88.659% |
| 0.25 | 0 | 143486.2 | 6.868% | 5.096598 | 39.239% | 0.148087 | 1.625997 | 0.233939 | 0.845525 | 85.233% |
| 0.5 | 0 | 149572.9 | 11.401% | 4.059839 | 51.599% | 0.119960 | 1.471695 | 0.287471 | 0.819515 | 81.843% |
| 1 | 0 | 159111.5 | 18.506% | 2.870131 | 65.783% | 0.076675 | 0.868558 | 0.253586 | 0.774975 | 75.495% |
| 2 | 0 | 173702.9 | 29.373% | 2.295322 | 72.636% | 0.053364 | 0.824407 | 0.257823 | 0.730909 | 69.352% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
