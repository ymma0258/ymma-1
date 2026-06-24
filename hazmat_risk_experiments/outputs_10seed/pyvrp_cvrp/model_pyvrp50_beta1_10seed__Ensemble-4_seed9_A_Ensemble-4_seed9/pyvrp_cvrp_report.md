# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.494044 | 0.000% | 0.213021 | 2.275843 | 0.176819 | 0.852524 | 87.967% |
| 1 | 0 | 157234.9 | 17.342% | 2.610788 | 65.162% | 0.054410 | 0.852985 | 0.242114 | 0.711836 | 70.287% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
