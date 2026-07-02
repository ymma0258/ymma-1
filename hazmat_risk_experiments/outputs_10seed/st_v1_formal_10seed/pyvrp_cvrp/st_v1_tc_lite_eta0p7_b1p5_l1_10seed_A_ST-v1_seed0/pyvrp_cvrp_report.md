# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.397525 | 0.000% | 0.232973 | 2.390638 | 0.223678 | 0.880360 | 90.067% |
| 1.5 | 1 | 169327.9 | 26.366% | 1.420155 | 80.802% | 0.022792 | 0.386180 | 0.151581 | 0.662578 | 57.112% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
