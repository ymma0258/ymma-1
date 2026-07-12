# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.8 | 0.000% | 8.980694 | 0.000% | 0.244348 | 3.079919 | 0.233168 | 0.880100 | 89.695% |
| 0.25 | 0 | 158541.3 | 7.512% | 7.961046 | 11.354% | 0.196701 | 2.482972 | 0.193985 | 0.881147 | 89.231% |
| 0.5 | 0 | 168835.1 | 14.493% | 6.645856 | 25.998% | 0.178246 | 2.157802 | 0.238239 | 0.873974 | 87.731% |
| 1 | 0 | 180926.9 | 22.692% | 3.732448 | 58.439% | 0.084535 | 1.246787 | 0.288700 | 0.830387 | 79.489% |
| 2 | 0 | 198683.6 | 34.734% | 3.212468 | 64.229% | 0.068617 | 1.179395 | 0.348342 | 0.812233 | 76.291% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
