# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.568974 | 0.000% | 0.262828 | 2.785558 | 0.217033 | 0.837764 | 86.972% |
| 1 | 0 | 179230.8 | 22.316% | 3.454428 | 59.687% | 0.075527 | 1.194631 | 0.250039 | 0.695829 | 68.593% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
