# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.3 | 0.000% | 10.188906 | 0.000% | 0.310294 | 3.447098 | 0.216513 | 0.857187 | 89.234% |
| 0.25 | 0 | 160035.0 | 8.672% | 8.948761 | 12.172% | 0.235663 | 2.716484 | 0.184797 | 0.856834 | 88.953% |
| 0.5 | 0 | 170992.1 | 16.112% | 7.288913 | 28.462% | 0.183779 | 2.481487 | 0.251500 | 0.849215 | 86.932% |
| 1 | 0 | 186328.6 | 26.527% | 5.049261 | 50.444% | 0.125114 | 1.767766 | 0.308531 | 0.815779 | 81.442% |
| 2 | 0 | 210195.7 | 42.734% | 4.245802 | 58.329% | 0.095159 | 1.601687 | 0.350121 | 0.797909 | 78.090% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
