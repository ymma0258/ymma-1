# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 8.149288 | 0.000% | 0.250149 | 2.302141 | 0.130087 | 0.862784 | 89.266% |
| 1 | 0 | 158666.7 | 18.410% | 3.284105 | 59.701% | 0.079740 | 1.322749 | 0.300749 | 0.799387 | 78.604% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
