# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.323610 | 0.000% | 0.204786 | 2.231959 | 0.178869 | 0.834297 | 86.007% |
| 0.5 | 0 | 149137.8 | 11.299% | 4.068159 | 44.451% | 0.111757 | 1.712190 | 0.304705 | 0.767243 | 77.659% |
| 1 | 0 | 158385.7 | 18.200% | 2.927334 | 60.029% | 0.063554 | 0.915462 | 0.191036 | 0.693318 | 68.812% |
| 1.5 | 0 | 166087.0 | 23.948% | 2.671596 | 63.521% | 0.053496 | 0.888479 | 0.235409 | 0.673013 | 65.844% |
| 2 | 0 | 173310.1 | 29.338% | 2.520981 | 65.577% | 0.044488 | 0.809366 | 0.220619 | 0.654968 | 63.775% |
| 3 | 0 | 186046.8 | 38.843% | 2.268687 | 69.022% | 0.039417 | 0.656493 | 0.175059 | 0.617897 | 59.470% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
