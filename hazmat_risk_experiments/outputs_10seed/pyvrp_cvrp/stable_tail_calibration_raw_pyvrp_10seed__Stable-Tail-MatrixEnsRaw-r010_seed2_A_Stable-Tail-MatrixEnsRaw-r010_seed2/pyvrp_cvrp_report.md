# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.796514 | 0.000% | 0.251460 | 2.270927 | 0.169438 | 0.875968 | 89.651% |
| 0.25 | 0 | 142434.7 | 6.296% | 5.485434 | 29.642% | 0.159383 | 1.920047 | 0.286799 | 0.866433 | 88.080% |
| 0.5 | 0 | 148519.8 | 10.837% | 4.173836 | 46.465% | 0.125057 | 1.398938 | 0.230402 | 0.852654 | 85.194% |
| 1 | 0 | 157860.0 | 17.808% | 2.898580 | 62.822% | 0.077698 | 1.160016 | 0.347882 | 0.811267 | 79.004% |
| 2 | 0 | 172515.0 | 28.744% | 2.587433 | 66.813% | 0.064332 | 1.064791 | 0.345078 | 0.791397 | 75.879% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
