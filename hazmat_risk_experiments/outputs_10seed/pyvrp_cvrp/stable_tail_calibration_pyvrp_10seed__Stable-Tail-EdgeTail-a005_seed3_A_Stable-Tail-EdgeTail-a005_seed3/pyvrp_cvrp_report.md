# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.8 | 0.000% | 6.537379 | 0.000% | 0.190333 | 1.970315 | 0.175978 | 0.868779 | 88.407% |
| 0.25 | 0 | 141490.1 | 5.539% | 5.061243 | 22.580% | 0.147017 | 1.596253 | 0.226071 | 0.861329 | 87.256% |
| 0.5 | 0 | 147173.8 | 9.778% | 3.648519 | 44.190% | 0.104216 | 1.238038 | 0.245136 | 0.834305 | 83.252% |
| 1 | 0 | 155013.7 | 15.626% | 2.452299 | 62.488% | 0.064058 | 0.743916 | 0.213081 | 0.772695 | 74.676% |
| 2 | 0 | 167512.5 | 24.949% | 2.073486 | 68.283% | 0.048828 | 0.737811 | 0.267099 | 0.746723 | 70.479% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
