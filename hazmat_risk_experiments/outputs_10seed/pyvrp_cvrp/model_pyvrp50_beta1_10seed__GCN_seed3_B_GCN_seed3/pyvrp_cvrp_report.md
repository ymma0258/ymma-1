# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.905733 | 0.000% | 0.244021 | 2.598277 | 0.223369 | 0.855276 | 88.562% |
| 1 | 0 | 179104.5 | 22.063% | 4.026756 | 49.065% | 0.101343 | 1.261857 | 0.248691 | 0.811339 | 81.263% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
