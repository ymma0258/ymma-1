# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.736093 | 0.000% | 0.233101 | 2.305522 | 0.160077 | 0.879734 | 89.716% |
| 2 | 2 | 192557.9 | 43.703% | 2.047019 | 73.539% | 0.035690 | 1.023010 | 0.370440 | 0.743678 | 68.157% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
