# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 7.520440 | 0.000% | 0.224469 | 2.344418 | 0.178063 | 0.870575 | 89.600% |
| 1 | 0 | 159586.7 | 19.097% | 2.855283 | 62.033% | 0.065880 | 0.966526 | 0.183671 | 0.796054 | 77.462% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
