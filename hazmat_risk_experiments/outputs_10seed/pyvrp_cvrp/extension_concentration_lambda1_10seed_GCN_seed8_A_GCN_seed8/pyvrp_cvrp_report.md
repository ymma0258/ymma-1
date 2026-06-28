# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.073798 | 0.000% | 0.250232 | 2.473256 | 0.160279 | 0.874056 | 89.912% |
| 1 | 0 | 160243.5 | 19.587% | 3.300414 | 59.122% | 0.075381 | 1.172542 | 0.302583 | 0.809202 | 79.525% |
| 1 | 1 | 173117.2 | 29.194% | 2.571810 | 68.146% | 0.052621 | 1.017795 | 0.321569 | 0.765947 | 72.943% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
