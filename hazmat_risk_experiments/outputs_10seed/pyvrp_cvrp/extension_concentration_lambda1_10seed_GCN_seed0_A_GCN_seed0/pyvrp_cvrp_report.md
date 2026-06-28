# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.356202 | 0.000% | 0.208555 | 2.433054 | 0.209684 | 0.865419 | 88.880% |
| 1 | 0 | 157100.0 | 17.241% | 2.601871 | 64.630% | 0.056984 | 0.833768 | 0.194819 | 0.763200 | 74.705% |
| 1 | 1 | 167385.5 | 24.917% | 2.310451 | 68.592% | 0.043607 | 0.707628 | 0.226537 | 0.739522 | 71.172% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
