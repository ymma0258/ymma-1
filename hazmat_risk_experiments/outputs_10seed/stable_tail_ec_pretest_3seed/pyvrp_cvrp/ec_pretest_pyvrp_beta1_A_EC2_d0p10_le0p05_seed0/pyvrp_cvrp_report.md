# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.137419 | 0.000% | 0.261622 | 2.318758 | 0.150592 | 0.864326 | 89.556% |
| 1 | 0 | 161146.6 | 20.261% | 3.267545 | 59.845% | 0.078164 | 1.007268 | 0.221729 | 0.803263 | 78.981% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
