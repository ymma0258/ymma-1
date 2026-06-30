# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 9.083314 | 0.000% | 0.279369 | 3.231489 | 0.267809 | 0.876904 | 90.392% |
| 1 | 0 | 175743.7 | 20.191% | 3.891276 | 57.160% | 0.101458 | 1.249226 | 0.239385 | 0.823094 | 80.002% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
