# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.1 | 0.000% | 8.626964 | 0.000% | 0.263143 | 2.804326 | 0.243384 | 0.876183 | 89.211% |
| 0.25 | 0 | 157352.6 | 6.754% | 7.544496 | 12.547% | 0.216277 | 2.387222 | 0.221410 | 0.873944 | 88.746% |
| 0.5 | 0 | 166387.4 | 12.884% | 5.168230 | 40.092% | 0.136564 | 1.750879 | 0.252660 | 0.849917 | 84.562% |
| 1 | 0 | 176875.3 | 19.999% | 3.541152 | 58.953% | 0.085225 | 1.131010 | 0.204085 | 0.808225 | 77.885% |
| 2 | 0 | 190430.5 | 29.196% | 2.733756 | 68.311% | 0.060850 | 0.799243 | 0.220394 | 0.778239 | 72.621% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
