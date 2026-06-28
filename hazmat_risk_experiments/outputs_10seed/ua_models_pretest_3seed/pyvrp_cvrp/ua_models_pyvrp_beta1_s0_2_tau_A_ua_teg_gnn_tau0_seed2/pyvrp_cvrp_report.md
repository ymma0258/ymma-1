# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 4.037168 | 0.000% | 0.139001 | 1.159442 | 0.145172 | 0.871451 | 89.393% |
| 1 | 0 | 154658.3 | 15.419% | 1.925593 | 52.303% | 0.056646 | 0.569686 | 0.193691 | 0.828400 | 82.520% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
