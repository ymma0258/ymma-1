# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.172981 | 0.000% | 0.186099 | 3.143793 | 0.181291 | 0.880005 | 89.297% |
| 1 | 0 | 178393.1 | 21.578% | 4.194838 | 58.765% | 0.052826 | 1.808024 | 0.317096 | 0.812042 | 77.477% |
| 2 | 0 | 195778.6 | 33.427% | 3.475525 | 65.836% | 0.043679 | 1.395204 | 0.321543 | 0.797020 | 74.726% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
