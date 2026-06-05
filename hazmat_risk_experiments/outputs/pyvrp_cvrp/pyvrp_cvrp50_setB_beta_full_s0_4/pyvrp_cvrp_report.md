# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 157625.0 | 0.000% | 7.846111 | 0.000% | 0.025541 | 3.246252 | 0.273891 | 0.920148 | 99.751% |
| 0.25 | 165678.4 | 5.109% | 5.847591 | 25.471% | 0.018899 | 2.392542 | 0.279832 | 0.936480 | 100.000% |
| 0.5 | 169990.6 | 7.845% | 3.480423 | 55.641% | 0.011065 | 1.134830 | 0.270003 | 0.957384 | 100.000% |
| 1 | 176550.4 | 12.007% | 2.386952 | 69.578% | 0.007455 | 1.170323 | 0.387893 | 0.970534 | 100.000% |
| 2 | 186683.0 | 18.435% | 1.913563 | 75.611% | 0.005877 | 0.928019 | 0.423417 | 0.976636 | 100.000% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
