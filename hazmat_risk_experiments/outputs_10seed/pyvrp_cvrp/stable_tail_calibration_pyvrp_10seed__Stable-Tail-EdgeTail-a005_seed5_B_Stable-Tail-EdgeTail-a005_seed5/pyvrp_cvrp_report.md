# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 7.682825 | 0.000% | 0.234086 | 2.488623 | 0.218645 | 0.872469 | 88.844% |
| 0.25 | 0 | 156847.9 | 6.508% | 6.500156 | 15.394% | 0.161858 | 2.233620 | 0.236661 | 0.869842 | 88.103% |
| 0.5 | 0 | 165764.0 | 12.563% | 5.038944 | 34.413% | 0.119912 | 1.783561 | 0.273399 | 0.846587 | 84.672% |
| 1 | 0 | 175856.4 | 19.416% | 3.407254 | 55.651% | 0.084957 | 1.236141 | 0.295344 | 0.816167 | 79.244% |
| 2 | 0 | 192144.3 | 30.476% | 2.820243 | 63.292% | 0.067967 | 0.909618 | 0.261214 | 0.793188 | 75.250% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
