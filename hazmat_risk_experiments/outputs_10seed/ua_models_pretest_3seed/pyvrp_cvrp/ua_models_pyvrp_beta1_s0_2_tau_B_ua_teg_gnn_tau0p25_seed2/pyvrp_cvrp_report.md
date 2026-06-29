# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 9.048810 | 0.000% | 0.275686 | 3.256646 | 0.245873 | 0.847472 | 89.567% |
| 1 | 0 | 181026.7 | 23.804% | 5.441584 | 39.864% | 0.150945 | 1.517811 | 0.132876 | 0.805469 | 83.933% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
