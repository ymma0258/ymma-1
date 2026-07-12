# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.8 | 0.000% | 9.060166 | 0.000% | 0.259819 | 3.063552 | 0.227626 | 0.855550 | 89.079% |
| 0.25 | 0 | 158287.7 | 7.437% | 7.975206 | 11.975% | 0.213498 | 2.622051 | 0.208077 | 0.853670 | 88.630% |
| 0.5 | 0 | 168352.1 | 14.268% | 6.884689 | 24.011% | 0.170841 | 2.146568 | 0.206754 | 0.850548 | 87.257% |
| 1 | 0 | 182978.7 | 24.196% | 4.906381 | 45.847% | 0.122200 | 1.750177 | 0.285992 | 0.820306 | 82.503% |
| 2 | 0 | 205038.1 | 39.169% | 3.803050 | 58.025% | 0.090067 | 1.273101 | 0.301475 | 0.796900 | 77.956% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
