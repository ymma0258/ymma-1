# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.2 | 0.000% | 7.311805 | 0.000% | 0.181545 | 2.660371 | 0.252183 | 0.879426 | 90.642% |
| 0.25 | 0 | 156815.8 | 6.534% | 6.173360 | 15.570% | 0.166293 | 1.944518 | 0.210634 | 0.879973 | 89.420% |
| 0.5 | 0 | 166061.5 | 12.816% | 5.303852 | 27.462% | 0.144010 | 1.904547 | 0.263199 | 0.870815 | 87.769% |
| 1 | 0 | 179527.6 | 21.964% | 4.091091 | 44.048% | 0.115074 | 1.392084 | 0.276380 | 0.859802 | 85.071% |
| 2 | 0 | 199181.3 | 35.316% | 3.118410 | 57.351% | 0.077571 | 1.272023 | 0.359581 | 0.844499 | 81.409% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
