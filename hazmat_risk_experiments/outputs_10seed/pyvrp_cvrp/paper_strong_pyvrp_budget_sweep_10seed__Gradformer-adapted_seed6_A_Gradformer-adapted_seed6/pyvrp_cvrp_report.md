# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 8.297847 | 0.000% | 0.266942 | 2.323832 | 0.147235 | 0.860335 | 88.760% |
| 0.25 | 0 | 144541.2 | 7.815% | 6.057527 | 26.999% | 0.165024 | 1.852733 | 0.213404 | 0.848108 | 86.639% |
| 0.5 | 0 | 152278.9 | 13.586% | 4.060323 | 51.068% | 0.111704 | 1.304137 | 0.248517 | 0.808021 | 80.622% |
| 1 | 0 | 163243.6 | 21.765% | 3.433884 | 58.617% | 0.091771 | 1.107295 | 0.248692 | 0.787105 | 77.353% |
| 2 | 0 | 180142.8 | 34.370% | 2.327793 | 71.947% | 0.042029 | 1.053500 | 0.363704 | 0.711077 | 66.925% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
