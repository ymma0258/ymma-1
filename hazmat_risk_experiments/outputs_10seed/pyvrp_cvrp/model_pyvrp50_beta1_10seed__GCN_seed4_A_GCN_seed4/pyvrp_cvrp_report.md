# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.228465 | 0.000% | 0.255166 | 2.459731 | 0.166601 | 0.863744 | 89.376% |
| 1 | 0 | 161510.6 | 20.532% | 3.316378 | 59.696% | 0.073059 | 1.166521 | 0.309959 | 0.796006 | 78.277% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
