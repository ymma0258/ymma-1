# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.6 | 0.000% | 8.444786 | 0.000% | 0.248875 | 2.752263 | 0.218824 | 0.873597 | 89.101% |
| 0.25 | 0 | 156148.0 | 6.225% | 7.311319 | 13.422% | 0.205319 | 2.229621 | 0.192146 | 0.869298 | 88.103% |
| 0.5 | 0 | 164702.7 | 12.044% | 5.579043 | 33.935% | 0.146406 | 1.968086 | 0.266069 | 0.851941 | 85.040% |
| 1 | 0 | 174957.5 | 19.021% | 3.856398 | 54.334% | 0.096768 | 1.496806 | 0.309238 | 0.816949 | 79.493% |
| 2 | 0 | 191408.2 | 30.212% | 3.136911 | 62.854% | 0.065728 | 1.224911 | 0.297514 | 0.797474 | 76.265% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
