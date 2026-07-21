# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.933512 | 0.000% | 0.231668 | 2.195001 | 0.146320 | 0.867192 | 88.838% |
| 0.25 | 0 | 143264.1 | 6.862% | 5.184210 | 34.654% | 0.143557 | 1.673945 | 0.226227 | 0.846831 | 85.593% |
| 0.5 | 0 | 148807.0 | 10.996% | 4.085622 | 48.502% | 0.120400 | 1.700205 | 0.354469 | 0.819890 | 82.051% |
| 1 | 0 | 158330.1 | 18.100% | 2.893164 | 63.532% | 0.076709 | 1.041801 | 0.301659 | 0.775311 | 75.553% |
| 2 | 0 | 172619.0 | 28.758% | 2.301855 | 70.986% | 0.053817 | 0.828390 | 0.266782 | 0.733325 | 69.653% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
