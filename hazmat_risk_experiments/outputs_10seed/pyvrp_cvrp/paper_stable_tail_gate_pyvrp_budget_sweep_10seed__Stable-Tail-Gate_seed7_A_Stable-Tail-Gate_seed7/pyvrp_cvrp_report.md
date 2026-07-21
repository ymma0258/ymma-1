# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.9 | 0.000% | 8.592750 | 0.000% | 0.267534 | 2.465226 | 0.154806 | 0.864495 | 89.063% |
| 0.25 | 0 | 142922.2 | 6.660% | 6.477652 | 24.615% | 0.206181 | 1.967848 | 0.205424 | 0.858858 | 88.108% |
| 0.5 | 0 | 149419.6 | 11.509% | 4.800550 | 44.133% | 0.134570 | 1.641556 | 0.237292 | 0.832544 | 84.239% |
| 1 | 0 | 158340.5 | 18.166% | 3.232538 | 62.381% | 0.070241 | 1.213789 | 0.286259 | 0.782660 | 77.019% |
| 2 | 0 | 172382.0 | 28.645% | 2.744763 | 68.057% | 0.055515 | 0.843172 | 0.243179 | 0.762724 | 73.799% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
