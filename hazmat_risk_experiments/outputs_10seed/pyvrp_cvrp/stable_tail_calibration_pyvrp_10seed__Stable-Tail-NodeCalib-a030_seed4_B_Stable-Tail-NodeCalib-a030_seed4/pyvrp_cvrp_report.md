# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 8.491804 | 0.000% | 0.256279 | 2.670069 | 0.197227 | 0.873641 | 89.068% |
| 0.25 | 0 | 155851.1 | 6.023% | 7.186620 | 15.370% | 0.193802 | 2.383899 | 0.213008 | 0.870836 | 88.152% |
| 0.5 | 0 | 164292.4 | 11.766% | 5.749997 | 32.288% | 0.150077 | 1.974333 | 0.284677 | 0.855550 | 85.520% |
| 1 | 0 | 174573.9 | 18.760% | 3.923822 | 53.793% | 0.089962 | 1.653436 | 0.339254 | 0.819667 | 79.970% |
| 2 | 0 | 190555.8 | 29.632% | 3.136658 | 63.063% | 0.065532 | 1.240440 | 0.304161 | 0.796133 | 76.187% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
