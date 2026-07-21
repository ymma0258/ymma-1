# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.0 | 0.000% | 9.401245 | 0.000% | 0.278082 | 2.856608 | 0.185536 | 0.876592 | 90.373% |
| 0.25 | 0 | 157646.1 | 7.196% | 7.595381 | 19.209% | 0.222645 | 2.447422 | 0.218084 | 0.876767 | 89.411% |
| 0.5 | 0 | 167083.1 | 13.613% | 5.956300 | 36.643% | 0.160359 | 2.014150 | 0.268033 | 0.862367 | 86.550% |
| 1 | 0 | 178245.0 | 21.202% | 3.758821 | 60.018% | 0.097874 | 1.312718 | 0.249792 | 0.825671 | 80.099% |
| 2 | 0 | 194994.6 | 32.592% | 3.213072 | 65.823% | 0.071426 | 1.008664 | 0.211571 | 0.810880 | 77.522% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
