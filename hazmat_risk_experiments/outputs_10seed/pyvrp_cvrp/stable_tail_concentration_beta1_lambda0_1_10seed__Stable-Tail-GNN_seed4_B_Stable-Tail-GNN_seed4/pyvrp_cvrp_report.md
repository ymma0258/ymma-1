# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.275491 | 0.000% | 0.291917 | 3.021439 | 0.209019 | 0.877111 | 89.848% |
| 1 | 0 | 176937.1 | 20.586% | 3.939516 | 57.528% | 0.092070 | 1.611153 | 0.356868 | 0.821067 | 79.929% |
| 1 | 1 | 190317.1 | 29.705% | 3.193449 | 65.571% | 0.065263 | 1.416537 | 0.359368 | 0.795769 | 75.979% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
