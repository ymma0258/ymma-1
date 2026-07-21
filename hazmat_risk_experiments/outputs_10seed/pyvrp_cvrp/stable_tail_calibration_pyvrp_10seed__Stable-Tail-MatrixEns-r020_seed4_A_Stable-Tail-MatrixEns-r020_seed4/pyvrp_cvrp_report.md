# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.129988 | 0.000% | 0.219422 | 2.001091 | 0.152577 | 0.879139 | 90.267% |
| 0.25 | 0 | 143063.3 | 6.765% | 5.608452 | 21.340% | 0.178444 | 1.698733 | 0.234377 | 0.876555 | 89.418% |
| 0.5 | 0 | 149954.2 | 11.908% | 4.043337 | 43.291% | 0.124005 | 1.325186 | 0.232178 | 0.854493 | 85.939% |
| 1 | 0 | 159393.5 | 18.952% | 2.850939 | 60.015% | 0.074437 | 0.826303 | 0.226576 | 0.818112 | 80.365% |
| 2 | 0 | 174284.7 | 30.065% | 2.323640 | 67.410% | 0.055299 | 0.851608 | 0.326323 | 0.794852 | 76.589% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
