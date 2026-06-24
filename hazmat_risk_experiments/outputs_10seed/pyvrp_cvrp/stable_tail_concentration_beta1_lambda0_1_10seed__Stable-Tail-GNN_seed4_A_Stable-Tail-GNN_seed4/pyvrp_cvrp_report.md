# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.651668 | 0.000% | 0.269117 | 2.477327 | 0.142433 | 0.874600 | 89.967% |
| 1 | 0 | 160054.1 | 19.445% | 3.409976 | 60.586% | 0.075068 | 1.160148 | 0.294724 | 0.811652 | 78.952% |
| 1 | 1 | 171317.5 | 27.851% | 2.660126 | 69.253% | 0.052335 | 1.099668 | 0.346765 | 0.767644 | 72.784% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
