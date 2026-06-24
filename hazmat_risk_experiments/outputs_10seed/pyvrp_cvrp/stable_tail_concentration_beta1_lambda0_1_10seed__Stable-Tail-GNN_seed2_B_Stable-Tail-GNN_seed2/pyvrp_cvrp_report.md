# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.938070 | 0.000% | 0.305060 | 3.409897 | 0.250389 | 0.878131 | 90.980% |
| 1 | 0 | 178441.2 | 21.611% | 4.575101 | 53.964% | 0.124312 | 1.701350 | 0.314377 | 0.851852 | 83.750% |
| 1 | 1 | 193699.0 | 32.010% | 3.677758 | 62.993% | 0.091856 | 1.523729 | 0.344801 | 0.832706 | 80.031% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
