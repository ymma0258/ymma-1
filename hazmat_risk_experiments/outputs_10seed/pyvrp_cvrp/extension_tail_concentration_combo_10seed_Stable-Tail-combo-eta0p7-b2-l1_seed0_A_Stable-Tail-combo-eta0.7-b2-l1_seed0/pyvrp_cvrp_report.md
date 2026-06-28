# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.576641 | 0.000% | 0.242584 | 2.483964 | 0.221180 | 0.882370 | 90.311% |
| 2 | 1 | 173562.2 | 29.526% | 1.417441 | 81.292% | 0.023349 | 0.372711 | 0.141879 | 0.663864 | 57.112% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
