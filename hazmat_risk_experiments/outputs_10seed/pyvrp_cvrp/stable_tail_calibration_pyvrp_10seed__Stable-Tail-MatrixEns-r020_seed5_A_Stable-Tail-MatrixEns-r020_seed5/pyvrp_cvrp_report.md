# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 5.859924 | 0.000% | 0.179211 | 1.711516 | 0.166840 | 0.872935 | 88.854% |
| 0.25 | 0 | 142496.7 | 6.342% | 3.615871 | 38.295% | 0.101391 | 1.255273 | 0.264252 | 0.847859 | 84.691% |
| 0.5 | 0 | 147984.7 | 10.438% | 2.895347 | 50.591% | 0.084461 | 1.064601 | 0.288711 | 0.825755 | 81.452% |
| 1 | 0 | 156180.9 | 16.555% | 1.998714 | 65.892% | 0.051190 | 0.769206 | 0.274336 | 0.770655 | 73.625% |
| 2 | 0 | 167710.3 | 25.159% | 1.451738 | 75.226% | 0.030769 | 0.485844 | 0.237599 | 0.705512 | 64.150% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
