# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.803669 | 0.000% | 0.278188 | 2.639760 | 0.155480 | 0.875826 | 90.106% |
| 1 | 0 | 160054.1 | 19.446% | 3.409976 | 61.266% | 0.075068 | 1.160148 | 0.294724 | 0.811652 | 78.952% |
| 1 | 0.5 | 166051.4 | 23.921% | 2.821856 | 67.947% | 0.055475 | 1.068021 | 0.342513 | 0.783929 | 74.993% |
| 1 | 1 | 171288.0 | 27.829% | 2.634154 | 70.079% | 0.051736 | 1.101809 | 0.351699 | 0.766440 | 72.589% |
| 1 | 2 | 180105.5 | 34.410% | 2.461192 | 72.044% | 0.048853 | 1.109419 | 0.350825 | 0.752197 | 70.441% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
