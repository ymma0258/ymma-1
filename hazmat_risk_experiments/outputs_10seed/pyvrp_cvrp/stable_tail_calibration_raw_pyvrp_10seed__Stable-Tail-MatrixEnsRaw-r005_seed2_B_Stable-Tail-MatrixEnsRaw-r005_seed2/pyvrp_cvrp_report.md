# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 8.430501 | 0.000% | 0.266830 | 3.168042 | 0.306604 | 0.873124 | 89.498% |
| 0.25 | 0 | 156661.3 | 6.381% | 6.980310 | 17.202% | 0.214838 | 2.654566 | 0.302453 | 0.871231 | 88.695% |
| 0.5 | 0 | 165539.5 | 12.410% | 5.832505 | 30.817% | 0.157077 | 2.091903 | 0.273688 | 0.861211 | 86.773% |
| 1 | 0 | 178070.1 | 20.919% | 4.081891 | 51.582% | 0.108855 | 1.664934 | 0.325343 | 0.841828 | 82.911% |
| 2 | 0 | 196537.9 | 33.460% | 3.503960 | 58.437% | 0.087548 | 1.460300 | 0.345735 | 0.826195 | 80.264% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
