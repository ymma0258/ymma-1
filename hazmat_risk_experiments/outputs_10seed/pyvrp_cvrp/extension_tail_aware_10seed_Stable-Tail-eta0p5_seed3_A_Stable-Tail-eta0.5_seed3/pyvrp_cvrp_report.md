# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.533651 | 0.000% | 0.172592 | 2.778064 | 0.210408 | 0.876516 | 89.264% |
| 1 | 0 | 154614.9 | 15.386% | 2.987556 | 64.991% | 0.045839 | 0.979243 | 0.232102 | 0.773569 | 74.475% |
| 2 | 0 | 166590.5 | 24.324% | 2.518849 | 70.483% | 0.035722 | 0.877898 | 0.243433 | 0.738708 | 69.110% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
