# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.2 | 0.000% | 6.685445 | 0.000% | 0.194889 | 2.100916 | 0.206961 | 0.852216 | 86.541% |
| 0.25 | 0 | 155142.7 | 5.350% | 5.190034 | 22.368% | 0.141107 | 1.748161 | 0.212777 | 0.841506 | 84.766% |
| 0.5 | 0 | 162394.2 | 10.274% | 4.668215 | 30.173% | 0.130905 | 1.536872 | 0.191605 | 0.837007 | 83.554% |
| 1 | 0 | 173520.4 | 17.829% | 3.526740 | 47.247% | 0.078041 | 0.980700 | 0.174086 | 0.808237 | 79.166% |
| 2 | 0 | 192771.2 | 30.902% | 2.904329 | 56.557% | 0.057282 | 0.888562 | 0.202131 | 0.783550 | 75.263% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
