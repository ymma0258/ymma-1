# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 8.025570 | 0.000% | 0.234151 | 2.238035 | 0.151115 | 0.866872 | 88.809% |
| 0.25 | 0 | 142685.9 | 6.484% | 5.710604 | 28.845% | 0.163764 | 1.990745 | 0.290959 | 0.857636 | 87.010% |
| 0.5 | 0 | 148289.3 | 10.665% | 4.104163 | 48.861% | 0.120651 | 1.631255 | 0.331533 | 0.820413 | 82.129% |
| 1 | 0 | 157592.4 | 17.608% | 2.863898 | 64.315% | 0.075968 | 0.970621 | 0.285526 | 0.775781 | 75.498% |
| 2 | 0 | 171282.3 | 27.824% | 2.360110 | 70.593% | 0.055254 | 0.798459 | 0.268437 | 0.736282 | 70.191% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
