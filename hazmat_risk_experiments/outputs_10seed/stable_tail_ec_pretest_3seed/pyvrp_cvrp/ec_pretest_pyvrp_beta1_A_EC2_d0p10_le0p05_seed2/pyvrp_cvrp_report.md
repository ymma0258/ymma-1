# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.519110 | 0.000% | 0.266765 | 2.333144 | 0.142590 | 0.867547 | 89.607% |
| 1 | 0 | 160658.2 | 19.896% | 3.590507 | 57.854% | 0.092147 | 1.196365 | 0.255994 | 0.819815 | 80.392% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
