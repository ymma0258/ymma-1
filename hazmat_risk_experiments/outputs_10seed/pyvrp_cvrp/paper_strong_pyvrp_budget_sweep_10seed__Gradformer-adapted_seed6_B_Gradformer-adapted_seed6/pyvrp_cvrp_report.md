# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 8.613147 | 0.000% | 0.262582 | 2.747930 | 0.204848 | 0.856309 | 88.196% |
| 0.25 | 0 | 158385.8 | 7.747% | 7.407024 | 14.003% | 0.221683 | 2.467151 | 0.214367 | 0.855927 | 87.834% |
| 0.5 | 0 | 169041.5 | 14.996% | 6.253433 | 27.397% | 0.164622 | 1.983241 | 0.243882 | 0.846808 | 85.874% |
| 1 | 0 | 183624.6 | 24.917% | 4.738047 | 44.991% | 0.120986 | 1.599511 | 0.264344 | 0.820203 | 81.966% |
| 2 | 0 | 209828.3 | 42.743% | 4.041863 | 53.073% | 0.101659 | 1.581343 | 0.361154 | 0.808523 | 79.330% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
