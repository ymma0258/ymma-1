# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 6.883367 | 0.000% | 0.204340 | 2.370042 | 0.226137 | 0.873010 | 88.919% |
| 2 | 1 | 199601.3 | 36.032% | 2.010837 | 70.787% | 0.038145 | 0.835426 | 0.313964 | 0.746332 | 68.490% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
