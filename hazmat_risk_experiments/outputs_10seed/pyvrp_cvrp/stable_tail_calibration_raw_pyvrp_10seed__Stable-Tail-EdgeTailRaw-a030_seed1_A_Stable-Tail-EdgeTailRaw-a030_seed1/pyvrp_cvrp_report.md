# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.5 | 0.000% | 10.003240 | 0.000% | 0.336067 | 2.758069 | 0.156419 | 0.872688 | 89.784% |
| 0.25 | 0 | 142222.9 | 5.770% | 6.958975 | 30.433% | 0.207515 | 2.181978 | 0.230465 | 0.870640 | 88.663% |
| 0.5 | 0 | 147677.8 | 9.827% | 5.054654 | 49.470% | 0.152271 | 1.752473 | 0.226142 | 0.847976 | 84.975% |
| 1 | 0 | 156192.1 | 16.159% | 3.377055 | 66.240% | 0.073671 | 1.173868 | 0.263377 | 0.797441 | 77.430% |
| 2 | 0 | 168493.1 | 25.307% | 2.717143 | 72.837% | 0.056348 | 0.750558 | 0.206752 | 0.773658 | 73.389% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
