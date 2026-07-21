# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.0 | 0.000% | 7.834396 | 0.000% | 0.208272 | 2.705312 | 0.269332 | 0.880911 | 89.911% |
| 0.25 | 0 | 157006.3 | 6.519% | 6.871720 | 12.288% | 0.171922 | 2.209024 | 0.228107 | 0.879738 | 89.303% |
| 0.5 | 0 | 165070.5 | 11.990% | 4.713810 | 39.832% | 0.120174 | 1.500400 | 0.213297 | 0.854451 | 85.035% |
| 1 | 0 | 175630.8 | 19.155% | 3.141557 | 59.900% | 0.078716 | 1.121676 | 0.269566 | 0.809065 | 78.098% |
| 2 | 0 | 190007.1 | 28.908% | 2.468044 | 68.497% | 0.051459 | 0.945820 | 0.298183 | 0.781653 | 72.964% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
