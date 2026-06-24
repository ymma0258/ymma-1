# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.128118 | 0.000% | 0.246506 | 2.353683 | 0.137337 | 0.846224 | 87.257% |
| 1 | 0 | 161268.8 | 20.352% | 3.584321 | 55.902% | 0.081316 | 1.144409 | 0.271574 | 0.751809 | 74.513% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
