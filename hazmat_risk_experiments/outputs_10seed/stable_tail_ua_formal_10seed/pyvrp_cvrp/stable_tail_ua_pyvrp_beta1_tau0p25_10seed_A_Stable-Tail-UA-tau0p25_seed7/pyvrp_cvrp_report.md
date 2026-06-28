# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 12.047408 | 0.000% | 0.301881 | 3.250456 | 0.130129 | 0.857760 | 89.139% |
| 1 | 0 | 161841.3 | 20.779% | 5.102162 | 57.649% | 0.105309 | 1.749297 | 0.286291 | 0.794972 | 78.956% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
