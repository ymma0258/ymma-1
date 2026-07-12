# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 9.235280 | 0.000% | 0.305244 | 2.849916 | 0.184215 | 0.872587 | 89.558% |
| 0.25 | 0 | 142172.8 | 5.837% | 6.645307 | 28.044% | 0.199580 | 1.999049 | 0.194208 | 0.866891 | 88.274% |
| 0.5 | 0 | 148457.3 | 10.516% | 4.704690 | 49.057% | 0.132573 | 1.485295 | 0.196830 | 0.839019 | 83.788% |
| 1 | 0 | 156853.0 | 16.766% | 3.314697 | 64.108% | 0.071374 | 0.969784 | 0.173190 | 0.793439 | 77.036% |
| 2 | 0 | 169937.5 | 26.506% | 2.698492 | 70.781% | 0.057672 | 0.901253 | 0.250028 | 0.766033 | 72.638% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
