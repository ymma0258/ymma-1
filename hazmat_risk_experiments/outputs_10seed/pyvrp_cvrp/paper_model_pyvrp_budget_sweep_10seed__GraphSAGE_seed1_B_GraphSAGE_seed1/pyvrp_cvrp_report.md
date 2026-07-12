# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.5 | 0.000% | 7.503779 | 0.000% | 0.216984 | 2.548491 | 0.247695 | 0.877059 | 88.871% |
| 0.25 | 0 | 156160.1 | 5.993% | 6.670188 | 11.109% | 0.189253 | 2.459567 | 0.255282 | 0.877161 | 88.698% |
| 0.5 | 0 | 163874.9 | 11.229% | 4.652849 | 37.993% | 0.128292 | 1.583552 | 0.242034 | 0.853691 | 84.273% |
| 1 | 0 | 173471.8 | 17.743% | 2.958564 | 60.572% | 0.064341 | 0.916511 | 0.214465 | 0.813534 | 77.519% |
| 2 | 0 | 186907.5 | 26.863% | 2.381852 | 68.258% | 0.045969 | 0.805401 | 0.248818 | 0.788729 | 73.099% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
