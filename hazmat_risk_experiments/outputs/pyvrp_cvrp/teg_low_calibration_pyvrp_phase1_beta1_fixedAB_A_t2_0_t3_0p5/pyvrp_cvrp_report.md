# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.199232 | 0.000% | 0.272481 | 2.632720 | 0.213871 | 0.836651 | 86.627% |
| 1 | 0 | 160070.4 | 19.458% | 3.177909 | 61.241% | 0.075101 | 1.210540 | 0.283218 | 0.699791 | 68.663% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
