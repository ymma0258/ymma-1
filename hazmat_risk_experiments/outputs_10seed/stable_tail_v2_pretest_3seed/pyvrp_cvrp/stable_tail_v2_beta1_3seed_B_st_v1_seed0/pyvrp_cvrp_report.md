# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 7.703406 | 0.000% | 0.242697 | 2.851072 | 0.267270 | 0.884536 | 90.608% |
| 1 | 0 | 176518.0 | 20.720% | 2.930263 | 61.961% | 0.064106 | 1.268501 | 0.359446 | 0.818509 | 78.667% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
