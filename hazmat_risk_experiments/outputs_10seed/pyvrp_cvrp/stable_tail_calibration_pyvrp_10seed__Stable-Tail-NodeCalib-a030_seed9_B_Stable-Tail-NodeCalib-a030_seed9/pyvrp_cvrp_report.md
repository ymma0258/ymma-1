# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.033434 | 0.000% | 0.287141 | 2.860284 | 0.211675 | 0.871352 | 89.935% |
| 0.25 | 0 | 158007.2 | 7.490% | 7.753948 | 14.164% | 0.214187 | 2.671169 | 0.245366 | 0.870289 | 89.515% |
| 0.5 | 0 | 167787.2 | 14.143% | 4.785333 | 47.026% | 0.135352 | 1.543660 | 0.243867 | 0.838650 | 84.120% |
| 1 | 0 | 179506.8 | 22.116% | 3.494889 | 61.312% | 0.079310 | 1.133189 | 0.234090 | 0.808782 | 78.797% |
| 2 | 0 | 196168.2 | 33.450% | 3.039944 | 66.348% | 0.060107 | 0.962376 | 0.243223 | 0.791693 | 76.150% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
