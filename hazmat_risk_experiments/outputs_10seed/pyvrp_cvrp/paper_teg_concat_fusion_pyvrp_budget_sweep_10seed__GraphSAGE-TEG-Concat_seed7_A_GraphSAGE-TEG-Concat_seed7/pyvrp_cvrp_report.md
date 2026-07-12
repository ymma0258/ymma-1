# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.8 | 0.000% | 10.388360 | 0.000% | 0.345614 | 2.992704 | 0.160197 | 0.870031 | 89.454% |
| 0.25 | 0 | 143309.2 | 6.631% | 7.872749 | 24.216% | 0.225790 | 2.739064 | 0.240895 | 0.870980 | 89.050% |
| 0.5 | 0 | 150139.0 | 11.712% | 5.698319 | 45.147% | 0.164990 | 2.022986 | 0.232964 | 0.847294 | 85.081% |
| 1 | 0 | 160730.0 | 19.593% | 4.090976 | 60.620% | 0.102068 | 1.390081 | 0.253214 | 0.817872 | 79.893% |
| 2 | 0 | 175759.4 | 30.776% | 3.093410 | 70.222% | 0.070326 | 1.283674 | 0.319561 | 0.780754 | 73.866% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
