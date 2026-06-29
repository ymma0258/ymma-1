# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.377422 | 0.000% | 0.258610 | 2.599789 | 0.176268 | 0.865255 | 89.556% |
| 1 | 0 | 161510.6 | 20.533% | 3.316378 | 60.413% | 0.073059 | 1.166521 | 0.309959 | 0.796006 | 78.277% |
| 1 | 1 | 174540.6 | 30.257% | 3.012835 | 64.036% | 0.064651 | 1.008473 | 0.282412 | 0.777585 | 75.570% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
