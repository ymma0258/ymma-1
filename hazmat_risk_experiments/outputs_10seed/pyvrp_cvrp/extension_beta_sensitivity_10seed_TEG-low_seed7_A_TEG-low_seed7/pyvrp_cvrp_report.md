# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.522296 | 0.000% | 0.241884 | 2.464672 | 0.144134 | 0.838407 | 86.896% |
| 0.5 | 0 | 150670.0 | 12.442% | 5.088703 | 40.290% | 0.140847 | 2.136985 | 0.304355 | 0.794678 | 80.755% |
| 1 | 0 | 161145.5 | 20.260% | 3.626391 | 57.448% | 0.089379 | 1.223560 | 0.266340 | 0.735429 | 72.857% |
| 1.5 | 0 | 169761.0 | 26.690% | 3.376304 | 60.383% | 0.078956 | 1.198509 | 0.264785 | 0.718463 | 70.817% |
| 2 | 0 | 177460.7 | 32.436% | 2.807848 | 67.053% | 0.048859 | 0.863092 | 0.226430 | 0.669527 | 64.527% |
| 3 | 0 | 189902.3 | 41.721% | 2.548019 | 70.102% | 0.041403 | 0.886039 | 0.295193 | 0.641435 | 61.123% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
