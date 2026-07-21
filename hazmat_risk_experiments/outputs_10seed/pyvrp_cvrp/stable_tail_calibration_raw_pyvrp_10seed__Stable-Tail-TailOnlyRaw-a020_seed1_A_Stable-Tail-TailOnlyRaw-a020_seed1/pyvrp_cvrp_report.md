# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.4 | 0.000% | 9.940318 | 0.000% | 0.325379 | 2.783430 | 0.164302 | 0.875959 | 90.402% |
| 0.25 | 0 | 141837.4 | 5.483% | 6.911397 | 30.471% | 0.213924 | 2.090715 | 0.197595 | 0.870269 | 88.599% |
| 0.5 | 0 | 147813.9 | 9.928% | 5.192032 | 47.768% | 0.146975 | 1.797786 | 0.245213 | 0.853562 | 85.522% |
| 1 | 0 | 156140.0 | 16.120% | 3.509937 | 64.690% | 0.089982 | 1.203456 | 0.249892 | 0.804561 | 78.421% |
| 2 | 0 | 168655.0 | 25.427% | 2.779400 | 72.039% | 0.059754 | 0.797686 | 0.221035 | 0.777891 | 74.051% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
