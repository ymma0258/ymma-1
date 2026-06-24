# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.065803 | 0.000% | 0.271807 | 2.839109 | 0.195218 | 0.836899 | 86.803% |
| 1 | 0 | 179001.2 | 21.993% | 4.321884 | 52.328% | 0.100907 | 1.356090 | 0.222545 | 0.740075 | 74.147% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
