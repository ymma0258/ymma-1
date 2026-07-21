# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 8.487487 | 0.000% | 0.267966 | 2.685225 | 0.209308 | 0.870574 | 89.912% |
| 0.25 | 0 | 158195.2 | 7.667% | 7.364917 | 13.226% | 0.209900 | 2.405126 | 0.218047 | 0.869017 | 89.477% |
| 0.5 | 0 | 167766.7 | 14.181% | 4.644414 | 45.279% | 0.119269 | 1.434765 | 0.245309 | 0.843722 | 84.610% |
| 1 | 0 | 179078.6 | 21.880% | 3.312852 | 60.968% | 0.074460 | 1.221281 | 0.302189 | 0.811147 | 78.988% |
| 2 | 0 | 196526.6 | 33.755% | 2.848460 | 66.439% | 0.055714 | 0.892919 | 0.232885 | 0.790686 | 76.068% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
