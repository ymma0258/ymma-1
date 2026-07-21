# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 7.016459 | 0.000% | 0.218504 | 2.617311 | 0.306303 | 0.874019 | 89.522% |
| 0.25 | 0 | 156514.3 | 6.378% | 5.995150 | 14.556% | 0.183998 | 2.184706 | 0.305564 | 0.873913 | 89.024% |
| 0.5 | 0 | 165116.9 | 12.225% | 5.046497 | 28.076% | 0.146742 | 1.718510 | 0.260171 | 0.859526 | 86.901% |
| 1 | 0 | 177907.6 | 20.918% | 3.577996 | 49.006% | 0.097419 | 1.299219 | 0.251704 | 0.844052 | 83.392% |
| 2 | 0 | 196845.3 | 33.790% | 2.899224 | 58.680% | 0.073102 | 1.293563 | 0.352021 | 0.826673 | 80.096% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
