# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 9.084675 | 0.000% | 0.304214 | 2.567506 | 0.152837 | 0.874263 | 89.593% |
| 0.25 | 0 | 143201.4 | 6.815% | 6.094909 | 32.910% | 0.166295 | 1.856973 | 0.212288 | 0.863772 | 86.783% |
| 0.5 | 0 | 149545.3 | 11.547% | 4.730656 | 47.927% | 0.130434 | 1.716098 | 0.272015 | 0.840311 | 83.270% |
| 1 | 0 | 158612.6 | 18.310% | 3.065306 | 66.258% | 0.072229 | 1.186427 | 0.294377 | 0.793302 | 75.381% |
| 2 | 0 | 171400.8 | 27.849% | 2.461681 | 72.903% | 0.048484 | 0.863846 | 0.277399 | 0.758648 | 70.629% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
