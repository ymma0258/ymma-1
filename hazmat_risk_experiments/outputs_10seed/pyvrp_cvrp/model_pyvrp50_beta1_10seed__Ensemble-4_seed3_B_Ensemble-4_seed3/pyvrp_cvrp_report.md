# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.879280 | 0.000% | 0.240289 | 2.529299 | 0.205932 | 0.843497 | 87.563% |
| 1 | 0 | 178688.4 | 21.780% | 3.819652 | 51.523% | 0.092416 | 1.210561 | 0.214009 | 0.770298 | 77.487% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
