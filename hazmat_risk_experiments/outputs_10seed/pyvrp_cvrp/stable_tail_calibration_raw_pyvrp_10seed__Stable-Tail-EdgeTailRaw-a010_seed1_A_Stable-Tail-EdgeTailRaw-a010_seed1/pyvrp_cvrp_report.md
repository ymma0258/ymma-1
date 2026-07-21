# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 9.475774 | 0.000% | 0.306853 | 2.642944 | 0.146341 | 0.872059 | 89.509% |
| 0.25 | 0 | 142133.4 | 5.808% | 6.541894 | 30.962% | 0.195442 | 1.817215 | 0.172012 | 0.865377 | 87.795% |
| 0.5 | 0 | 148184.9 | 10.313% | 4.999297 | 47.241% | 0.132806 | 1.639384 | 0.237690 | 0.848535 | 84.841% |
| 1 | 0 | 156385.0 | 16.417% | 3.267746 | 65.515% | 0.072153 | 1.126510 | 0.236739 | 0.793158 | 76.844% |
| 2 | 0 | 169146.3 | 25.917% | 2.728727 | 71.203% | 0.055180 | 0.843389 | 0.238988 | 0.769493 | 73.075% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
