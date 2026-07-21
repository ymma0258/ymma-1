# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 8.901518 | 0.000% | 0.282791 | 2.590657 | 0.172168 | 0.873355 | 89.552% |
| 0.25 | 0 | 142868.4 | 6.408% | 5.709949 | 35.854% | 0.162144 | 1.740851 | 0.215160 | 0.862429 | 87.448% |
| 0.5 | 0 | 149432.8 | 11.297% | 4.135128 | 53.546% | 0.116321 | 1.396927 | 0.248246 | 0.831061 | 82.760% |
| 1 | 0 | 158001.1 | 17.679% | 2.900290 | 67.418% | 0.074613 | 0.873739 | 0.215910 | 0.791558 | 76.748% |
| 2 | 0 | 172318.9 | 28.343% | 2.374059 | 73.330% | 0.049571 | 0.738343 | 0.214948 | 0.756855 | 71.406% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
