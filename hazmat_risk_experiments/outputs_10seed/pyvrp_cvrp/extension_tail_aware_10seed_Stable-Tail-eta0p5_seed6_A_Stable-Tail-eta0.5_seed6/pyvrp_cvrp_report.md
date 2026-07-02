# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 10.303378 | 0.000% | 0.201300 | 3.051435 | 0.161247 | 0.880746 | 89.593% |
| 1 | 0 | 159608.9 | 19.113% | 3.730368 | 63.795% | 0.053948 | 1.348816 | 0.352871 | 0.805006 | 76.365% |
| 2 | 0 | 174148.0 | 29.964% | 3.104819 | 69.866% | 0.041744 | 1.301963 | 0.333777 | 0.775500 | 72.526% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
