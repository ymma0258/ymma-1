# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 7.474742 | 0.000% | 0.204190 | 2.529200 | 0.248802 | 0.877333 | 89.339% |
| 0.25 | 0 | 156402.2 | 6.495% | 6.367863 | 14.808% | 0.155791 | 2.296319 | 0.264657 | 0.872344 | 88.470% |
| 0.5 | 0 | 165149.5 | 12.451% | 4.427166 | 40.772% | 0.112744 | 1.461531 | 0.231328 | 0.848932 | 84.238% |
| 1 | 0 | 175368.0 | 19.409% | 2.997979 | 59.892% | 0.068606 | 1.087398 | 0.292458 | 0.805810 | 77.350% |
| 2 | 0 | 190814.9 | 29.926% | 2.464773 | 67.025% | 0.052477 | 0.949187 | 0.292001 | 0.782279 | 73.079% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
