# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.365869 | 0.000% | 0.203249 | 2.526459 | 0.234141 | 0.862975 | 88.437% |
| 1 | 0 | 177845.5 | 21.205% | 3.174338 | 56.905% | 0.080723 | 1.080873 | 0.300202 | 0.801873 | 78.061% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
