# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.529046 | 0.000% | 0.258772 | 2.457982 | 0.131836 | 0.845500 | 87.460% |
| 1 | 0 | 161521.2 | 20.540% | 3.658152 | 57.109% | 0.086245 | 1.299867 | 0.306020 | 0.746411 | 73.782% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
