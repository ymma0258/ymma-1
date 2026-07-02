# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.554942 | 0.000% | 0.238247 | 2.277329 | 0.167129 | 0.837137 | 86.143% |
| 0.5 | 0 | 148725.4 | 10.991% | 4.412721 | 41.592% | 0.109399 | 1.832320 | 0.308409 | 0.782258 | 79.122% |
| 1 | 0 | 157340.2 | 17.420% | 2.922636 | 61.315% | 0.060573 | 0.934375 | 0.228478 | 0.692118 | 68.227% |
| 1.5 | 0 | 164143.4 | 22.497% | 2.781425 | 63.184% | 0.056000 | 0.973107 | 0.243320 | 0.676586 | 66.155% |
| 2 | 0 | 170478.9 | 27.225% | 2.224030 | 70.562% | 0.040369 | 0.617519 | 0.158894 | 0.604740 | 57.666% |
| 3 | 0 | 181092.8 | 35.146% | 2.195731 | 70.936% | 0.038267 | 0.712178 | 0.226902 | 0.592558 | 56.365% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
