# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 7.902089 | 0.000% | 0.244699 | 2.471068 | 0.200695 | 0.864031 | 88.189% |
| 0.25 | 0 | 156098.7 | 6.288% | 6.316280 | 20.068% | 0.149051 | 2.097992 | 0.218589 | 0.858096 | 87.053% |
| 0.5 | 0 | 164454.1 | 11.977% | 5.098070 | 35.485% | 0.124988 | 1.603406 | 0.204132 | 0.844934 | 84.622% |
| 1 | 0 | 174739.9 | 18.981% | 3.215464 | 59.309% | 0.077604 | 0.996308 | 0.217836 | 0.792090 | 76.869% |
| 2 | 0 | 188795.5 | 28.551% | 2.485728 | 68.543% | 0.055156 | 0.704316 | 0.199163 | 0.753925 | 70.873% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
