# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 8.307054 | 0.000% | 0.239985 | 2.434947 | 0.187300 | 0.873376 | 89.765% |
| 0.25 | 0 | 143932.2 | 7.360% | 5.850983 | 29.566% | 0.166654 | 1.886027 | 0.238869 | 0.859898 | 86.840% |
| 0.5 | 0 | 150842.8 | 12.515% | 4.173630 | 49.758% | 0.116820 | 1.619095 | 0.276102 | 0.830501 | 82.175% |
| 1 | 0 | 160844.9 | 19.976% | 3.238032 | 61.021% | 0.076783 | 0.977143 | 0.220156 | 0.802581 | 77.553% |
| 2 | 0 | 176378.5 | 31.562% | 2.322251 | 72.045% | 0.045388 | 0.908430 | 0.291192 | 0.735230 | 67.852% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
