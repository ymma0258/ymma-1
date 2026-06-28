# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.695492 | 0.000% | 0.195570 | 2.189409 | 0.216915 | 0.875815 | 89.250% |
| 3 | 1 | 181984.1 | 35.811% | 1.485157 | 77.819% | 0.022531 | 0.469718 | 0.226494 | 0.666765 | 59.016% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
