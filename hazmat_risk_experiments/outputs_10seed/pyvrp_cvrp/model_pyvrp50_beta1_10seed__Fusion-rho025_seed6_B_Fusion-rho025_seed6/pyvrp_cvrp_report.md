# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.944080 | 0.000% | 0.281356 | 3.019661 | 0.228286 | 0.862987 | 89.394% |
| 1 | 0 | 180448.8 | 22.979% | 4.516028 | 49.508% | 0.102169 | 1.550232 | 0.292451 | 0.825126 | 82.463% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
