# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.9 | 0.000% | 9.990080 | 0.000% | 0.290793 | 3.270984 | 0.222178 | 0.878393 | 90.653% |
| 0.25 | 0 | 158073.6 | 7.437% | 8.222366 | 17.695% | 0.246209 | 2.517715 | 0.203299 | 0.878191 | 89.692% |
| 0.5 | 0 | 167844.2 | 14.078% | 6.319581 | 36.741% | 0.179312 | 2.360523 | 0.273239 | 0.861113 | 86.619% |
| 1 | 0 | 178977.0 | 21.645% | 4.144214 | 58.517% | 0.105305 | 1.363255 | 0.223879 | 0.830104 | 80.709% |
| 2 | 0 | 196669.1 | 33.669% | 3.362261 | 66.344% | 0.068961 | 1.140373 | 0.250271 | 0.810228 | 76.970% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
