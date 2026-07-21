# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.6 | 0.000% | 8.039590 | 0.000% | 0.245348 | 2.723453 | 0.244100 | 0.876751 | 89.381% |
| 0.25 | 0 | 157216.1 | 6.613% | 6.745173 | 16.101% | 0.171199 | 2.414926 | 0.268586 | 0.872997 | 88.532% |
| 0.5 | 0 | 165355.2 | 12.133% | 4.799559 | 40.301% | 0.117033 | 1.659626 | 0.265932 | 0.845837 | 84.427% |
| 1 | 0 | 175903.2 | 19.286% | 3.504515 | 56.409% | 0.086188 | 1.244020 | 0.292667 | 0.818711 | 79.504% |
| 2 | 0 | 191057.6 | 29.563% | 2.811018 | 65.035% | 0.067766 | 0.864651 | 0.263580 | 0.793635 | 75.365% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
