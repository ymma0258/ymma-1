# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.133457 | 0.000% | 0.227682 | 2.946641 | 0.286162 | 0.884312 | 90.216% |
| 1 | 0 | 173280.8 | 18.255% | 3.234555 | 60.231% | 0.072767 | 1.068172 | 0.250976 | 0.817225 | 77.745% |
| 1 | 1 | 184232.4 | 25.729% | 2.757312 | 66.099% | 0.053528 | 1.030787 | 0.282790 | 0.801124 | 75.010% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
