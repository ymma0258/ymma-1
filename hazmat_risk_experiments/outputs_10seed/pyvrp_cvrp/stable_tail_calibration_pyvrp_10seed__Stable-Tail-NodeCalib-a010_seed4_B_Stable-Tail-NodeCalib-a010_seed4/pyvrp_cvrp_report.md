# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 8.429831 | 0.000% | 0.254374 | 2.643925 | 0.195887 | 0.873195 | 89.053% |
| 0.25 | 0 | 156244.9 | 6.291% | 7.283202 | 13.602% | 0.206605 | 2.339751 | 0.204049 | 0.870188 | 88.232% |
| 0.5 | 0 | 164859.1 | 12.151% | 5.839580 | 30.727% | 0.153436 | 2.014356 | 0.278195 | 0.857786 | 85.843% |
| 1 | 0 | 175010.1 | 19.057% | 3.804973 | 54.863% | 0.087088 | 1.494246 | 0.308858 | 0.818088 | 79.477% |
| 2 | 0 | 191715.8 | 30.421% | 3.178955 | 62.289% | 0.066187 | 1.287845 | 0.316440 | 0.801167 | 76.769% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
