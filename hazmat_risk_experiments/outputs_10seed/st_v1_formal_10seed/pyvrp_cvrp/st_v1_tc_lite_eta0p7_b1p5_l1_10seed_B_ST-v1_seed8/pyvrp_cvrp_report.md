# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.411502 | 0.000% | 0.217501 | 2.359232 | 0.193685 | 0.878172 | 89.049% |
| 1.5 | 1 | 198133.9 | 35.032% | 2.409629 | 67.488% | 0.049854 | 0.982549 | 0.322952 | 0.780417 | 72.531% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
