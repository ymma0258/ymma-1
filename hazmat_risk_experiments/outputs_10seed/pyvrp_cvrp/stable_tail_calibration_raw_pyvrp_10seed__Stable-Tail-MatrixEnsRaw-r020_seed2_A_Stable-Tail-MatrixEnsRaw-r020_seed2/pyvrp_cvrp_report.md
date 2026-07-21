# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 6.979336 | 0.000% | 0.225894 | 1.994637 | 0.164277 | 0.877257 | 89.948% |
| 0.25 | 0 | 142352.6 | 6.182% | 4.853399 | 30.460% | 0.144540 | 1.643075 | 0.257322 | 0.868115 | 88.049% |
| 0.5 | 0 | 148543.2 | 10.800% | 3.886491 | 44.314% | 0.114602 | 1.519240 | 0.282123 | 0.852967 | 85.617% |
| 1 | 0 | 157841.8 | 17.736% | 2.598288 | 62.772% | 0.068603 | 0.996532 | 0.321448 | 0.809401 | 78.897% |
| 2 | 0 | 172060.9 | 28.342% | 2.296223 | 67.100% | 0.054207 | 0.928989 | 0.328817 | 0.793919 | 76.208% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
