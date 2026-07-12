# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 8.217699 | 0.000% | 0.234954 | 2.561342 | 0.210387 | 0.872186 | 89.193% |
| 0.25 | 0 | 142745.3 | 6.475% | 5.845353 | 28.869% | 0.167894 | 1.992185 | 0.232916 | 0.857066 | 86.901% |
| 0.5 | 0 | 148731.3 | 10.940% | 4.124885 | 49.805% | 0.118060 | 1.585623 | 0.265541 | 0.825706 | 82.508% |
| 1 | 0 | 157565.0 | 17.529% | 2.917006 | 64.503% | 0.069252 | 1.056517 | 0.233259 | 0.778297 | 75.816% |
| 2 | 0 | 170312.7 | 27.038% | 2.065461 | 74.866% | 0.034056 | 0.712495 | 0.248373 | 0.697563 | 65.023% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
