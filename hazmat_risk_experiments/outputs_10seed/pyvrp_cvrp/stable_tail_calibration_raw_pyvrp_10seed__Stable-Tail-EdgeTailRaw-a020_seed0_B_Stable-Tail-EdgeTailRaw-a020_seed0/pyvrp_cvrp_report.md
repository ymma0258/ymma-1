# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.4 | 0.000% | 7.930831 | 0.000% | 0.227511 | 2.705533 | 0.261930 | 0.881389 | 89.955% |
| 0.25 | 0 | 156974.9 | 6.546% | 6.557549 | 17.316% | 0.159380 | 2.198314 | 0.241447 | 0.875282 | 88.576% |
| 0.5 | 0 | 165349.5 | 12.230% | 4.518892 | 43.021% | 0.114146 | 1.540369 | 0.238223 | 0.850222 | 84.333% |
| 1 | 0 | 175375.4 | 19.035% | 3.203909 | 59.602% | 0.081768 | 1.169697 | 0.266101 | 0.815377 | 78.816% |
| 2 | 0 | 190621.0 | 29.383% | 2.494475 | 68.547% | 0.052415 | 0.938868 | 0.282415 | 0.783333 | 73.334% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
