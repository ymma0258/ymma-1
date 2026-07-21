# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.6 | 0.000% | 9.034588 | 0.000% | 0.284684 | 3.398022 | 0.309545 | 0.875235 | 89.634% |
| 0.25 | 0 | 156893.2 | 6.539% | 7.349199 | 18.655% | 0.213925 | 2.912723 | 0.311375 | 0.871744 | 88.660% |
| 0.5 | 0 | 165869.8 | 12.635% | 6.139415 | 32.045% | 0.161275 | 2.264260 | 0.257032 | 0.862933 | 87.103% |
| 1 | 0 | 178126.0 | 20.957% | 4.447065 | 50.777% | 0.116974 | 1.761761 | 0.302377 | 0.841773 | 83.026% |
| 2 | 0 | 196458.4 | 33.406% | 3.650730 | 59.592% | 0.092706 | 1.681976 | 0.367205 | 0.826619 | 80.006% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
