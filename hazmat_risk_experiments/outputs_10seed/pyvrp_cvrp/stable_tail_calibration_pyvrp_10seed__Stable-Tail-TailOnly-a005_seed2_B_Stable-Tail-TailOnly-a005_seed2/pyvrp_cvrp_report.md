# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.6 | 0.000% | 8.918316 | 0.000% | 0.281308 | 3.447865 | 0.323469 | 0.876018 | 89.800% |
| 0.25 | 0 | 156765.0 | 6.404% | 7.440935 | 16.566% | 0.212309 | 3.055369 | 0.329470 | 0.872366 | 88.880% |
| 0.5 | 0 | 165208.3 | 12.134% | 6.242215 | 30.007% | 0.170912 | 2.414799 | 0.284442 | 0.861835 | 86.924% |
| 1 | 0 | 177919.6 | 20.762% | 4.502923 | 49.509% | 0.120360 | 1.815286 | 0.294130 | 0.844450 | 83.495% |
| 2 | 0 | 196276.5 | 33.222% | 3.739355 | 58.071% | 0.093093 | 1.584021 | 0.345708 | 0.830737 | 80.611% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
