# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.0 | 0.000% | 8.717152 | 0.000% | 0.232754 | 2.537966 | 0.171529 | 0.831594 | 86.365% |
| 0.25 | 0 | 157459.7 | 6.923% | 7.565906 | 13.207% | 0.181489 | 2.364905 | 0.203702 | 0.822230 | 85.234% |
| 0.5 | 0 | 167240.1 | 13.565% | 5.836542 | 33.045% | 0.140217 | 1.783231 | 0.224462 | 0.789382 | 80.788% |
| 1 | 0 | 179557.8 | 21.929% | 3.943132 | 54.766% | 0.090878 | 1.313705 | 0.212580 | 0.716690 | 71.580% |
| 2 | 0 | 196540.2 | 33.461% | 3.078480 | 64.685% | 0.057695 | 0.910560 | 0.202212 | 0.655560 | 63.686% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
