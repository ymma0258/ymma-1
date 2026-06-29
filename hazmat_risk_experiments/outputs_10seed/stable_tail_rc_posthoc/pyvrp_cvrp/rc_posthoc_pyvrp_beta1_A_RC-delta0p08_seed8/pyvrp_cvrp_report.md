# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.653606 | 0.000% | 0.224580 | 2.282950 | 0.157604 | 0.883911 | 90.189% |
| 1 | 0 | 158061.8 | 17.959% | 3.109717 | 59.369% | 0.075341 | 0.940549 | 0.226820 | 0.824959 | 80.283% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
