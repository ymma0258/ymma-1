# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 7.477219 | 0.000% | 0.246833 | 2.206344 | 0.156650 | 0.873682 | 89.170% |
| 1 | 0 | 154975.0 | 15.655% | 2.633713 | 64.777% | 0.064342 | 0.890463 | 0.247196 | 0.793134 | 75.677% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
