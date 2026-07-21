# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 5.581609 | 0.000% | 0.170889 | 1.627907 | 0.167525 | 0.871146 | 88.885% |
| 0.25 | 0 | 142785.3 | 6.558% | 3.820117 | 31.559% | 0.109136 | 1.230430 | 0.246421 | 0.858292 | 86.886% |
| 0.5 | 0 | 149018.3 | 11.209% | 2.823999 | 49.405% | 0.082529 | 1.105023 | 0.256723 | 0.828338 | 82.652% |
| 1 | 0 | 157995.4 | 17.909% | 2.049561 | 63.280% | 0.051334 | 0.564151 | 0.151128 | 0.784594 | 76.334% |
| 2 | 0 | 172485.2 | 28.722% | 1.604407 | 71.255% | 0.032782 | 0.492079 | 0.215885 | 0.750717 | 70.770% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
