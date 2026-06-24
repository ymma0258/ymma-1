# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.535550 | 0.000% | 0.210085 | 2.330493 | 0.179790 | 0.835901 | 86.235% |
| 1 | 0 | 158711.7 | 18.444% | 3.022258 | 59.893% | 0.066419 | 0.959614 | 0.200004 | 0.704070 | 69.427% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
