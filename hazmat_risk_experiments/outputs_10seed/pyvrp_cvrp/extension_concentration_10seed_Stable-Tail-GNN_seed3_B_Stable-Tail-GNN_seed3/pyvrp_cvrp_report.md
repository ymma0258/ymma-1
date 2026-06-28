# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 6.883367 | 0.000% | 0.204340 | 2.370042 | 0.226137 | 0.873010 | 88.919% |
| 1 | 0 | 173995.4 | 18.581% | 2.945257 | 57.212% | 0.073990 | 1.154991 | 0.293761 | 0.801541 | 77.746% |
| 1 | 0.5 | 180287.2 | 22.869% | 2.606876 | 62.128% | 0.060718 | 1.038079 | 0.299332 | 0.783608 | 74.937% |
| 1 | 1 | 185796.8 | 26.624% | 2.307294 | 66.480% | 0.048817 | 0.854771 | 0.270667 | 0.773036 | 72.745% |
| 1 | 2 | 195682.1 | 33.361% | 2.045472 | 70.284% | 0.037910 | 0.851324 | 0.311847 | 0.750479 | 69.166% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
