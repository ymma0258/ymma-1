# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.6 | 0.000% | 7.505554 | 0.000% | 0.243333 | 2.382852 | 0.216268 | 0.869639 | 88.663% |
| 0.25 | 0 | 142289.6 | 5.924% | 5.902850 | 21.354% | 0.169668 | 1.955375 | 0.249881 | 0.864088 | 87.675% |
| 0.5 | 0 | 150366.3 | 11.937% | 4.663221 | 37.870% | 0.131508 | 1.588875 | 0.231201 | 0.847764 | 84.753% |
| 1 | 0 | 160027.5 | 19.129% | 3.189439 | 57.506% | 0.073279 | 1.163138 | 0.306128 | 0.809192 | 78.755% |
| 2 | 0 | 175942.4 | 30.976% | 2.734370 | 63.569% | 0.060526 | 1.159788 | 0.363237 | 0.790005 | 75.419% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
