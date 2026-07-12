# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.2 | 0.000% | 7.521849 | 0.000% | 0.230404 | 2.472652 | 0.213064 | 0.873331 | 90.895% |
| 0.25 | 0 | 157157.3 | 6.622% | 6.222512 | 17.274% | 0.180474 | 2.073019 | 0.252341 | 0.872270 | 90.071% |
| 0.5 | 0 | 166090.4 | 12.682% | 5.442614 | 27.643% | 0.160467 | 1.586893 | 0.171529 | 0.872629 | 89.157% |
| 1 | 0 | 178224.2 | 20.914% | 3.418687 | 54.550% | 0.091365 | 1.201142 | 0.289854 | 0.844885 | 83.935% |
| 2 | 0 | 196364.5 | 33.221% | 2.776524 | 63.087% | 0.069922 | 1.025034 | 0.303795 | 0.827284 | 80.130% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
