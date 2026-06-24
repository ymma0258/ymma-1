# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.323610 | 0.000% | 0.204786 | 2.231959 | 0.178869 | 0.834297 | 86.007% |
| 1 | 0 | 158385.7 | 18.200% | 2.927334 | 60.029% | 0.063554 | 0.915462 | 0.191036 | 0.693318 | 68.812% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
