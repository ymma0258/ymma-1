# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 8.205989 | 0.000% | 0.245860 | 2.370249 | 0.167401 | 0.874785 | 88.204% |
| 0.25 | 0 | 156879.1 | 6.722% | 6.559382 | 20.066% | 0.170364 | 1.929738 | 0.190500 | 0.868237 | 86.725% |
| 0.5 | 0 | 164750.1 | 12.077% | 4.546708 | 44.593% | 0.116638 | 1.498971 | 0.261675 | 0.836756 | 81.746% |
| 1 | 0 | 174145.0 | 18.468% | 2.941383 | 64.156% | 0.066866 | 0.976573 | 0.207097 | 0.782379 | 73.112% |
| 2 | 0 | 188020.3 | 27.907% | 2.385132 | 70.934% | 0.043327 | 0.737283 | 0.192869 | 0.760998 | 68.827% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
