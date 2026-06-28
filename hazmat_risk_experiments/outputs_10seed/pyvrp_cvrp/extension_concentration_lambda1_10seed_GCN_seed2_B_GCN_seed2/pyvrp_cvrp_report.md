# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.702564 | 0.000% | 0.301776 | 3.363959 | 0.257524 | 0.865768 | 89.860% |
| 1 | 0 | 180791.2 | 23.213% | 4.997998 | 48.488% | 0.139483 | 1.910272 | 0.307068 | 0.840048 | 83.943% |
| 1 | 1 | 197545.0 | 34.631% | 4.008726 | 58.684% | 0.103034 | 1.625715 | 0.270821 | 0.815162 | 79.985% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
