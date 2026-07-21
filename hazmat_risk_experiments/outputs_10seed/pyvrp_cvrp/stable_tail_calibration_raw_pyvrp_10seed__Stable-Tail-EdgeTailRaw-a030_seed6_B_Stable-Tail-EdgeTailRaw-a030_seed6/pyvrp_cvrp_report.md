# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.2 | 0.000% | 9.538585 | 0.000% | 0.284107 | 3.298262 | 0.243554 | 0.873704 | 89.849% |
| 0.25 | 0 | 157925.6 | 7.288% | 8.328015 | 12.691% | 0.203806 | 2.630327 | 0.224981 | 0.874185 | 89.910% |
| 0.5 | 0 | 168432.4 | 14.426% | 6.798129 | 28.730% | 0.170380 | 2.373154 | 0.262172 | 0.867116 | 87.879% |
| 1 | 0 | 181300.5 | 23.168% | 4.277848 | 55.152% | 0.107503 | 1.592060 | 0.312652 | 0.830715 | 81.447% |
| 2 | 0 | 201930.1 | 37.183% | 3.894549 | 59.171% | 0.100909 | 1.443019 | 0.343305 | 0.824499 | 80.100% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
