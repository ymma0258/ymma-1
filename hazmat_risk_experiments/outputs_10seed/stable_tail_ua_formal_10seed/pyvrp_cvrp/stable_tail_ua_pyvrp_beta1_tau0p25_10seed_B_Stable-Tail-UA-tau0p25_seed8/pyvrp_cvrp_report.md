# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 14.309233 | 0.000% | 0.365131 | 4.251741 | 0.175220 | 0.845559 | 88.263% |
| 1 | 0 | 185539.8 | 26.449% | 6.592555 | 53.928% | 0.134135 | 2.383520 | 0.307794 | 0.788978 | 79.988% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
