# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 14.031321 | 0.000% | 0.343385 | 4.480644 | 0.203712 | 0.858269 | 89.746% |
| 1 | 0 | 181941.0 | 23.996% | 6.919314 | 50.687% | 0.120864 | 2.286985 | 0.252037 | 0.821820 | 83.162% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
