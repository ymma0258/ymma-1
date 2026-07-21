# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 6.338704 | 0.000% | 0.208757 | 1.795055 | 0.173360 | 0.874669 | 89.745% |
| 0.25 | 0 | 142975.9 | 6.647% | 4.243872 | 33.048% | 0.126741 | 1.232898 | 0.186162 | 0.860870 | 86.944% |
| 0.5 | 0 | 149170.1 | 11.267% | 3.278395 | 48.280% | 0.097039 | 1.069268 | 0.212202 | 0.839344 | 83.692% |
| 1 | 0 | 158232.0 | 18.027% | 2.290853 | 63.859% | 0.059836 | 0.912055 | 0.293835 | 0.799594 | 77.403% |
| 2 | 0 | 171301.5 | 27.775% | 1.856994 | 70.704% | 0.045093 | 0.593592 | 0.248179 | 0.766606 | 72.212% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
