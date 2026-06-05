# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.637977 | 0.000% | 0.274955 | 2.635374 | 0.161201 | 0.841396 | 87.590% |
| 1 | 0 | 160417.2 | 19.717% | 3.633338 | 57.938% | 0.077678 | 1.164667 | 0.277671 | 0.738084 | 73.401% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
