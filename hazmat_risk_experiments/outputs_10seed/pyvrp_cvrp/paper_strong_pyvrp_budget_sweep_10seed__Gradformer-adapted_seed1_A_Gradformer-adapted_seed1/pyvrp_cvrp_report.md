# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 8.060977 | 0.000% | 0.253717 | 2.249096 | 0.156664 | 0.859617 | 88.677% |
| 0.25 | 0 | 143390.3 | 6.850% | 5.552113 | 31.124% | 0.164951 | 1.793979 | 0.199963 | 0.847414 | 86.719% |
| 0.5 | 0 | 150390.6 | 12.066% | 4.247899 | 47.303% | 0.126238 | 1.392074 | 0.194587 | 0.822050 | 83.148% |
| 1 | 0 | 160881.0 | 19.883% | 3.290105 | 59.185% | 0.091746 | 1.100727 | 0.222783 | 0.794719 | 78.512% |
| 2 | 0 | 174794.2 | 30.251% | 2.195650 | 72.762% | 0.050257 | 0.715576 | 0.251774 | 0.724436 | 68.187% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
