# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.855013 | 0.000% | 0.233560 | 2.421813 | 0.211237 | 0.884496 | 90.497% |
| 0.25 | 0 | 142414.3 | 6.281% | 4.555697 | 42.003% | 0.137981 | 1.593109 | 0.255647 | 0.860926 | 86.274% |
| 0.5 | 0 | 148229.9 | 10.621% | 3.617057 | 53.952% | 0.104624 | 1.537889 | 0.314246 | 0.832444 | 82.642% |
| 1 | 0 | 156034.9 | 16.446% | 2.261611 | 71.208% | 0.049704 | 0.908453 | 0.296639 | 0.776536 | 73.672% |
| 2 | 0 | 168079.9 | 25.435% | 1.707193 | 78.266% | 0.031751 | 0.550833 | 0.241092 | 0.717515 | 64.734% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
