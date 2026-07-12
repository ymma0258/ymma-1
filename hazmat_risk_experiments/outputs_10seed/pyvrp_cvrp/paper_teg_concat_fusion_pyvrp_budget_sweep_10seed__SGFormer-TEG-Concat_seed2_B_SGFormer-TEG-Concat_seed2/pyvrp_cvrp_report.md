# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.5 | 0.000% | 8.987150 | 0.000% | 0.264257 | 3.223630 | 0.268308 | 0.879067 | 89.301% |
| 0.25 | 0 | 158527.7 | 7.503% | 7.708657 | 14.226% | 0.206702 | 2.554855 | 0.236613 | 0.876173 | 88.369% |
| 0.5 | 0 | 168222.1 | 14.077% | 6.214567 | 30.851% | 0.162192 | 2.047853 | 0.225736 | 0.865216 | 86.174% |
| 1 | 0 | 181654.0 | 23.186% | 4.224517 | 52.994% | 0.097158 | 1.654100 | 0.321308 | 0.828555 | 80.160% |
| 2 | 0 | 200569.6 | 36.013% | 3.504551 | 61.005% | 0.071672 | 1.645173 | 0.352160 | 0.811033 | 77.008% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
