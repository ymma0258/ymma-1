# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.658028 | 0.000% | 0.271105 | 2.383079 | 0.144916 | 0.867768 | 89.615% |
| 1 | 0 | 160534.6 | 19.804% | 3.704102 | 57.218% | 0.089011 | 1.163108 | 0.211661 | 0.820393 | 80.675% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
