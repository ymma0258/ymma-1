# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.9 | 0.000% | 8.698935 | 0.000% | 0.264313 | 2.618999 | 0.185780 | 0.876189 | 89.486% |
| 0.25 | 0 | 156041.0 | 6.056% | 7.643810 | 12.129% | 0.213807 | 2.517301 | 0.228982 | 0.873364 | 88.711% |
| 0.5 | 0 | 164838.6 | 12.035% | 5.857113 | 32.669% | 0.161147 | 1.956077 | 0.264993 | 0.859513 | 85.822% |
| 1 | 0 | 175245.5 | 19.109% | 4.060125 | 53.326% | 0.102809 | 1.539300 | 0.292614 | 0.824978 | 80.706% |
| 2 | 0 | 191090.1 | 29.878% | 3.314305 | 61.900% | 0.067650 | 1.317889 | 0.308144 | 0.808054 | 77.805% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
