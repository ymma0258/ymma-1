# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.9 | 0.000% | 7.668112 | 0.000% | 0.231614 | 2.544360 | 0.221494 | 0.861999 | 88.167% |
| 0.25 | 0 | 157237.5 | 6.724% | 6.403372 | 16.494% | 0.155056 | 2.058688 | 0.200376 | 0.858291 | 87.221% |
| 0.5 | 0 | 165594.9 | 12.397% | 4.555963 | 40.586% | 0.114096 | 1.439531 | 0.225033 | 0.829749 | 82.800% |
| 1 | 0 | 176529.6 | 19.818% | 3.133456 | 59.137% | 0.075527 | 1.061541 | 0.217646 | 0.785736 | 76.095% |
| 2 | 0 | 191511.8 | 29.988% | 2.555468 | 66.674% | 0.056897 | 0.697889 | 0.171566 | 0.759297 | 71.586% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
