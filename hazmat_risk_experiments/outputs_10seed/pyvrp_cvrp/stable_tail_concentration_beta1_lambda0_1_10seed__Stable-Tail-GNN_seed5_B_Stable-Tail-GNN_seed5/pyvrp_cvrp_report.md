# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.035681 | 0.000% | 0.219598 | 2.415906 | 0.234400 | 0.876974 | 89.513% |
| 1 | 0 | 174282.6 | 18.777% | 2.886487 | 58.974% | 0.068141 | 1.181970 | 0.354590 | 0.811504 | 78.202% |
| 1 | 1 | 186832.2 | 27.330% | 2.352041 | 66.570% | 0.054595 | 0.871138 | 0.318216 | 0.780836 | 73.275% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
