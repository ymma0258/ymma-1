# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.4 | 0.000% | 8.205363 | 0.000% | 0.250009 | 2.733987 | 0.267366 | 0.869580 | 88.348% |
| 0.25 | 0 | 158019.1 | 7.352% | 6.913640 | 15.742% | 0.186721 | 2.446272 | 0.299803 | 0.864738 | 87.385% |
| 0.5 | 0 | 167399.1 | 13.724% | 4.826964 | 41.173% | 0.127054 | 1.931117 | 0.334438 | 0.835238 | 82.407% |
| 1 | 0 | 179205.7 | 21.745% | 3.636743 | 55.678% | 0.081774 | 1.489505 | 0.351642 | 0.807145 | 77.860% |
| 2 | 0 | 197879.1 | 34.431% | 2.645734 | 67.756% | 0.051501 | 1.412186 | 0.401791 | 0.756766 | 70.065% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
