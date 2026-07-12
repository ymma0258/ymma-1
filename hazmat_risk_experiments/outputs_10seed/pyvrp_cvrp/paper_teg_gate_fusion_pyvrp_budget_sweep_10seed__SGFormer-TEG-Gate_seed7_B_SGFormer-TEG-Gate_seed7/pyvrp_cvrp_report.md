# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 8.856498 | 0.000% | 0.273974 | 2.491374 | 0.175176 | 0.880052 | 88.929% |
| 0.25 | 0 | 157876.1 | 7.401% | 7.475561 | 15.592% | 0.232011 | 2.327644 | 0.260573 | 0.876748 | 87.498% |
| 0.5 | 0 | 166366.3 | 13.176% | 4.786379 | 45.956% | 0.127729 | 1.556392 | 0.265148 | 0.843994 | 81.771% |
| 1 | 0 | 177147.8 | 20.511% | 3.101412 | 64.982% | 0.071687 | 1.124645 | 0.314144 | 0.798390 | 73.438% |
| 2 | 0 | 193861.8 | 31.881% | 2.824670 | 68.106% | 0.060075 | 0.986954 | 0.296826 | 0.782153 | 70.869% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
