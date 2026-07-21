# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 6.207338 | 0.000% | 0.182626 | 1.716988 | 0.143651 | 0.865941 | 88.605% |
| 0.25 | 0 | 143331.2 | 6.912% | 4.016131 | 35.300% | 0.113920 | 1.280890 | 0.237080 | 0.843030 | 85.028% |
| 0.5 | 0 | 149258.6 | 11.333% | 3.322201 | 46.479% | 0.099020 | 1.197008 | 0.283145 | 0.821774 | 82.228% |
| 1 | 0 | 158916.8 | 18.537% | 2.299627 | 62.953% | 0.060868 | 0.758695 | 0.277270 | 0.776039 | 75.602% |
| 2 | 0 | 173569.8 | 29.467% | 1.846089 | 70.260% | 0.042751 | 0.667774 | 0.278316 | 0.734029 | 69.723% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
