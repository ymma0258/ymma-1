# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 12.319116 | 0.000% | 0.258518 | 3.355540 | 0.131401 | 0.844401 | 87.921% |
| 1 | 0 | 161373.6 | 20.430% | 5.210121 | 57.707% | 0.082827 | 1.722169 | 0.253221 | 0.759004 | 76.015% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
