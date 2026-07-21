# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.9 | 0.000% | 8.839015 | 0.000% | 0.245056 | 2.878617 | 0.212300 | 0.868870 | 89.059% |
| 0.25 | 0 | 157822.1 | 7.315% | 7.728106 | 12.568% | 0.189656 | 2.536792 | 0.233925 | 0.868263 | 89.138% |
| 0.5 | 0 | 167975.9 | 14.220% | 6.038318 | 31.686% | 0.156567 | 2.102275 | 0.256336 | 0.856439 | 86.466% |
| 1 | 0 | 181326.3 | 23.298% | 4.130405 | 53.271% | 0.108337 | 1.549321 | 0.313715 | 0.824258 | 80.894% |
| 2 | 0 | 202772.3 | 37.880% | 3.703923 | 58.096% | 0.095088 | 1.452558 | 0.349679 | 0.817137 | 79.178% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
