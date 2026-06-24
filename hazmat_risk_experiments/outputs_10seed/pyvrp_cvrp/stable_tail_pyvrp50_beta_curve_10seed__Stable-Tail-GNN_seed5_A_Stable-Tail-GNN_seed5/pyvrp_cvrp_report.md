# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.152817 | 0.000% | 0.175570 | 1.791873 | 0.170530 | 0.873796 | 89.035% |
| 0.25 | 0 | 142019.1 | 5.986% | 4.515920 | 26.604% | 0.126217 | 1.505093 | 0.238235 | 0.861333 | 86.532% |
| 0.5 | 0 | 147093.7 | 9.773% | 3.146264 | 48.865% | 0.090319 | 1.145701 | 0.296597 | 0.825530 | 81.443% |
| 1 | 0 | 155535.2 | 16.073% | 2.202071 | 64.210% | 0.057789 | 0.828697 | 0.300631 | 0.770454 | 73.534% |
| 2 | 0 | 166945.6 | 24.589% | 1.801428 | 70.722% | 0.041499 | 0.580317 | 0.251754 | 0.738269 | 68.619% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
