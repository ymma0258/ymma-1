# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134531.1 | 0.000% | 7.108124 | 0.000% | 0.226022 | 2.173295 | 0.192938 | 0.877587 | 89.287% |
| 0.25 | 0 | 142830.5 | 6.169% | 4.580155 | 35.565% | 0.140499 | 1.369209 | 0.177637 | 0.870151 | 88.043% |
| 0.5 | 0 | 149454.6 | 11.093% | 3.461912 | 51.296% | 0.101347 | 1.270677 | 0.235726 | 0.843901 | 84.174% |
| 1 | 0 | 158401.4 | 17.743% | 2.593200 | 63.518% | 0.057713 | 0.770342 | 0.174652 | 0.810538 | 78.962% |
| 2 | 0 | 172747.4 | 28.407% | 1.845178 | 74.041% | 0.034997 | 0.549754 | 0.191805 | 0.760111 | 71.048% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
