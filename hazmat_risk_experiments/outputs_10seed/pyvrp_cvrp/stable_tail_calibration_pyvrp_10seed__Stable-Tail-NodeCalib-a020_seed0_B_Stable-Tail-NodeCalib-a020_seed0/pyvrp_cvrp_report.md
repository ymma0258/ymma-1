# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 7.519526 | 0.000% | 0.206002 | 2.525639 | 0.249128 | 0.878138 | 89.439% |
| 0.25 | 0 | 156642.2 | 6.561% | 6.367239 | 15.324% | 0.156066 | 2.299937 | 0.260326 | 0.872979 | 88.252% |
| 0.5 | 0 | 164947.4 | 12.211% | 4.454533 | 40.760% | 0.112828 | 1.525415 | 0.242159 | 0.848009 | 84.014% |
| 1 | 0 | 175532.6 | 19.412% | 3.109391 | 58.649% | 0.076443 | 1.206447 | 0.297479 | 0.809707 | 78.124% |
| 2 | 0 | 190401.9 | 29.527% | 2.383703 | 68.300% | 0.051378 | 0.869092 | 0.267589 | 0.775348 | 71.942% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
