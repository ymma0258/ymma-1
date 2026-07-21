# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.4 | 0.000% | 7.819166 | 0.000% | 0.235848 | 2.179902 | 0.149564 | 0.859026 | 88.354% |
| 0.25 | 0 | 142954.7 | 6.578% | 5.757444 | 26.368% | 0.166813 | 1.692413 | 0.176291 | 0.852399 | 87.409% |
| 0.5 | 0 | 148911.1 | 11.019% | 4.204341 | 46.230% | 0.122951 | 1.378242 | 0.225961 | 0.826369 | 83.482% |
| 1 | 0 | 158033.0 | 17.820% | 2.803363 | 64.148% | 0.074436 | 0.920830 | 0.225062 | 0.764876 | 75.411% |
| 2 | 0 | 171658.7 | 27.978% | 2.322393 | 70.299% | 0.054079 | 0.727206 | 0.246256 | 0.720787 | 69.385% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
