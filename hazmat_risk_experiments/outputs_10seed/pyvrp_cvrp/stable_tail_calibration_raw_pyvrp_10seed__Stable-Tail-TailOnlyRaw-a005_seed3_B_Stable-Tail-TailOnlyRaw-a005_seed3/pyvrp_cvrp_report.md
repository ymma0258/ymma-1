# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 6.836253 | 0.000% | 0.203109 | 2.259768 | 0.229134 | 0.868447 | 88.716% |
| 0.25 | 0 | 155515.0 | 5.603% | 5.938268 | 13.136% | 0.148384 | 2.240138 | 0.264597 | 0.864580 | 87.992% |
| 0.5 | 0 | 163314.7 | 10.899% | 4.920918 | 28.017% | 0.123676 | 1.975880 | 0.289226 | 0.855724 | 86.155% |
| 1 | 0 | 175330.9 | 19.059% | 3.629919 | 46.902% | 0.090222 | 1.470076 | 0.304772 | 0.835589 | 82.294% |
| 2 | 0 | 192656.4 | 30.824% | 2.786647 | 59.237% | 0.069085 | 1.214847 | 0.320167 | 0.809777 | 77.672% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
