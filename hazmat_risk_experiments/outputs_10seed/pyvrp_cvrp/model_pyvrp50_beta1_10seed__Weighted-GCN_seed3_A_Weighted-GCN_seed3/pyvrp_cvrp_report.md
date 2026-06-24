# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.513224 | 0.000% | 0.208596 | 2.303721 | 0.177406 | 0.836103 | 85.872% |
| 1 | 0 | 158083.9 | 17.975% | 3.127690 | 58.371% | 0.068154 | 0.957545 | 0.223614 | 0.714379 | 70.612% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
