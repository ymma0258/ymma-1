# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.9 | 0.000% | 7.932990 | 0.000% | 0.247704 | 2.622501 | 0.226035 | 0.876445 | 89.296% |
| 0.25 | 0 | 155975.1 | 6.059% | 6.769923 | 14.661% | 0.170218 | 2.241592 | 0.220627 | 0.873227 | 88.649% |
| 0.5 | 0 | 164217.3 | 11.664% | 5.432401 | 31.521% | 0.128871 | 1.697865 | 0.204406 | 0.855436 | 85.824% |
| 1 | 0 | 174479.5 | 18.642% | 3.596292 | 54.667% | 0.090670 | 1.200137 | 0.267476 | 0.821228 | 80.103% |
| 2 | 0 | 190030.3 | 29.216% | 2.915747 | 63.245% | 0.071645 | 0.993843 | 0.294888 | 0.800158 | 76.346% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
