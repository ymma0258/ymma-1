# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.0 | 0.000% | 8.403358 | 0.000% | 0.262897 | 2.561343 | 0.185325 | 0.866947 | 88.888% |
| 0.25 | 0 | 157124.3 | 6.841% | 6.755102 | 19.614% | 0.169018 | 2.160545 | 0.205208 | 0.863805 | 87.861% |
| 0.5 | 0 | 165864.4 | 12.784% | 5.210215 | 37.998% | 0.127302 | 1.695478 | 0.222707 | 0.844024 | 84.669% |
| 1 | 0 | 176415.5 | 19.958% | 3.184019 | 62.110% | 0.075092 | 1.040145 | 0.214434 | 0.792001 | 76.736% |
| 2 | 0 | 191246.2 | 30.043% | 2.641606 | 68.565% | 0.058859 | 0.768222 | 0.220852 | 0.765352 | 72.341% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
