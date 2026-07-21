# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.7 | 0.000% | 8.758683 | 0.000% | 0.269614 | 3.473873 | 0.331437 | 0.875114 | 89.750% |
| 0.25 | 0 | 156836.7 | 6.356% | 7.893662 | 9.876% | 0.235770 | 3.134598 | 0.304392 | 0.873672 | 89.352% |
| 0.5 | 0 | 165332.2 | 12.117% | 5.993793 | 31.567% | 0.152777 | 2.164732 | 0.248568 | 0.857953 | 86.468% |
| 1 | 0 | 177833.0 | 20.594% | 4.483455 | 48.811% | 0.122156 | 1.665165 | 0.263287 | 0.843897 | 83.360% |
| 2 | 0 | 196990.5 | 33.586% | 3.569545 | 59.246% | 0.086468 | 1.649600 | 0.377055 | 0.821498 | 79.359% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
