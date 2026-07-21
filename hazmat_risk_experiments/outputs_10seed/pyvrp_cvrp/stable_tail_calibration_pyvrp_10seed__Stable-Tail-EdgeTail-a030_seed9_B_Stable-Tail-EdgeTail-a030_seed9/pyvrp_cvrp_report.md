# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.238187 | 0.000% | 0.292661 | 2.946146 | 0.219122 | 0.873660 | 90.247% |
| 0.25 | 0 | 157954.8 | 7.454% | 7.863134 | 14.884% | 0.226799 | 2.518581 | 0.223232 | 0.871387 | 89.608% |
| 0.5 | 0 | 167894.2 | 14.216% | 5.665120 | 38.677% | 0.155413 | 1.779639 | 0.226403 | 0.856014 | 86.589% |
| 1 | 0 | 178344.1 | 21.325% | 3.487983 | 62.244% | 0.078444 | 1.155477 | 0.253367 | 0.810455 | 79.240% |
| 2 | 0 | 194896.2 | 32.585% | 3.050730 | 66.977% | 0.059950 | 0.956093 | 0.234717 | 0.792542 | 76.305% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
