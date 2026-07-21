# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134197.8 | 0.000% | 8.164118 | 0.000% | 0.255454 | 2.470994 | 0.175038 | 0.872903 | 89.162% |
| 0.25 | 0 | 143280.4 | 6.768% | 5.423371 | 33.571% | 0.152198 | 1.711801 | 0.217180 | 0.855661 | 86.539% |
| 0.5 | 0 | 149360.6 | 11.299% | 4.101110 | 49.767% | 0.117613 | 1.636763 | 0.277723 | 0.830003 | 82.788% |
| 1 | 0 | 158600.5 | 18.184% | 2.893011 | 64.564% | 0.070797 | 0.817650 | 0.168136 | 0.785700 | 76.517% |
| 2 | 0 | 173386.4 | 29.202% | 2.236171 | 72.610% | 0.043721 | 0.691562 | 0.221674 | 0.746754 | 70.135% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
