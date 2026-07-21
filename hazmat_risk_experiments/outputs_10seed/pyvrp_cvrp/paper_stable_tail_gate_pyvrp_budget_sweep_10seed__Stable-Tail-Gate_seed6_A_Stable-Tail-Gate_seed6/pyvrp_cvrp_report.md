# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.9 | 0.000% | 8.885744 | 0.000% | 0.259004 | 2.464918 | 0.138420 | 0.854455 | 88.281% |
| 0.25 | 0 | 143689.9 | 7.233% | 6.782531 | 23.670% | 0.204612 | 1.989366 | 0.186495 | 0.845848 | 87.516% |
| 0.5 | 0 | 150890.6 | 12.607% | 5.047772 | 43.192% | 0.148879 | 1.821476 | 0.248407 | 0.822252 | 83.932% |
| 1 | 0 | 161371.4 | 20.428% | 3.400173 | 61.735% | 0.077648 | 1.072027 | 0.268094 | 0.766028 | 76.252% |
| 2 | 0 | 177109.1 | 32.173% | 2.548081 | 71.324% | 0.051525 | 0.949416 | 0.280229 | 0.701546 | 68.061% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
