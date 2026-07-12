# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.0 | 0.000% | 9.079400 | 0.000% | 0.263960 | 2.771055 | 0.201625 | 0.865997 | 89.217% |
| 0.25 | 0 | 160119.3 | 8.729% | 7.485302 | 17.557% | 0.190162 | 2.093204 | 0.185816 | 0.868773 | 89.041% |
| 0.5 | 0 | 170621.4 | 15.861% | 5.437761 | 40.109% | 0.148962 | 1.722421 | 0.240138 | 0.855106 | 85.826% |
| 1 | 0 | 182640.4 | 24.022% | 3.664624 | 59.638% | 0.081765 | 1.245408 | 0.272075 | 0.821267 | 79.649% |
| 2 | 0 | 202145.0 | 37.267% | 3.067047 | 66.220% | 0.065074 | 1.112038 | 0.275918 | 0.799556 | 75.632% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
