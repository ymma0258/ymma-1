# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 8.281531 | 0.000% | 0.268190 | 2.347979 | 0.169103 | 0.872329 | 89.384% |
| 0.25 | 0 | 142982.7 | 6.652% | 6.109801 | 26.224% | 0.181381 | 2.023508 | 0.218908 | 0.863640 | 87.586% |
| 0.5 | 0 | 149208.8 | 11.296% | 4.457978 | 46.170% | 0.129698 | 1.552266 | 0.220083 | 0.841144 | 84.001% |
| 1 | 0 | 158321.2 | 18.093% | 3.096334 | 62.612% | 0.082860 | 1.212649 | 0.287271 | 0.801743 | 77.587% |
| 2 | 0 | 171848.8 | 28.183% | 2.479025 | 70.066% | 0.059567 | 0.831701 | 0.253530 | 0.764025 | 71.692% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
