# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.1 | 0.000% | 8.374076 | 0.000% | 0.261086 | 3.301665 | 0.340314 | 0.871490 | 90.025% |
| 0.25 | 0 | 156902.6 | 6.545% | 7.284718 | 13.009% | 0.218120 | 2.849673 | 0.339896 | 0.874022 | 89.444% |
| 0.5 | 0 | 165635.8 | 12.475% | 6.047917 | 27.778% | 0.162995 | 2.277735 | 0.281940 | 0.861681 | 87.131% |
| 1 | 0 | 178918.5 | 21.495% | 4.572648 | 45.395% | 0.126139 | 1.901102 | 0.335366 | 0.851743 | 84.543% |
| 2 | 0 | 199951.3 | 35.777% | 3.767150 | 55.014% | 0.095442 | 1.593211 | 0.359311 | 0.833544 | 81.498% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
