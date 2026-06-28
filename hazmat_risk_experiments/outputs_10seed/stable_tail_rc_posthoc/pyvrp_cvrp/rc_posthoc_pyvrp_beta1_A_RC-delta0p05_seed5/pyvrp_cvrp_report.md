# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.255081 | 0.000% | 0.178421 | 1.822616 | 0.170778 | 0.873504 | 89.005% |
| 1 | 0 | 155621.4 | 16.137% | 2.553050 | 59.184% | 0.069169 | 0.920873 | 0.281685 | 0.796322 | 76.803% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
