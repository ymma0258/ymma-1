# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.992007 | 0.000% | 0.296676 | 3.041854 | 0.187406 | 0.878072 | 90.521% |
| 0.25 | 0 | 157640.8 | 7.241% | 7.819789 | 21.740% | 0.226406 | 2.574715 | 0.237547 | 0.874618 | 89.002% |
| 0.5 | 0 | 167110.3 | 13.683% | 5.685874 | 43.096% | 0.161572 | 1.842820 | 0.242854 | 0.853704 | 85.243% |
| 1 | 0 | 178502.0 | 21.432% | 4.114260 | 58.824% | 0.109637 | 1.452916 | 0.251798 | 0.829807 | 80.745% |
| 2 | 0 | 195333.3 | 32.882% | 3.318550 | 66.788% | 0.071103 | 1.101346 | 0.238831 | 0.808424 | 77.093% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
