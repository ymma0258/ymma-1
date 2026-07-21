# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.6 | 0.000% | 10.389976 | 0.000% | 0.325436 | 3.829425 | 0.312259 | 0.885157 | 91.044% |
| 0.25 | 0 | 156765.0 | 6.645% | 8.620474 | 17.031% | 0.272824 | 3.253701 | 0.303764 | 0.881646 | 90.249% |
| 0.5 | 0 | 165499.0 | 12.586% | 6.946592 | 33.141% | 0.194893 | 2.617591 | 0.275530 | 0.874625 | 88.583% |
| 1 | 0 | 177771.8 | 20.935% | 4.794571 | 53.854% | 0.131561 | 2.038578 | 0.342664 | 0.856594 | 84.681% |
| 2 | 0 | 196764.7 | 33.856% | 4.060902 | 60.915% | 0.103067 | 2.082125 | 0.403531 | 0.844114 | 82.105% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
