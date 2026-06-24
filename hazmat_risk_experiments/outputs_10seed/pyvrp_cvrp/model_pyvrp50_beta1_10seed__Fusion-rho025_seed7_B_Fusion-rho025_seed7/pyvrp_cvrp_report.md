# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.018759 | 0.000% | 0.280364 | 3.236472 | 0.213455 | 0.851716 | 89.309% |
| 1 | 0 | 180257.4 | 22.849% | 4.972834 | 50.365% | 0.136769 | 1.706524 | 0.254967 | 0.803750 | 81.385% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
