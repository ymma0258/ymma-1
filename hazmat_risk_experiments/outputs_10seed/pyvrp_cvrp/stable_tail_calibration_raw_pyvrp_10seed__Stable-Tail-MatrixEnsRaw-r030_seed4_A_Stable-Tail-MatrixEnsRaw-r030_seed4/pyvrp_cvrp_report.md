# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.8 | 0.000% | 6.219025 | 0.000% | 0.194037 | 1.711727 | 0.151659 | 0.881025 | 90.415% |
| 0.25 | 0 | 143205.0 | 6.818% | 4.666659 | 24.962% | 0.146672 | 1.502326 | 0.231100 | 0.873137 | 88.785% |
| 0.5 | 0 | 149910.3 | 11.819% | 3.545658 | 42.987% | 0.109804 | 1.281842 | 0.280520 | 0.854975 | 85.949% |
| 1 | 0 | 159342.5 | 18.855% | 2.619157 | 57.885% | 0.071172 | 0.820690 | 0.254805 | 0.822870 | 81.028% |
| 2 | 0 | 174333.8 | 30.037% | 2.060618 | 66.866% | 0.048577 | 0.765345 | 0.355933 | 0.796210 | 76.752% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
