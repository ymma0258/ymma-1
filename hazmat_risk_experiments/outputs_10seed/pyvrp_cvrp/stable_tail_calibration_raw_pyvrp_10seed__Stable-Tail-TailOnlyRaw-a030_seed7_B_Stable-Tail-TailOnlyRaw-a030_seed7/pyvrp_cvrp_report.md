# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 11.378049 | 0.000% | 0.342663 | 3.314685 | 0.173532 | 0.885023 | 91.689% |
| 0.25 | 0 | 158403.7 | 7.662% | 9.240134 | 18.790% | 0.276155 | 2.930006 | 0.218993 | 0.884340 | 90.594% |
| 0.5 | 0 | 167767.9 | 14.027% | 6.832191 | 39.953% | 0.200335 | 2.352772 | 0.248138 | 0.870860 | 87.912% |
| 1 | 0 | 178932.3 | 21.615% | 4.524285 | 60.237% | 0.119132 | 1.704020 | 0.299700 | 0.846149 | 82.828% |
| 2 | 0 | 196057.1 | 33.254% | 3.813762 | 66.481% | 0.090900 | 1.251527 | 0.256024 | 0.829517 | 79.868% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
