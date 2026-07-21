# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.1 | 0.000% | 7.923364 | 0.000% | 0.243724 | 2.545950 | 0.205172 | 0.871317 | 88.942% |
| 0.25 | 0 | 156644.8 | 6.418% | 6.739925 | 14.936% | 0.191421 | 2.242757 | 0.231504 | 0.867846 | 87.953% |
| 0.5 | 0 | 165169.8 | 12.210% | 5.217298 | 34.153% | 0.136962 | 1.717167 | 0.259576 | 0.852647 | 84.943% |
| 1 | 0 | 175555.8 | 19.266% | 3.668410 | 53.701% | 0.086216 | 1.381785 | 0.299382 | 0.819363 | 79.894% |
| 2 | 0 | 191896.4 | 30.367% | 2.872268 | 63.749% | 0.056943 | 1.135177 | 0.319609 | 0.794487 | 75.996% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
