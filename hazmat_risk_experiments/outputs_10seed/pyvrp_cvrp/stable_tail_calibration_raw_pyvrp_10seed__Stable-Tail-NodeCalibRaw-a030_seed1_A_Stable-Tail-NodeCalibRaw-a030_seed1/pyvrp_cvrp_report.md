# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 9.496875 | 0.000% | 0.319953 | 2.540897 | 0.147793 | 0.871493 | 89.537% |
| 0.25 | 0 | 141989.1 | 5.701% | 6.639754 | 30.085% | 0.203814 | 2.016469 | 0.200514 | 0.865748 | 88.043% |
| 0.5 | 0 | 147722.7 | 9.969% | 4.685855 | 50.659% | 0.118087 | 1.576737 | 0.224387 | 0.840123 | 83.682% |
| 1 | 0 | 156199.1 | 16.279% | 3.254716 | 65.729% | 0.071063 | 1.057655 | 0.221817 | 0.795042 | 77.087% |
| 2 | 0 | 168890.6 | 25.727% | 2.638376 | 72.218% | 0.053146 | 0.803846 | 0.235932 | 0.768233 | 72.637% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
