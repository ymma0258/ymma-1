# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.651668 | 0.000% | 0.269117 | 2.477327 | 0.142433 | 0.874600 | 89.967% |
| 3 | 1 | 201600.5 | 50.451% | 2.343049 | 72.918% | 0.043202 | 1.099400 | 0.368948 | 0.731660 | 67.859% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
