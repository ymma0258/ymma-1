# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.035681 | 0.000% | 0.219598 | 2.415906 | 0.234400 | 0.876974 | 89.513% |
| 1 | 0 | 174255.2 | 18.758% | 2.892914 | 58.882% | 0.068165 | 1.181970 | 0.354783 | 0.811699 | 78.206% |
| 1 | 0.5 | 181120.5 | 23.437% | 2.607158 | 62.944% | 0.060294 | 1.050146 | 0.325268 | 0.796081 | 75.683% |
| 1 | 1 | 186832.2 | 27.330% | 2.352041 | 66.570% | 0.054595 | 0.871138 | 0.318216 | 0.780836 | 73.275% |
| 1 | 2 | 197210.8 | 34.403% | 2.292267 | 67.419% | 0.052631 | 0.810687 | 0.295202 | 0.777839 | 72.669% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
