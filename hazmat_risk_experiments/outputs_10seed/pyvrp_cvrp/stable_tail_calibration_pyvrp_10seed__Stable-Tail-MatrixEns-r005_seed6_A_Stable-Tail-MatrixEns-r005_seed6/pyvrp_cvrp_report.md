# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.442319 | 0.000% | 0.216101 | 2.101212 | 0.147616 | 0.865429 | 88.540% |
| 0.25 | 0 | 143271.7 | 6.921% | 4.821144 | 35.220% | 0.139010 | 1.700443 | 0.284913 | 0.848032 | 85.446% |
| 0.5 | 0 | 149327.2 | 11.440% | 3.770359 | 49.339% | 0.110457 | 1.356027 | 0.289254 | 0.817178 | 81.477% |
| 1 | 0 | 158903.3 | 18.586% | 2.753326 | 63.004% | 0.073987 | 0.899493 | 0.263186 | 0.777049 | 75.738% |
| 2 | 0 | 173353.4 | 29.370% | 2.115366 | 71.577% | 0.048330 | 0.776300 | 0.296176 | 0.725220 | 68.713% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
