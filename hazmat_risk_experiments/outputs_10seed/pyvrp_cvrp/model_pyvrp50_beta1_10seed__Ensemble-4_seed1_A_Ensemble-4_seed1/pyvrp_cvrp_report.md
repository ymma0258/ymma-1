# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.442726 | 0.000% | 0.217010 | 2.204498 | 0.162102 | 0.850192 | 87.410% |
| 1 | 0 | 156857.8 | 17.060% | 2.898232 | 61.060% | 0.069494 | 0.951187 | 0.252799 | 0.732143 | 72.063% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
