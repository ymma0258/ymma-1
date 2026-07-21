# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 8.956759 | 0.000% | 0.279763 | 2.862864 | 0.215440 | 0.871560 | 90.133% |
| 0.25 | 0 | 158322.8 | 7.510% | 7.725526 | 13.746% | 0.221907 | 2.660090 | 0.246582 | 0.868738 | 89.490% |
| 0.5 | 0 | 168126.5 | 14.167% | 5.543051 | 38.113% | 0.151742 | 1.751927 | 0.235221 | 0.848435 | 85.785% |
| 1 | 0 | 179295.6 | 21.751% | 3.360982 | 62.475% | 0.069488 | 1.106745 | 0.250030 | 0.804239 | 78.109% |
| 2 | 0 | 197574.9 | 34.164% | 3.044745 | 66.006% | 0.059946 | 0.969792 | 0.258265 | 0.791196 | 76.081% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
