# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.7 | 0.000% | 7.669823 | 0.000% | 0.248791 | 2.356868 | 0.187883 | 0.876383 | 89.264% |
| 0.25 | 0 | 142440.8 | 6.090% | 5.039454 | 34.295% | 0.141112 | 1.658193 | 0.245606 | 0.856998 | 86.049% |
| 0.5 | 0 | 148092.7 | 10.299% | 3.705353 | 51.689% | 0.106804 | 1.390861 | 0.299239 | 0.831544 | 81.990% |
| 1 | 0 | 156011.0 | 16.197% | 2.672786 | 65.152% | 0.070956 | 1.003025 | 0.268826 | 0.785389 | 75.406% |
| 2 | 0 | 167037.8 | 24.409% | 1.910836 | 75.086% | 0.041692 | 0.643007 | 0.267583 | 0.721808 | 66.128% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
