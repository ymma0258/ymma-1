# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.840243 | 0.000% | 0.292715 | 2.623962 | 0.156524 | 0.868498 | 89.641% |
| 1 | 0 | 160111.3 | 19.488% | 3.696089 | 58.190% | 0.106159 | 1.209314 | 0.262893 | 0.812018 | 80.083% |
| 1 | 1 | 173715.4 | 29.641% | 3.353839 | 62.062% | 0.088056 | 1.111116 | 0.284907 | 0.800445 | 78.147% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
