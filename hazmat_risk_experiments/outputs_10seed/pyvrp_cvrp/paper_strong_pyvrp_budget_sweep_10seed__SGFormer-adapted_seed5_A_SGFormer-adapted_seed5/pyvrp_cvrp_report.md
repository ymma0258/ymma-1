# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.6 | 0.000% | 8.941383 | 0.000% | 0.307238 | 2.679328 | 0.193354 | 0.883994 | 89.585% |
| 0.25 | 0 | 141932.4 | 5.554% | 6.338528 | 29.110% | 0.195911 | 1.952657 | 0.210900 | 0.871301 | 86.701% |
| 0.5 | 0 | 147637.3 | 9.796% | 4.165562 | 53.413% | 0.097611 | 1.569615 | 0.306404 | 0.839715 | 81.202% |
| 1 | 0 | 154271.4 | 14.730% | 2.682537 | 69.999% | 0.052849 | 1.060521 | 0.268206 | 0.780813 | 72.277% |
| 2 | 0 | 163203.1 | 21.373% | 1.871364 | 79.071% | 0.025058 | 0.524497 | 0.200276 | 0.702828 | 60.908% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
