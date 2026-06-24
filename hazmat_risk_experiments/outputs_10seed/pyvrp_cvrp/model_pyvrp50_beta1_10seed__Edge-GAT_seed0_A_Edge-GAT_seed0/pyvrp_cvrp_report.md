# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.590026 | 0.000% | 0.235277 | 2.433344 | 0.209293 | 0.870615 | 89.293% |
| 1 | 0 | 157093.9 | 17.236% | 2.623446 | 65.436% | 0.061320 | 0.904541 | 0.231489 | 0.771530 | 74.871% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
