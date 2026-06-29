# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.577929 | 0.000% | 0.238557 | 2.442522 | 0.222753 | 0.879945 | 90.033% |
| 1 | 0 | 156791.2 | 17.010% | 2.469142 | 67.417% | 0.052817 | 0.906304 | 0.269736 | 0.790882 | 75.433% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
