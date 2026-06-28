# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 12.238317 | 0.000% | 0.255293 | 4.195936 | 0.250131 | 0.879253 | 91.134% |
| 1 | 0 | 177653.1 | 21.074% | 5.043615 | 58.788% | 0.079983 | 1.782278 | 0.255275 | 0.847662 | 82.393% |
| 2 | 0 | 195171.7 | 33.013% | 4.379489 | 64.215% | 0.067131 | 1.758856 | 0.316346 | 0.832723 | 79.751% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
