# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.1 | 0.000% | 6.146128 | 0.000% | 0.181951 | 1.871289 | 0.195241 | 0.880017 | 90.784% |
| 0.25 | 0 | 157696.0 | 7.133% | 4.973659 | 19.077% | 0.146846 | 1.496136 | 0.193994 | 0.878096 | 89.780% |
| 0.5 | 0 | 167020.7 | 13.467% | 3.901457 | 36.522% | 0.111059 | 1.423192 | 0.269306 | 0.866497 | 87.185% |
| 1 | 0 | 178067.2 | 20.972% | 2.451914 | 60.106% | 0.060623 | 0.839212 | 0.263954 | 0.833616 | 81.063% |
| 2 | 0 | 194993.9 | 32.471% | 2.105521 | 65.742% | 0.050540 | 0.668021 | 0.215746 | 0.815299 | 78.030% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
