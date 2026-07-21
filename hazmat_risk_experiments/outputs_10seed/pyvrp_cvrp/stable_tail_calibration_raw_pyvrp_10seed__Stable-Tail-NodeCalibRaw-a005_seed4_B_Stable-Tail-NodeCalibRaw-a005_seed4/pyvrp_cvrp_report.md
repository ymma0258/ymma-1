# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.0 | 0.000% | 8.458827 | 0.000% | 0.253775 | 2.686387 | 0.208811 | 0.873025 | 89.139% |
| 0.25 | 0 | 156790.7 | 6.469% | 7.208498 | 14.781% | 0.202092 | 2.559148 | 0.246897 | 0.870650 | 88.253% |
| 0.5 | 0 | 165101.1 | 12.112% | 5.131502 | 39.336% | 0.134156 | 1.762492 | 0.276254 | 0.845789 | 84.121% |
| 1 | 0 | 175442.1 | 19.134% | 3.719594 | 56.027% | 0.093123 | 1.362166 | 0.306455 | 0.815095 | 79.133% |
| 2 | 0 | 192634.0 | 30.809% | 3.146743 | 62.799% | 0.069342 | 1.261472 | 0.320629 | 0.797408 | 76.469% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
