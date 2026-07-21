# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.1 | 0.000% | 8.981312 | 0.000% | 0.281717 | 3.346446 | 0.309935 | 0.874010 | 89.541% |
| 0.25 | 0 | 156859.6 | 6.516% | 7.392548 | 17.690% | 0.215707 | 2.620735 | 0.293300 | 0.871954 | 88.759% |
| 0.5 | 0 | 165544.6 | 12.413% | 6.339176 | 29.418% | 0.174217 | 2.204019 | 0.259782 | 0.862877 | 87.144% |
| 1 | 0 | 178557.4 | 21.250% | 4.804181 | 46.509% | 0.127464 | 1.750172 | 0.258458 | 0.845324 | 84.092% |
| 2 | 0 | 197022.3 | 33.788% | 3.521788 | 60.788% | 0.084030 | 1.672615 | 0.364594 | 0.822355 | 79.397% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
