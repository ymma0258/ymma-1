# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.021509 | 0.000% | 0.246099 | 2.667315 | 0.224341 | 0.854309 | 88.115% |
| 0.25 | 0 | 156191.0 | 6.447% | 6.676106 | 16.772% | 0.159423 | 2.168503 | 0.225793 | 0.850114 | 87.193% |
| 0.5 | 0 | 164718.3 | 12.259% | 5.903707 | 26.402% | 0.145660 | 1.762577 | 0.175645 | 0.845149 | 86.006% |
| 1 | 0 | 176449.4 | 20.254% | 3.501387 | 56.350% | 0.084508 | 1.205867 | 0.263175 | 0.787702 | 77.619% |
| 2 | 0 | 191379.1 | 30.429% | 2.758185 | 65.615% | 0.057898 | 0.833780 | 0.221766 | 0.749171 | 71.843% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
