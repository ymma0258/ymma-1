# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.458300 | 0.000% | 0.211358 | 2.433926 | 0.203560 | 0.861448 | 88.683% |
| 1 | 0 | 157168.7 | 17.292% | 2.702133 | 63.770% | 0.062687 | 0.917234 | 0.226062 | 0.755739 | 74.299% |
| 1 | 1 | 166666.8 | 24.381% | 2.209254 | 70.379% | 0.039705 | 0.680607 | 0.236459 | 0.706008 | 67.375% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
