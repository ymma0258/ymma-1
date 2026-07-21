# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 6.407102 | 0.000% | 0.197616 | 1.897486 | 0.168003 | 0.870979 | 88.545% |
| 0.25 | 0 | 142525.0 | 6.363% | 4.716947 | 26.379% | 0.133276 | 1.606295 | 0.253294 | 0.859617 | 86.500% |
| 0.5 | 0 | 147991.8 | 10.443% | 3.221461 | 49.720% | 0.093957 | 1.203326 | 0.303403 | 0.826702 | 81.440% |
| 1 | 0 | 156221.4 | 16.585% | 2.194963 | 65.742% | 0.055369 | 0.920859 | 0.318510 | 0.762105 | 72.511% |
| 2 | 0 | 167880.6 | 25.286% | 1.666331 | 73.992% | 0.035543 | 0.551127 | 0.246923 | 0.711521 | 64.804% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
