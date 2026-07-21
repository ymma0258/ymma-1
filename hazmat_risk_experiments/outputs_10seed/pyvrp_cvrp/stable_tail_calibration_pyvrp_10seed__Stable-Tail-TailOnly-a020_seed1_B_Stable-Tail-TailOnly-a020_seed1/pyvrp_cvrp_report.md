# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 10.141639 | 0.000% | 0.321630 | 3.612003 | 0.268397 | 0.875047 | 90.201% |
| 0.25 | 0 | 155653.8 | 5.985% | 8.325825 | 17.905% | 0.242887 | 2.779354 | 0.254760 | 0.871662 | 88.950% |
| 0.5 | 0 | 163765.5 | 11.508% | 6.871482 | 32.245% | 0.189446 | 2.089556 | 0.216874 | 0.866839 | 87.564% |
| 1 | 0 | 172793.5 | 17.656% | 3.944514 | 61.106% | 0.092490 | 1.346393 | 0.245801 | 0.816870 | 79.398% |
| 2 | 0 | 186777.3 | 27.177% | 3.448990 | 65.992% | 0.068373 | 1.250904 | 0.267382 | 0.803209 | 76.956% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
