# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.767275 | 0.000% | 0.244530 | 2.976577 | 0.243380 | 0.863051 | 89.308% |
| 0.5 | 0 | 166258.9 | 13.309% | 5.748497 | 34.432% | 0.149052 | 1.957169 | 0.253944 | 0.846090 | 86.234% |
| 1 | 0 | 178430.4 | 21.604% | 4.090628 | 53.342% | 0.110921 | 1.463062 | 0.312983 | 0.815907 | 81.526% |
| 1.5 | 0 | 188459.2 | 28.439% | 3.682875 | 57.993% | 0.095903 | 1.295112 | 0.303115 | 0.802832 | 79.368% |
| 2 | 0 | 197350.7 | 34.498% | 3.403854 | 61.175% | 0.082633 | 1.229809 | 0.299092 | 0.794926 | 77.652% |
| 3 | 0 | 214279.8 | 46.036% | 3.275071 | 62.644% | 0.078365 | 1.199989 | 0.308772 | 0.789935 | 76.839% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
