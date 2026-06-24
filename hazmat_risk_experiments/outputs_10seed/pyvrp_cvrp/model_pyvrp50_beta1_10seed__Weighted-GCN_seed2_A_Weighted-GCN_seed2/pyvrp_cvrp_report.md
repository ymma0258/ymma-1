# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.910546 | 0.000% | 0.272443 | 2.519947 | 0.140397 | 0.848180 | 88.032% |
| 1 | 0 | 160394.0 | 19.699% | 3.745034 | 57.971% | 0.093508 | 1.177268 | 0.249277 | 0.754300 | 74.828% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
