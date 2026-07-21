# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 7.739550 | 0.000% | 0.238397 | 2.251699 | 0.169594 | 0.869282 | 88.671% |
| 0.25 | 0 | 142895.6 | 6.587% | 5.643422 | 27.083% | 0.163757 | 1.756556 | 0.237724 | 0.859864 | 87.196% |
| 0.5 | 0 | 149339.9 | 11.394% | 3.914096 | 49.427% | 0.113234 | 1.475040 | 0.242275 | 0.822737 | 81.876% |
| 1 | 0 | 158470.7 | 18.205% | 2.804750 | 63.761% | 0.062956 | 0.789727 | 0.174516 | 0.779626 | 75.495% |
| 2 | 0 | 173559.3 | 29.459% | 2.371390 | 69.360% | 0.049763 | 0.738741 | 0.213012 | 0.755979 | 71.411% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
