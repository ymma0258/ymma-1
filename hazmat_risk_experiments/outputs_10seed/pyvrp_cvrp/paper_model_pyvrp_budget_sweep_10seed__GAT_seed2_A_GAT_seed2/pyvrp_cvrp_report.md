# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.7 | 0.000% | 8.519488 | 0.000% | 0.285044 | 2.792379 | 0.216347 | 0.876365 | 89.491% |
| 0.25 | 0 | 142637.2 | 6.341% | 6.010021 | 29.456% | 0.174083 | 1.879452 | 0.206592 | 0.869885 | 88.237% |
| 0.5 | 0 | 148833.9 | 10.961% | 4.735251 | 44.419% | 0.140602 | 1.600309 | 0.243908 | 0.855934 | 85.765% |
| 1 | 0 | 158346.1 | 18.053% | 3.450331 | 59.501% | 0.094791 | 1.335244 | 0.291070 | 0.820358 | 80.666% |
| 2 | 0 | 173405.7 | 29.280% | 2.968377 | 65.158% | 0.077988 | 1.192461 | 0.334817 | 0.805036 | 77.872% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
