# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.905733 | 0.000% | 0.244021 | 2.598277 | 0.223369 | 0.855276 | 88.562% |
| 1 | 0 | 179053.8 | 22.029% | 4.029240 | 49.034% | 0.100713 | 1.266508 | 0.250284 | 0.810906 | 81.223% |
| 1 | 1 | 193949.3 | 32.180% | 2.879429 | 63.578% | 0.064949 | 0.965641 | 0.270586 | 0.760986 | 73.645% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
