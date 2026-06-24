# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.576641 | 0.000% | 0.242584 | 2.483964 | 0.221180 | 0.882370 | 90.311% |
| 1 | 0 | 156818.2 | 17.031% | 2.407933 | 68.219% | 0.052249 | 0.874088 | 0.254022 | 0.789544 | 75.383% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
