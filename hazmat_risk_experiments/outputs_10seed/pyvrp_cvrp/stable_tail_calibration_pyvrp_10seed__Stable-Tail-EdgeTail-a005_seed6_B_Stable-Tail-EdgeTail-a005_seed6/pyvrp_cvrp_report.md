# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146931.0 | 0.000% | 8.933184 | 0.000% | 0.261844 | 3.018602 | 0.231898 | 0.869213 | 89.261% |
| 0.25 | 0 | 158232.7 | 7.692% | 7.835903 | 12.283% | 0.200584 | 2.647677 | 0.252155 | 0.868129 | 89.121% |
| 0.5 | 0 | 168458.6 | 14.652% | 5.743679 | 35.704% | 0.147646 | 1.967107 | 0.272974 | 0.854472 | 86.080% |
| 1 | 0 | 182123.9 | 23.952% | 4.144305 | 53.608% | 0.104090 | 1.661395 | 0.333394 | 0.826993 | 81.090% |
| 2 | 0 | 202824.5 | 38.041% | 3.674603 | 58.866% | 0.092814 | 1.406329 | 0.328792 | 0.814553 | 78.860% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
