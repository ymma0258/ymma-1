# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.5 | 0.000% | 6.096112 | 0.000% | 0.168028 | 2.072401 | 0.256446 | 0.879698 | 89.699% |
| 0.25 | 0 | 156496.5 | 6.462% | 5.079983 | 16.668% | 0.122065 | 1.877802 | 0.276357 | 0.871303 | 88.236% |
| 0.5 | 0 | 164821.7 | 12.126% | 3.599442 | 40.955% | 0.092193 | 1.137262 | 0.196140 | 0.849901 | 84.374% |
| 1 | 0 | 175412.7 | 19.330% | 2.490050 | 59.153% | 0.062798 | 0.908288 | 0.281765 | 0.811238 | 78.100% |
| 2 | 0 | 190051.4 | 29.289% | 1.937111 | 68.224% | 0.039155 | 0.767345 | 0.306932 | 0.779294 | 72.677% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
