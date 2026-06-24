# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.181534 | 0.000% | 0.205961 | 2.330343 | 0.206503 | 0.863271 | 88.639% |
| 1 | 0 | 157100.0 | 17.241% | 2.601871 | 63.770% | 0.056984 | 0.833768 | 0.194819 | 0.763200 | 74.705% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
