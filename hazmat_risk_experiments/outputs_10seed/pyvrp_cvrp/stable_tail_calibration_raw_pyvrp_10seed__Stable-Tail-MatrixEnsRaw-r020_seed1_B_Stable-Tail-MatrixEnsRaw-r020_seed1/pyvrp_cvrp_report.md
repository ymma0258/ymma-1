# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.4 | 0.000% | 7.916508 | 0.000% | 0.250599 | 2.639153 | 0.247498 | 0.874509 | 90.118% |
| 0.25 | 0 | 155703.2 | 5.922% | 5.937050 | 25.004% | 0.150563 | 1.808601 | 0.231775 | 0.865129 | 87.814% |
| 0.5 | 0 | 164037.1 | 11.592% | 5.375466 | 32.098% | 0.134983 | 1.652676 | 0.215368 | 0.858335 | 86.707% |
| 1 | 0 | 173372.7 | 17.943% | 3.118943 | 60.602% | 0.070025 | 1.168781 | 0.290456 | 0.815940 | 79.291% |
| 2 | 0 | 187945.4 | 27.856% | 2.669486 | 66.280% | 0.057005 | 0.929308 | 0.252741 | 0.795731 | 76.000% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
