# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.4 | 0.000% | 9.772170 | 0.000% | 0.320104 | 2.974760 | 0.182702 | 0.885471 | 90.653% |
| 0.25 | 0 | 144357.0 | 7.357% | 6.803787 | 30.376% | 0.208433 | 2.152477 | 0.225441 | 0.880287 | 89.552% |
| 0.5 | 0 | 151370.4 | 12.573% | 4.947398 | 49.373% | 0.127214 | 1.661231 | 0.273366 | 0.861895 | 86.256% |
| 1 | 0 | 162155.7 | 20.594% | 3.437528 | 64.823% | 0.083198 | 1.290068 | 0.330400 | 0.827999 | 80.499% |
| 2 | 0 | 176689.6 | 31.403% | 2.555291 | 73.851% | 0.058167 | 1.061535 | 0.363030 | 0.786423 | 74.133% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
