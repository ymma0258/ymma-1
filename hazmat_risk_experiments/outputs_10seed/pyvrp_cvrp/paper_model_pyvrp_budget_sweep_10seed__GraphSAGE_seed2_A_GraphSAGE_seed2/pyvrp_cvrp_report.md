# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.7 | 0.000% | 8.826474 | 0.000% | 0.291145 | 2.581143 | 0.172924 | 0.874254 | 89.404% |
| 0.25 | 0 | 142702.7 | 6.285% | 6.018017 | 31.819% | 0.176319 | 2.037266 | 0.249676 | 0.862607 | 87.289% |
| 0.5 | 0 | 149157.0 | 11.092% | 4.669855 | 47.093% | 0.131966 | 1.775175 | 0.288278 | 0.846493 | 84.153% |
| 1 | 0 | 158473.3 | 18.031% | 3.347607 | 62.073% | 0.082743 | 1.190247 | 0.294913 | 0.812456 | 78.600% |
| 2 | 0 | 172958.3 | 28.819% | 2.881842 | 67.350% | 0.063886 | 1.167230 | 0.345296 | 0.786837 | 74.717% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
