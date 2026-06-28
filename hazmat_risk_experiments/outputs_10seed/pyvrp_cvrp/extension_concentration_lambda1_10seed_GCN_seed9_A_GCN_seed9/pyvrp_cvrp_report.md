# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.630782 | 0.000% | 0.219914 | 2.316810 | 0.174649 | 0.864607 | 89.123% |
| 1 | 0 | 157030.2 | 17.189% | 2.802485 | 63.274% | 0.073444 | 0.915619 | 0.250840 | 0.760583 | 75.072% |
| 1 | 1 | 167567.9 | 25.053% | 2.526986 | 66.884% | 0.051760 | 0.758324 | 0.225862 | 0.745221 | 72.508% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
