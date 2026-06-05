# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.304544 | 0.000% | 0.231815 | 2.764398 | 0.235490 | 0.849092 | 87.525% |
| 1 | 0 | 157764.6 | 17.737% | 3.065268 | 63.089% | 0.067133 | 1.153714 | 0.266837 | 0.714206 | 69.729% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
