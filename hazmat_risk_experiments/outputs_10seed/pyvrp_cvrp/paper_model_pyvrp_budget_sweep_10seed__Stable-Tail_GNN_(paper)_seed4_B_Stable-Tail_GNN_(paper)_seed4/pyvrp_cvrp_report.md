# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.5 | 0.000% | 8.313607 | 0.000% | 0.254641 | 2.834034 | 0.237173 | 0.871226 | 88.925% |
| 0.25 | 0 | 156691.4 | 6.354% | 7.179194 | 13.645% | 0.190155 | 2.224303 | 0.192213 | 0.870053 | 88.173% |
| 0.5 | 0 | 165523.3 | 12.348% | 5.694041 | 31.509% | 0.152676 | 1.910663 | 0.252214 | 0.855360 | 85.550% |
| 1 | 0 | 175743.9 | 19.285% | 3.824089 | 54.002% | 0.097891 | 1.411610 | 0.321327 | 0.818319 | 79.612% |
| 2 | 0 | 193052.8 | 31.034% | 3.151610 | 62.091% | 0.066981 | 1.275370 | 0.316351 | 0.797306 | 76.488% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
