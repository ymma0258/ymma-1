# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.393913 | 0.000% | 0.290408 | 3.411005 | 0.277049 | 0.861733 | 89.228% |
| 0.25 | 0 | 157080.4 | 6.859% | 8.083221 | 13.953% | 0.248115 | 3.096061 | 0.289748 | 0.862473 | 89.125% |
| 0.5 | 0 | 166549.7 | 13.301% | 7.193978 | 23.419% | 0.196321 | 2.530269 | 0.255628 | 0.857705 | 87.933% |
| 1 | 0 | 179795.5 | 22.312% | 4.942123 | 47.390% | 0.133802 | 1.788172 | 0.277572 | 0.833079 | 83.452% |
| 2 | 0 | 199998.9 | 36.056% | 3.744550 | 60.139% | 0.084202 | 1.688855 | 0.357767 | 0.801178 | 78.094% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
