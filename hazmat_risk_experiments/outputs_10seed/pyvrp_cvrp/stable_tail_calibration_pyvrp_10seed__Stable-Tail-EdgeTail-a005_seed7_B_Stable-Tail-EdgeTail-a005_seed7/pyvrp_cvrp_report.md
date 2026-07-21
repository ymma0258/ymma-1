# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.9 | 0.000% | 9.680835 | 0.000% | 0.288466 | 3.007942 | 0.190859 | 0.877897 | 90.463% |
| 0.25 | 0 | 158011.7 | 7.492% | 7.941199 | 17.970% | 0.223095 | 2.739998 | 0.254603 | 0.873740 | 89.114% |
| 0.5 | 0 | 167746.4 | 14.115% | 5.633610 | 41.807% | 0.153625 | 1.928156 | 0.253758 | 0.852117 | 85.039% |
| 1 | 0 | 179310.7 | 21.982% | 3.850009 | 60.231% | 0.090903 | 1.368706 | 0.257027 | 0.824355 | 79.697% |
| 2 | 0 | 196160.9 | 33.445% | 3.400236 | 64.877% | 0.080783 | 1.091463 | 0.223026 | 0.809372 | 77.220% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
