# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.803669 | 0.000% | 0.278188 | 2.639760 | 0.155480 | 0.875826 | 90.106% |
| 2 | 1 | 188327.0 | 40.545% | 2.348037 | 73.329% | 0.044064 | 1.114417 | 0.368285 | 0.733107 | 68.034% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
