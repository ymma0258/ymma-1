# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.8 | 0.000% | 8.620763 | 0.000% | 0.250709 | 2.742046 | 0.221382 | 0.856681 | 88.586% |
| 0.25 | 0 | 158323.7 | 7.607% | 7.424714 | 13.874% | 0.205629 | 2.528295 | 0.228279 | 0.855776 | 88.350% |
| 0.5 | 0 | 168535.4 | 14.548% | 6.330553 | 26.566% | 0.170834 | 2.156396 | 0.241634 | 0.849932 | 86.593% |
| 1 | 0 | 184107.0 | 25.132% | 4.815817 | 44.137% | 0.110409 | 1.977530 | 0.329769 | 0.825239 | 82.841% |
| 2 | 0 | 205612.0 | 39.748% | 3.547762 | 58.846% | 0.075894 | 1.478770 | 0.352227 | 0.789650 | 76.868% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
