# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 9.263978 | 0.000% | 0.304620 | 2.641327 | 0.177802 | 0.872596 | 89.080% |
| 0.25 | 0 | 143356.4 | 6.719% | 5.960098 | 35.664% | 0.176791 | 1.844126 | 0.200309 | 0.855960 | 86.540% |
| 0.5 | 0 | 149429.4 | 11.239% | 4.820114 | 47.969% | 0.139889 | 1.697660 | 0.249032 | 0.837673 | 83.720% |
| 1 | 0 | 158583.8 | 18.054% | 3.323605 | 64.123% | 0.087455 | 1.335597 | 0.277125 | 0.796882 | 77.146% |
| 2 | 0 | 171994.9 | 28.038% | 2.567725 | 72.283% | 0.054262 | 0.829726 | 0.230020 | 0.761293 | 71.346% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
