# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.5 | 0.000% | 8.509228 | 0.000% | 0.254976 | 2.979552 | 0.243475 | 0.873849 | 89.242% |
| 0.25 | 0 | 156674.7 | 6.438% | 7.052250 | 17.122% | 0.194289 | 2.239093 | 0.234468 | 0.867692 | 87.787% |
| 0.5 | 0 | 165188.6 | 12.222% | 5.759558 | 32.314% | 0.154334 | 1.879104 | 0.235164 | 0.855043 | 85.512% |
| 1 | 0 | 175714.2 | 19.373% | 3.691401 | 56.619% | 0.084759 | 1.597569 | 0.335769 | 0.813417 | 78.902% |
| 2 | 0 | 192393.5 | 30.704% | 3.121968 | 63.311% | 0.064338 | 1.130967 | 0.281630 | 0.796445 | 76.186% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
