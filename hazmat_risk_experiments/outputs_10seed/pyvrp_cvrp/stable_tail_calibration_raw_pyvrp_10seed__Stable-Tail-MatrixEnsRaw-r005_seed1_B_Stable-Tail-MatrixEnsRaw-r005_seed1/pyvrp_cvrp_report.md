# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147196.9 | 0.000% | 9.302033 | 0.000% | 0.295136 | 3.249648 | 0.259086 | 0.872083 | 89.852% |
| 0.25 | 0 | 155930.4 | 5.933% | 7.538054 | 18.963% | 0.206553 | 2.561382 | 0.251964 | 0.868641 | 88.603% |
| 0.5 | 0 | 164229.6 | 11.571% | 6.231199 | 33.013% | 0.174979 | 1.952875 | 0.226011 | 0.859353 | 86.690% |
| 1 | 0 | 173640.7 | 17.965% | 3.691148 | 60.319% | 0.086128 | 1.321088 | 0.262026 | 0.813580 | 78.959% |
| 2 | 0 | 187900.1 | 27.652% | 3.090698 | 66.774% | 0.063552 | 1.148788 | 0.286214 | 0.795547 | 75.821% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
