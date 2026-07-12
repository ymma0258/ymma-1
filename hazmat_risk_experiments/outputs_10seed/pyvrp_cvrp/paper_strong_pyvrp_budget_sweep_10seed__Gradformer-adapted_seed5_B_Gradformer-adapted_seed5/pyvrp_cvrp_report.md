# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.3 | 0.000% | 9.470459 | 0.000% | 0.290209 | 2.884365 | 0.201739 | 0.864398 | 89.699% |
| 0.25 | 0 | 155429.9 | 5.545% | 7.522262 | 20.571% | 0.209260 | 2.361156 | 0.216237 | 0.855345 | 88.498% |
| 0.5 | 0 | 163328.5 | 10.908% | 6.481421 | 31.562% | 0.170022 | 1.899609 | 0.184897 | 0.850898 | 87.052% |
| 1 | 0 | 173644.5 | 17.914% | 4.281436 | 54.792% | 0.092622 | 1.349212 | 0.226777 | 0.807224 | 80.955% |
| 2 | 0 | 190181.9 | 29.143% | 3.471769 | 63.341% | 0.073751 | 1.104172 | 0.223366 | 0.784490 | 76.921% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
