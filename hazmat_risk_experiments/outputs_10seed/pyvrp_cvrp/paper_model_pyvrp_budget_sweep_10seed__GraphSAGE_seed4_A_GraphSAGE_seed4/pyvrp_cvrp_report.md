# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 8.726097 | 0.000% | 0.281334 | 2.568529 | 0.178236 | 0.878999 | 90.216% |
| 0.25 | 0 | 142973.8 | 6.381% | 6.377062 | 26.920% | 0.188260 | 1.970482 | 0.211662 | 0.871719 | 88.507% |
| 0.5 | 0 | 149599.4 | 11.311% | 5.197903 | 40.433% | 0.156993 | 1.800787 | 0.272059 | 0.860008 | 86.446% |
| 1 | 0 | 159465.7 | 18.652% | 3.625409 | 58.453% | 0.088685 | 1.260362 | 0.316753 | 0.823886 | 80.687% |
| 2 | 0 | 175099.7 | 30.285% | 2.919993 | 66.537% | 0.071181 | 1.159851 | 0.358476 | 0.799004 | 76.748% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
