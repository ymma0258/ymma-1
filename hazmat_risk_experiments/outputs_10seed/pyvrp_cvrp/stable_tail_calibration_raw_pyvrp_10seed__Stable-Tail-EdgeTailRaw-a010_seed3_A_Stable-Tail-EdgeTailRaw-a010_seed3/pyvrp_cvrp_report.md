# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.0 | 0.000% | 6.912090 | 0.000% | 0.204234 | 2.241174 | 0.203481 | 0.873382 | 89.072% |
| 0.25 | 0 | 141608.9 | 5.522% | 4.870084 | 29.543% | 0.139005 | 1.433374 | 0.183195 | 0.855924 | 86.782% |
| 0.5 | 0 | 146975.5 | 9.521% | 3.721958 | 46.153% | 0.107866 | 1.312180 | 0.239754 | 0.834241 | 83.400% |
| 1 | 0 | 154605.0 | 15.207% | 2.428878 | 64.860% | 0.063313 | 0.713160 | 0.206009 | 0.771639 | 74.501% |
| 2 | 0 | 166233.7 | 23.872% | 2.136443 | 69.091% | 0.051553 | 0.729137 | 0.251183 | 0.749924 | 71.151% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
