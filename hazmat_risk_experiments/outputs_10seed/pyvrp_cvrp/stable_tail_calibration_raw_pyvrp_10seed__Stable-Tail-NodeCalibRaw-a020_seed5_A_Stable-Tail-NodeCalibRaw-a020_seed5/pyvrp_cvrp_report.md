# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.1 | 0.000% | 7.352700 | 0.000% | 0.230303 | 2.241768 | 0.180464 | 0.870395 | 88.464% |
| 0.25 | 0 | 142739.3 | 6.206% | 4.902817 | 33.319% | 0.140938 | 1.663968 | 0.234948 | 0.854802 | 85.787% |
| 0.5 | 0 | 147968.5 | 10.097% | 3.685598 | 49.874% | 0.108191 | 1.338139 | 0.293116 | 0.825705 | 81.530% |
| 1 | 0 | 156338.1 | 16.325% | 2.497557 | 66.032% | 0.065467 | 0.887179 | 0.257019 | 0.772895 | 73.837% |
| 2 | 0 | 168182.1 | 25.137% | 1.836263 | 75.026% | 0.039025 | 0.602437 | 0.243722 | 0.708703 | 64.625% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
