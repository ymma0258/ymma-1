# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.570464 | 0.000% | 0.208857 | 2.743691 | 0.204223 | 0.879014 | 89.656% |
| 1 | 0 | 153911.2 | 14.861% | 2.542940 | 70.329% | 0.048334 | 0.915372 | 0.237289 | 0.756409 | 71.413% |
| 2 | 0 | 164540.6 | 22.794% | 2.199554 | 74.336% | 0.038775 | 0.703234 | 0.230687 | 0.729432 | 67.507% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
