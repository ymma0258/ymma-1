# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.2 | 0.000% | 8.014476 | 0.000% | 0.252112 | 2.550552 | 0.205354 | 0.870487 | 89.883% |
| 0.25 | 0 | 158057.6 | 7.524% | 6.980706 | 12.899% | 0.201528 | 2.280279 | 0.222671 | 0.868903 | 89.476% |
| 0.5 | 0 | 167808.1 | 14.157% | 4.489478 | 43.983% | 0.118513 | 1.422360 | 0.231894 | 0.846128 | 84.920% |
| 1 | 0 | 179105.7 | 21.843% | 3.309750 | 58.703% | 0.071759 | 1.131810 | 0.286448 | 0.817530 | 80.057% |
| 2 | 0 | 196347.6 | 33.572% | 2.692035 | 66.410% | 0.053233 | 0.830758 | 0.230843 | 0.791048 | 76.094% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
