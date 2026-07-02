# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.180222 | 0.000% | 0.289950 | 2.789470 | 0.179834 | 0.863781 | 89.759% |
| 1 | 0 | 181593.2 | 23.759% | 4.374464 | 52.349% | 0.116270 | 1.524516 | 0.273411 | 0.836722 | 83.492% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
