# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 10.214266 | 0.000% | 0.198135 | 3.067726 | 0.155920 | 0.883846 | 90.191% |
| 1 | 0 | 160551.6 | 19.817% | 4.093343 | 59.925% | 0.059571 | 1.335400 | 0.288923 | 0.824116 | 79.696% |
| 2 | 0 | 175371.4 | 30.877% | 3.148068 | 69.180% | 0.043253 | 1.296434 | 0.342424 | 0.792314 | 74.249% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
