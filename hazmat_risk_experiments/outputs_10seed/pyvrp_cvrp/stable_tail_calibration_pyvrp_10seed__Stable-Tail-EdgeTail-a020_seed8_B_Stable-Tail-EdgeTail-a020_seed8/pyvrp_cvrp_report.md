# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.737743 | 0.000% | 0.239070 | 2.409597 | 0.194849 | 0.861940 | 87.947% |
| 0.25 | 0 | 156126.6 | 6.259% | 6.149111 | 20.531% | 0.142545 | 2.054941 | 0.216769 | 0.853931 | 86.515% |
| 0.5 | 0 | 164635.0 | 12.049% | 5.162389 | 33.283% | 0.126375 | 1.766930 | 0.244233 | 0.844514 | 84.576% |
| 1 | 0 | 175439.7 | 19.403% | 2.930332 | 62.129% | 0.069394 | 0.918262 | 0.201913 | 0.776197 | 74.628% |
| 2 | 0 | 189616.1 | 29.051% | 2.474922 | 68.015% | 0.052776 | 0.714569 | 0.195871 | 0.753804 | 70.845% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
