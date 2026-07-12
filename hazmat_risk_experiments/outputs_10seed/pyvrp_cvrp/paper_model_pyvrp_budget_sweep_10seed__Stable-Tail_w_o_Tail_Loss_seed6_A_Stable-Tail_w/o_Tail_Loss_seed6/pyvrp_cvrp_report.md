# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134065.0 | 0.000% | 4.831810 | 0.000% | 0.162700 | 1.280909 | 0.139805 | 0.845192 | 88.234% |
| 0.25 | 0 | 143949.4 | 7.373% | 3.637737 | 24.713% | 0.116751 | 1.112205 | 0.173910 | 0.836596 | 87.007% |
| 0.5 | 0 | 151457.4 | 12.973% | 2.766223 | 42.750% | 0.082270 | 0.866830 | 0.188451 | 0.815622 | 83.248% |
| 1 | 0 | 162983.9 | 21.571% | 2.087122 | 56.805% | 0.056710 | 0.854141 | 0.320146 | 0.780096 | 78.189% |
| 2 | 0 | 180039.3 | 34.293% | 1.511214 | 68.724% | 0.034662 | 0.638083 | 0.352346 | 0.717549 | 70.095% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
