# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 12.811176 | 0.000% | 0.385321 | 4.207842 | 0.212345 | 0.831477 | 88.302% |
| 1 | 0 | 185139.3 | 26.616% | 7.722127 | 39.724% | 0.201783 | 2.477879 | 0.240229 | 0.789929 | 82.015% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
