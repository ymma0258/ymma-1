# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.851676 | 0.000% | 0.287040 | 3.185509 | 0.204509 | 0.879458 | 90.687% |
| 0.25 | 0 | 157369.5 | 7.250% | 8.094376 | 17.838% | 0.243630 | 2.418228 | 0.185326 | 0.878688 | 89.527% |
| 0.5 | 0 | 166657.2 | 13.580% | 6.305308 | 35.998% | 0.163915 | 2.171839 | 0.277731 | 0.866291 | 86.937% |
| 1 | 0 | 177195.9 | 20.762% | 3.751834 | 61.917% | 0.081972 | 1.312701 | 0.279289 | 0.821691 | 79.070% |
| 2 | 0 | 193431.3 | 31.827% | 3.301975 | 66.483% | 0.071917 | 1.026371 | 0.247779 | 0.811350 | 76.963% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
