# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 6.705562 | 0.000% | 0.183616 | 2.238745 | 0.246557 | 0.877337 | 89.397% |
| 0.25 | 0 | 156511.1 | 6.520% | 5.790549 | 13.646% | 0.143843 | 1.762068 | 0.227543 | 0.873274 | 88.586% |
| 0.5 | 0 | 164874.1 | 12.212% | 3.809630 | 43.187% | 0.097447 | 1.243290 | 0.216093 | 0.844287 | 83.558% |
| 1 | 0 | 175465.9 | 19.421% | 2.734378 | 59.222% | 0.068382 | 1.002659 | 0.290617 | 0.807302 | 77.691% |
| 2 | 0 | 190614.8 | 29.731% | 2.106114 | 68.592% | 0.042646 | 0.798012 | 0.288824 | 0.770974 | 71.329% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
