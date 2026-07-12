# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.4 | 0.000% | 8.492499 | 0.000% | 0.259190 | 3.390665 | 0.348148 | 0.880432 | 89.389% |
| 0.25 | 0 | 156979.4 | 6.645% | 7.140790 | 15.917% | 0.210712 | 2.975855 | 0.337101 | 0.876852 | 87.836% |
| 0.5 | 0 | 164869.3 | 12.006% | 5.816932 | 31.505% | 0.161471 | 2.064385 | 0.278094 | 0.865495 | 85.228% |
| 1 | 0 | 177641.3 | 20.682% | 4.091634 | 51.821% | 0.088720 | 1.450030 | 0.287767 | 0.833560 | 79.558% |
| 2 | 0 | 196211.4 | 33.298% | 3.642485 | 57.109% | 0.075815 | 1.550589 | 0.363239 | 0.824267 | 77.363% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
