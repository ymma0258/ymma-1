# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.547423 | 0.000% | 0.267414 | 2.314659 | 0.134066 | 0.870504 | 90.025% |
| 1 | 0 | 159825.5 | 19.275% | 3.658927 | 57.193% | 0.104315 | 1.273795 | 0.275474 | 0.822582 | 80.465% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
