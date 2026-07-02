# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.089351 | 0.000% | 0.181055 | 2.691551 | 0.218966 | 0.878981 | 89.419% |
| 1 | 0 | 153768.7 | 14.755% | 2.709545 | 66.505% | 0.046941 | 1.070953 | 0.297203 | 0.770923 | 73.918% |
| 2 | 0 | 165207.1 | 23.291% | 2.524976 | 68.786% | 0.043926 | 0.917621 | 0.270616 | 0.757361 | 71.823% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
