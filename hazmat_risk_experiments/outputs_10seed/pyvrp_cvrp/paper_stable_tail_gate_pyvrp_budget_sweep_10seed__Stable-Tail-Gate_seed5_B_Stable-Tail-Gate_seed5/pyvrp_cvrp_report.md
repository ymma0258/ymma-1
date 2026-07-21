# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 7.990433 | 0.000% | 0.246947 | 2.561656 | 0.199134 | 0.862469 | 88.460% |
| 0.25 | 0 | 156301.7 | 6.426% | 6.852704 | 14.239% | 0.164503 | 2.296533 | 0.231913 | 0.857717 | 88.114% |
| 0.5 | 0 | 165604.7 | 12.761% | 5.180881 | 35.161% | 0.131903 | 1.476532 | 0.169134 | 0.841298 | 84.814% |
| 1 | 0 | 176665.3 | 20.292% | 3.718214 | 53.467% | 0.092980 | 1.268910 | 0.295707 | 0.807912 | 79.767% |
| 2 | 0 | 193111.7 | 31.490% | 2.983274 | 62.664% | 0.071381 | 0.891795 | 0.237167 | 0.777702 | 74.932% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
