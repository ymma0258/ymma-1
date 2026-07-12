# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134530.9 | 0.000% | 8.133657 | 0.000% | 0.278664 | 2.534114 | 0.185307 | 0.858509 | 88.164% |
| 0.25 | 0 | 142439.1 | 5.878% | 4.978081 | 38.797% | 0.133294 | 1.717632 | 0.273108 | 0.843916 | 85.495% |
| 0.5 | 0 | 148505.6 | 10.388% | 3.947204 | 51.471% | 0.110705 | 1.391483 | 0.268913 | 0.821719 | 82.032% |
| 1 | 0 | 157650.3 | 17.185% | 3.013212 | 62.954% | 0.079498 | 0.998442 | 0.215636 | 0.777784 | 76.446% |
| 2 | 0 | 172583.8 | 28.286% | 2.610913 | 67.900% | 0.060876 | 0.810682 | 0.225909 | 0.758964 | 73.142% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
