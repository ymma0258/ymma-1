# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 4.851563 | 0.000% | 0.143237 | 1.436143 | 0.169173 | 0.872164 | 88.862% |
| 0.25 | 0 | 141808.6 | 5.829% | 3.536140 | 27.113% | 0.102306 | 1.092016 | 0.198282 | 0.862813 | 87.357% |
| 0.5 | 0 | 147067.2 | 9.753% | 2.541837 | 47.608% | 0.072679 | 0.832178 | 0.227165 | 0.834842 | 83.227% |
| 1 | 0 | 154885.8 | 15.588% | 1.569264 | 67.654% | 0.040137 | 0.474243 | 0.230055 | 0.758353 | 72.603% |
| 2 | 0 | 166699.9 | 24.405% | 1.494290 | 69.200% | 0.036309 | 0.474985 | 0.268704 | 0.750744 | 71.361% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
