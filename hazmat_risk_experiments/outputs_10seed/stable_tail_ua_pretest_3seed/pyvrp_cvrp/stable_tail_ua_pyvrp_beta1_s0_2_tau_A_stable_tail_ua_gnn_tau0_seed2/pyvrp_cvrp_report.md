# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 8.560855 | 0.000% | 0.279519 | 2.448471 | 0.133257 | 0.868430 | 89.733% |
| 1 | 0 | 159207.3 | 18.814% | 3.454037 | 59.653% | 0.084241 | 1.215306 | 0.322855 | 0.818468 | 79.867% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
