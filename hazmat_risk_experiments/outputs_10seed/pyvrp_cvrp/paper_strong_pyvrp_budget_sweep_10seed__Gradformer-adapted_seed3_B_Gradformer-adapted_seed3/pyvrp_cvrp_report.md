# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.3 | 0.000% | 8.109284 | 0.000% | 0.212014 | 2.782813 | 0.244110 | 0.858778 | 88.724% |
| 0.25 | 0 | 157482.6 | 6.987% | 6.994032 | 13.753% | 0.173284 | 2.345843 | 0.219800 | 0.854533 | 88.311% |
| 0.5 | 0 | 167049.7 | 13.487% | 5.884649 | 27.433% | 0.156009 | 1.827971 | 0.214561 | 0.848188 | 86.561% |
| 1 | 0 | 180763.6 | 22.804% | 4.138940 | 48.960% | 0.107468 | 1.632228 | 0.313787 | 0.816976 | 81.177% |
| 2 | 0 | 200135.0 | 35.964% | 3.407586 | 57.979% | 0.085823 | 1.167349 | 0.277746 | 0.801396 | 77.787% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
