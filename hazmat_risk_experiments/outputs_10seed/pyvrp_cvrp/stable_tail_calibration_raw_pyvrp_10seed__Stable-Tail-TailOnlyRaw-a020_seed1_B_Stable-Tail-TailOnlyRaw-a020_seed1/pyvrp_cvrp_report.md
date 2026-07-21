# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.6 | 0.000% | 10.660853 | 0.000% | 0.339907 | 3.789517 | 0.269447 | 0.876646 | 90.707% |
| 0.25 | 0 | 156650.9 | 6.374% | 8.644393 | 18.915% | 0.254499 | 2.626482 | 0.211144 | 0.873740 | 89.338% |
| 0.5 | 0 | 164666.4 | 11.817% | 7.067532 | 33.706% | 0.191242 | 2.201871 | 0.241580 | 0.866393 | 87.595% |
| 1 | 0 | 174803.8 | 18.701% | 4.229586 | 60.326% | 0.103441 | 1.403857 | 0.264551 | 0.825034 | 80.507% |
| 2 | 0 | 188124.2 | 27.747% | 3.469707 | 67.454% | 0.068559 | 1.281007 | 0.295127 | 0.805129 | 76.991% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
