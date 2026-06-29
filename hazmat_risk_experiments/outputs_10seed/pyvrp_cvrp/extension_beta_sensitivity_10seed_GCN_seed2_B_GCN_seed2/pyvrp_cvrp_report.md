# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.702564 | 0.000% | 0.301776 | 3.363959 | 0.257524 | 0.865768 | 89.860% |
| 0.5 | 0 | 167145.8 | 13.913% | 7.334602 | 24.406% | 0.193083 | 2.326277 | 0.225835 | 0.860474 | 87.993% |
| 1 | 0 | 180857.3 | 23.258% | 4.931109 | 49.177% | 0.136447 | 1.942191 | 0.324426 | 0.839113 | 83.738% |
| 1.5 | 0 | 191433.6 | 30.466% | 4.155225 | 57.174% | 0.109037 | 1.681723 | 0.310633 | 0.819817 | 80.685% |
| 2 | 0 | 201128.3 | 37.073% | 3.903245 | 59.771% | 0.095031 | 1.678614 | 0.340750 | 0.812657 | 79.476% |
| 3 | 0 | 219526.0 | 49.611% | 3.695923 | 61.908% | 0.086196 | 1.612275 | 0.325271 | 0.805477 | 78.223% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
