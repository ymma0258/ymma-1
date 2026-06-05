# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146531.2 | 0.000% | 7.845854 | 0.000% | 0.235475 | 2.688076 | 0.242810 | 0.854566 | 88.707% |
| 1 | 178980.0 | 22.145% | 3.514736 | 55.203% | 0.083867 | 1.204038 | 0.283802 | 0.785942 | 78.085% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
