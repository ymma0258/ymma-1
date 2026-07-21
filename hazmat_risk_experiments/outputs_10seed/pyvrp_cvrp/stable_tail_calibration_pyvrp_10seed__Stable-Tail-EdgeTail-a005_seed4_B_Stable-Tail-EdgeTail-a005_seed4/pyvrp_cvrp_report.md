# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.0 | 0.000% | 8.452083 | 0.000% | 0.259417 | 2.666277 | 0.198141 | 0.872679 | 89.050% |
| 0.25 | 0 | 156524.0 | 6.433% | 7.305858 | 13.561% | 0.199356 | 2.361686 | 0.219359 | 0.870569 | 88.290% |
| 0.5 | 0 | 165123.3 | 12.280% | 5.092315 | 39.751% | 0.136691 | 1.661993 | 0.268475 | 0.846861 | 84.013% |
| 1 | 0 | 175742.7 | 19.501% | 3.847683 | 54.477% | 0.095779 | 1.510251 | 0.319449 | 0.818588 | 79.928% |
| 2 | 0 | 192126.4 | 30.641% | 3.127319 | 62.999% | 0.067491 | 1.280793 | 0.334863 | 0.793671 | 75.944% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
