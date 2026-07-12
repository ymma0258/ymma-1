# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.2 | 0.000% | 7.735239 | 0.000% | 0.235905 | 2.505013 | 0.223472 | 0.874199 | 89.079% |
| 0.25 | 0 | 156861.4 | 6.469% | 6.488270 | 16.121% | 0.180272 | 2.309819 | 0.264239 | 0.871043 | 88.180% |
| 0.5 | 0 | 165424.2 | 12.281% | 4.847932 | 37.327% | 0.112878 | 1.530738 | 0.223316 | 0.844455 | 84.092% |
| 1 | 0 | 176392.5 | 19.726% | 3.436898 | 55.568% | 0.085004 | 1.302171 | 0.305306 | 0.816585 | 79.398% |
| 2 | 0 | 192063.7 | 30.363% | 2.792641 | 63.897% | 0.066602 | 0.876136 | 0.266373 | 0.792526 | 75.049% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
