# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 8.119664 | 0.000% | 0.253658 | 2.234534 | 0.138989 | 0.861731 | 87.819% |
| 0.25 | 0 | 143333.6 | 6.649% | 4.813619 | 40.717% | 0.142063 | 1.651819 | 0.274143 | 0.839085 | 84.437% |
| 0.5 | 0 | 149623.1 | 11.328% | 4.074203 | 49.823% | 0.119849 | 1.530928 | 0.298275 | 0.820550 | 81.877% |
| 1 | 0 | 158840.3 | 18.187% | 2.931530 | 63.896% | 0.078196 | 0.990239 | 0.279385 | 0.776617 | 75.682% |
| 2 | 0 | 173644.2 | 29.201% | 2.365664 | 70.865% | 0.055717 | 0.842213 | 0.274751 | 0.737749 | 70.112% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
