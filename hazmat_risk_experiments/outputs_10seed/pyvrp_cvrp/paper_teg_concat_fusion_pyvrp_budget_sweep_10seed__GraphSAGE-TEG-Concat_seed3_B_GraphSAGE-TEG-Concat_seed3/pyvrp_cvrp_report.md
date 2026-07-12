# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.1 | 0.000% | 7.986487 | 0.000% | 0.236765 | 2.514308 | 0.204411 | 0.871914 | 88.974% |
| 0.25 | 0 | 158255.9 | 7.464% | 6.739776 | 15.610% | 0.172482 | 2.258139 | 0.233277 | 0.870621 | 88.434% |
| 0.5 | 0 | 168634.7 | 14.512% | 5.150267 | 35.513% | 0.133451 | 1.733537 | 0.254343 | 0.863143 | 86.034% |
| 1 | 0 | 179946.7 | 22.193% | 3.029035 | 62.073% | 0.071302 | 1.237069 | 0.277593 | 0.806089 | 76.844% |
| 2 | 0 | 195000.8 | 32.416% | 2.361322 | 70.434% | 0.044029 | 0.963328 | 0.311306 | 0.766722 | 70.658% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
