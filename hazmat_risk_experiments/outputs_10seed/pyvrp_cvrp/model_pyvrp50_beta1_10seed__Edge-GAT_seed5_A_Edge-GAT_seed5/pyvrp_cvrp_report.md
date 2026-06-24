# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.240113 | 0.000% | 0.217252 | 2.175983 | 0.171127 | 0.855360 | 88.099% |
| 1 | 0 | 156800.2 | 17.017% | 2.622424 | 63.779% | 0.064135 | 0.864548 | 0.224338 | 0.738128 | 72.629% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
