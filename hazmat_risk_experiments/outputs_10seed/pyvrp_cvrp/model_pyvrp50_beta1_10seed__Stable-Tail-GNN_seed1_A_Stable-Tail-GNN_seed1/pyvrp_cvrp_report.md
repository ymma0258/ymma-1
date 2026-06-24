# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.593196 | 0.000% | 0.239314 | 2.265632 | 0.172750 | 0.878710 | 89.538% |
| 1 | 0 | 155007.6 | 15.679% | 2.614960 | 65.562% | 0.061735 | 0.899936 | 0.243726 | 0.792743 | 75.546% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
