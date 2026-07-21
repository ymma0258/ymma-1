# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 7.891200 | 0.000% | 0.240835 | 2.531350 | 0.214183 | 0.884401 | 90.290% |
| 0.25 | 0 | 142593.4 | 6.098% | 4.761367 | 39.662% | 0.142570 | 1.527089 | 0.212396 | 0.862691 | 86.654% |
| 0.5 | 0 | 148571.9 | 10.546% | 3.606582 | 54.296% | 0.106856 | 1.435125 | 0.306971 | 0.831885 | 82.401% |
| 1 | 0 | 156189.0 | 16.214% | 2.355293 | 70.153% | 0.050642 | 1.021508 | 0.329243 | 0.779295 | 74.246% |
| 2 | 0 | 168204.3 | 25.154% | 1.813324 | 77.021% | 0.034900 | 0.568470 | 0.214179 | 0.731921 | 66.974% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
