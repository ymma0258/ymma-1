# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 8.114402 | 0.000% | 0.247968 | 2.652149 | 0.222154 | 0.877443 | 89.434% |
| 0.25 | 0 | 156560.8 | 6.313% | 7.042767 | 13.207% | 0.190181 | 2.250087 | 0.218349 | 0.874343 | 88.905% |
| 0.5 | 0 | 165485.6 | 12.374% | 5.072518 | 37.487% | 0.123434 | 1.737884 | 0.245209 | 0.853399 | 85.237% |
| 1 | 0 | 175366.7 | 19.083% | 3.514867 | 56.684% | 0.087437 | 1.350662 | 0.328768 | 0.819667 | 79.665% |
| 2 | 0 | 190817.4 | 29.575% | 2.867273 | 64.664% | 0.068116 | 0.901977 | 0.264670 | 0.796557 | 75.594% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
