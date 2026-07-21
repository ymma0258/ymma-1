# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.365056 | 0.000% | 0.283084 | 3.140689 | 0.232260 | 0.873236 | 89.686% |
| 0.25 | 0 | 157763.1 | 7.324% | 8.144398 | 13.034% | 0.206682 | 2.707811 | 0.243111 | 0.872256 | 89.631% |
| 0.5 | 0 | 168231.8 | 14.446% | 6.373577 | 31.943% | 0.152898 | 2.032041 | 0.223121 | 0.857312 | 86.808% |
| 1 | 0 | 180695.9 | 22.925% | 4.063497 | 56.610% | 0.103223 | 1.532529 | 0.317520 | 0.825429 | 80.701% |
| 2 | 0 | 201014.0 | 36.747% | 3.788591 | 59.545% | 0.097897 | 1.427049 | 0.336098 | 0.820424 | 79.652% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
