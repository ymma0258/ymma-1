# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 7.044863 | 0.000% | 0.220801 | 2.688141 | 0.309764 | 0.873746 | 89.470% |
| 0.25 | 0 | 156555.8 | 6.599% | 5.869169 | 16.689% | 0.176706 | 2.149797 | 0.301756 | 0.869942 | 88.518% |
| 0.5 | 0 | 165076.4 | 12.401% | 4.933024 | 29.977% | 0.136813 | 1.845063 | 0.278827 | 0.860353 | 86.774% |
| 1 | 0 | 177145.5 | 20.619% | 3.406223 | 51.650% | 0.092751 | 1.405591 | 0.323211 | 0.841545 | 82.799% |
| 2 | 0 | 196206.2 | 33.597% | 2.815078 | 60.041% | 0.069552 | 1.317388 | 0.346176 | 0.822684 | 79.495% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
