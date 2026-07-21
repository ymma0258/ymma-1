# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.8 | 0.000% | 7.505580 | 0.000% | 0.231667 | 2.266551 | 0.185111 | 0.858898 | 87.633% |
| 0.25 | 0 | 156513.8 | 6.426% | 6.133275 | 18.284% | 0.144510 | 1.916510 | 0.183458 | 0.853408 | 86.531% |
| 0.5 | 0 | 164694.8 | 11.989% | 4.834978 | 35.582% | 0.119931 | 1.554320 | 0.219280 | 0.839344 | 83.744% |
| 1 | 0 | 175865.9 | 19.585% | 3.003274 | 59.986% | 0.067283 | 0.918933 | 0.183418 | 0.781515 | 75.134% |
| 2 | 0 | 190639.3 | 29.630% | 2.518344 | 66.447% | 0.050696 | 0.691309 | 0.170647 | 0.754091 | 71.024% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
