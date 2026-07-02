# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 6.883367 | 0.000% | 0.204340 | 2.370042 | 0.226137 | 0.873010 | 88.919% |
| 0.5 | 0 | 163532.6 | 11.451% | 4.401264 | 36.059% | 0.113867 | 1.463655 | 0.216067 | 0.848600 | 84.363% |
| 1 | 0 | 173995.4 | 18.581% | 2.945257 | 57.212% | 0.073990 | 1.154991 | 0.293761 | 0.801541 | 77.746% |
| 1.5 | 0 | 181915.7 | 23.979% | 2.608521 | 62.104% | 0.060685 | 1.088640 | 0.319336 | 0.784076 | 75.005% |
| 2 | 0 | 189411.1 | 29.087% | 2.441765 | 64.527% | 0.054897 | 0.966689 | 0.306609 | 0.775725 | 73.524% |
| 3 | 0 | 202355.4 | 37.909% | 2.158104 | 68.648% | 0.042497 | 0.876738 | 0.295614 | 0.759497 | 70.688% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
