# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.2 | 0.000% | 7.912046 | 0.000% | 0.241725 | 2.597126 | 0.222998 | 0.874071 | 89.100% |
| 0.25 | 0 | 156544.2 | 6.350% | 6.808979 | 13.942% | 0.168665 | 2.294487 | 0.253857 | 0.872371 | 88.645% |
| 0.5 | 0 | 165006.7 | 12.099% | 5.094537 | 35.610% | 0.130106 | 1.476394 | 0.188123 | 0.852975 | 85.043% |
| 1 | 0 | 175291.6 | 19.086% | 3.589395 | 54.634% | 0.092482 | 1.271845 | 0.298577 | 0.819566 | 79.823% |
| 2 | 0 | 191798.8 | 30.301% | 2.878564 | 63.618% | 0.070288 | 0.945409 | 0.267206 | 0.794851 | 75.501% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
