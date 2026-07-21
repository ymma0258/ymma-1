# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134531.0 | 0.000% | 10.190173 | 0.000% | 0.341601 | 3.029302 | 0.185654 | 0.876445 | 89.576% |
| 0.25 | 0 | 143583.3 | 6.729% | 6.897533 | 32.312% | 0.210082 | 2.411446 | 0.260774 | 0.873499 | 88.513% |
| 0.5 | 0 | 149462.6 | 11.099% | 4.947203 | 51.451% | 0.141586 | 1.824630 | 0.269847 | 0.845882 | 84.517% |
| 1 | 0 | 158791.5 | 18.033% | 3.652596 | 64.156% | 0.103342 | 1.493655 | 0.314881 | 0.812334 | 79.240% |
| 2 | 0 | 171721.9 | 27.645% | 2.782966 | 72.690% | 0.065923 | 0.961650 | 0.263109 | 0.776066 | 73.449% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
