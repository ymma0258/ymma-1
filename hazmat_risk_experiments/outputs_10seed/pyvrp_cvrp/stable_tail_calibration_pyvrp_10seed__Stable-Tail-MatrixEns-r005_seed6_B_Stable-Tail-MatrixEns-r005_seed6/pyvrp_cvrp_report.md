# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 8.432572 | 0.000% | 0.260805 | 2.713650 | 0.210975 | 0.868491 | 89.024% |
| 0.25 | 0 | 157731.7 | 7.351% | 7.401565 | 12.226% | 0.185966 | 2.421834 | 0.217832 | 0.867475 | 89.201% |
| 0.5 | 0 | 167984.7 | 14.329% | 5.823369 | 30.942% | 0.146104 | 2.239484 | 0.282938 | 0.856783 | 86.679% |
| 1 | 0 | 181396.9 | 23.458% | 4.020466 | 52.322% | 0.101836 | 1.609415 | 0.358960 | 0.826986 | 81.358% |
| 2 | 0 | 202513.5 | 37.829% | 3.467761 | 58.877% | 0.088283 | 1.258935 | 0.338860 | 0.815556 | 78.921% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
