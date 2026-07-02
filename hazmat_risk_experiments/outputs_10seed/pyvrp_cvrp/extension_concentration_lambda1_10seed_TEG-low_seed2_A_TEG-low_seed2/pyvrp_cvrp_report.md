# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 9.076478 | 0.000% | 0.269885 | 2.726032 | 0.166068 | 0.848920 | 88.488% |
| 1 | 0 | 160591.9 | 19.847% | 3.597740 | 60.362% | 0.076383 | 1.189036 | 0.279900 | 0.743618 | 73.646% |
| 1 | 1 | 173074.7 | 29.163% | 3.368011 | 62.893% | 0.069492 | 1.103168 | 0.279405 | 0.726955 | 71.622% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
