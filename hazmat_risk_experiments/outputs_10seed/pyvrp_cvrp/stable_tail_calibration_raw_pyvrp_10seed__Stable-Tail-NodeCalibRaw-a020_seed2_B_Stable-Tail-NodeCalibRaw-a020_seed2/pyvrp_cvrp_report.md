# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.2 | 0.000% | 9.030631 | 0.000% | 0.284255 | 3.375856 | 0.313044 | 0.874626 | 89.577% |
| 0.25 | 0 | 157061.8 | 6.653% | 7.745000 | 14.236% | 0.227220 | 2.663328 | 0.281906 | 0.872785 | 88.990% |
| 0.5 | 0 | 165486.0 | 12.374% | 6.472648 | 28.326% | 0.176959 | 2.291128 | 0.267699 | 0.862450 | 87.162% |
| 1 | 0 | 177960.7 | 20.845% | 4.506481 | 50.098% | 0.120486 | 1.724898 | 0.273344 | 0.842414 | 83.226% |
| 2 | 0 | 197065.7 | 33.818% | 3.663794 | 59.429% | 0.090736 | 1.600843 | 0.351434 | 0.826921 | 80.089% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
