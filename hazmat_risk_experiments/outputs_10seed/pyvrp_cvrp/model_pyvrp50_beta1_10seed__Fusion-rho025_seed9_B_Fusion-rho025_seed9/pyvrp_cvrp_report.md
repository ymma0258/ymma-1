# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.565160 | 0.000% | 0.238006 | 2.879323 | 0.237559 | 0.857941 | 88.635% |
| 1 | 0 | 178401.8 | 21.584% | 3.872427 | 54.789% | 0.099273 | 1.441603 | 0.329676 | 0.793877 | 79.273% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
