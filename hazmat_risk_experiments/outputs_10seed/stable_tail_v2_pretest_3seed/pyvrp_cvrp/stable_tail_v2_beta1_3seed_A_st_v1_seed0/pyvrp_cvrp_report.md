# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 7.273075 | 0.000% | 0.232537 | 2.334707 | 0.200029 | 0.873958 | 89.609% |
| 1 | 0 | 156582.0 | 16.855% | 2.507529 | 65.523% | 0.051042 | 0.954687 | 0.300343 | 0.798406 | 76.225% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
