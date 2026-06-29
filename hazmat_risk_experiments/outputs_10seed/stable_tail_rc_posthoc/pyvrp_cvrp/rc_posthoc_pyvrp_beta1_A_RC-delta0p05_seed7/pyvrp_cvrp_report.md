# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.828291 | 0.000% | 0.274772 | 2.502279 | 0.146765 | 0.874238 | 89.711% |
| 1 | 0 | 158473.0 | 18.266% | 3.234511 | 63.362% | 0.071957 | 1.206981 | 0.289372 | 0.803086 | 77.268% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
