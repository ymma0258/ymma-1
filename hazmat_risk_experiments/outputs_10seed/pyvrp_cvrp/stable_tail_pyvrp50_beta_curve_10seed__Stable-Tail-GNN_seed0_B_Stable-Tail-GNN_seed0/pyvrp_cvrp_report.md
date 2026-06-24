# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.003160 | 0.000% | 0.253942 | 2.625387 | 0.223399 | 0.881536 | 90.545% |
| 0.25 | 0 | 156964.6 | 6.974% | 6.890926 | 13.897% | 0.196426 | 2.234709 | 0.231003 | 0.880389 | 89.958% |
| 0.5 | 0 | 165974.3 | 13.115% | 4.830099 | 39.648% | 0.128343 | 1.474630 | 0.211486 | 0.862606 | 86.121% |
| 1 | 0 | 176634.0 | 20.380% | 2.972396 | 62.860% | 0.063120 | 1.084746 | 0.291678 | 0.819607 | 79.015% |
| 2 | 0 | 191338.2 | 30.401% | 2.407683 | 69.916% | 0.051014 | 0.984439 | 0.310561 | 0.788973 | 73.644% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
