# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 7.767150 | 0.000% | 0.240824 | 2.131996 | 0.146812 | 0.877203 | 90.017% |
| 0.25 | 0 | 143251.0 | 6.852% | 6.051873 | 22.084% | 0.187006 | 1.877563 | 0.223415 | 0.872365 | 88.851% |
| 0.5 | 0 | 150025.8 | 11.906% | 4.338288 | 44.146% | 0.131327 | 1.350479 | 0.235406 | 0.850307 | 85.186% |
| 1 | 0 | 159561.4 | 19.018% | 3.132503 | 59.670% | 0.075204 | 1.162702 | 0.328340 | 0.814956 | 79.931% |
| 2 | 0 | 174492.5 | 30.155% | 2.539538 | 67.304% | 0.059092 | 0.950090 | 0.342632 | 0.786898 | 75.618% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
