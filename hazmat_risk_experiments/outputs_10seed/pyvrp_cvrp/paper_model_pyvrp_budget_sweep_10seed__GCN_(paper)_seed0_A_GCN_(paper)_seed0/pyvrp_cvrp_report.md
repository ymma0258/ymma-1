# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.9 | 0.000% | 7.079444 | 0.000% | 0.224044 | 2.262590 | 0.199204 | 0.865449 | 88.475% |
| 0.25 | 0 | 142699.9 | 6.441% | 4.752683 | 32.866% | 0.130700 | 1.435448 | 0.178564 | 0.847130 | 86.219% |
| 0.5 | 0 | 148715.2 | 10.928% | 3.935410 | 44.411% | 0.101474 | 1.340972 | 0.222147 | 0.826915 | 83.740% |
| 1 | 0 | 157124.6 | 17.200% | 2.558817 | 63.856% | 0.062106 | 0.929708 | 0.239439 | 0.762104 | 74.959% |
| 2 | 0 | 170783.9 | 27.389% | 2.194195 | 69.006% | 0.048797 | 0.725542 | 0.236073 | 0.736955 | 71.264% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
