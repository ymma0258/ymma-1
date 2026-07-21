# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.2 | 0.000% | 9.125555 | 0.000% | 0.261914 | 3.137881 | 0.239625 | 0.869216 | 89.272% |
| 0.25 | 0 | 158053.6 | 7.375% | 8.004136 | 12.289% | 0.197575 | 2.738541 | 0.236596 | 0.870713 | 89.524% |
| 0.5 | 0 | 167926.6 | 14.083% | 6.353332 | 30.379% | 0.168806 | 2.181897 | 0.247225 | 0.861645 | 87.142% |
| 1 | 0 | 181803.0 | 23.510% | 4.252362 | 53.402% | 0.113136 | 1.750886 | 0.361566 | 0.829109 | 81.315% |
| 2 | 0 | 202858.4 | 37.814% | 3.906951 | 57.187% | 0.101000 | 1.417598 | 0.335693 | 0.822069 | 79.868% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
