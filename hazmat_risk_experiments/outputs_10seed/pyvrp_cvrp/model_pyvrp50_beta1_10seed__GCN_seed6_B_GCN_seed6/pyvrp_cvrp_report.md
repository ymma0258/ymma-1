# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.087849 | 0.000% | 0.287981 | 3.104612 | 0.234715 | 0.869422 | 90.051% |
| 1 | 0 | 180960.0 | 23.328% | 4.669360 | 48.620% | 0.110511 | 1.629229 | 0.315009 | 0.840184 | 83.695% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
