# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.4 | 0.000% | 7.679535 | 0.000% | 0.234862 | 2.538280 | 0.236312 | 0.873045 | 89.090% |
| 0.25 | 0 | 156406.1 | 6.160% | 6.474922 | 15.686% | 0.153454 | 2.255680 | 0.235128 | 0.869971 | 88.080% |
| 0.5 | 0 | 165078.5 | 12.046% | 4.759720 | 38.021% | 0.120585 | 1.507959 | 0.235573 | 0.844385 | 84.134% |
| 1 | 0 | 175741.5 | 19.284% | 3.399157 | 55.737% | 0.086282 | 1.224458 | 0.301539 | 0.812891 | 78.868% |
| 2 | 0 | 191766.1 | 30.161% | 2.803496 | 63.494% | 0.067498 | 0.970506 | 0.286176 | 0.793968 | 75.320% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
