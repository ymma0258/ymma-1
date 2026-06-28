# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 11.800067 | 0.000% | 0.208173 | 3.394876 | 0.148610 | 0.872517 | 89.889% |
| 1 | 0 | 161084.4 | 20.214% | 4.616305 | 60.879% | 0.055187 | 1.887683 | 0.357277 | 0.803971 | 78.133% |
| 2 | 0 | 175406.7 | 30.903% | 3.386359 | 71.302% | 0.037727 | 1.339458 | 0.333758 | 0.747307 | 70.063% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
