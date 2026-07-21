# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 5.551458 | 0.000% | 0.162105 | 1.540431 | 0.147753 | 0.867407 | 88.834% |
| 0.25 | 0 | 143124.7 | 6.758% | 3.649135 | 34.267% | 0.103037 | 1.236904 | 0.267805 | 0.847785 | 85.524% |
| 0.5 | 0 | 149097.5 | 11.213% | 2.882940 | 48.069% | 0.085489 | 1.065297 | 0.299708 | 0.822301 | 82.196% |
| 1 | 0 | 158439.8 | 18.182% | 2.022814 | 63.562% | 0.054614 | 0.635700 | 0.248631 | 0.777408 | 75.780% |
| 2 | 0 | 172672.0 | 28.798% | 1.624270 | 70.742% | 0.037864 | 0.567276 | 0.276370 | 0.733641 | 69.815% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
