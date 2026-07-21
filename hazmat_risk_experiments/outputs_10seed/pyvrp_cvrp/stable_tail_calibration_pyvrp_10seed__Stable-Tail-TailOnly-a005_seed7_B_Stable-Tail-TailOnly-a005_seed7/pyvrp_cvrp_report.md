# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.7 | 0.000% | 9.759910 | 0.000% | 0.290108 | 3.249608 | 0.214962 | 0.878426 | 90.519% |
| 0.25 | 0 | 158361.6 | 7.390% | 8.119788 | 16.805% | 0.235226 | 2.796304 | 0.250317 | 0.875828 | 89.460% |
| 0.5 | 0 | 167403.5 | 13.522% | 5.674614 | 41.858% | 0.160706 | 1.990795 | 0.255513 | 0.854238 | 85.376% |
| 1 | 0 | 179183.2 | 21.510% | 3.958756 | 59.439% | 0.100429 | 1.333236 | 0.221723 | 0.826130 | 80.088% |
| 2 | 0 | 196253.8 | 33.086% | 3.448226 | 64.669% | 0.080395 | 1.129092 | 0.232098 | 0.812355 | 77.676% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
