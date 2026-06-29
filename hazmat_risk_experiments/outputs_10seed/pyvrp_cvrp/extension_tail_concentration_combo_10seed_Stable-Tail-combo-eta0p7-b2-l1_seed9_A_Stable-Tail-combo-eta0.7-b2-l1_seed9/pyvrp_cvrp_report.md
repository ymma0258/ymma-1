# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.072629 | 0.000% | 0.224033 | 2.220910 | 0.199043 | 0.877152 | 89.589% |
| 2 | 1 | 174480.5 | 30.212% | 1.732694 | 75.501% | 0.030781 | 0.527269 | 0.222904 | 0.706149 | 64.314% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
