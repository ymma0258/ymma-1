# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 8.546629 | 0.000% | 0.270046 | 2.546346 | 0.185243 | 0.870585 | 88.436% |
| 0.25 | 0 | 142690.1 | 6.275% | 5.536679 | 35.218% | 0.152684 | 1.755352 | 0.231951 | 0.856992 | 85.403% |
| 0.5 | 0 | 148774.6 | 10.807% | 4.004845 | 53.141% | 0.114073 | 1.190272 | 0.225248 | 0.829122 | 80.742% |
| 1 | 0 | 156161.8 | 16.309% | 2.652365 | 68.966% | 0.064761 | 1.083145 | 0.297923 | 0.767031 | 71.820% |
| 2 | 0 | 167075.2 | 24.437% | 2.136369 | 75.003% | 0.040921 | 0.659750 | 0.214080 | 0.721958 | 65.593% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
