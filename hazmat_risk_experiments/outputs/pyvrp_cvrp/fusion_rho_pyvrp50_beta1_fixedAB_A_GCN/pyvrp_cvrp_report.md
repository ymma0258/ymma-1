# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.4 | 0.000% | 6.901845 | 0.000% | 0.199384 | 2.335080 | 0.226010 | 0.859819 | 88.450% |
| 1 | 156975.8 | 17.148% | 2.507068 | 63.675% | 0.052613 | 0.790557 | 0.218823 | 0.759431 | 74.105% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
