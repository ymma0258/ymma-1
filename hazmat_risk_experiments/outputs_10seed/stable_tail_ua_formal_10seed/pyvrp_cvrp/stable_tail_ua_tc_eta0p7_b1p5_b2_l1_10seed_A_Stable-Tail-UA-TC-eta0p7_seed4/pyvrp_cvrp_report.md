# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 11.281493 | 0.000% | 0.278192 | 3.127426 | 0.135664 | 0.857543 | 89.022% |
| 1.5 | 1 | 185632.1 | 38.534% | 3.257026 | 71.129% | 0.054549 | 1.344996 | 0.332493 | 0.691206 | 66.406% |
| 2 | 1 | 193183.6 | 44.169% | 3.254422 | 71.153% | 0.055455 | 1.281586 | 0.324596 | 0.690387 | 66.245% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
