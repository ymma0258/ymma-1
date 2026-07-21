# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 8.216911 | 0.000% | 0.267038 | 2.581381 | 0.182232 | 0.867860 | 88.356% |
| 0.25 | 0 | 143136.7 | 6.555% | 5.460788 | 33.542% | 0.156258 | 1.800200 | 0.246536 | 0.859591 | 87.069% |
| 0.5 | 0 | 149515.0 | 11.303% | 4.345769 | 47.112% | 0.130200 | 1.737949 | 0.287197 | 0.836396 | 83.825% |
| 1 | 0 | 158767.5 | 18.191% | 2.904148 | 64.656% | 0.073267 | 0.853473 | 0.207168 | 0.787519 | 76.450% |
| 2 | 0 | 173582.1 | 29.219% | 2.309220 | 71.897% | 0.046240 | 0.716953 | 0.218051 | 0.752037 | 70.782% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
