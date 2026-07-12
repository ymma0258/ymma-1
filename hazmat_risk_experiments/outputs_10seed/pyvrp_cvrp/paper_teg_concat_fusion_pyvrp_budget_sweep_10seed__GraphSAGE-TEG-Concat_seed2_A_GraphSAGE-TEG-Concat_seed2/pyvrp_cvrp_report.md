# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 8.561911 | 0.000% | 0.283032 | 2.521859 | 0.187776 | 0.878198 | 89.864% |
| 0.25 | 0 | 142363.4 | 6.137% | 5.759415 | 32.732% | 0.171117 | 1.905422 | 0.218778 | 0.865513 | 87.540% |
| 0.5 | 0 | 148613.6 | 10.797% | 4.758509 | 44.422% | 0.140698 | 1.729945 | 0.259135 | 0.857376 | 85.586% |
| 1 | 0 | 157495.8 | 17.419% | 3.130068 | 63.442% | 0.085675 | 1.175277 | 0.301005 | 0.817027 | 78.472% |
| 2 | 0 | 171695.3 | 28.005% | 2.712123 | 68.323% | 0.067259 | 1.052760 | 0.295511 | 0.791361 | 74.521% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
