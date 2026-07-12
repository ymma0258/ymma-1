# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.458377 | 0.000% | 0.295657 | 3.021221 | 0.210769 | 0.854357 | 88.885% |
| 0.25 | 0 | 157875.5 | 7.400% | 8.355693 | 11.658% | 0.206172 | 2.892855 | 0.223233 | 0.853299 | 89.405% |
| 0.5 | 0 | 168457.6 | 14.599% | 7.083982 | 25.104% | 0.185355 | 2.211837 | 0.181867 | 0.850506 | 87.885% |
| 1 | 0 | 183826.9 | 25.055% | 4.998603 | 47.152% | 0.135273 | 1.640540 | 0.253630 | 0.822140 | 83.210% |
| 2 | 0 | 204833.2 | 39.345% | 3.702821 | 60.851% | 0.087261 | 1.423000 | 0.334545 | 0.789096 | 77.390% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
