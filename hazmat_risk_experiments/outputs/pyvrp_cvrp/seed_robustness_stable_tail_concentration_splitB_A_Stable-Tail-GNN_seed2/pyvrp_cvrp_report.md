# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.474323 | 0.000% | 0.264041 | 2.476389 | 0.144052 | 0.875805 | 90.183% |
| 1 | 0 | 157966.6 | 17.888% | 3.424332 | 59.592% | 0.089724 | 1.139935 | 0.306056 | 0.827837 | 80.254% |
| 1 | 1 | 170306.0 | 27.096% | 3.238630 | 61.783% | 0.076930 | 1.097352 | 0.287783 | 0.820298 | 78.967% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
