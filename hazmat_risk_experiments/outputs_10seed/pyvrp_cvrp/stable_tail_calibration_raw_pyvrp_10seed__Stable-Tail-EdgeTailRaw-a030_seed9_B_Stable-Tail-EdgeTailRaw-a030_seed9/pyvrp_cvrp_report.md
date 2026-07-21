# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.8 | 0.000% | 9.441082 | 0.000% | 0.293913 | 2.973280 | 0.205741 | 0.874387 | 90.458% |
| 0.25 | 0 | 158203.6 | 7.526% | 8.210936 | 13.030% | 0.246948 | 2.693402 | 0.228378 | 0.874961 | 90.102% |
| 0.5 | 0 | 167745.6 | 14.011% | 5.224545 | 44.662% | 0.143462 | 1.696927 | 0.258249 | 0.852078 | 85.662% |
| 1 | 0 | 178940.4 | 21.620% | 3.461443 | 63.336% | 0.080130 | 1.178380 | 0.263729 | 0.811348 | 79.095% |
| 2 | 0 | 195854.0 | 33.116% | 3.196472 | 66.143% | 0.063888 | 1.018917 | 0.256334 | 0.800809 | 77.386% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
