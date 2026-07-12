# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.8 | 0.000% | 7.868667 | 0.000% | 0.223538 | 2.406528 | 0.193151 | 0.819111 | 85.201% |
| 0.25 | 0 | 156841.9 | 6.600% | 6.852777 | 12.911% | 0.167408 | 2.180546 | 0.198259 | 0.809855 | 84.277% |
| 0.5 | 0 | 166036.6 | 12.850% | 5.251354 | 33.262% | 0.123499 | 1.748728 | 0.236195 | 0.781331 | 80.002% |
| 1 | 0 | 179421.5 | 21.947% | 4.471479 | 43.174% | 0.107724 | 1.354989 | 0.192141 | 0.753415 | 76.594% |
| 2 | 0 | 199227.3 | 35.408% | 3.220328 | 59.074% | 0.065085 | 1.154819 | 0.255803 | 0.677706 | 66.700% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
