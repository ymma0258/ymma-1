# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 11.002735 | 0.000% | 0.278194 | 3.121404 | 0.152338 | 0.856595 | 88.793% |
| 1 | 0 | 158805.0 | 18.514% | 4.169347 | 62.106% | 0.077055 | 1.449780 | 0.300881 | 0.768408 | 76.290% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
