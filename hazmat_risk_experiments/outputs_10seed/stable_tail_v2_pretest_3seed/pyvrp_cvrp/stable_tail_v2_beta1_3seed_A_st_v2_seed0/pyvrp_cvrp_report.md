# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 7.169510 | 0.000% | 0.218403 | 2.331208 | 0.205228 | 0.875002 | 89.836% |
| 1 | 0 | 156026.7 | 16.440% | 2.306344 | 67.831% | 0.049762 | 0.894740 | 0.262477 | 0.785102 | 74.772% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
