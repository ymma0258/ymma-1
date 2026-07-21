# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 4.893383 | 0.000% | 0.149473 | 1.644647 | 0.244991 | 0.869735 | 88.975% |
| 0.25 | 0 | 155084.6 | 5.550% | 3.993205 | 18.396% | 0.098671 | 1.508103 | 0.278697 | 0.863644 | 87.794% |
| 0.5 | 0 | 162858.5 | 10.840% | 3.258102 | 33.418% | 0.083134 | 1.297896 | 0.285850 | 0.852528 | 85.668% |
| 1 | 0 | 175033.0 | 19.126% | 2.636650 | 46.118% | 0.067383 | 0.983691 | 0.268088 | 0.839281 | 82.995% |
| 2 | 0 | 191965.3 | 30.650% | 1.926057 | 60.640% | 0.048097 | 0.753839 | 0.245432 | 0.808743 | 77.445% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
