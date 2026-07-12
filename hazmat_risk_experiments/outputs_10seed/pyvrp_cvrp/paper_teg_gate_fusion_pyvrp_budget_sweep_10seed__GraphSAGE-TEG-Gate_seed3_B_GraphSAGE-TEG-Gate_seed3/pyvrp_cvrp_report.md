# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.4 | 0.000% | 7.394114 | 0.000% | 0.225240 | 2.207061 | 0.175811 | 0.867513 | 89.222% |
| 0.25 | 0 | 157019.9 | 6.722% | 6.387616 | 13.612% | 0.162115 | 2.037397 | 0.208723 | 0.867471 | 89.204% |
| 0.5 | 0 | 166244.2 | 12.991% | 5.310163 | 28.184% | 0.134440 | 1.623421 | 0.206432 | 0.862858 | 87.739% |
| 1 | 0 | 178766.5 | 21.502% | 3.631791 | 50.883% | 0.094722 | 1.188970 | 0.234707 | 0.835413 | 83.066% |
| 2 | 0 | 198618.9 | 34.995% | 2.866334 | 61.235% | 0.069266 | 1.147710 | 0.290382 | 0.813120 | 78.780% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
