# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.087849 | 0.000% | 0.287981 | 3.104612 | 0.234715 | 0.869422 | 90.051% |
| 0.5 | 0 | 167028.7 | 13.833% | 6.551509 | 27.909% | 0.185804 | 2.134592 | 0.216171 | 0.863717 | 88.158% |
| 1 | 0 | 180960.9 | 23.328% | 4.669568 | 48.617% | 0.110511 | 1.626878 | 0.314213 | 0.840349 | 83.715% |
| 1.5 | 0 | 192274.5 | 31.039% | 4.288483 | 52.811% | 0.092343 | 1.521108 | 0.297652 | 0.835845 | 82.572% |
| 2 | 0 | 202688.6 | 38.136% | 3.926688 | 56.792% | 0.084556 | 1.469453 | 0.325229 | 0.827812 | 81.217% |
| 3 | 0 | 221712.3 | 51.101% | 3.738574 | 58.862% | 0.077184 | 1.521344 | 0.361122 | 0.821296 | 80.162% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
