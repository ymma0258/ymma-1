# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147396.8 | 0.000% | 9.877291 | 0.000% | 0.313555 | 3.441481 | 0.261874 | 0.873186 | 89.987% |
| 0.25 | 0 | 156705.6 | 6.315% | 7.848914 | 20.536% | 0.232498 | 2.872583 | 0.266036 | 0.867371 | 88.487% |
| 0.5 | 0 | 164668.3 | 11.718% | 6.331468 | 35.899% | 0.174668 | 1.948621 | 0.207176 | 0.858816 | 86.453% |
| 1 | 0 | 175158.0 | 18.834% | 4.007719 | 59.425% | 0.090533 | 1.270818 | 0.244363 | 0.817675 | 79.477% |
| 2 | 0 | 188593.3 | 27.949% | 3.282600 | 66.766% | 0.065056 | 1.091804 | 0.249294 | 0.795513 | 75.770% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
