# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.0 | 0.000% | 9.482837 | 0.000% | 0.284113 | 3.005184 | 0.202979 | 0.880765 | 91.655% |
| 0.25 | 0 | 157836.3 | 7.179% | 7.764281 | 18.123% | 0.231783 | 2.474715 | 0.214916 | 0.883368 | 90.867% |
| 0.5 | 0 | 167401.1 | 13.674% | 6.068139 | 36.009% | 0.179053 | 2.022489 | 0.239360 | 0.875674 | 88.644% |
| 1 | 0 | 179608.2 | 21.963% | 4.336582 | 54.269% | 0.117744 | 1.691469 | 0.299534 | 0.857970 | 84.548% |
| 2 | 0 | 198897.0 | 35.062% | 3.365494 | 64.510% | 0.079586 | 1.050539 | 0.251114 | 0.841477 | 80.089% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
