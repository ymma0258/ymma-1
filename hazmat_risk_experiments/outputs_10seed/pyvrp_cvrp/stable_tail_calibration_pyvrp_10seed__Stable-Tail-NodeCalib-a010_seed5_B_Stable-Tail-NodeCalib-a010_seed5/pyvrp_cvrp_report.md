# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.686537 | 0.000% | 0.239012 | 2.532617 | 0.219810 | 0.873421 | 88.798% |
| 0.25 | 0 | 156234.9 | 6.332% | 6.470264 | 15.823% | 0.155448 | 2.087468 | 0.213593 | 0.869401 | 88.160% |
| 0.5 | 0 | 164785.9 | 12.152% | 5.010585 | 34.813% | 0.123174 | 1.704268 | 0.264350 | 0.848039 | 84.791% |
| 1 | 0 | 175162.7 | 19.215% | 3.439537 | 55.252% | 0.088467 | 1.294430 | 0.307204 | 0.817733 | 79.531% |
| 2 | 0 | 191448.4 | 30.299% | 2.765324 | 64.024% | 0.066737 | 0.870117 | 0.261484 | 0.791751 | 74.991% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
