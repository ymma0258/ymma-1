# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.0 | 0.000% | 8.645362 | 0.000% | 0.255552 | 3.037900 | 0.248128 | 0.868497 | 89.148% |
| 0.25 | 0 | 158068.1 | 7.240% | 7.711429 | 10.803% | 0.194385 | 2.634039 | 0.260575 | 0.867497 | 89.022% |
| 0.5 | 0 | 168270.8 | 14.162% | 6.434481 | 25.573% | 0.166544 | 2.163829 | 0.244734 | 0.862188 | 87.370% |
| 1 | 0 | 181619.7 | 23.218% | 4.178232 | 51.671% | 0.103994 | 1.591701 | 0.334884 | 0.826094 | 81.090% |
| 2 | 0 | 203124.7 | 37.808% | 3.685455 | 57.371% | 0.093923 | 1.409148 | 0.356689 | 0.816022 | 78.963% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
