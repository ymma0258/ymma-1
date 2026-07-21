# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 7.806188 | 0.000% | 0.214855 | 2.672742 | 0.260662 | 0.881571 | 89.893% |
| 0.25 | 0 | 156483.3 | 6.453% | 6.604019 | 15.400% | 0.161632 | 2.368440 | 0.284956 | 0.875289 | 88.645% |
| 0.5 | 0 | 164557.1 | 11.946% | 4.229700 | 45.816% | 0.108379 | 1.406244 | 0.209974 | 0.843009 | 83.446% |
| 1 | 0 | 174606.2 | 18.782% | 3.116175 | 60.081% | 0.078898 | 1.145613 | 0.288207 | 0.812048 | 78.421% |
| 2 | 0 | 189440.1 | 28.873% | 2.429865 | 68.873% | 0.050562 | 0.869655 | 0.261773 | 0.778663 | 72.729% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
