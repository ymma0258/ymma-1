# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.111522 | 0.000% | 0.236582 | 2.758887 | 0.235558 | 0.865353 | 89.159% |
| 1 | 0 | 181576.9 | 23.748% | 3.824150 | 52.855% | 0.092369 | 1.371463 | 0.328018 | 0.815095 | 80.089% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
