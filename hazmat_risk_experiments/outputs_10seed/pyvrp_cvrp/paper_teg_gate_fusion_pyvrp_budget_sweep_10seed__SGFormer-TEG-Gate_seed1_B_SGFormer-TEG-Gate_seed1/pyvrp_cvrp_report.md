# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 9.853164 | 0.000% | 0.308286 | 3.213724 | 0.221202 | 0.868187 | 89.044% |
| 0.25 | 0 | 156719.4 | 6.662% | 8.154492 | 17.240% | 0.242828 | 2.626012 | 0.240951 | 0.866311 | 88.263% |
| 0.5 | 0 | 165514.2 | 12.648% | 6.170554 | 37.375% | 0.161450 | 2.024390 | 0.270039 | 0.850243 | 84.852% |
| 1 | 0 | 174807.3 | 18.973% | 3.875501 | 60.667% | 0.084675 | 1.235010 | 0.258525 | 0.805551 | 77.134% |
| 2 | 0 | 189668.9 | 29.087% | 3.119760 | 68.337% | 0.057791 | 1.116365 | 0.289013 | 0.778513 | 72.809% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
