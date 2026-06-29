# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 12.238523 | 0.000% | 0.294205 | 3.241829 | 0.121181 | 0.844699 | 88.176% |
| 1 | 0 | 161098.3 | 20.225% | 5.317900 | 56.548% | 0.087521 | 1.879469 | 0.248871 | 0.780046 | 78.195% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
