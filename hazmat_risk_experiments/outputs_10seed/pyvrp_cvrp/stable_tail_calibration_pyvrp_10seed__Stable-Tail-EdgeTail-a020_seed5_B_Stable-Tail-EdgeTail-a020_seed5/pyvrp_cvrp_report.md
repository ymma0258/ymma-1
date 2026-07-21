# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.765309 | 0.000% | 0.241886 | 2.533636 | 0.219871 | 0.874746 | 89.039% |
| 0.25 | 0 | 156248.5 | 6.342% | 6.777689 | 12.718% | 0.180180 | 2.118189 | 0.211678 | 0.872410 | 88.676% |
| 0.5 | 0 | 164750.3 | 12.128% | 5.136756 | 33.850% | 0.120434 | 1.435466 | 0.190622 | 0.851079 | 85.105% |
| 1 | 0 | 175000.6 | 19.104% | 3.435164 | 55.763% | 0.083067 | 1.280780 | 0.318757 | 0.815340 | 79.143% |
| 2 | 0 | 190605.6 | 29.725% | 2.822346 | 63.654% | 0.068610 | 0.914198 | 0.273918 | 0.793991 | 75.525% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
