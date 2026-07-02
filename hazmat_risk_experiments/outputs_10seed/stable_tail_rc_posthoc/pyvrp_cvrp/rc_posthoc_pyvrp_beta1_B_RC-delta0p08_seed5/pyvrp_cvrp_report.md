# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.228393 | 0.000% | 0.225543 | 2.472833 | 0.232709 | 0.876678 | 89.495% |
| 1 | 0 | 174520.6 | 18.939% | 3.127105 | 56.739% | 0.075838 | 1.210807 | 0.351930 | 0.817366 | 79.187% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
