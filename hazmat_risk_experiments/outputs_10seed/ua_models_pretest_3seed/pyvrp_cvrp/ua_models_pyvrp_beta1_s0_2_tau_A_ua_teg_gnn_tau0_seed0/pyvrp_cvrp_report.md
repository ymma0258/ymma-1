# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 7.818012 | 0.000% | 0.237053 | 2.410924 | 0.163571 | 0.873348 | 89.736% |
| 1 | 0 | 159591.7 | 19.101% | 2.664764 | 65.915% | 0.065680 | 0.934613 | 0.270257 | 0.789478 | 75.516% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
