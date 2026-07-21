# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.1 | 0.000% | 7.487471 | 0.000% | 0.197643 | 2.446780 | 0.236490 | 0.877531 | 89.440% |
| 0.25 | 0 | 156847.1 | 6.556% | 6.356439 | 15.106% | 0.156995 | 2.212823 | 0.257129 | 0.872218 | 88.203% |
| 0.5 | 0 | 165252.2 | 12.266% | 4.613832 | 38.379% | 0.117908 | 1.528804 | 0.251324 | 0.852089 | 84.521% |
| 1 | 0 | 175714.4 | 19.374% | 3.105125 | 58.529% | 0.073518 | 1.152982 | 0.295803 | 0.807693 | 77.642% |
| 2 | 0 | 191036.7 | 29.783% | 2.527907 | 66.238% | 0.054404 | 0.951194 | 0.290554 | 0.784230 | 73.350% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
