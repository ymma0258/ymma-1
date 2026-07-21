# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 10.606116 | 0.000% | 0.322973 | 3.184868 | 0.188156 | 0.881398 | 91.078% |
| 0.25 | 0 | 158231.1 | 7.447% | 8.065724 | 23.952% | 0.237490 | 2.783881 | 0.246673 | 0.878119 | 89.559% |
| 0.5 | 0 | 167734.1 | 13.900% | 6.382035 | 39.827% | 0.177988 | 2.291733 | 0.265081 | 0.863779 | 86.804% |
| 1 | 0 | 178918.6 | 21.495% | 4.082250 | 61.510% | 0.104655 | 1.370797 | 0.249213 | 0.830419 | 80.596% |
| 2 | 0 | 196075.2 | 33.146% | 3.539234 | 66.630% | 0.084648 | 1.144824 | 0.245350 | 0.817681 | 78.174% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
