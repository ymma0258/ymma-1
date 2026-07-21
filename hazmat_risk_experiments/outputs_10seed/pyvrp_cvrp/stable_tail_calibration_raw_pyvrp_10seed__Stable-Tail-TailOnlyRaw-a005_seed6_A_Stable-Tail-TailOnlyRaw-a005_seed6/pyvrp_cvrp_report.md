# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.8 | 0.000% | 8.377859 | 0.000% | 0.269592 | 2.408988 | 0.148649 | 0.865176 | 88.289% |
| 0.25 | 0 | 143483.7 | 6.760% | 5.075060 | 39.423% | 0.147797 | 1.682877 | 0.236742 | 0.842265 | 85.027% |
| 0.5 | 0 | 149753.0 | 11.425% | 4.168678 | 50.242% | 0.123040 | 1.564135 | 0.312256 | 0.822711 | 82.271% |
| 1 | 0 | 158991.1 | 18.299% | 2.958929 | 64.682% | 0.079161 | 1.009998 | 0.276733 | 0.781346 | 76.188% |
| 2 | 0 | 173194.2 | 28.867% | 2.340353 | 72.065% | 0.054527 | 0.847582 | 0.290264 | 0.735993 | 70.059% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
