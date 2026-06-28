# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 10.834740 | 0.000% | 0.213506 | 3.803237 | 0.240390 | 0.852649 | 89.353% |
| 1 | 0 | 181669.7 | 24.243% | 5.535600 | 48.909% | 0.116212 | 2.045316 | 0.308176 | 0.805521 | 81.766% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
