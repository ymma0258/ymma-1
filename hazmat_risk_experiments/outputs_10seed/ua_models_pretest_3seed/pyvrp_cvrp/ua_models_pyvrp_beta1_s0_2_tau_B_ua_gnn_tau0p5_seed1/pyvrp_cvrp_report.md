# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 14.024005 | 0.000% | 0.225976 | 4.471771 | 0.196185 | 0.855695 | 90.060% |
| 1 | 0 | 182188.3 | 24.598% | 7.003786 | 50.059% | 0.116123 | 2.370247 | 0.274388 | 0.809623 | 81.883% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
