# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.7 | 0.000% | 5.447489 | 0.000% | 0.168453 | 1.962164 | 0.298776 | 0.876562 | 89.808% |
| 0.25 | 0 | 156425.5 | 6.414% | 4.541997 | 16.622% | 0.139383 | 1.740533 | 0.321525 | 0.872907 | 88.900% |
| 0.5 | 0 | 165235.8 | 12.407% | 3.676496 | 32.510% | 0.098109 | 1.484909 | 0.297894 | 0.861474 | 86.790% |
| 1 | 0 | 177873.2 | 21.004% | 2.619666 | 51.911% | 0.068892 | 1.043751 | 0.324691 | 0.844720 | 83.236% |
| 2 | 0 | 196621.1 | 33.758% | 2.225848 | 59.140% | 0.055762 | 0.998596 | 0.356230 | 0.830858 | 80.627% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
