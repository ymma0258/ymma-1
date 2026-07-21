# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.1 | 0.000% | 9.707327 | 0.000% | 0.322668 | 2.845807 | 0.175898 | 0.881123 | 90.169% |
| 0.25 | 0 | 142386.4 | 5.944% | 6.405155 | 34.017% | 0.185978 | 2.201801 | 0.258942 | 0.872570 | 88.546% |
| 0.5 | 0 | 148473.0 | 10.473% | 5.096863 | 47.495% | 0.153026 | 1.868913 | 0.269127 | 0.862069 | 86.420% |
| 1 | 0 | 157584.0 | 17.252% | 3.520730 | 63.731% | 0.098349 | 1.421920 | 0.359384 | 0.823225 | 80.427% |
| 2 | 0 | 171687.0 | 27.745% | 3.087989 | 68.189% | 0.075983 | 1.335115 | 0.362482 | 0.807679 | 77.887% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
