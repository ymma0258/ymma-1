# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 14.734490 | 0.000% | 0.193985 | 4.691089 | 0.207257 | 0.852400 | 89.704% |
| 1 | 0 | 182774.3 | 24.999% | 6.944253 | 52.871% | 0.092544 | 2.100097 | 0.215504 | 0.791922 | 79.631% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
