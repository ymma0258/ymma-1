# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.935750 | 0.000% | 0.312158 | 3.955624 | 0.334435 | 0.884959 | 90.711% |
| 0.25 | 0 | 156199.8 | 6.260% | 7.815755 | 21.337% | 0.236640 | 3.234328 | 0.344803 | 0.878465 | 89.247% |
| 0.5 | 0 | 164250.9 | 11.737% | 6.978164 | 29.767% | 0.206646 | 2.559438 | 0.285135 | 0.871196 | 88.234% |
| 1 | 0 | 176426.0 | 20.020% | 4.891918 | 50.764% | 0.132651 | 1.849655 | 0.269201 | 0.854077 | 84.523% |
| 2 | 0 | 195134.2 | 32.747% | 4.073635 | 59.000% | 0.105473 | 2.023169 | 0.393229 | 0.844621 | 82.394% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
