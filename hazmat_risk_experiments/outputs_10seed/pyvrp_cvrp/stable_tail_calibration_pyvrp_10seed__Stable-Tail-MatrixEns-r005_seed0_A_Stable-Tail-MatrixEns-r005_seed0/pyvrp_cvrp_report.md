# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 7.174444 | 0.000% | 0.213557 | 2.239784 | 0.215001 | 0.882503 | 90.166% |
| 0.25 | 0 | 142459.2 | 6.262% | 4.386292 | 38.862% | 0.132949 | 1.501899 | 0.247310 | 0.862341 | 86.486% |
| 0.5 | 0 | 148198.4 | 10.542% | 3.500234 | 51.212% | 0.100406 | 1.613570 | 0.359599 | 0.839870 | 83.418% |
| 1 | 0 | 156246.2 | 16.545% | 2.291333 | 68.063% | 0.048304 | 0.866308 | 0.261333 | 0.782504 | 74.853% |
| 2 | 0 | 168134.4 | 25.413% | 1.856207 | 74.128% | 0.034765 | 0.611350 | 0.231372 | 0.751029 | 69.754% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
