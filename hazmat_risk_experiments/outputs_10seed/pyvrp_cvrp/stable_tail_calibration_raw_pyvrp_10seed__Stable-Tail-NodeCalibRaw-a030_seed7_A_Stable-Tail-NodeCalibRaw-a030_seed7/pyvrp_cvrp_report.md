# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.1 | 0.000% | 9.530303 | 0.000% | 0.318137 | 2.702479 | 0.177293 | 0.874753 | 89.560% |
| 0.25 | 0 | 143191.4 | 6.702% | 6.518164 | 31.606% | 0.190054 | 2.232080 | 0.229018 | 0.864511 | 87.509% |
| 0.5 | 0 | 149132.0 | 11.128% | 4.626964 | 51.450% | 0.121488 | 1.587935 | 0.226556 | 0.837235 | 83.312% |
| 1 | 0 | 158419.7 | 18.049% | 3.277022 | 65.615% | 0.080042 | 1.309617 | 0.301877 | 0.797030 | 76.968% |
| 2 | 0 | 171526.1 | 27.816% | 2.601696 | 72.701% | 0.053520 | 0.816401 | 0.241671 | 0.763753 | 71.727% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
