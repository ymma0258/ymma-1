# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.510121 | 0.000% | 0.222249 | 2.332543 | 0.180009 | 0.868800 | 88.909% |
| 1 | 0 | 157140.5 | 17.271% | 2.838696 | 62.202% | 0.071675 | 0.892156 | 0.233124 | 0.779667 | 75.954% |
| 1 | 1 | 167216.5 | 24.791% | 2.040901 | 72.825% | 0.041542 | 0.644228 | 0.228568 | 0.716328 | 66.358% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
