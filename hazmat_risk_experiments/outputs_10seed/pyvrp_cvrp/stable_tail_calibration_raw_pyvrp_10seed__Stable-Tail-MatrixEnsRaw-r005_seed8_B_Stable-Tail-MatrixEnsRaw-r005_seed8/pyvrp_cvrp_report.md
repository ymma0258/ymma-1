# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 7.281994 | 0.000% | 0.218953 | 2.183140 | 0.191751 | 0.861299 | 87.915% |
| 0.25 | 0 | 156413.3 | 6.213% | 6.149938 | 15.546% | 0.151968 | 2.101350 | 0.219484 | 0.855187 | 87.158% |
| 0.5 | 0 | 164625.2 | 11.789% | 4.449991 | 38.890% | 0.109408 | 1.492434 | 0.231304 | 0.835855 | 83.317% |
| 1 | 0 | 175602.1 | 19.243% | 3.076633 | 57.750% | 0.074495 | 1.048537 | 0.239151 | 0.789365 | 76.806% |
| 2 | 0 | 190523.0 | 29.375% | 2.320095 | 68.139% | 0.049926 | 0.669530 | 0.189295 | 0.753378 | 70.593% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
