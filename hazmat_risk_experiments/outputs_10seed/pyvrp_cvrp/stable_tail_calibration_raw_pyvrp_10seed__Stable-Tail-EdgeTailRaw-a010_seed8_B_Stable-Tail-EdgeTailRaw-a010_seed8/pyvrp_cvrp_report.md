# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 7.570532 | 0.000% | 0.227968 | 2.252837 | 0.184193 | 0.860698 | 87.875% |
| 0.25 | 0 | 156720.3 | 6.518% | 6.365473 | 15.918% | 0.153569 | 1.992985 | 0.198222 | 0.855704 | 87.067% |
| 0.5 | 0 | 165258.6 | 12.321% | 4.690615 | 38.041% | 0.111472 | 1.469197 | 0.205148 | 0.830786 | 83.129% |
| 1 | 0 | 176143.9 | 19.719% | 3.003610 | 60.325% | 0.071633 | 1.061001 | 0.239446 | 0.781472 | 75.323% |
| 2 | 0 | 191011.8 | 29.825% | 2.500118 | 66.976% | 0.053576 | 0.698665 | 0.184647 | 0.754273 | 70.952% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
