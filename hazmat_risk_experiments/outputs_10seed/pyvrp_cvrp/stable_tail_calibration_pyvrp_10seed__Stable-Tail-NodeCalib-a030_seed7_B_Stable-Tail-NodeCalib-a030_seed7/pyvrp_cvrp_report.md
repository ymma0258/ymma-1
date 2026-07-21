# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 10.077910 | 0.000% | 0.299293 | 3.069896 | 0.188445 | 0.878542 | 90.545% |
| 0.25 | 0 | 157755.6 | 7.319% | 7.574208 | 24.843% | 0.224490 | 2.443777 | 0.230061 | 0.873981 | 88.734% |
| 0.5 | 0 | 166988.2 | 13.600% | 5.875808 | 41.696% | 0.161090 | 1.989109 | 0.245433 | 0.856343 | 85.605% |
| 1 | 0 | 178459.1 | 21.403% | 3.858514 | 61.713% | 0.084530 | 1.235409 | 0.214331 | 0.821375 | 79.340% |
| 2 | 0 | 195333.0 | 32.882% | 3.428220 | 65.983% | 0.070978 | 1.071958 | 0.216587 | 0.811939 | 77.614% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
