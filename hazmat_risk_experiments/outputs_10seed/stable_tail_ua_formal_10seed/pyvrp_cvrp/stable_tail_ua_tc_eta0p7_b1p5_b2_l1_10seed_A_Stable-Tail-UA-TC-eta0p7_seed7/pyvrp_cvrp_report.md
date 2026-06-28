# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.7 | 0.000% | 12.268203 | 0.000% | 0.305958 | 3.288803 | 0.134126 | 0.859275 | 89.325% |
| 1.5 | 1 | 187420.9 | 39.869% | 3.789985 | 69.107% | 0.070459 | 1.572204 | 0.361316 | 0.729410 | 70.186% |
| 2 | 1 | 195414.2 | 45.834% | 3.791746 | 69.093% | 0.070388 | 1.386820 | 0.337792 | 0.728324 | 70.110% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
