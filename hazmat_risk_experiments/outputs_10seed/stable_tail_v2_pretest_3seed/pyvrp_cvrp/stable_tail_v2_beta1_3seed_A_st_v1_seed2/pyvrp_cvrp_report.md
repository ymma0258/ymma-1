# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 8.581312 | 0.000% | 0.275175 | 2.437927 | 0.131234 | 0.872453 | 89.905% |
| 1 | 0 | 158011.7 | 17.922% | 3.356202 | 60.889% | 0.084680 | 1.169036 | 0.329026 | 0.827285 | 80.090% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
