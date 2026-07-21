# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.5 | 0.000% | 7.597852 | 0.000% | 0.224113 | 2.376784 | 0.202135 | 0.874514 | 89.186% |
| 0.25 | 0 | 156557.0 | 6.503% | 6.467445 | 14.878% | 0.182282 | 2.115657 | 0.219042 | 0.868632 | 88.032% |
| 0.5 | 0 | 164936.4 | 12.204% | 4.996600 | 34.237% | 0.133111 | 1.586306 | 0.241921 | 0.853900 | 85.174% |
| 1 | 0 | 175524.0 | 19.406% | 3.437848 | 54.752% | 0.086254 | 1.348132 | 0.315007 | 0.818546 | 79.748% |
| 2 | 0 | 192092.7 | 30.678% | 2.762935 | 63.635% | 0.057411 | 1.093901 | 0.320321 | 0.793577 | 75.825% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
