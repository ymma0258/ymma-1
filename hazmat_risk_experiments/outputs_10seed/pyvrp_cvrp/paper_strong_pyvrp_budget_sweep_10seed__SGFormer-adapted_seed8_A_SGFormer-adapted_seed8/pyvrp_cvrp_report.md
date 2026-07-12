# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 7.885441 | 0.000% | 0.259789 | 2.665284 | 0.233665 | 0.885385 | 89.226% |
| 0.25 | 0 | 142814.2 | 6.368% | 4.749286 | 39.771% | 0.127179 | 1.589432 | 0.251455 | 0.866458 | 84.605% |
| 0.5 | 0 | 149118.4 | 11.063% | 3.498963 | 55.628% | 0.089309 | 1.226747 | 0.270663 | 0.835658 | 79.382% |
| 1 | 0 | 156071.0 | 16.241% | 2.426847 | 69.224% | 0.052821 | 0.955612 | 0.295356 | 0.791067 | 71.495% |
| 2 | 0 | 168197.0 | 25.273% | 1.870483 | 76.279% | 0.036586 | 0.575492 | 0.220519 | 0.736184 | 63.457% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
