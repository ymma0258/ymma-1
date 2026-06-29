# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 14.086169 | 0.000% | 0.360164 | 4.368801 | 0.196285 | 0.848109 | 88.856% |
| 1 | 0 | 183884.8 | 25.321% | 6.878447 | 51.169% | 0.139970 | 2.346703 | 0.273660 | 0.798340 | 81.327% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
