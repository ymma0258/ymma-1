# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 5.359974 | 0.000% | 0.172380 | 1.521130 | 0.164933 | 0.874996 | 90.103% |
| 0.25 | 0 | 143130.5 | 6.762% | 3.757805 | 29.891% | 0.109369 | 1.268499 | 0.259900 | 0.866297 | 88.449% |
| 0.5 | 0 | 149127.6 | 11.236% | 2.787714 | 47.990% | 0.065144 | 1.211572 | 0.306237 | 0.837458 | 84.731% |
| 1 | 0 | 157917.1 | 17.792% | 1.842253 | 65.629% | 0.043397 | 0.645510 | 0.253438 | 0.786560 | 77.395% |
| 2 | 0 | 171129.5 | 27.647% | 1.518878 | 71.663% | 0.035122 | 0.444643 | 0.214196 | 0.754673 | 72.635% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
