# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 7.833149 | 0.000% | 0.252949 | 2.265775 | 0.165770 | 0.876149 | 89.704% |
| 0.25 | 0 | 142480.7 | 6.330% | 5.071528 | 35.256% | 0.149034 | 1.894470 | 0.282864 | 0.860824 | 87.104% |
| 0.5 | 0 | 148559.9 | 10.867% | 4.299944 | 45.106% | 0.127330 | 1.662559 | 0.280336 | 0.852813 | 85.479% |
| 1 | 0 | 157569.1 | 17.591% | 2.946966 | 62.378% | 0.081030 | 1.168791 | 0.346595 | 0.813714 | 79.300% |
| 2 | 0 | 171959.6 | 28.330% | 2.602398 | 66.777% | 0.062302 | 1.033632 | 0.336867 | 0.792801 | 76.121% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
