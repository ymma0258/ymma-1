# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134531.2 | 0.000% | 7.934859 | 0.000% | 0.254318 | 2.498324 | 0.188390 | 0.877789 | 89.248% |
| 0.25 | 0 | 142709.9 | 6.079% | 5.482479 | 30.906% | 0.154428 | 1.737145 | 0.193370 | 0.864913 | 87.315% |
| 0.5 | 0 | 148305.8 | 10.239% | 3.570458 | 55.003% | 0.103977 | 1.264378 | 0.294438 | 0.825492 | 81.227% |
| 1 | 0 | 155772.4 | 15.789% | 2.495166 | 68.554% | 0.063931 | 1.037604 | 0.301916 | 0.770780 | 73.417% |
| 2 | 0 | 167140.7 | 24.239% | 1.911838 | 75.906% | 0.041857 | 0.627713 | 0.231842 | 0.717422 | 65.808% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
