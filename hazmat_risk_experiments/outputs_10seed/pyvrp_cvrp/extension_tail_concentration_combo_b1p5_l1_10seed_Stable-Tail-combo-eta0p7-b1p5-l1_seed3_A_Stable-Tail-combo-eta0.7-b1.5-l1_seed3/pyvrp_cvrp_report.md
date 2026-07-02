# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.695492 | 0.000% | 0.195570 | 2.189409 | 0.216915 | 0.875815 | 89.250% |
| 1.5 | 1 | 169417.2 | 26.433% | 1.483763 | 77.839% | 0.022674 | 0.475105 | 0.231489 | 0.666225 | 58.933% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
