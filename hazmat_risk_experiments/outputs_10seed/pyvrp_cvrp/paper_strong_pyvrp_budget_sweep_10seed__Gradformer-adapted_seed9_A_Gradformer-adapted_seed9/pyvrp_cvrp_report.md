# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 8.020537 | 0.000% | 0.235421 | 2.211437 | 0.152933 | 0.859626 | 88.728% |
| 0.25 | 0 | 144314.5 | 7.645% | 5.685791 | 29.110% | 0.167414 | 1.868375 | 0.246603 | 0.845727 | 86.682% |
| 0.5 | 0 | 151876.2 | 13.286% | 4.588833 | 42.786% | 0.125350 | 1.622437 | 0.245392 | 0.828857 | 84.052% |
| 1 | 0 | 163365.1 | 21.856% | 3.571946 | 55.465% | 0.084161 | 1.212107 | 0.293215 | 0.797069 | 79.633% |
| 2 | 0 | 181813.0 | 35.616% | 2.501878 | 68.807% | 0.048464 | 0.979181 | 0.350357 | 0.739008 | 70.783% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
