# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 8.447257 | 0.000% | 0.274096 | 2.448858 | 0.172301 | 0.867723 | 89.115% |
| 0.25 | 0 | 143258.1 | 6.645% | 5.665439 | 32.932% | 0.157550 | 1.803438 | 0.214475 | 0.854701 | 87.047% |
| 0.5 | 0 | 149637.3 | 11.394% | 4.329466 | 48.747% | 0.115810 | 1.689918 | 0.266810 | 0.825758 | 83.197% |
| 1 | 0 | 158412.3 | 17.926% | 2.987085 | 64.638% | 0.072600 | 1.021798 | 0.235578 | 0.778658 | 76.428% |
| 2 | 0 | 172186.6 | 28.180% | 2.446153 | 71.042% | 0.054367 | 0.722251 | 0.212243 | 0.747369 | 71.768% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
