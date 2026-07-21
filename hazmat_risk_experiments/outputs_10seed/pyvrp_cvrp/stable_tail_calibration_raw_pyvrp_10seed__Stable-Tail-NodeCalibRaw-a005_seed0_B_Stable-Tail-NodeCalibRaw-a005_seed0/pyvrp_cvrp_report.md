# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.4 | 0.000% | 7.537463 | 0.000% | 0.213983 | 2.482667 | 0.247761 | 0.877240 | 89.442% |
| 0.25 | 0 | 156974.4 | 6.546% | 6.411652 | 14.936% | 0.157873 | 2.279122 | 0.268868 | 0.873276 | 88.264% |
| 0.5 | 0 | 165358.9 | 12.237% | 4.528759 | 39.917% | 0.113176 | 1.435199 | 0.208742 | 0.849581 | 84.381% |
| 1 | 0 | 175699.8 | 19.256% | 3.044199 | 59.612% | 0.070911 | 1.071459 | 0.282435 | 0.810025 | 78.011% |
| 2 | 0 | 191020.9 | 29.655% | 2.416731 | 67.937% | 0.052245 | 0.895881 | 0.282473 | 0.776947 | 72.382% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
