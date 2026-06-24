# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.925219 | 0.000% | 0.239685 | 2.388882 | 0.151881 | 0.841356 | 86.491% |
| 1 | 0 | 160347.7 | 19.665% | 3.287219 | 58.522% | 0.077616 | 0.943761 | 0.217719 | 0.731119 | 72.046% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
