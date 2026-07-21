# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147396.9 | 0.000% | 9.891853 | 0.000% | 0.313877 | 3.490620 | 0.270028 | 0.872593 | 89.943% |
| 0.25 | 0 | 156216.5 | 5.984% | 8.165166 | 17.456% | 0.241561 | 2.978176 | 0.250265 | 0.869062 | 88.790% |
| 0.5 | 0 | 164725.3 | 11.756% | 6.627611 | 32.999% | 0.175862 | 2.350439 | 0.248362 | 0.858933 | 86.745% |
| 1 | 0 | 174576.4 | 18.440% | 3.996998 | 59.593% | 0.084638 | 1.502789 | 0.282109 | 0.819609 | 79.766% |
| 2 | 0 | 188733.9 | 28.045% | 3.207131 | 67.578% | 0.065307 | 1.156724 | 0.265620 | 0.792053 | 75.252% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
