# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 7.678251 | 0.000% | 0.224554 | 2.152275 | 0.142390 | 0.863795 | 88.265% |
| 0.25 | 0 | 143028.7 | 6.739% | 5.503262 | 28.327% | 0.162791 | 1.754193 | 0.256622 | 0.852987 | 86.340% |
| 0.5 | 0 | 149184.8 | 11.334% | 4.056159 | 47.173% | 0.120119 | 1.609351 | 0.328675 | 0.820707 | 82.028% |
| 1 | 0 | 158388.9 | 18.202% | 2.837042 | 63.051% | 0.075867 | 0.849635 | 0.253932 | 0.773517 | 75.198% |
| 2 | 0 | 172251.8 | 28.548% | 2.295613 | 70.102% | 0.053612 | 0.837188 | 0.289267 | 0.732814 | 69.566% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
