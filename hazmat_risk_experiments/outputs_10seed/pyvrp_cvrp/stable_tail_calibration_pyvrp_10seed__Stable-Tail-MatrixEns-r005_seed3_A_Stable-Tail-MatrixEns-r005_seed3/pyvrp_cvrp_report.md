# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 6.505024 | 0.000% | 0.191814 | 1.915753 | 0.166472 | 0.870903 | 88.730% |
| 0.25 | 0 | 141802.7 | 5.824% | 4.404394 | 32.292% | 0.128441 | 1.386756 | 0.225721 | 0.855712 | 86.451% |
| 0.5 | 0 | 147288.0 | 9.918% | 3.376692 | 48.091% | 0.096862 | 1.198577 | 0.257996 | 0.831180 | 82.773% |
| 1 | 0 | 155255.3 | 15.864% | 2.215823 | 65.937% | 0.056832 | 0.683448 | 0.241942 | 0.765002 | 73.673% |
| 2 | 0 | 167370.9 | 24.906% | 2.006015 | 69.162% | 0.048938 | 0.645246 | 0.262460 | 0.747494 | 70.881% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
