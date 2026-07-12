# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.0 | 0.000% | 9.574992 | 0.000% | 0.283161 | 3.041377 | 0.212944 | 0.852796 | 89.218% |
| 0.25 | 0 | 158239.2 | 7.453% | 8.425109 | 12.009% | 0.237325 | 2.667922 | 0.195965 | 0.853779 | 89.515% |
| 0.5 | 0 | 168273.1 | 14.266% | 6.956064 | 27.352% | 0.205081 | 2.153012 | 0.196219 | 0.849842 | 87.857% |
| 1 | 0 | 182371.6 | 23.840% | 4.895406 | 48.873% | 0.117688 | 1.577207 | 0.248038 | 0.816534 | 82.785% |
| 2 | 0 | 203627.3 | 38.274% | 3.857224 | 59.716% | 0.079760 | 1.461143 | 0.343589 | 0.793123 | 78.553% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
