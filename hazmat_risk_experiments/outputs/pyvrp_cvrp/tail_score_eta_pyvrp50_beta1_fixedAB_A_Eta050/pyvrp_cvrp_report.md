# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.4 | 0.000% | 10.686691 | 0.000% | 0.231571 | 3.326099 | 0.210624 | 0.839114 | 86.825% |
| 1 | 159092.8 | 18.728% | 4.342663 | 59.364% | 0.066384 | 1.652311 | 0.287995 | 0.717009 | 70.671% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
