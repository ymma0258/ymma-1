# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 9.785296 | 0.000% | 0.217206 | 3.173264 | 0.224966 | 0.882463 | 90.181% |
| 1 | 0 | 155956.6 | 16.388% | 3.009977 | 69.240% | 0.052965 | 1.062073 | 0.291689 | 0.786868 | 74.237% |
| 2 | 0 | 166886.1 | 24.544% | 2.099605 | 78.543% | 0.031452 | 0.617486 | 0.216826 | 0.698770 | 61.878% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
