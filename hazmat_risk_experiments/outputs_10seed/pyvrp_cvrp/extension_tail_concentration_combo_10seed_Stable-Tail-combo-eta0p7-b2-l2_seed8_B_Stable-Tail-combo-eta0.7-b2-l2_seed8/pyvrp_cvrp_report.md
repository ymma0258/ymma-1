# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.420933 | 0.000% | 0.217788 | 2.362199 | 0.193787 | 0.878179 | 89.055% |
| 2 | 2 | 215320.3 | 46.745% | 2.302299 | 68.976% | 0.042662 | 0.964167 | 0.337696 | 0.770005 | 71.073% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
