# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.424856 | 0.000% | 0.223992 | 2.242427 | 0.174918 | 0.838461 | 86.292% |
| 1 | 0 | 156626.6 | 16.888% | 2.801614 | 62.267% | 0.052189 | 0.831515 | 0.206956 | 0.687628 | 67.518% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
