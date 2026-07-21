# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.4 | 0.000% | 7.478527 | 0.000% | 0.240204 | 2.156232 | 0.168290 | 0.872084 | 88.776% |
| 0.25 | 0 | 142675.1 | 6.106% | 5.240161 | 29.931% | 0.151519 | 1.726764 | 0.211071 | 0.860049 | 86.655% |
| 0.5 | 0 | 148185.7 | 10.204% | 3.499644 | 53.204% | 0.101132 | 1.370283 | 0.334675 | 0.819101 | 80.540% |
| 1 | 0 | 156385.6 | 16.303% | 2.382089 | 68.148% | 0.061132 | 0.958665 | 0.300451 | 0.765081 | 72.536% |
| 2 | 0 | 168096.9 | 25.012% | 1.947108 | 73.964% | 0.043007 | 0.624534 | 0.225587 | 0.726041 | 66.944% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
