# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.9 | 0.000% | 9.713763 | 0.000% | 0.286085 | 3.226406 | 0.223611 | 0.876630 | 90.407% |
| 0.25 | 0 | 157986.3 | 7.136% | 8.053984 | 17.087% | 0.235983 | 2.645774 | 0.244159 | 0.875836 | 89.325% |
| 0.5 | 0 | 167600.8 | 13.655% | 5.723120 | 41.082% | 0.161149 | 2.106480 | 0.272542 | 0.855015 | 85.473% |
| 1 | 0 | 178861.1 | 21.291% | 4.011477 | 58.703% | 0.105511 | 1.370459 | 0.260839 | 0.828570 | 80.438% |
| 2 | 0 | 195723.7 | 32.727% | 3.463994 | 64.339% | 0.083763 | 1.121017 | 0.228809 | 0.811912 | 77.629% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
