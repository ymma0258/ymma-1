# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.679435 | 0.000% | 0.282402 | 2.453869 | 0.143745 | 0.867135 | 89.473% |
| 1 | 0 | 160111.4 | 19.488% | 3.696051 | 57.416% | 0.106159 | 1.209314 | 0.262903 | 0.811868 | 80.068% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
