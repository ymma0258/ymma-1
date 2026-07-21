# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 8.754533 | 0.000% | 0.291192 | 2.669461 | 0.164432 | 0.870682 | 89.243% |
| 0.25 | 0 | 143010.7 | 6.461% | 5.833415 | 33.367% | 0.163467 | 2.016617 | 0.276875 | 0.860199 | 87.717% |
| 0.5 | 0 | 149473.1 | 11.272% | 4.591161 | 47.557% | 0.118000 | 1.935358 | 0.316373 | 0.835627 | 84.356% |
| 1 | 0 | 158419.6 | 17.932% | 2.930531 | 66.526% | 0.066158 | 1.145800 | 0.288631 | 0.777907 | 76.050% |
| 2 | 0 | 172152.2 | 28.155% | 2.611432 | 70.171% | 0.059097 | 0.755339 | 0.201055 | 0.760137 | 73.409% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
