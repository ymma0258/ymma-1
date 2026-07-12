# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 7.328072 | 0.000% | 0.234387 | 2.107288 | 0.162286 | 0.860194 | 87.885% |
| 0.25 | 0 | 142524.2 | 6.099% | 5.473070 | 25.314% | 0.147304 | 1.610108 | 0.168211 | 0.849448 | 86.909% |
| 0.5 | 0 | 148077.9 | 10.233% | 3.943530 | 46.186% | 0.110851 | 1.261887 | 0.224880 | 0.824365 | 82.650% |
| 1 | 0 | 156754.2 | 16.692% | 2.704581 | 63.093% | 0.071532 | 0.886013 | 0.226022 | 0.766810 | 74.627% |
| 2 | 0 | 169059.8 | 25.853% | 2.163666 | 70.474% | 0.050292 | 0.697231 | 0.266960 | 0.727687 | 68.877% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
