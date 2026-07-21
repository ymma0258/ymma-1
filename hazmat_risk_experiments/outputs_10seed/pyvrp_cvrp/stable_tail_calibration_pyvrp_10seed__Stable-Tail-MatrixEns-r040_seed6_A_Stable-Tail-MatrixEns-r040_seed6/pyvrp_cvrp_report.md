# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 4.642540 | 0.000% | 0.135962 | 1.308385 | 0.145141 | 0.864927 | 88.419% |
| 0.25 | 0 | 143048.3 | 6.754% | 3.253968 | 29.910% | 0.092874 | 1.108356 | 0.267154 | 0.851587 | 86.136% |
| 0.5 | 0 | 148952.5 | 11.160% | 2.413843 | 48.006% | 0.071734 | 0.878272 | 0.288479 | 0.819209 | 81.789% |
| 1 | 0 | 158193.9 | 18.057% | 1.757367 | 62.146% | 0.047431 | 0.543173 | 0.236306 | 0.780087 | 76.103% |
| 2 | 0 | 172209.3 | 28.516% | 1.349548 | 70.931% | 0.030625 | 0.483081 | 0.296539 | 0.728001 | 68.831% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
