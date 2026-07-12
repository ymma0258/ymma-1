# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.7 | 0.000% | 8.179873 | 0.000% | 0.265950 | 2.421412 | 0.192390 | 0.879844 | 90.024% |
| 0.25 | 0 | 143332.8 | 6.967% | 5.588004 | 31.686% | 0.152072 | 2.099846 | 0.282620 | 0.868036 | 87.461% |
| 0.5 | 0 | 149492.2 | 11.563% | 4.423287 | 45.925% | 0.129411 | 1.828116 | 0.311804 | 0.846819 | 84.855% |
| 1 | 0 | 158806.8 | 18.515% | 3.166696 | 61.287% | 0.086866 | 1.247967 | 0.300439 | 0.809446 | 78.796% |
| 2 | 0 | 171007.3 | 27.620% | 2.201281 | 73.089% | 0.051609 | 0.729493 | 0.257370 | 0.752936 | 70.431% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
