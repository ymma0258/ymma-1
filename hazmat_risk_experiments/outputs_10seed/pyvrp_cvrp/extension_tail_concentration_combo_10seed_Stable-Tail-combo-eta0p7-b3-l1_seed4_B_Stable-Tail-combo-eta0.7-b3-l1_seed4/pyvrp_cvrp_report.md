# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.275491 | 0.000% | 0.291917 | 3.021439 | 0.209019 | 0.877111 | 89.848% |
| 3 | 1 | 226961.5 | 54.679% | 2.844632 | 69.332% | 0.054286 | 1.270092 | 0.353657 | 0.779271 | 73.076% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
