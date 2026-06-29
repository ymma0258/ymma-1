# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 14.031321 | 0.000% | 0.343385 | 4.480644 | 0.203712 | 0.858269 | 89.746% |
| 1.5 | 1 | 218372.6 | 48.825% | 5.254476 | 62.552% | 0.085010 | 2.119915 | 0.371568 | 0.787361 | 77.384% |
| 2 | 1 | 229669.0 | 56.524% | 5.257939 | 62.527% | 0.085164 | 2.001181 | 0.373844 | 0.786490 | 77.294% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
