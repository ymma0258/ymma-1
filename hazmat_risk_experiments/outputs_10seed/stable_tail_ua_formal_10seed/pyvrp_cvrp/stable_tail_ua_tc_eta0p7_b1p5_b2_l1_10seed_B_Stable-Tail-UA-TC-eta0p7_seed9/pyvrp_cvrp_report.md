# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 14.086169 | 0.000% | 0.360164 | 4.368801 | 0.196285 | 0.848109 | 88.856% |
| 1.5 | 1 | 218509.4 | 48.918% | 5.216148 | 62.970% | 0.097082 | 2.340099 | 0.405853 | 0.753885 | 74.859% |
| 2 | 1 | 229736.7 | 56.570% | 5.222445 | 62.925% | 0.097958 | 2.143169 | 0.394215 | 0.753300 | 74.813% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
