# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.275491 | 0.000% | 0.291917 | 3.021439 | 0.209019 | 0.877111 | 89.848% |
| 1 | 0 | 176919.7 | 20.574% | 3.931551 | 57.614% | 0.091864 | 1.593242 | 0.352781 | 0.820942 | 79.889% |
| 1 | 0.5 | 183850.5 | 25.298% | 3.184450 | 65.668% | 0.063117 | 1.424855 | 0.344989 | 0.796745 | 76.008% |
| 1 | 1 | 190207.2 | 29.630% | 3.174651 | 65.774% | 0.064034 | 1.413433 | 0.352606 | 0.795752 | 75.966% |
| 1 | 2 | 201925.1 | 37.616% | 2.909863 | 68.628% | 0.052732 | 1.378610 | 0.358768 | 0.779293 | 73.121% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
