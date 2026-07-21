# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 9.499465 | 0.000% | 0.309215 | 2.804950 | 0.177010 | 0.883499 | 90.567% |
| 0.25 | 0 | 142149.1 | 6.083% | 6.381483 | 32.823% | 0.190604 | 2.116687 | 0.246203 | 0.874579 | 88.732% |
| 0.5 | 0 | 148057.4 | 10.492% | 4.841797 | 49.031% | 0.144513 | 1.719057 | 0.266159 | 0.859045 | 85.763% |
| 1 | 0 | 157052.9 | 17.205% | 3.483585 | 63.329% | 0.096450 | 1.384642 | 0.303100 | 0.821716 | 80.325% |
| 2 | 0 | 171036.3 | 27.641% | 3.074403 | 67.636% | 0.075044 | 1.412234 | 0.388485 | 0.807424 | 77.855% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
