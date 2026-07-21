# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.7 | 0.000% | 8.997229 | 0.000% | 0.279091 | 3.006912 | 0.231984 | 0.869931 | 90.036% |
| 0.25 | 0 | 158450.0 | 7.547% | 7.979377 | 11.313% | 0.225400 | 2.447889 | 0.202767 | 0.869870 | 89.522% |
| 0.5 | 0 | 168401.2 | 14.301% | 5.097331 | 43.346% | 0.144777 | 1.677845 | 0.263437 | 0.844639 | 84.840% |
| 1 | 0 | 180070.5 | 22.222% | 3.688174 | 59.008% | 0.083441 | 1.272425 | 0.272136 | 0.816485 | 80.017% |
| 2 | 0 | 197634.3 | 34.143% | 3.150220 | 64.987% | 0.064085 | 1.003170 | 0.251589 | 0.797784 | 76.860% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
