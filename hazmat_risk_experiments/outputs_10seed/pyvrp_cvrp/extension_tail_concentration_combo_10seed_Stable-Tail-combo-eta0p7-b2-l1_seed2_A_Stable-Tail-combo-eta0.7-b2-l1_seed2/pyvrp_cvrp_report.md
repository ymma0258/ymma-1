# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.698255 | 0.000% | 0.272341 | 2.457055 | 0.145302 | 0.877596 | 90.238% |
| 2 | 1 | 190118.1 | 41.882% | 2.648334 | 69.553% | 0.055043 | 1.594601 | 0.457556 | 0.785287 | 73.342% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
