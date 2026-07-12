# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.5 | 0.000% | 7.086051 | 0.000% | 0.214850 | 2.318224 | 0.232917 | 0.862765 | 87.894% |
| 0.25 | 0 | 156970.5 | 6.639% | 6.058515 | 14.501% | 0.165658 | 2.118166 | 0.237488 | 0.860664 | 87.037% |
| 0.5 | 0 | 165362.7 | 12.341% | 4.371559 | 38.308% | 0.111822 | 1.397675 | 0.214358 | 0.831664 | 82.606% |
| 1 | 0 | 174991.7 | 18.882% | 2.946166 | 58.423% | 0.061482 | 0.946985 | 0.211839 | 0.784393 | 75.577% |
| 2 | 0 | 188818.9 | 28.276% | 2.314205 | 67.341% | 0.042101 | 0.665722 | 0.181432 | 0.750561 | 69.906% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
