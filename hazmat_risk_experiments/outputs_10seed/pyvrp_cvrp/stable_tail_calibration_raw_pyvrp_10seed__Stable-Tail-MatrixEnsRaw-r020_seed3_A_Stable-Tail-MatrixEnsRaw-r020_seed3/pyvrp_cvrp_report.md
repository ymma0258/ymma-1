# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.2 | 0.000% | 5.382993 | 0.000% | 0.160689 | 1.578741 | 0.172808 | 0.869782 | 88.537% |
| 0.25 | 0 | 141834.2 | 5.848% | 3.578913 | 33.514% | 0.101265 | 1.117929 | 0.201333 | 0.850197 | 85.781% |
| 0.5 | 0 | 147212.9 | 9.862% | 2.918578 | 45.782% | 0.083053 | 0.971995 | 0.236197 | 0.836552 | 83.363% |
| 1 | 0 | 155032.0 | 15.697% | 1.846176 | 65.704% | 0.046968 | 0.582992 | 0.254328 | 0.762696 | 73.212% |
| 2 | 0 | 167023.6 | 24.646% | 1.710129 | 68.231% | 0.042436 | 0.612898 | 0.266399 | 0.751121 | 71.370% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
