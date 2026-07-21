# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 4.532108 | 0.000% | 0.131740 | 1.397051 | 0.178186 | 0.870416 | 88.996% |
| 0.25 | 0 | 142671.9 | 6.473% | 3.379605 | 25.430% | 0.097162 | 1.067101 | 0.237549 | 0.862644 | 87.351% |
| 0.5 | 0 | 148810.3 | 11.054% | 2.485517 | 45.158% | 0.073370 | 0.967955 | 0.260990 | 0.836203 | 83.498% |
| 1 | 0 | 157475.2 | 17.521% | 1.709192 | 62.287% | 0.043683 | 0.529103 | 0.198799 | 0.788784 | 76.507% |
| 2 | 0 | 171797.9 | 28.210% | 1.434706 | 68.344% | 0.028715 | 0.459551 | 0.206149 | 0.761271 | 72.166% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
