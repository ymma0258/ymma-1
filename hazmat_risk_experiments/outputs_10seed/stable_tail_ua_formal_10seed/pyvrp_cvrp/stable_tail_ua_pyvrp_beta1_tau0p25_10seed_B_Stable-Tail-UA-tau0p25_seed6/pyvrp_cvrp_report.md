# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 15.108525 | 0.000% | 0.427328 | 4.630639 | 0.186149 | 0.850595 | 89.004% |
| 1 | 0 | 185787.4 | 26.618% | 7.764617 | 48.608% | 0.210181 | 2.818633 | 0.310887 | 0.809727 | 82.655% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
