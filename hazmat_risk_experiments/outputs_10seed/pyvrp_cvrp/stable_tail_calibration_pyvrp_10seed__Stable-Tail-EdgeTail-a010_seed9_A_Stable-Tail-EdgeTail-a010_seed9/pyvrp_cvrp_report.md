# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.5 | 0.000% | 8.821092 | 0.000% | 0.279895 | 2.631157 | 0.173340 | 0.870844 | 89.090% |
| 0.25 | 0 | 142993.1 | 6.343% | 5.984892 | 32.152% | 0.167676 | 1.946662 | 0.218692 | 0.859361 | 87.747% |
| 0.5 | 0 | 149438.0 | 11.136% | 4.354967 | 50.630% | 0.117561 | 1.424705 | 0.217803 | 0.829694 | 83.443% |
| 1 | 0 | 157909.1 | 17.436% | 3.021911 | 65.742% | 0.066285 | 1.106013 | 0.265686 | 0.779524 | 76.549% |
| 2 | 0 | 171504.4 | 27.546% | 2.608933 | 70.424% | 0.058156 | 0.813853 | 0.216643 | 0.758213 | 73.165% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
