# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.803669 | 0.000% | 0.278188 | 2.639760 | 0.155480 | 0.875826 | 90.106% |
| 2 | 2 | 196370.1 | 46.548% | 2.333298 | 73.496% | 0.044316 | 1.105791 | 0.369240 | 0.732689 | 67.930% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
