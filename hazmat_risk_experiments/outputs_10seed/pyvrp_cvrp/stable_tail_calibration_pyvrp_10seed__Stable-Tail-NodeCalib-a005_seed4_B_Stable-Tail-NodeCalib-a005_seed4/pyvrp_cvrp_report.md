# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.5 | 0.000% | 8.417078 | 0.000% | 0.254842 | 2.926253 | 0.241101 | 0.872552 | 89.155% |
| 0.25 | 0 | 157076.9 | 6.615% | 7.006533 | 16.758% | 0.190726 | 2.203747 | 0.206466 | 0.866353 | 87.640% |
| 0.5 | 0 | 165705.1 | 12.472% | 5.504590 | 34.602% | 0.153697 | 1.788149 | 0.245354 | 0.853086 | 85.100% |
| 1 | 0 | 176213.0 | 19.604% | 3.845690 | 54.311% | 0.096100 | 1.347054 | 0.272992 | 0.817125 | 79.663% |
| 2 | 0 | 192687.2 | 30.786% | 3.184183 | 62.170% | 0.065820 | 1.240953 | 0.311208 | 0.799005 | 76.625% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
