# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 8.415612 | 0.000% | 0.246440 | 2.933372 | 0.265068 | 0.882626 | 90.171% |
| 1 | 0 | 173649.6 | 18.131% | 3.092592 | 63.252% | 0.062398 | 1.115421 | 0.275470 | 0.813336 | 76.961% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
