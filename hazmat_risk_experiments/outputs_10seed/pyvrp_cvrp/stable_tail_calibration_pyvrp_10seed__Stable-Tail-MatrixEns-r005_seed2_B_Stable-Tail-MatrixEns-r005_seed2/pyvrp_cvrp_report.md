# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 8.276526 | 0.000% | 0.256625 | 3.118757 | 0.303517 | 0.873271 | 89.410% |
| 0.25 | 0 | 156511.6 | 6.521% | 7.173657 | 13.325% | 0.220400 | 2.726611 | 0.312753 | 0.871613 | 88.847% |
| 0.5 | 0 | 165069.0 | 12.345% | 5.861796 | 29.176% | 0.163433 | 2.214022 | 0.278548 | 0.861671 | 87.054% |
| 1 | 0 | 177690.3 | 20.935% | 4.155529 | 49.791% | 0.110935 | 1.648904 | 0.306155 | 0.842767 | 83.084% |
| 2 | 0 | 196553.7 | 33.773% | 3.361501 | 59.385% | 0.083490 | 1.544627 | 0.362210 | 0.823128 | 79.621% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
