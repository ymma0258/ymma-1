# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.7 | 0.000% | 7.916345 | 0.000% | 0.244008 | 2.474485 | 0.211581 | 0.882766 | 90.123% |
| 0.25 | 0 | 142503.1 | 6.031% | 4.744094 | 40.072% | 0.142143 | 1.525607 | 0.216737 | 0.862441 | 86.552% |
| 0.5 | 0 | 148496.5 | 10.490% | 3.591026 | 54.638% | 0.096636 | 1.289579 | 0.268868 | 0.833975 | 82.538% |
| 1 | 0 | 156094.1 | 16.143% | 2.413269 | 69.515% | 0.051527 | 0.954155 | 0.279375 | 0.783753 | 75.077% |
| 2 | 0 | 168516.2 | 25.386% | 1.801525 | 77.243% | 0.034857 | 0.543942 | 0.200119 | 0.727627 | 66.337% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
