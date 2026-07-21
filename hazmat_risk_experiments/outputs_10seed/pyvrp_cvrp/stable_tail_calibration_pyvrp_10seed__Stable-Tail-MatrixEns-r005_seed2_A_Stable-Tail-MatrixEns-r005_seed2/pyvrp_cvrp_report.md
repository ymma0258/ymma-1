# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.186484 | 0.000% | 0.263897 | 2.383622 | 0.169237 | 0.875600 | 89.601% |
| 0.25 | 0 | 142418.2 | 6.284% | 5.508107 | 32.717% | 0.160557 | 1.902953 | 0.255241 | 0.863878 | 87.566% |
| 0.5 | 0 | 148667.3 | 10.947% | 4.392174 | 46.348% | 0.130841 | 1.517956 | 0.261096 | 0.851477 | 85.072% |
| 1 | 0 | 157618.4 | 17.627% | 3.122454 | 61.858% | 0.084667 | 1.121615 | 0.284103 | 0.812111 | 79.184% |
| 2 | 0 | 172241.0 | 28.540% | 2.698556 | 67.036% | 0.066140 | 1.116816 | 0.343008 | 0.791078 | 75.823% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
