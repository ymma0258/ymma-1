# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.6 | 0.000% | 6.986388 | 0.000% | 0.211734 | 2.299275 | 0.199949 | 0.873387 | 88.757% |
| 0.25 | 0 | 142031.8 | 5.785% | 4.651778 | 33.417% | 0.133694 | 1.350174 | 0.165061 | 0.848965 | 85.878% |
| 0.5 | 0 | 147217.4 | 9.647% | 3.562615 | 49.006% | 0.105531 | 1.131358 | 0.226448 | 0.832654 | 82.842% |
| 1 | 0 | 155537.7 | 15.844% | 2.405592 | 65.567% | 0.062895 | 0.786053 | 0.240671 | 0.769329 | 74.237% |
| 2 | 0 | 167716.3 | 24.915% | 2.096965 | 69.985% | 0.050414 | 0.703659 | 0.263832 | 0.747427 | 70.757% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
