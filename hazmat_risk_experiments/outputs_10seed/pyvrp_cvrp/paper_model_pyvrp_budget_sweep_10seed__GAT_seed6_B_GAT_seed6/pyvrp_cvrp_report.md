# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.2 | 0.000% | 9.072415 | 0.000% | 0.266929 | 2.991127 | 0.231035 | 0.855456 | 88.698% |
| 0.25 | 0 | 159077.1 | 8.022% | 7.966301 | 12.192% | 0.230262 | 2.628478 | 0.222081 | 0.855450 | 88.930% |
| 0.5 | 0 | 169485.4 | 15.089% | 6.559880 | 27.694% | 0.161645 | 2.338491 | 0.258882 | 0.849258 | 87.207% |
| 1 | 0 | 185232.6 | 25.783% | 4.860502 | 46.425% | 0.123490 | 1.704659 | 0.294999 | 0.827879 | 83.179% |
| 2 | 0 | 208909.8 | 41.861% | 3.777196 | 58.366% | 0.086352 | 1.270183 | 0.284147 | 0.799782 | 78.617% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
