# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 14.257603 | 0.000% | 0.372467 | 4.444715 | 0.189360 | 0.860755 | 89.850% |
| 1.5 | 1 | 220294.3 | 50.135% | 5.289719 | 62.899% | 0.101184 | 2.575457 | 0.433593 | 0.789016 | 77.242% |
| 2 | 1 | 231803.8 | 57.979% | 5.297343 | 62.845% | 0.099865 | 2.074157 | 0.387514 | 0.789984 | 77.269% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
