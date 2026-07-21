# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.1 | 0.000% | 7.796432 | 0.000% | 0.236558 | 2.671735 | 0.237392 | 0.883977 | 90.269% |
| 0.25 | 0 | 142451.3 | 6.150% | 4.577262 | 41.290% | 0.137918 | 1.567918 | 0.244411 | 0.860339 | 86.209% |
| 0.5 | 0 | 148504.6 | 10.661% | 3.798061 | 51.285% | 0.111979 | 1.296398 | 0.246668 | 0.839193 | 83.212% |
| 1 | 0 | 156212.9 | 16.405% | 2.384405 | 69.417% | 0.056560 | 0.897835 | 0.277558 | 0.778291 | 74.282% |
| 2 | 0 | 168267.7 | 25.388% | 1.935194 | 75.178% | 0.035972 | 0.646544 | 0.234939 | 0.743662 | 68.833% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
