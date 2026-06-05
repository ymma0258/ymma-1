# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146531.2 | 0.000% | 7.985896 | 0.000% | 0.238196 | 2.702093 | 0.233976 | 0.850347 | 88.274% |
| 1 | 178934.8 | 22.114% | 3.449506 | 56.805% | 0.078623 | 1.247577 | 0.288171 | 0.756292 | 75.107% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
