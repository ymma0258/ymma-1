# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 8.635066 | 0.000% | 0.289480 | 2.633836 | 0.178996 | 0.879971 | 90.260% |
| 0.25 | 0 | 143244.7 | 6.688% | 5.842142 | 32.344% | 0.179261 | 1.695247 | 0.184564 | 0.877024 | 88.816% |
| 0.5 | 0 | 149935.6 | 11.672% | 4.717259 | 45.371% | 0.143560 | 1.632528 | 0.203431 | 0.866791 | 86.733% |
| 1 | 0 | 159826.3 | 19.038% | 3.491998 | 59.560% | 0.101218 | 1.048229 | 0.202079 | 0.840159 | 82.023% |
| 2 | 0 | 174395.0 | 29.889% | 2.597455 | 69.920% | 0.066362 | 1.012694 | 0.275172 | 0.811461 | 76.412% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
