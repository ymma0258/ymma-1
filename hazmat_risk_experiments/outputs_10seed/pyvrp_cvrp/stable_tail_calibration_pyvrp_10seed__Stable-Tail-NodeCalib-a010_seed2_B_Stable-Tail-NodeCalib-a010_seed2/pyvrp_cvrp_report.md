# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 8.784810 | 0.000% | 0.272515 | 3.325678 | 0.305625 | 0.873946 | 89.459% |
| 0.25 | 0 | 156511.7 | 6.472% | 7.470780 | 14.958% | 0.225867 | 2.849721 | 0.321028 | 0.872175 | 88.884% |
| 0.5 | 0 | 165128.3 | 12.334% | 5.679954 | 35.343% | 0.156191 | 2.139520 | 0.250704 | 0.854734 | 85.912% |
| 1 | 0 | 177422.1 | 20.698% | 4.403596 | 49.873% | 0.116740 | 1.713877 | 0.293347 | 0.841087 | 82.912% |
| 2 | 0 | 196301.3 | 33.541% | 3.486928 | 60.307% | 0.086602 | 1.682175 | 0.393185 | 0.822563 | 79.345% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
