# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 9.555685 | 0.000% | 0.288398 | 2.884522 | 0.180599 | 0.877719 | 90.562% |
| 0.25 | 0 | 157755.6 | 7.367% | 7.551576 | 20.973% | 0.222997 | 2.400105 | 0.216100 | 0.874967 | 89.316% |
| 0.5 | 0 | 166803.0 | 13.525% | 5.512538 | 42.311% | 0.153871 | 2.083245 | 0.281167 | 0.855953 | 85.594% |
| 1 | 0 | 178334.5 | 21.373% | 3.818212 | 60.043% | 0.098059 | 1.324791 | 0.286341 | 0.830586 | 80.675% |
| 2 | 0 | 195098.6 | 32.783% | 3.302750 | 65.437% | 0.079581 | 1.022141 | 0.211858 | 0.813361 | 78.058% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
