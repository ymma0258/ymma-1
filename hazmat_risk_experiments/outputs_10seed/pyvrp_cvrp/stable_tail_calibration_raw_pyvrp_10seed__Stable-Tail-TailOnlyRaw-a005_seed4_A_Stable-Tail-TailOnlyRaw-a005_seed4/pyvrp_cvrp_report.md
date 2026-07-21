# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 9.058242 | 0.000% | 0.286670 | 2.648371 | 0.181044 | 0.878374 | 90.000% |
| 0.25 | 0 | 143560.2 | 6.817% | 6.246097 | 31.045% | 0.189119 | 1.753439 | 0.193994 | 0.865522 | 87.794% |
| 0.5 | 0 | 150387.5 | 11.897% | 5.146138 | 43.188% | 0.155136 | 1.673206 | 0.246904 | 0.855512 | 86.038% |
| 1 | 0 | 160212.2 | 19.207% | 3.707551 | 59.070% | 0.098119 | 1.217620 | 0.269682 | 0.822778 | 81.011% |
| 2 | 0 | 175123.2 | 30.302% | 2.947934 | 67.456% | 0.069313 | 1.091079 | 0.343877 | 0.794590 | 76.654% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
