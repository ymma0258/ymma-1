# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.5 | 0.000% | 9.646235 | 0.000% | 0.312755 | 2.654821 | 0.142093 | 0.872947 | 89.654% |
| 0.25 | 0 | 142025.7 | 5.728% | 6.341729 | 34.257% | 0.192130 | 2.005037 | 0.222196 | 0.863948 | 87.590% |
| 0.5 | 0 | 147999.1 | 10.175% | 4.871332 | 49.500% | 0.123712 | 1.523209 | 0.228249 | 0.848639 | 84.589% |
| 1 | 0 | 156144.6 | 16.238% | 3.196505 | 66.863% | 0.068471 | 1.150467 | 0.275936 | 0.789660 | 76.266% |
| 2 | 0 | 168418.5 | 25.375% | 2.559768 | 73.464% | 0.050169 | 0.750261 | 0.246482 | 0.762343 | 71.962% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
