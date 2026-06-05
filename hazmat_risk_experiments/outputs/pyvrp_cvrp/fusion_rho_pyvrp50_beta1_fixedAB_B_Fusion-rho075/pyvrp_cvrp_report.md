# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146531.2 | 0.000% | 8.177589 | 0.000% | 0.242098 | 2.724496 | 0.226244 | 0.845005 | 87.756% |
| 1 | 178771.2 | 22.002% | 3.694470 | 54.822% | 0.085299 | 1.150153 | 0.213440 | 0.743965 | 74.234% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
