# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.3 | 0.000% | 8.360721 | 0.000% | 0.249712 | 2.819789 | 0.230715 | 0.873422 | 89.120% |
| 0.25 | 0 | 156444.2 | 6.282% | 7.314242 | 12.517% | 0.205326 | 2.328325 | 0.198547 | 0.870922 | 88.322% |
| 0.5 | 0 | 165152.1 | 12.198% | 5.551142 | 33.605% | 0.144297 | 1.926332 | 0.262444 | 0.851669 | 85.017% |
| 1 | 0 | 175477.9 | 19.213% | 3.779120 | 54.799% | 0.095147 | 1.421944 | 0.282766 | 0.815348 | 79.467% |
| 2 | 0 | 191854.4 | 30.338% | 3.165936 | 62.133% | 0.066230 | 1.264715 | 0.310079 | 0.798426 | 76.617% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
