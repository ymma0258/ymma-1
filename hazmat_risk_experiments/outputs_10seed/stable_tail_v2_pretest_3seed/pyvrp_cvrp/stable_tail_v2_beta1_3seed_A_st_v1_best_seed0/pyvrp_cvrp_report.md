# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 7.145451 | 0.000% | 0.237806 | 2.301566 | 0.195699 | 0.874510 | 89.834% |
| 1 | 0 | 156750.3 | 16.980% | 2.505069 | 64.942% | 0.057150 | 0.780216 | 0.214435 | 0.795516 | 76.374% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
