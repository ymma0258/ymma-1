# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.6 | 0.000% | 9.649833 | 0.000% | 0.317019 | 2.762171 | 0.164792 | 0.872677 | 89.684% |
| 0.25 | 0 | 142157.3 | 5.878% | 6.574683 | 31.867% | 0.198547 | 2.111261 | 0.241157 | 0.867763 | 88.184% |
| 0.5 | 0 | 148009.0 | 10.237% | 4.673842 | 51.566% | 0.120163 | 1.752513 | 0.269586 | 0.839635 | 83.741% |
| 1 | 0 | 156585.7 | 16.625% | 3.477377 | 63.964% | 0.082086 | 1.181332 | 0.265100 | 0.802576 | 78.409% |
| 2 | 0 | 169303.0 | 26.097% | 2.594215 | 73.116% | 0.052423 | 0.836537 | 0.267887 | 0.763782 | 72.029% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
