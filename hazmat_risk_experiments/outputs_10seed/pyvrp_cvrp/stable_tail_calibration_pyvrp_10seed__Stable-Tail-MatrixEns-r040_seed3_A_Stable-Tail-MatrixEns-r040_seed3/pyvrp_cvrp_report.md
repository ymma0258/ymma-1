# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 4.029702 | 0.000% | 0.120142 | 1.196710 | 0.171478 | 0.870050 | 88.532% |
| 0.25 | 0 | 141618.9 | 5.687% | 3.126753 | 22.407% | 0.090564 | 0.943781 | 0.220734 | 0.864104 | 87.811% |
| 0.5 | 0 | 146986.3 | 9.693% | 2.156380 | 46.488% | 0.060786 | 0.732816 | 0.248552 | 0.832821 | 82.923% |
| 1 | 0 | 154861.4 | 15.570% | 1.450896 | 63.995% | 0.037598 | 0.447043 | 0.226434 | 0.772764 | 74.799% |
| 2 | 0 | 166510.2 | 24.263% | 1.304633 | 67.625% | 0.031513 | 0.410068 | 0.231389 | 0.756928 | 72.263% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
