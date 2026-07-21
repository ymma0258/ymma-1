# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 9.169709 | 0.000% | 0.287555 | 2.770135 | 0.179635 | 0.881949 | 90.346% |
| 0.25 | 0 | 143508.9 | 6.832% | 6.473477 | 29.404% | 0.203134 | 2.007195 | 0.212973 | 0.870360 | 88.457% |
| 0.5 | 0 | 150314.8 | 11.899% | 4.941563 | 46.110% | 0.146308 | 1.593988 | 0.267219 | 0.851166 | 85.302% |
| 1 | 0 | 160064.5 | 19.157% | 3.678431 | 59.885% | 0.095570 | 1.281306 | 0.312273 | 0.821705 | 80.905% |
| 2 | 0 | 175246.4 | 30.458% | 2.877409 | 68.621% | 0.069385 | 1.059722 | 0.335832 | 0.791701 | 76.187% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
