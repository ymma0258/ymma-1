# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 12.319116 | 0.000% | 0.258518 | 3.355540 | 0.131401 | 0.844401 | 87.921% |
| 1.5 | 1 | 184008.3 | 37.322% | 3.727296 | 69.744% | 0.050664 | 1.396657 | 0.315956 | 0.674041 | 65.510% |
| 2 | 1 | 191475.0 | 42.894% | 3.698972 | 69.974% | 0.049395 | 1.537380 | 0.341793 | 0.670615 | 65.159% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
