# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.2 | 0.000% | 7.133987 | 0.000% | 0.230659 | 2.013368 | 0.172111 | 0.874485 | 89.642% |
| 0.25 | 0 | 143028.8 | 6.634% | 4.720799 | 33.827% | 0.141222 | 1.732390 | 0.245699 | 0.857573 | 86.576% |
| 0.5 | 0 | 149161.7 | 11.206% | 3.680212 | 48.413% | 0.107691 | 1.177002 | 0.214633 | 0.839059 | 83.488% |
| 1 | 0 | 158448.7 | 18.130% | 2.665302 | 62.639% | 0.073272 | 1.036078 | 0.309323 | 0.799562 | 77.379% |
| 2 | 0 | 171411.1 | 27.794% | 2.076068 | 70.899% | 0.049112 | 0.675075 | 0.244794 | 0.766882 | 72.142% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
