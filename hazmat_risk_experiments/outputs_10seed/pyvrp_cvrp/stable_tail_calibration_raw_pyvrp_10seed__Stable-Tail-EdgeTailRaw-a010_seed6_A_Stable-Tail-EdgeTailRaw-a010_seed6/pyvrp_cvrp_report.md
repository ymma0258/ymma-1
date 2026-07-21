# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.1 | 0.000% | 7.924189 | 0.000% | 0.237970 | 2.444495 | 0.174662 | 0.867012 | 88.591% |
| 0.25 | 0 | 143329.3 | 6.804% | 5.359446 | 32.366% | 0.153523 | 1.721855 | 0.240253 | 0.850650 | 86.042% |
| 0.5 | 0 | 149490.3 | 11.395% | 4.203945 | 46.948% | 0.122555 | 1.538432 | 0.303176 | 0.825646 | 82.503% |
| 1 | 0 | 158858.3 | 18.376% | 2.888938 | 63.543% | 0.077019 | 0.958253 | 0.269726 | 0.775795 | 75.538% |
| 2 | 0 | 173262.5 | 29.110% | 2.266007 | 71.404% | 0.052478 | 0.855724 | 0.306620 | 0.729505 | 69.136% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
