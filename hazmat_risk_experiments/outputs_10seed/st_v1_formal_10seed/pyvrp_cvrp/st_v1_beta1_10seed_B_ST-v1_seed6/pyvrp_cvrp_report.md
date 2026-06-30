# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.958100 | 0.000% | 0.279888 | 2.949124 | 0.219800 | 0.881360 | 90.236% |
| 1 | 0 | 180438.2 | 22.972% | 4.037701 | 54.927% | 0.094482 | 1.491439 | 0.308897 | 0.838356 | 81.425% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
