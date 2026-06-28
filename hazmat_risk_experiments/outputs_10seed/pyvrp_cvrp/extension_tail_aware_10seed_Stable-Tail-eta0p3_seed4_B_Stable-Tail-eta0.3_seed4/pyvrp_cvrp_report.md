# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 11.092885 | 0.000% | 0.263260 | 3.591749 | 0.205373 | 0.878541 | 89.914% |
| 1 | 0 | 176674.0 | 20.407% | 4.503579 | 59.401% | 0.069830 | 1.788792 | 0.333437 | 0.817439 | 78.893% |
| 2 | 0 | 192265.4 | 31.033% | 3.798409 | 65.758% | 0.060007 | 1.706673 | 0.349016 | 0.798408 | 76.025% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
