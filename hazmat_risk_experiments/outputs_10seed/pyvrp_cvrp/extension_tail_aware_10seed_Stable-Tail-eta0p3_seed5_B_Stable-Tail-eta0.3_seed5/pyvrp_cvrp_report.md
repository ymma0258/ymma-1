# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.516464 | 0.000% | 0.208024 | 2.908932 | 0.235210 | 0.879393 | 89.531% |
| 1 | 0 | 173758.3 | 18.420% | 3.475471 | 59.191% | 0.080582 | 1.451864 | 0.364268 | 0.812774 | 77.979% |
| 2 | 0 | 188722.5 | 28.618% | 2.888361 | 66.085% | 0.067582 | 1.141179 | 0.336398 | 0.787553 | 73.969% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
