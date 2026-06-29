# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 10.039826 | 0.000% | 0.254544 | 2.749255 | 0.116929 | 0.851833 | 88.274% |
| 1 | 0 | 158935.0 | 18.611% | 4.267477 | 57.495% | 0.077490 | 1.414060 | 0.257017 | 0.782103 | 77.916% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
