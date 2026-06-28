# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.029886 | 0.000% | 0.189973 | 3.508988 | 0.271115 | 0.885803 | 90.268% |
| 1 | 0 | 172961.2 | 17.876% | 3.469104 | 65.412% | 0.055898 | 1.203595 | 0.268551 | 0.813391 | 76.253% |
| 2 | 0 | 186046.0 | 26.794% | 3.203339 | 68.062% | 0.050680 | 1.191196 | 0.284348 | 0.801199 | 74.402% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
