# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.2 | 0.000% | 7.670176 | 0.000% | 0.240132 | 2.676851 | 0.238896 | 0.871397 | 89.491% |
| 1 | 157023.6 | 17.184% | 2.642552 | 65.548% | 0.062989 | 0.858964 | 0.217762 | 0.773426 | 75.186% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
