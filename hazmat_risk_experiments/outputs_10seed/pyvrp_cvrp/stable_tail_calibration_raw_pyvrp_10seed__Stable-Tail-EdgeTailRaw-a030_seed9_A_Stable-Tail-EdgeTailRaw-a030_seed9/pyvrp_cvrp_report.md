# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.3 | 0.000% | 8.923133 | 0.000% | 0.289746 | 2.803001 | 0.213864 | 0.872661 | 89.827% |
| 0.25 | 0 | 143043.2 | 6.432% | 5.689287 | 36.241% | 0.157941 | 1.846219 | 0.241347 | 0.856327 | 87.180% |
| 0.5 | 0 | 149401.9 | 11.164% | 4.373131 | 50.991% | 0.124708 | 1.568658 | 0.244839 | 0.829831 | 83.598% |
| 1 | 0 | 158268.2 | 17.761% | 3.065350 | 65.647% | 0.069297 | 1.095163 | 0.263022 | 0.785283 | 77.223% |
| 2 | 0 | 171656.4 | 27.722% | 2.435251 | 72.709% | 0.051347 | 0.800499 | 0.263450 | 0.746157 | 71.563% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
