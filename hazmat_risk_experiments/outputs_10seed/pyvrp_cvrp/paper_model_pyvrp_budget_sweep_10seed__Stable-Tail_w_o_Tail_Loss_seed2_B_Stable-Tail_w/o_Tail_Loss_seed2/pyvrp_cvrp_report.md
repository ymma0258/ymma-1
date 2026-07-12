# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.7 | 0.000% | 8.029572 | 0.000% | 0.247088 | 2.943015 | 0.290758 | 0.883923 | 90.967% |
| 0.25 | 0 | 156575.0 | 6.419% | 6.959726 | 13.324% | 0.192209 | 2.369418 | 0.257334 | 0.885561 | 90.251% |
| 0.5 | 0 | 165472.7 | 12.466% | 5.780579 | 28.009% | 0.157998 | 2.248258 | 0.273158 | 0.880662 | 88.807% |
| 1 | 0 | 177481.8 | 20.629% | 4.045417 | 49.619% | 0.110051 | 1.697081 | 0.350066 | 0.863400 | 84.820% |
| 2 | 0 | 194801.9 | 32.401% | 3.108829 | 61.283% | 0.078272 | 1.442066 | 0.339576 | 0.843865 | 80.605% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
