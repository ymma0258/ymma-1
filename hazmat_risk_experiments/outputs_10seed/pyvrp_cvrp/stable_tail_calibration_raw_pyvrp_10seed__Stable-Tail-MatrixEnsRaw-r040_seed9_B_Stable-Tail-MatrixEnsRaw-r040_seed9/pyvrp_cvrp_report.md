# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146797.4 | 0.000% | 5.677295 | 0.000% | 0.181157 | 1.839115 | 0.216934 | 0.874398 | 90.580% |
| 0.25 | 0 | 157790.6 | 7.489% | 4.822775 | 15.052% | 0.138630 | 1.731321 | 0.254349 | 0.873877 | 90.021% |
| 0.5 | 0 | 167474.1 | 14.085% | 3.037815 | 46.492% | 0.082923 | 1.059168 | 0.274212 | 0.845139 | 84.889% |
| 1 | 0 | 178500.4 | 21.596% | 2.022680 | 64.372% | 0.041789 | 0.710966 | 0.278175 | 0.806642 | 78.515% |
| 2 | 0 | 195162.9 | 32.947% | 1.886176 | 66.777% | 0.037227 | 0.615703 | 0.251261 | 0.798581 | 77.175% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
