# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.035681 | 0.000% | 0.219598 | 2.415906 | 0.234400 | 0.876974 | 89.513% |
| 0.5 | 0 | 164583.4 | 12.167% | 4.204350 | 40.242% | 0.098594 | 1.295623 | 0.207014 | 0.841356 | 83.593% |
| 1 | 0 | 174255.2 | 18.758% | 2.892914 | 58.882% | 0.068165 | 1.181970 | 0.354783 | 0.811699 | 78.206% |
| 1.5 | 0 | 182507.1 | 24.382% | 2.683686 | 61.856% | 0.062520 | 1.090547 | 0.323008 | 0.801332 | 76.604% |
| 2 | 0 | 190009.9 | 29.495% | 2.356972 | 66.500% | 0.054372 | 0.859464 | 0.305110 | 0.782381 | 73.420% |
| 3 | 0 | 203805.8 | 38.898% | 2.329434 | 66.891% | 0.053309 | 0.805378 | 0.281025 | 0.782422 | 73.397% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
