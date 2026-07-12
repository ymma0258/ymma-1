# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 7.239079 | 0.000% | 0.208100 | 2.503804 | 0.283739 | 0.858730 | 88.548% |
| 0.25 | 0 | 157001.9 | 6.709% | 6.288453 | 13.132% | 0.169532 | 2.210794 | 0.279226 | 0.854146 | 87.573% |
| 0.5 | 0 | 165739.2 | 12.648% | 5.166035 | 28.637% | 0.144863 | 1.772013 | 0.254211 | 0.840542 | 85.168% |
| 1 | 0 | 178229.9 | 21.137% | 3.820804 | 47.220% | 0.102734 | 1.394123 | 0.292748 | 0.823567 | 81.440% |
| 2 | 0 | 197739.3 | 34.397% | 2.853273 | 60.585% | 0.060476 | 1.118542 | 0.318794 | 0.788925 | 75.571% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
