# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 5.937710 | 0.000% | 0.182628 | 1.794970 | 0.193393 | 0.874749 | 89.313% |
| 0.25 | 0 | 142853.6 | 6.503% | 3.934566 | 33.736% | 0.112777 | 1.232007 | 0.218385 | 0.862546 | 87.445% |
| 0.5 | 0 | 149004.7 | 11.089% | 2.770320 | 53.344% | 0.078881 | 1.044862 | 0.252100 | 0.826051 | 82.224% |
| 1 | 0 | 157771.8 | 17.625% | 2.043796 | 65.579% | 0.051587 | 0.604417 | 0.184559 | 0.787626 | 76.510% |
| 2 | 0 | 172329.7 | 28.478% | 1.772076 | 70.156% | 0.038020 | 0.537984 | 0.220805 | 0.767189 | 73.092% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
