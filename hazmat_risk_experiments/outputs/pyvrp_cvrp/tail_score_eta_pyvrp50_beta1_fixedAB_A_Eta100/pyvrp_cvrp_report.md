# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.4 | 0.000% | 12.395042 | 0.000% | 0.213959 | 3.650433 | 0.193636 | 0.831343 | 86.224% |
| 1 | 161440.0 | 20.480% | 4.832297 | 61.014% | 0.049091 | 1.810985 | 0.235601 | 0.691082 | 67.389% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
