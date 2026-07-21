# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 7.774292 | 0.000% | 0.234713 | 2.513154 | 0.223296 | 0.885866 | 90.447% |
| 0.25 | 0 | 142515.3 | 6.198% | 4.585396 | 41.018% | 0.136646 | 1.545590 | 0.245399 | 0.858870 | 86.140% |
| 0.5 | 0 | 148197.1 | 10.432% | 3.764383 | 51.579% | 0.110131 | 1.679087 | 0.346689 | 0.841593 | 83.780% |
| 1 | 0 | 156091.8 | 16.314% | 2.356724 | 69.686% | 0.051230 | 0.884933 | 0.257030 | 0.781572 | 74.422% |
| 2 | 0 | 168392.5 | 25.480% | 1.824876 | 76.527% | 0.035099 | 0.560500 | 0.198352 | 0.730386 | 66.688% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
