# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.355225 | 0.000% | 0.238039 | 2.580661 | 0.191426 | 0.845731 | 87.330% |
| 1 | 0 | 159882.2 | 19.317% | 3.258230 | 61.004% | 0.076408 | 1.173070 | 0.263136 | 0.723506 | 71.488% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
