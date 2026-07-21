# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.8 | 0.000% | 8.904005 | 0.000% | 0.281955 | 2.822034 | 0.204313 | 0.869926 | 89.834% |
| 0.25 | 0 | 157852.1 | 7.336% | 7.730587 | 13.179% | 0.215204 | 2.614856 | 0.232837 | 0.869958 | 89.526% |
| 0.5 | 0 | 167927.6 | 14.187% | 4.826045 | 45.799% | 0.125196 | 1.649365 | 0.261359 | 0.841371 | 84.356% |
| 1 | 0 | 178976.6 | 21.700% | 3.501394 | 60.676% | 0.072416 | 1.227809 | 0.296354 | 0.813081 | 79.313% |
| 2 | 0 | 196829.6 | 33.840% | 3.033209 | 65.934% | 0.061368 | 0.974599 | 0.248024 | 0.792685 | 76.202% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
