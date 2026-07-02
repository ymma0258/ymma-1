# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.401179 | 0.000% | 0.295818 | 3.057320 | 0.208092 | 0.876834 | 89.836% |
| 1 | 0 | 176998.2 | 20.628% | 3.922598 | 58.275% | 0.092379 | 1.575889 | 0.339133 | 0.818471 | 79.552% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
