# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.0 | 0.000% | 10.082160 | 0.000% | 0.301700 | 3.198609 | 0.210610 | 0.878580 | 90.721% |
| 0.25 | 0 | 158050.7 | 7.228% | 8.303309 | 17.644% | 0.232108 | 2.689091 | 0.223233 | 0.878340 | 89.749% |
| 0.5 | 0 | 167681.6 | 13.762% | 5.638216 | 44.077% | 0.153328 | 1.869133 | 0.240263 | 0.853822 | 85.248% |
| 1 | 0 | 178482.1 | 21.089% | 3.991216 | 60.413% | 0.103679 | 1.421632 | 0.270054 | 0.829408 | 80.408% |
| 2 | 0 | 195846.3 | 32.870% | 3.392459 | 66.352% | 0.081770 | 1.083673 | 0.241294 | 0.811607 | 77.326% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
