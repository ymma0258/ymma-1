# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.5 | 0.000% | 8.324698 | 0.000% | 0.260926 | 2.535350 | 0.180508 | 0.865514 | 88.316% |
| 0.25 | 0 | 143064.7 | 6.501% | 5.238522 | 37.073% | 0.156897 | 1.691318 | 0.210667 | 0.844796 | 86.164% |
| 0.5 | 0 | 149191.7 | 11.062% | 4.142831 | 50.234% | 0.120179 | 1.448352 | 0.244740 | 0.821167 | 83.058% |
| 1 | 0 | 157997.8 | 17.618% | 2.838025 | 65.908% | 0.070368 | 0.811483 | 0.181649 | 0.760589 | 75.185% |
| 2 | 0 | 172450.7 | 28.377% | 2.461121 | 70.436% | 0.048998 | 0.733075 | 0.193085 | 0.739346 | 71.530% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
