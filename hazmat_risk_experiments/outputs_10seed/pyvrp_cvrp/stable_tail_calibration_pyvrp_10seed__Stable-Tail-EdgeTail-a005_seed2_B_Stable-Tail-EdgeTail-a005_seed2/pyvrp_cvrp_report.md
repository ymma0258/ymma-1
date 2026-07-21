# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147196.9 | 0.000% | 8.865540 | 0.000% | 0.280748 | 3.413406 | 0.313835 | 0.873880 | 89.538% |
| 0.25 | 0 | 156918.0 | 6.604% | 7.260518 | 18.104% | 0.212753 | 2.929562 | 0.318594 | 0.870405 | 88.521% |
| 0.5 | 0 | 165878.3 | 12.691% | 6.211547 | 29.936% | 0.163910 | 2.182320 | 0.240563 | 0.859837 | 86.803% |
| 1 | 0 | 178456.3 | 21.236% | 4.524678 | 48.963% | 0.121417 | 1.771123 | 0.287634 | 0.844167 | 83.383% |
| 2 | 0 | 196636.6 | 33.587% | 3.576091 | 59.663% | 0.088986 | 1.641420 | 0.370688 | 0.825161 | 79.795% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
