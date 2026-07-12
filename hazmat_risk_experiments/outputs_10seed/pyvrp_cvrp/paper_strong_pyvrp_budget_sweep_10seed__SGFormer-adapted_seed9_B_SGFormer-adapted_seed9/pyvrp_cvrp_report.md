# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.6 | 0.000% | 6.686262 | 0.000% | 0.192688 | 2.376002 | 0.272554 | 0.879406 | 88.180% |
| 0.25 | 0 | 155182.7 | 5.330% | 5.053568 | 24.419% | 0.122695 | 1.749385 | 0.256861 | 0.867712 | 85.509% |
| 0.5 | 0 | 161440.2 | 9.577% | 2.596021 | 61.174% | 0.055867 | 0.852869 | 0.200520 | 0.779051 | 72.775% |
| 1 | 0 | 167858.1 | 13.933% | 2.084478 | 68.824% | 0.043415 | 0.572403 | 0.151140 | 0.746270 | 67.863% |
| 2 | 0 | 178242.1 | 20.981% | 1.511546 | 77.393% | 0.026768 | 0.440001 | 0.173974 | 0.679306 | 56.979% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
