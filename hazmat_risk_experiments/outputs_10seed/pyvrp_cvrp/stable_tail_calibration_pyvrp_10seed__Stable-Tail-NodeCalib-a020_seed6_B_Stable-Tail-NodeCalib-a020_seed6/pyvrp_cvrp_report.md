# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.6 | 0.000% | 8.949932 | 0.000% | 0.240328 | 3.074776 | 0.239662 | 0.869243 | 89.269% |
| 0.25 | 0 | 157938.7 | 7.443% | 7.798124 | 12.869% | 0.190067 | 2.654942 | 0.253128 | 0.868344 | 89.240% |
| 0.5 | 0 | 168462.8 | 14.602% | 6.048819 | 32.415% | 0.157781 | 2.189829 | 0.266036 | 0.855877 | 86.381% |
| 1 | 0 | 181696.5 | 23.605% | 4.367531 | 51.200% | 0.113856 | 1.705279 | 0.324477 | 0.828753 | 81.671% |
| 2 | 0 | 202487.7 | 37.749% | 3.678895 | 58.895% | 0.092926 | 1.473148 | 0.343444 | 0.815500 | 78.948% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
