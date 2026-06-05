# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 6.985489 | 0.000% | 0.200820 | 2.368076 | 0.224586 | 0.855157 | 88.134% |
| 1 | 0 | 157491.4 | 17.533% | 2.791210 | 60.043% | 0.065787 | 0.926497 | 0.213967 | 0.760959 | 75.171% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
