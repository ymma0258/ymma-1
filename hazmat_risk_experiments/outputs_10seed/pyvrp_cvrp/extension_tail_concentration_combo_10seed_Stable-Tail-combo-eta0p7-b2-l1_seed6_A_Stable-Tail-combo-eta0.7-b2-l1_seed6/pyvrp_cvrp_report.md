# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.736093 | 0.000% | 0.233101 | 2.305522 | 0.160077 | 0.879734 | 89.716% |
| 2 | 1 | 184943.5 | 38.020% | 2.072320 | 73.212% | 0.035386 | 1.022848 | 0.366342 | 0.747471 | 68.786% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
