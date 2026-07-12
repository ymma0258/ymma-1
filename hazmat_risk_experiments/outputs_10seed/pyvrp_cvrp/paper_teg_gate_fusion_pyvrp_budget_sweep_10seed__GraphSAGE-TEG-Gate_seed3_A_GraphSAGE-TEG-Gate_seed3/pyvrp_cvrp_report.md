# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 7.405353 | 0.000% | 0.218334 | 2.230212 | 0.178769 | 0.873468 | 89.718% |
| 0.25 | 0 | 143389.5 | 7.009% | 4.977499 | 32.785% | 0.137766 | 1.583032 | 0.204362 | 0.861004 | 87.792% |
| 0.5 | 0 | 149647.4 | 11.679% | 3.693092 | 50.129% | 0.108881 | 1.465375 | 0.293237 | 0.830019 | 83.704% |
| 1 | 0 | 158969.4 | 18.636% | 2.660464 | 64.074% | 0.069508 | 0.955120 | 0.247104 | 0.790225 | 77.702% |
| 2 | 0 | 173086.9 | 29.171% | 1.995879 | 73.048% | 0.038168 | 0.650717 | 0.217349 | 0.737710 | 70.120% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
