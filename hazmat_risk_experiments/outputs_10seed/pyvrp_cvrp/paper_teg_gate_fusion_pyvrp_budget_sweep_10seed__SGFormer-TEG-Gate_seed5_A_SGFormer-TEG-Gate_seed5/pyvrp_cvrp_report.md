# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.2 | 0.000% | 7.869427 | 0.000% | 0.228108 | 2.358051 | 0.163999 | 0.862567 | 88.216% |
| 0.25 | 0 | 141801.2 | 5.823% | 5.909765 | 24.902% | 0.170905 | 1.855453 | 0.231035 | 0.855868 | 86.523% |
| 0.5 | 0 | 147532.9 | 10.101% | 4.038354 | 48.683% | 0.115957 | 1.258472 | 0.226257 | 0.826768 | 81.375% |
| 1 | 0 | 155013.4 | 15.683% | 2.586009 | 67.139% | 0.064562 | 0.864248 | 0.229751 | 0.755099 | 71.193% |
| 2 | 0 | 165997.8 | 23.881% | 2.061341 | 73.806% | 0.039774 | 0.659107 | 0.245070 | 0.706580 | 64.302% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
