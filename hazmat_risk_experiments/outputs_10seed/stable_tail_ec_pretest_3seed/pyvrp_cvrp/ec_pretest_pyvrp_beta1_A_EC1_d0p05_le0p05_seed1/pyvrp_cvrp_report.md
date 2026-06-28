# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.802228 | 0.000% | 0.275647 | 2.394989 | 0.136395 | 0.871990 | 90.051% |
| 1 | 0 | 159518.8 | 19.046% | 3.774842 | 57.115% | 0.106621 | 1.335395 | 0.279639 | 0.827128 | 80.912% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
