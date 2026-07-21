# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.1 | 0.000% | 10.254316 | 0.000% | 0.306380 | 3.349899 | 0.225555 | 0.879435 | 90.903% |
| 0.25 | 0 | 158311.0 | 7.404% | 8.330666 | 18.759% | 0.246808 | 2.624432 | 0.219750 | 0.878497 | 89.882% |
| 0.5 | 0 | 167764.5 | 13.818% | 5.244721 | 48.854% | 0.143109 | 2.098788 | 0.306342 | 0.847324 | 84.315% |
| 1 | 0 | 178953.3 | 21.409% | 3.957613 | 61.405% | 0.099328 | 1.495678 | 0.291194 | 0.825953 | 79.995% |
| 2 | 0 | 196183.5 | 33.099% | 3.422422 | 66.625% | 0.078555 | 1.086606 | 0.228197 | 0.810165 | 77.335% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
