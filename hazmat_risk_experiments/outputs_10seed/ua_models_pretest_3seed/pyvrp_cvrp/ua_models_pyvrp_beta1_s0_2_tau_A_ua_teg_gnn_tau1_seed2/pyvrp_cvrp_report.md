# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 16.836607 | 0.000% | 0.259036 | 4.479026 | 0.135498 | 0.809369 | 84.701% |
| 1 | 0 | 167632.3 | 25.101% | 7.685578 | 54.352% | 0.035354 | 2.377360 | 0.213356 | 0.711058 | 72.234% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
