# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.006667 | 0.000% | 0.291547 | 3.231694 | 0.203715 | 0.879205 | 90.682% |
| 1 | 0 | 177363.1 | 20.876% | 3.711318 | 62.912% | 0.078864 | 1.211532 | 0.239812 | 0.820896 | 78.781% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
