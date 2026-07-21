# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 6.563652 | 0.000% | 0.201052 | 1.863802 | 0.164367 | 0.873217 | 88.948% |
| 0.25 | 0 | 142396.3 | 6.215% | 4.786256 | 27.079% | 0.133744 | 1.493407 | 0.227513 | 0.861646 | 86.754% |
| 0.5 | 0 | 148073.6 | 10.449% | 3.216389 | 50.997% | 0.093815 | 1.224266 | 0.297481 | 0.825107 | 81.363% |
| 1 | 0 | 156180.6 | 16.497% | 2.228224 | 66.052% | 0.056789 | 0.881453 | 0.300870 | 0.766857 | 73.198% |
| 2 | 0 | 167612.9 | 25.024% | 1.741979 | 73.460% | 0.038587 | 0.561354 | 0.226679 | 0.724634 | 66.576% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
