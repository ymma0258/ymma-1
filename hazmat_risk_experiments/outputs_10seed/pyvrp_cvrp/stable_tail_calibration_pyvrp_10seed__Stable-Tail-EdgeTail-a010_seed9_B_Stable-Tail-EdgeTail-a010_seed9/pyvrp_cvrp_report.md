# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.2 | 0.000% | 9.060535 | 0.000% | 0.278869 | 3.044795 | 0.235428 | 0.872040 | 90.314% |
| 0.25 | 0 | 158684.8 | 7.755% | 7.640686 | 15.671% | 0.221913 | 2.103465 | 0.143472 | 0.870693 | 89.583% |
| 0.5 | 0 | 168050.6 | 14.115% | 5.016516 | 44.633% | 0.130108 | 1.575470 | 0.249419 | 0.843575 | 84.769% |
| 1 | 0 | 179825.9 | 22.111% | 3.601165 | 60.254% | 0.080127 | 1.240605 | 0.265243 | 0.810426 | 79.567% |
| 2 | 0 | 197488.7 | 34.105% | 3.074308 | 66.069% | 0.059984 | 1.027103 | 0.280950 | 0.795003 | 76.571% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
