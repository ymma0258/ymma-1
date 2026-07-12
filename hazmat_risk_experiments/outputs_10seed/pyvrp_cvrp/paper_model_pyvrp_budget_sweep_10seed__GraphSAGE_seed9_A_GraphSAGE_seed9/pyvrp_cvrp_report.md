# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 9.051585 | 0.000% | 0.288494 | 2.600689 | 0.167412 | 0.856537 | 88.699% |
| 0.25 | 0 | 143311.3 | 6.632% | 6.146904 | 32.090% | 0.192664 | 1.754455 | 0.161290 | 0.842872 | 86.966% |
| 0.5 | 0 | 150018.8 | 11.623% | 5.093231 | 43.731% | 0.155475 | 1.677339 | 0.229647 | 0.830289 | 84.854% |
| 1 | 0 | 160193.6 | 19.193% | 3.435175 | 62.049% | 0.085049 | 1.231801 | 0.289637 | 0.770797 | 77.080% |
| 2 | 0 | 175802.7 | 30.808% | 3.009971 | 66.746% | 0.074099 | 0.961575 | 0.252591 | 0.750559 | 73.891% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
