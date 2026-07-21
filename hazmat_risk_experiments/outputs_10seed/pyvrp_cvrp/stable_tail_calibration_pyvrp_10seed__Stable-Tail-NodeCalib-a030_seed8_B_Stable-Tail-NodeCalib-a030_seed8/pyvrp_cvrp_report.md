# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.592730 | 0.000% | 0.209258 | 2.307606 | 0.189752 | 0.860185 | 87.723% |
| 0.25 | 0 | 156477.6 | 6.498% | 6.251317 | 17.667% | 0.148181 | 2.084757 | 0.214250 | 0.852997 | 86.588% |
| 0.5 | 0 | 164842.9 | 12.191% | 4.711259 | 37.950% | 0.117453 | 1.630306 | 0.257391 | 0.834695 | 83.217% |
| 1 | 0 | 175993.7 | 19.780% | 3.166018 | 58.302% | 0.073345 | 1.129356 | 0.267566 | 0.787280 | 76.131% |
| 2 | 0 | 190541.8 | 29.681% | 2.472597 | 67.435% | 0.048679 | 0.691960 | 0.188493 | 0.752362 | 70.581% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
