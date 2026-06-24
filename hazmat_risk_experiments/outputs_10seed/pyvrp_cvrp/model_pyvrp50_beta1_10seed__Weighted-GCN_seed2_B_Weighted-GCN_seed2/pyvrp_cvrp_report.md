# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.924598 | 0.000% | 0.303789 | 3.250202 | 0.232963 | 0.846648 | 88.438% |
| 1 | 0 | 178717.2 | 21.799% | 4.832010 | 51.313% | 0.119022 | 1.698567 | 0.235812 | 0.780090 | 78.819% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
