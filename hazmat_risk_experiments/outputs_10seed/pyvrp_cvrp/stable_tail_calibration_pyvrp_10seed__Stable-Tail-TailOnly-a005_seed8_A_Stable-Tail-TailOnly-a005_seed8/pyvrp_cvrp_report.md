# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.6 | 0.000% | 7.944471 | 0.000% | 0.250628 | 2.352344 | 0.167459 | 0.869222 | 88.801% |
| 0.25 | 0 | 143283.0 | 6.717% | 5.292876 | 33.377% | 0.148105 | 1.639325 | 0.214621 | 0.853950 | 86.419% |
| 0.5 | 0 | 149954.4 | 11.686% | 4.017032 | 49.436% | 0.116437 | 1.486060 | 0.259840 | 0.828829 | 82.521% |
| 1 | 0 | 158624.7 | 18.143% | 2.889456 | 63.629% | 0.074232 | 0.801934 | 0.167574 | 0.782549 | 75.994% |
| 2 | 0 | 173986.8 | 29.585% | 2.294868 | 71.114% | 0.045740 | 0.741015 | 0.216376 | 0.752911 | 70.989% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
