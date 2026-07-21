# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.506106 | 0.000% | 0.270176 | 2.424497 | 0.160879 | 0.870504 | 89.406% |
| 0.25 | 0 | 142965.6 | 6.692% | 5.721070 | 32.742% | 0.179533 | 1.775206 | 0.215902 | 0.855350 | 87.126% |
| 0.5 | 0 | 149285.8 | 11.409% | 4.335173 | 49.035% | 0.104407 | 1.600354 | 0.252755 | 0.829554 | 83.499% |
| 1 | 0 | 158140.9 | 18.017% | 2.952281 | 65.292% | 0.067415 | 1.074919 | 0.263592 | 0.776903 | 75.988% |
| 2 | 0 | 171724.0 | 28.154% | 2.443978 | 71.268% | 0.056236 | 0.725849 | 0.220043 | 0.744791 | 71.355% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
