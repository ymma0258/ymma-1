# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.2 | 0.000% | 6.238766 | 0.000% | 0.194478 | 2.291862 | 0.302054 | 0.874744 | 89.625% |
| 0.25 | 0 | 156612.6 | 6.493% | 5.292198 | 15.172% | 0.157504 | 2.006477 | 0.316939 | 0.873387 | 89.002% |
| 0.5 | 0 | 165196.3 | 12.329% | 4.377624 | 29.832% | 0.114736 | 1.434980 | 0.237969 | 0.863514 | 87.216% |
| 1 | 0 | 177845.9 | 20.931% | 3.243501 | 48.011% | 0.088079 | 1.237208 | 0.275297 | 0.846790 | 83.841% |
| 2 | 0 | 196226.6 | 33.429% | 2.549818 | 59.129% | 0.064189 | 1.170209 | 0.362254 | 0.825801 | 80.017% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
