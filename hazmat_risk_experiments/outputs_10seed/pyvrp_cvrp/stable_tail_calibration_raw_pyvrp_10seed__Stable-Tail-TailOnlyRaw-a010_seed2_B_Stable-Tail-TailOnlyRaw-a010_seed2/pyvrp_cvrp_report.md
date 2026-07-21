# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.1 | 0.000% | 9.237239 | 0.000% | 0.291967 | 3.509607 | 0.312301 | 0.877270 | 89.950% |
| 0.25 | 0 | 156664.9 | 6.528% | 8.257520 | 10.606% | 0.250556 | 3.105061 | 0.321071 | 0.876669 | 89.626% |
| 0.5 | 0 | 165257.9 | 12.371% | 6.462469 | 30.039% | 0.175745 | 2.526003 | 0.284881 | 0.866617 | 87.636% |
| 1 | 0 | 177677.3 | 20.816% | 4.535542 | 50.899% | 0.120377 | 1.862010 | 0.326192 | 0.847295 | 83.566% |
| 2 | 0 | 195814.8 | 33.149% | 3.787261 | 59.000% | 0.094412 | 1.728790 | 0.350225 | 0.830633 | 80.615% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
