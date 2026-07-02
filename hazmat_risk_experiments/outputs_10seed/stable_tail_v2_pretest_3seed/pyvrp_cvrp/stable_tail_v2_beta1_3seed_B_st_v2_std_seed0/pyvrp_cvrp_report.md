# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 3.606059 | 0.000% | 0.091656 | 1.072330 | 0.160090 | 0.766432 | 76.624% |
| 1 | 0 | 179361.3 | 22.665% | 2.241573 | 37.839% | 0.047749 | 0.759157 | 0.248856 | 0.688854 | 65.211% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
