# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 7.315354 | 0.000% | 0.231159 | 2.447960 | 0.230619 | 0.867859 | 89.079% |
| 1 | 0 | 157023.6 | 17.184% | 2.642552 | 63.877% | 0.062989 | 0.858964 | 0.217762 | 0.773426 | 75.186% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
