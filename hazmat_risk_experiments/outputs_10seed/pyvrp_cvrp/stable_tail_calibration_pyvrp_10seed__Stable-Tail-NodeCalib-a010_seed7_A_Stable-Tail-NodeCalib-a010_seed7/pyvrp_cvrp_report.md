# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 8.983219 | 0.000% | 0.295519 | 2.540916 | 0.172017 | 0.873789 | 89.642% |
| 0.25 | 0 | 143072.6 | 6.719% | 5.759742 | 35.883% | 0.169260 | 2.083316 | 0.267710 | 0.856052 | 86.345% |
| 0.5 | 0 | 149175.8 | 11.272% | 4.641025 | 48.337% | 0.136336 | 1.507964 | 0.204257 | 0.838851 | 83.553% |
| 1 | 0 | 158538.5 | 18.255% | 3.263781 | 63.668% | 0.086920 | 1.258313 | 0.305069 | 0.797037 | 77.182% |
| 2 | 0 | 171655.3 | 28.039% | 2.563838 | 71.460% | 0.060927 | 0.839751 | 0.246047 | 0.762481 | 71.462% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
