# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 14.025463 | 0.000% | 0.213123 | 4.550372 | 0.213277 | 0.852132 | 89.572% |
| 1 | 0 | 182146.3 | 24.569% | 6.357375 | 54.673% | 0.100896 | 2.173374 | 0.266698 | 0.787859 | 78.982% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
