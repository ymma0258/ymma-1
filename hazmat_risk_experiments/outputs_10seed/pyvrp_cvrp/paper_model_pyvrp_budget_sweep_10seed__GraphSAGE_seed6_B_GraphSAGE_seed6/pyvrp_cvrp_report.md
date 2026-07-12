# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.9 | 0.000% | 9.629375 | 0.000% | 0.283863 | 2.994517 | 0.199339 | 0.856238 | 89.212% |
| 0.25 | 0 | 158783.7 | 7.920% | 8.569294 | 11.009% | 0.218009 | 2.993384 | 0.227580 | 0.857304 | 89.410% |
| 0.5 | 0 | 169927.1 | 15.494% | 6.860945 | 28.750% | 0.177867 | 2.289474 | 0.246744 | 0.849489 | 87.285% |
| 1 | 0 | 184796.8 | 25.600% | 5.219936 | 45.792% | 0.134281 | 1.877623 | 0.292096 | 0.824781 | 83.527% |
| 2 | 0 | 208203.5 | 41.509% | 4.082450 | 57.604% | 0.095670 | 1.457205 | 0.327638 | 0.800409 | 78.849% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
