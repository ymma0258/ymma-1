# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.6 | 0.000% | 9.871238 | 0.000% | 0.291337 | 3.155883 | 0.212587 | 0.879361 | 90.603% |
| 0.25 | 0 | 158163.9 | 7.256% | 8.014979 | 18.805% | 0.231662 | 2.506489 | 0.218151 | 0.876604 | 89.348% |
| 0.5 | 0 | 167606.5 | 13.660% | 5.942881 | 39.796% | 0.156298 | 2.146206 | 0.276218 | 0.856474 | 85.941% |
| 1 | 0 | 178987.8 | 21.378% | 3.831480 | 61.185% | 0.096151 | 1.271251 | 0.235824 | 0.824372 | 79.542% |
| 2 | 0 | 196141.8 | 33.010% | 3.346961 | 66.094% | 0.074460 | 1.132117 | 0.255925 | 0.808894 | 76.987% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
