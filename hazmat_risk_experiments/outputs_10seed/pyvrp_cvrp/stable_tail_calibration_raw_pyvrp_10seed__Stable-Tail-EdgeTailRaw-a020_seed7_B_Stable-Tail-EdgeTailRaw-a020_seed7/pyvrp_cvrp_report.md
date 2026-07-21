# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 10.487658 | 0.000% | 0.321581 | 3.085172 | 0.179575 | 0.881750 | 91.011% |
| 0.25 | 0 | 158197.7 | 7.425% | 8.814620 | 15.952% | 0.258253 | 2.939754 | 0.227634 | 0.879857 | 90.305% |
| 0.5 | 0 | 167850.4 | 13.979% | 5.518109 | 47.385% | 0.152532 | 1.991664 | 0.275884 | 0.852318 | 84.928% |
| 1 | 0 | 178706.8 | 21.351% | 4.182988 | 60.115% | 0.108060 | 1.389591 | 0.237919 | 0.832686 | 80.997% |
| 2 | 0 | 195914.2 | 33.036% | 3.472783 | 66.887% | 0.082197 | 1.114105 | 0.207048 | 0.815503 | 77.850% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
