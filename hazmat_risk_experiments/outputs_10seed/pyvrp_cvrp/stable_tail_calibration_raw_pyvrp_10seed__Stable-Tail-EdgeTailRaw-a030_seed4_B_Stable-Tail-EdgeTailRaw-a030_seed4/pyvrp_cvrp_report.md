# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.3 | 0.000% | 8.752888 | 0.000% | 0.273363 | 2.825051 | 0.205278 | 0.876873 | 89.537% |
| 0.25 | 0 | 156174.3 | 6.099% | 7.788846 | 11.014% | 0.223074 | 2.444459 | 0.210941 | 0.875344 | 88.968% |
| 0.5 | 0 | 164422.1 | 11.702% | 6.106904 | 30.230% | 0.167565 | 2.069951 | 0.256041 | 0.861072 | 86.342% |
| 1 | 0 | 174354.7 | 18.450% | 4.200390 | 52.011% | 0.107348 | 1.499064 | 0.299765 | 0.829174 | 81.270% |
| 2 | 0 | 190613.1 | 29.495% | 3.287098 | 62.446% | 0.074891 | 1.382076 | 0.311339 | 0.801697 | 77.015% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
