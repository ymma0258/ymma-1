# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.9 | 0.000% | 8.102040 | 0.000% | 0.255908 | 2.325647 | 0.171216 | 0.885662 | 90.328% |
| 1 | 0 | 158190.8 | 17.996% | 3.032221 | 62.575% | 0.069652 | 0.910271 | 0.228358 | 0.819425 | 79.647% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
