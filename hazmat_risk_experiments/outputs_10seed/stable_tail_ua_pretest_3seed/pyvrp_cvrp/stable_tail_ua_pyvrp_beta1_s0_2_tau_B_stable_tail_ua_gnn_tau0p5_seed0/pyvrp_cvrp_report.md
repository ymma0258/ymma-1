# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 14.193235 | 0.000% | 0.236150 | 4.512298 | 0.202764 | 0.842143 | 88.674% |
| 1 | 0 | 183849.7 | 25.734% | 7.412860 | 47.772% | 0.125811 | 2.385186 | 0.226927 | 0.783695 | 80.037% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
