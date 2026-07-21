# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.743544 | 0.000% | 0.239232 | 2.360155 | 0.195799 | 0.862649 | 88.042% |
| 0.25 | 0 | 156128.9 | 6.260% | 6.504061 | 16.007% | 0.156941 | 2.268811 | 0.232725 | 0.856041 | 87.244% |
| 0.5 | 0 | 164453.5 | 11.926% | 4.870276 | 37.105% | 0.116124 | 1.671479 | 0.244078 | 0.836273 | 83.605% |
| 1 | 0 | 174514.5 | 18.773% | 3.109465 | 59.844% | 0.073431 | 1.017683 | 0.225040 | 0.782559 | 75.750% |
| 2 | 0 | 188890.5 | 28.558% | 2.432787 | 68.583% | 0.054451 | 0.732400 | 0.204817 | 0.751212 | 70.448% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
