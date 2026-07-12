# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 8.454738 | 0.000% | 0.255428 | 2.658627 | 0.213883 | 0.870494 | 89.041% |
| 0.25 | 0 | 155825.5 | 5.814% | 7.239349 | 14.375% | 0.213990 | 2.526539 | 0.248184 | 0.869294 | 88.375% |
| 0.5 | 0 | 164439.8 | 11.663% | 6.179526 | 26.910% | 0.161844 | 1.989050 | 0.239055 | 0.860658 | 86.674% |
| 1 | 0 | 176210.1 | 19.656% | 4.172490 | 50.649% | 0.103522 | 1.550349 | 0.305424 | 0.827867 | 81.311% |
| 2 | 0 | 193548.7 | 31.430% | 3.466227 | 59.003% | 0.076842 | 1.495214 | 0.344193 | 0.807539 | 77.753% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
