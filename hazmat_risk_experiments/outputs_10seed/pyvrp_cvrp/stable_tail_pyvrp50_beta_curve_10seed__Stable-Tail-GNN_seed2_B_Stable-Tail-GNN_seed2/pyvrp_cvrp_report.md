# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.938070 | 0.000% | 0.305060 | 3.409897 | 0.250389 | 0.878131 | 90.980% |
| 0.25 | 0 | 156908.7 | 6.936% | 8.147796 | 18.014% | 0.228454 | 2.643116 | 0.257857 | 0.878497 | 89.877% |
| 0.5 | 0 | 166122.4 | 13.216% | 7.135140 | 28.204% | 0.192876 | 2.396540 | 0.255120 | 0.875369 | 88.745% |
| 1 | 0 | 178478.1 | 21.636% | 4.512622 | 54.593% | 0.121898 | 1.703002 | 0.320887 | 0.850198 | 83.471% |
| 2 | 0 | 196768.7 | 34.102% | 3.623636 | 63.538% | 0.089905 | 1.568298 | 0.361488 | 0.830343 | 79.604% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
