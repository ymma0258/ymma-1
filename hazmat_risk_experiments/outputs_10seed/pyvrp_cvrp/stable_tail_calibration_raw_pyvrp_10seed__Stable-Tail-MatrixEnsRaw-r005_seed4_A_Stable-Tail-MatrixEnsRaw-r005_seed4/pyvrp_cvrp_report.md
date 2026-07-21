# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 8.492212 | 0.000% | 0.269310 | 2.436691 | 0.167932 | 0.877898 | 90.025% |
| 0.25 | 0 | 143285.5 | 6.772% | 5.867276 | 30.910% | 0.184194 | 1.960626 | 0.267681 | 0.868057 | 88.036% |
| 0.5 | 0 | 150058.4 | 11.818% | 4.801375 | 43.461% | 0.146554 | 1.593159 | 0.240823 | 0.855426 | 85.954% |
| 1 | 0 | 159662.1 | 18.975% | 3.360552 | 60.428% | 0.086025 | 1.193794 | 0.300366 | 0.816542 | 80.231% |
| 2 | 0 | 175006.1 | 30.409% | 2.686583 | 68.364% | 0.063364 | 0.997056 | 0.331688 | 0.785369 | 75.391% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
