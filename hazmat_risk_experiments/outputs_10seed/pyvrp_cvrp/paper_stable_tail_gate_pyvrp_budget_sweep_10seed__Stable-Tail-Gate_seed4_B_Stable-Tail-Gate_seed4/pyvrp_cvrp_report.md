# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 8.934734 | 0.000% | 0.275569 | 2.880299 | 0.215208 | 0.859507 | 88.686% |
| 0.25 | 0 | 157396.3 | 7.172% | 7.693569 | 13.891% | 0.235178 | 2.933590 | 0.258520 | 0.856263 | 88.320% |
| 0.5 | 0 | 167861.7 | 14.297% | 6.044199 | 32.352% | 0.159587 | 1.959473 | 0.228596 | 0.840966 | 85.429% |
| 1 | 0 | 181881.4 | 23.844% | 4.634351 | 48.131% | 0.119608 | 1.697053 | 0.316721 | 0.817585 | 81.595% |
| 2 | 0 | 203564.1 | 38.607% | 3.585231 | 59.873% | 0.074120 | 1.574388 | 0.375531 | 0.787274 | 76.576% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
