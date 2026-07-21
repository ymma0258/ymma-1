# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 10.016393 | 0.000% | 0.318559 | 3.411629 | 0.252420 | 0.874937 | 90.217% |
| 0.25 | 0 | 156070.4 | 6.076% | 8.088114 | 19.251% | 0.238572 | 2.775822 | 0.263520 | 0.871781 | 88.800% |
| 0.5 | 0 | 164314.7 | 11.679% | 6.954546 | 30.568% | 0.192014 | 2.224736 | 0.228328 | 0.864390 | 87.430% |
| 1 | 0 | 174593.1 | 18.665% | 4.137351 | 58.694% | 0.095707 | 1.414026 | 0.249404 | 0.818717 | 79.842% |
| 2 | 0 | 188300.1 | 27.982% | 3.402084 | 66.035% | 0.067189 | 1.209302 | 0.281052 | 0.799299 | 76.456% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
