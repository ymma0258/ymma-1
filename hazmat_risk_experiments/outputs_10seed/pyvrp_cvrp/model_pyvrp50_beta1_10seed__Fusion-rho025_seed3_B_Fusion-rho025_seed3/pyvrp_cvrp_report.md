# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.862385 | 0.000% | 0.241488 | 2.558784 | 0.215740 | 0.849600 | 88.157% |
| 1 | 0 | 178796.2 | 21.853% | 3.791428 | 51.778% | 0.096452 | 1.110086 | 0.199794 | 0.789139 | 78.996% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
