# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.030872 | 0.000% | 0.213061 | 2.140597 | 0.187897 | 0.878589 | 90.594% |
| 0.25 | 0 | 157496.6 | 7.191% | 5.770886 | 17.921% | 0.167271 | 1.768967 | 0.202839 | 0.877080 | 89.610% |
| 0.5 | 0 | 167100.2 | 13.727% | 4.413513 | 37.227% | 0.124144 | 1.492331 | 0.253220 | 0.861582 | 86.527% |
| 1 | 0 | 178053.3 | 21.182% | 2.782902 | 60.419% | 0.070457 | 0.939896 | 0.244715 | 0.824941 | 79.995% |
| 2 | 0 | 194800.4 | 32.580% | 2.388781 | 66.024% | 0.055445 | 0.745470 | 0.216528 | 0.811398 | 77.595% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
