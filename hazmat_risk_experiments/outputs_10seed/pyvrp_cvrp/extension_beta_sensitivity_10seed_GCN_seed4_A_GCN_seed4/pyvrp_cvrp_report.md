# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.228465 | 0.000% | 0.255166 | 2.459731 | 0.166601 | 0.863744 | 89.376% |
| 0.5 | 0 | 150912.4 | 12.623% | 5.058801 | 38.521% | 0.145924 | 1.576354 | 0.205199 | 0.845841 | 85.550% |
| 1 | 0 | 161510.6 | 20.532% | 3.316378 | 59.696% | 0.073059 | 1.166521 | 0.309959 | 0.796006 | 78.277% |
| 1.5 | 0 | 170593.6 | 27.311% | 3.032166 | 63.150% | 0.066960 | 1.071658 | 0.317032 | 0.779339 | 75.876% |
| 2 | 0 | 178460.7 | 33.182% | 2.913731 | 64.590% | 0.062538 | 1.003324 | 0.299426 | 0.771851 | 74.755% |
| 3 | 0 | 193230.2 | 44.204% | 2.534635 | 69.197% | 0.052924 | 1.043208 | 0.363157 | 0.747775 | 71.223% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
