# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 9.668637 | 0.000% | 0.257118 | 2.876237 | 0.156008 | 0.865566 | 89.311% |
| 1 | 0 | 158784.3 | 18.498% | 3.819228 | 60.499% | 0.084472 | 1.232936 | 0.235043 | 0.793707 | 78.379% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
