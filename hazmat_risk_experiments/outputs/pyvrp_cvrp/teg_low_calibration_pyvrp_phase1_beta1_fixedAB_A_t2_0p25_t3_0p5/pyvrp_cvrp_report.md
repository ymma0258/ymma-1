# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.176042 | 0.000% | 0.272287 | 2.667921 | 0.224117 | 0.840529 | 86.861% |
| 1 | 0 | 159442.0 | 18.989% | 3.252473 | 60.219% | 0.076948 | 1.200708 | 0.263131 | 0.714206 | 70.386% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
